import os
import re
import csv
from collections import defaultdict

# --- KONFIGURACJA ---
INPUT_FILE = 'OpCode.eu.org/booklets/booklets-sections/url-databse.tex'
EXT_URL_FILE = 'ext_video_url.txt'
OUTPUT_HTML_FILE = 'index.html'
REDIRECTS_FILE = '_redirects'

HTML_HEAD="""
<!DOCTYPE html>
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
	<meta charset="utf-8">
	<title>Video.OpCode.eu.org</title>
	<link rel="stylesheet" href="/index.css">
	<style>
		div.video_name {
			padding: 8px 16px 8px 16px;
			font-weight: 550;
		}
		div.link {
			display: inline-block;
		}
		div.link > a {
			padding: 8px 8px 8px 8px;
		}
		div.section ul > li.repo_clone {
			display: block;
			width: min-content;
			margin-left: auto;
			margin-right: auto;
		}
		#linux {
			max-width: 700px; grid-area: 1 / 1 / span 2 / span 7;
		}
		#sieci-komputerowe {
			max-width: 600px; grid-area: 1 / 8 / span 1 / span 6;
		}
		#warsztat-elektroniczny {
			min-width: 450px; grid-area: 2 / 8 / span 1 / span 6;
		}
		#elektronika {
			max-width: 560px; grid-area: 3 / 1 / span 1 / span 6;
		}
		#python {
			max-width: 620px; grid-area: 3 / 7 / span 1 / span 8; justify-self: center;
		}
		#c-i-c {
			max-width: 800px; grid-area: 4 / 1 / span 1 / span 12; justify-self: center;
		}
		#links {
			max-width: none; grid-area: 1 / 1 / span 1 / span 13; justify-self: center;
		}
		@media all and (max-width: 1333px) {
			.menu > div > div {
				grid-template-columns: 100%;
			}
			#linux {
				max-width: none; grid-area: 1 / 1 / span 1 / span 1;
			}
			#python {
				max-width: none; grid-area: 2 / 1 / span 1 / span 1;
			}
			#c-i-c {
				max-width: none; grid-area: 3 / 1 / span 1 / span 1;
			}
			#warsztat-elektroniczny {
				max-width: none; grid-area: 4 / 1 / span 1 / span 1;
			}
			#elektronika {
				max-width: none; grid-area: 5 / 1 / span 1 / span 1;
			}
			#sieci-komputerowe {
				max-width: none; grid-area: 6 / 1 / span 1 / span 1;
			}
		}
	</style>
</head>
<body>
	<h1 style="font-size: 32px;">Video.OpCode.eu.org</h1>
	
	<div class="menu"> <div> <div>
"""

def SUB_HTML_HEAD(title):
	return """
<!DOCTYPE html>
<html><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
	<meta charset="utf-8">
	<title>""" + title + """</title>
	<link rel="stylesheet" href="/index.css">
	<style>
		#links { max-width: none; grid-area: 1 / 1 / span 1 / span 13; justify-self: center; }
		#home { max-width: none; grid-area: 2 / 8 / span 1 / span 2; padding: 10px; justify-self: center; }
	</style>
</head>
<body>
	<div class="menu"> <div> <div>
"""

HTML_TAIL="""
	</div> </div> </div>
</body></html>
"""

script_dir = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(script_dir, INPUT_FILE)
EXT_URL_FILE = os.path.join(script_dir, EXT_URL_FILE)

def load_ext_urls(filename):
	"""Wczytuje plik z linkami zewnętrznymi jako słownik."""
	ext_urls = {}
	if not os.path.exists(filename):
		print(f"Ostrzeżenie: Plik {filename} nie istnieje.")
		return ext_urls
		
	with open(filename, 'r', encoding='utf-8') as f:
		reader = csv.reader(f, delimiter='\t')
		for row in reader:
			if not row or len(row) < 1:
				continue
			plik = row[0]
			# Pozostałe kolumny: Drive, GitHub, YouTube (jeśli są dostępne)
			links = row[1:] if len(row) > 1 else []
			ext_urls[plik] = [link for link in links if link.strip()]
	return ext_urls

def safe_id(text):
	"""Generuje bezpieczny identyfikator do atrybutu id w HTML."""
	return re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-').lower()

def main():
	ext_urls = load_ext_urls(EXT_URL_FILE)
	categories = defaultdict(list)
	
	# Czyszczenie/tworzenie pliku _redirects
	open(REDIRECTS_FILE, 'w', encoding='utf-8').close()
	
	# Wyrażenie regularne do wyłuskania parametrów z \AddURL
	# Założenie: format to \AddURL{NAZWA}{BASEURL/PLIK}{KATEGORIA}
	pattern = re.compile(r'\\AddURL\{(.*?)\}\{.*/(.*?)\}\{(.*?)\}')
	
	if not os.path.exists(INPUT_FILE):
		print(f"Błąd: Plik wejściowy {INPUT_FILE} nie istnieje.")
		return
	
	with open(INPUT_FILE, 'r', encoding='utf-8') as f:
		content = f.read()
	
	print("Wczytany plik wejściowy:", content)
	
	matches = pattern.findall(content)
	
	for nazwa, plik, kategoria in matches:
		# 1. Usunięcie prefixu "KATEGORIA: " z nazwy, jeśli istnieje
		prefix = f"{kategoria}: "
		if nazwa.startswith(prefix):
			nazwa = nazwa[len(prefix):].strip()
			
		categories[kategoria].append({
			'nazwa': nazwa[0].upper()+nazwa[1:],
			'plik': plik
		})
	
	print("Wczytana mapa kategorii:", categories)
	
	html_blocks = [HTML_HEAD]
	
	for kategoria, items in categories.items():
		cat_id = safe_id(kategoria)
		html_blocks.append(f'	<div class="section" id="{cat_id}">')
		html_blocks.append(f'		<h3>{kategoria}</h3>')
		html_blocks.append(f'		<ul>')
		
		for item in items:
			nazwa = item['nazwa']
			plik = item['plik']
			
			# 2. Sprawdzanie czy plik istnieje
			if os.path.isfile(plik):
				# Zwykły przypadek - plik istnieje na dysku
				li_content = f'<li> <div class="link video_name"><a href="/{plik}">{nazwa}</a></div> </li>'
				html_blocks.append(f'			{li_content}')
			else:
				# Plik nie istnieje
				if plik not in ext_urls:
					# 2.1 Brak wpisu w ext_video_url.txt
					print(f"Ostrzeżenie: Plik '{plik}' nie istnieje i brakuje dla niego wpisu w {EXT_URL_FILE}!")
					# Dodajemy mimo to jako zwykły, niedziałający link, aby zachować ciągłość:
					li_content = f'<li> <div class="link video_name"><a href="/{plik}">{nazwa}</a></div> </li>'
					html_blocks.append(f'			{li_content}')
				else:
					# 2.2 Jest wpis w ext_video_url.txt
					links = ext_urls[plik]
					if not links:
						print(f"Ostrzeżenie: Wpis dla '{plik}' w {EXT_URL_FILE} istnieje, ale nie zawiera linków.")
						continue
						
					# 2.2.1 Dodajemy linki zamiast /PLIK w ramach jednego <li>
					# Przypisujemy odpowiednie nazwy etykiet dla czytelności (np. Drive, GitHub, YouTube)
					labels = ["Google Drive", "GitHub", "YouTube"]
					div_links = []
					div_links.append(f'<div class="video_name">{nazwa}</div> <br />')
					for i, url in enumerate(links):
						label = labels[i] if i < len(labels) else f"Źródło {i+1}"
						div_links.append(f'<div class="link"><a href="{url}">{label}</a></div>')
					
					html_blocks.append(f'			<li> {" ".join(div_links)} </li>')
					
					# 2.2.2 Tworzenie wpisu w _redirects
					first_link = links[0]
					with open(REDIRECTS_FILE, 'a', encoding='utf-8') as rf:
						rf.write(f"/{plik} {first_link} 302\n")
						
					# 2.2.3 Tworzenie katalogu PLIK i generowanie lokalnego kodu HTML ("przesunięty o poziom")
					os.makedirs(plik, exist_ok=True)
					sub_html_path = os.path.join(plik, 'index.html')
					
					sub_html_lines = [SUB_HTML_HEAD(f"{kategoria}: {nazwa} ({plik})")]
					sub_id = safe_id(nazwa)
					sub_html_lines.append(f'<div class="section" id="links">')
					sub_html_lines.append(f'	<h3>{nazwa}</h3>')
					sub_html_lines.append(f'	<ul>')
					for i, url in enumerate(links):
						label = labels[i] if i < len(labels) else f"Link {i+1}"
						sub_html_lines.append(f'		<li><a href="{url}">{label}</a></li>')
					sub_html_lines.append(f'	</ul>')
					sub_html_lines.append(f'</div>')
					sub_html_lines.append(f'<div class="section" id="home"><span>Inne filmy na <a href="/">video.opcode.eu.org</a></span></div>')
					sub_html_lines.append(HTML_TAIL)
					
					with open(sub_html_path, 'w', encoding='utf-8') as subf:
						subf.write("\n".join(sub_html_lines))

		html_blocks.append(f'		</ul>')
		html_blocks.append(f'	</div>')
	
	html_blocks.append(HTML_TAIL)

	# Zapisz główny plik wyjściowy
	with open(OUTPUT_HTML_FILE, 'w', encoding='utf-8') as out_f:
		out_f.write("\n".join(html_blocks))
		
	print("Przetwarzanie zakończone!")

if __name__ == '__main__':
	main()

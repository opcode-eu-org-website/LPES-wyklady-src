# Copyright (c) 2020-2021 Matematyka dla Ciekawych Świata (http://ciekawi.icm.edu.pl/)
# Copyright (c) 2020-2021 Robert Ryszard Paciorek <rrp@opcode.eu.org>
# 
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'DNS' },
	{
		'image': [
			["nazwadomenowa", eduMovie.convertFile('dns.svg')],
		],
		'text' : [
			"DNS służy do zamiany nazw <domenowych>[domen'owych], <m> takich jak np. <ciekawi.icm.edu.pl>[ciekawi kropka ICM kropka edu kropka PL], na numery IP. <m>"
			
			'Z punktu widzenia programisty całą robotę z zamianą takiej nazwy <m> na numer IP robi biblioteka standardowa C, oferująca odpowiednie funkcje. <m>'
			'Ze względu na bardzo duże znaczenie systemu DNS <m> warto jednak poznać ten mechanizm w trochę większych szczegółach. <m>'
			'Na skutek wywołania takiej funkcji, nasz komputer generuje zapytanie <m> o adres związany z daną nazwą, <m> do serwera rozwiązującego nazwy DNS (określonego w stosownym pliku konfiguracyjnym). <m>'
            'I to ten serwer, nazywany resolverem, zajmuje się uzyskaniem odpowiedzi <m> na otrzymane pytanie poprzez generowanie zapytań do innych serwerów DNS. <mark name="nazwadomenowa" />'
			
			'DNS jest systemem hierarchicznym, <m> gdzie kolejne poziomy hierarchii rozdzielane są kropkami <m> i (w przeciwieństwie na przykład do ścieżek w drzewie katalogów) <m> im bardziej w prawo tym wyższy poziom. <m>'
			"Dodatkowo na końcu każdej nazwy <domenowej>[domen'owej] znajduje się, <m> nie zapisywana zazwyczaj, kropka oznaczająca korzeń tego systemu. <m>",
			
			"Serwer rozwiązujący nazwy DNS zna adresy IP serwerów <m> obsługująccyh wspomniany korzeń (czyli tą kropkę na końcu pełnej nazwy <domenowej>[domen'owej]) <m> nazywanych root serwerami DNS <m>"
				'i wysyła do któregoś z nich zapytanie o rozwiązywaną domenę. <m>'
			'Jako że root serwer zna tylko adresy wszystkich serwerów <m> obsługujących domeny najwyższego poziomu i nie jest serwerem rozwijającym, <m>'
				'to odpowiada że daną domenę najwyższego poziomu (w tym wypadku <pl>[PL]) <m> obsługują takie a nie inne serwery. <m>'
			'Wtedy resolver może zapytać się któregoś z wskazanych <m> w tej odpowiedzi serwerów o tą domenę i tak dalej, aż znajdzie serwer <m> od którego otrzyma odpowiedź dotyczącą rozwijanej domeny. <m>'
			'Odpowiedzią tą może być też informacja, <m> że dany rekord w systemie DNS nie istnieje. <m>'
			
			'Zasadą jest że serwer obsługujący daną domenę zna adresy <m> wszystkich serwerów obsługujących poddomeny w niej utworzone <m>'
				'oraz wszystkie adresy utworzone bezpośrednio w niej, <m> czyli nie przekazane pod obsługę innym serwerom. <m>'
			'Dzięki temu może udzielać autorytatywnych odpowiedzi <m> na wszystkie pytania o swoje domeny. <m>'
			
			'Oczywiście resolver aby zmniejszyć ilość wysyłanych zapytań, skrócić czas <m> odpowiedzi i tak dalej przechowuje przez pewien czas uzyskane informację, <m>'
				'czyli jeżeli minutę temu właśnie sprawdził kto obsługuje <edu.pl>[edu kropka PL] <m> to teraz nadal to wie i wie kogo pytać się o <uw.edu.pl>[UW kropka edu kropka PL], <m> bez konieczności przechodzenia wszystkich etapów. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.convertFile('dns_rekordy.tex')],
		],
		'text' : [
			'Wspomnieliśmy o czymś takim jak typ rekordu. <m>'
			"DNS jest rozproszoną hierarchiczną bazą danych, <m> która (także dla tej samej nazwy <domenowej>[domen'owej]) może przechowywać <m> rekordy różnych typów, a nie tylko mapowanie nazwy na numer IP. <m>"
			
			'Chyba najważniejszym rekordem jest rekord NS, służący do <m> tworzenia tej hierarchii i określający serwer obsługujący daną poddomenę. <m>'
			'To właśnie rekord NS związany z domeną <pl>[PL] otrzymał resolver <m> od root serwera DNS w rozważanym przykładzie <m> znajdowania adresu związanego z nazwą <ciekawi.icm.edu.pl>[ciekawi kropka ICM kropka edu kropka Pe eL]. <m>'
			
			'Jednymi z podstawowych typów rekordów są rekordy A i AAAA, <m> związane z mapowaniem nazwy na związany z nią numer IP, <m> w przypadku rekordu A na IPv4 a rekordu AAAA na IPv6. <m>'
			'Innymi rekordami o których warto wspomnieć są MX <m> informujący o serwerach do których należy kierować pocztę do danej domeny <m> i SRV informujący o serwerach dostarczających konkretne usługi w danej domenie. <m>'
			'SRV pełni rolę podobną do MX tyle że może być używany dla <m> dowolnych usług a nie tylko poczty, najczęściej wykorzystywany jest w <m> usługach typu VoIP, instant message i tym podobnych. <m>'
			
			'Mamy również m.in. rekordy PTR używane w mapowaniu adresów IP na nazwy <m> i rekordy TXT mogące przechowywać dowolne dane. <m>'
			'Często używane są do wystawiania jakiś informacji autoryzacyjnych, <m> informacji jakie serwery pocztowe mają prawo wysyłać maile z danej domeny <m> i tym podobnych. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"nslookup ciekawi.icm.edu.pl")],
			[1.0, eduMovie.runCommandString(r"host ciekawi.icm.edu.pl")],
		],
		'text' : [
			'Istnieje wiele narzędzi służących odpytywaniu systemu DNS, <m> należy w śród nich wymienić <nslookup>[NS-lookup], host i dig. <m>'
			'Oferują one podobne możliwości – możemy odpytywać o rekord danego typu, <m> możemy zapytanie kierować do konkretnego serwera i tak dalej. <m>'
			'Szczegóły jak zwykle można sprawdzić w dokumentacji man tych poleceń. <m>'
		]
	},
]

import json

digCacheFile = "cache/dig.json"

if not eduMovie.checkCachedFile(digCacheFile, "dig output"):
	def runAndGetIP(cmd, noFail=False):
		print("  run: " + cmd)
		txt = eduMovie.runCommandString(cmd)
		for l in txt.split("\n\r"):
			if '\tA\t' in l:
				return txt, l.split("\t")[-1]
		if noFail:
			return txt, ""
		raise BaseException(f"no found IP in runAndGetIP, cmd_output={txt}")
	
	code_dig = {}
	
	code_dig["1a"]      = eduMovie.runCommandString(r"dig . NS")
	code_dig["1b"], rip = runAndGetIP("dig . NS | grep -A5 ' SECTION:'")
	code_dig["2"],  ip  = runAndGetIP("dig @" + rip + " pl. NS | grep -A5 ' SECTION:'")
	code_dig["3"],  _   = runAndGetIP("dig @" + ip + " edu.pl. NS | grep -A5 ' SECTION:'", True)
	code_dig["4"],  ip  = runAndGetIP("dig @" + ip + " icm.edu.pl. NS | grep -A5 ' SECTION:'")
	code_dig["5"],  _   = runAndGetIP("dig @" + ip + " ciekawi.icm.edu.pl. NS | grep -A5 ' SECTION:'", True)
	code_dig["6"],  _   = runAndGetIP("dig @" + ip + " www2.icm.edu.pl. NS | grep -A5 ' SECTION:'", True)
	code_dig["7"],  ip  = runAndGetIP("dig @" + ip + " www2.icm.edu.pl. A | grep -A5 ' SECTION:'")
	
	code_dig["rip"] = rip
	code_dig["12"], code_dig["ip1"] = runAndGetIP("dig @" + code_dig["rip"] + " ciekawi.icm.edu.pl. A | grep -A5 ' SECTION:'")
	code_dig["13"], code_dig["ip2"] = runAndGetIP("dig @" + code_dig["ip1"] + " ciekawi.icm.edu.pl. A | grep -A2 ' SECTION:'")
	code_dig["14"], code_dig["ip3"] = runAndGetIP("dig @" + code_dig["ip2"] + " ciekawi.icm.edu.pl. A | grep -A2 ' SECTION:'")
	
	
	json.dump(code_dig, open(digCacheFile,"w"))
else:
	code_dig = json.load(open(digCacheFile))

dig_info  = eduMovie.prompt() + "# root dns (" + code_dig["rip"] + ") kazał pytać " + code_dig["ip1"] + "\n\r"
dig_info += eduMovie.prompt() + "# dns " + code_dig["ip1"] + " kazał pytać " + code_dig["ip2"] + "\n\r"
dig_info += eduMovie.prompt() + "# dns " + code_dig["ip2"] + " odpowiedział że host ten to " + code_dig["ip3"] + "\n\r"

clipData += [
	{
		'console': [
			[0.0, ""],
			["dig1a", code_dig["1a"]],
			["dig1b", code_dig["1b"]],
			["dig2",  code_dig["2"]],
			["dig3",  code_dig["3"]],
			["dig4",  code_dig["4"]],
			["dig5",  code_dig["5"]],
			["dig6",  code_dig["6"]],
			["dig7",  code_dig["7"]],
			["dig12", code_dig["12"]],
			["dig13", code_dig["13"]],
			["dig14", code_dig["14"]],
			["diginfo", dig_info],
		],
		'text' : [
			'Użyjemy polecenia dig do zasymulowania pracy resolvera próbującego <m> ustalić odpowiedź na pytanie o rekord typu A dla domeny <ciekawi.icm.edu.pl>[ciekawi ICM edu PL ]. <mark name="dig1a" />'
			'Najpierw zapytajmy się naszego resolvera o listę root serwerów <m> – prawdziwy resolver ją po prostu zna. <m>'
			'''Otrzymaliśmy dość długą listę nazw <domenowych>[domen'owych] root serwerów oraz ich numery IP. <mark name="dig1b" />'''
			'Jako że nie mieści się ona nam na ekranie to ponówmy to pytanie, <m> przekierowując wyjście do polecenia grep, <m> które wypisze nam tylko pierwsze linie z poszczególnych sekcji. <m>'
			"Widzimy teraz że polecenie to wypisało nam sekcję odpowiedzi, <m> w której otrzymaliśmy informację o nazwach <domenowych>[domen'owych] root serwerów DNS <m>"
				'oraz sekcję dodatkową w której otrzymaliśmy mapowania <m> tych nazw na adresy IPv4 i IPv6 w postaci rekordów A i AAAA. <mark name="dig2" />'
			
			'Następnie symulując pracę resolvera możemy zapytać się <m> któregoś z tych serwerów o to kto obsługuje domenę <pl>[PL ]. <m>'
			'Także otrzymaliśmy wiele serwerów wraz z ich adresami IP. <mark name="dig3" />'
			
			'Zapytajmy się jednego z nich o <edu.pl>[edu PL ]. <m>'
			'Złożyło się tak że otrzymaliśmy tą samą listę co wcześniej. <mark name="dig4" />'
			'Zatem możemy zapytać się tego serwera o <icm.edu.pl>[ICM edu PL] i dostaliśmy <m> odpowiedź jaki serwer zajmuje się tą domeną. <mark name="dig5" />'
			'Gdy zapytamy go o NS dla <ciekawi.icm.edu.pl>[ciekawi ICM edu PL] to dostaniemy informację, <m> iż jest to alias dla <www2.icm.edu.pl>[WWW dwa ICM edu PL] i należy pytać się o taką domenę. <mark name="dig6" />'
			'Moglibyśmy zacząć od nowa, ale pamiętamy kto zajmuje się <icm.edu.pl>[ICM edu PL], <m> więc pytamy go o www2. <m>'
			'Nie dostajemy odpowiedzi, czyli nie jest to wydelegowana poddomena, <mark name="dig7" /> zatem pytamy o rekord typu A i otrzymujemy odpowiedź, <m> że jest to IP <213.135.59.55>[213 kropka 135 kropka 59 kropka 55]. <mark name="dig12" />'
			
			'Warto zauważyć że jeżeli root serwerowi od razu zadalibyśmy pytanie <m> o IP hosta <ciekawi.icm.edu.pl>[ciekawi ICM edu PL], to otrzymalibyśmy taką samą odpowiedź <m> jak na pytanie o NS dla domeny <pl>[PL ]. <m>'
			'Ten serwer nie pośredniczy w rozwijaniu nazw <m> i odpowiada tylko tym co sam wie, a on zna tylko nazwy i adresy IP serwerów NS <m> obsługujących domeny najwyższego poziomu. <m>'
			'Jednak, jak widzimy, udziela on najlepszej znanej mu odpowiedzi <m> na pytanie na które nie zna pełnej odpowiedzi. <mark name="dig13" />'
			
			'Takie działanie ułatwia tworzenie algorytmu działania serwera rozwijającego <m> – może on pytać root serwera od razu o docelową domenę, <mark name="dig14" />'
				'jeżeli dostanie odpowiedź typu NS to to samo pytanie <m> wysyła do serwera z tej odpowiedzi i tak dalej. <mark name="diginfo" />'
			'Ogranicza to też ilość wysyłanych zapytań – w naszym wypadku <m> wyeliminowałoby konieczność osobnego pytania o <edu.pl>[edu PL] i <icm.edu.pl>[ICM edu PL] <m>'
				'oraz pytania o NS dla samego <ciekawi.icm.edu.pl>[ciekawi ICM edu PL] i <www2.icm.edu.pl>[WWW dwa ICM edu PL ]. <m>'
			'Czyli zapytania wyglądałyby tak jak pokazano to teraz na ekranie <m> i to bardziej odpowiada rzeczywistemu działaniu niż nasza wcześniejsza symulacja. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			["revdns", eduMovie.runCommandString(r"host 213.135.59.55")],
			["revdns+0.7", eduMovie.runCommandString(r"host 2001:6a0:0:21::60:13")],
		],
		'text' : [
			'Jak można łatwo zaobserwować rozproszoność systemu DNS <m> oraz jego niezależność od struktur routingu IP, <m> nie pozwalają na łatwe ustalenie nazw, które wskazują na dany adres IP. <m>'
			'Coś takiego wymagałoby odpytania wszystkich serwerów obsługujących <m> jakieś domeny o to czy któraś z ich domen <m> przypadkiem nie wskazuje na dany numer IP. <m>'
			'Ze względu na ilość serwerów takie podejście jest niewykonalne <m>'
			'Jednak uzyskanie takiej informacji może być przydatne i wspomnieliśmy już <m> o rekordach typu PTR używanych do mapowania adresów IP na nazwy. <m> Zatem jakoś jest to robione. <m>'
			
			'Odbywa się to poprzez zapisanie adresu IP <m> w postaci nazwy domeny w jednej z dwóch dedykowanych temu <m> poddomen specjalnej domeny najwyższego poziomu arpa, <m>'
				'której nazwa pochodzi od Agencji Zaawansowanych Projektów Badawczych <m> Departamentu Obrony USA, znanej dziś pod nazwą DARPA. <mark name="revdns" />'
			
			'Taka domena z punktu widzenia DNS jest zwykłym jego elementem <m> i również może być delegowana z użyciem rekordów NS <m> do innych serwerów obsługujących dany poziom. <m>'
			'Aby móc zachować taką hierarchiczność adres IP musi być <m> zapisany w odwrotnej kolejności niż zwykle. <m>'
			'''Wynika to z faktu że w nazwach <domenowych>[domen'owych] szczegółowość rośnie <m> od prawej do lewej (skrajnie po prawej mamy korzeń DNS), a w adresach IP <m>'''
				'rośnie od lewej do prawej (n bitów od lewej wyznacza prefix sieci). <m>'
			
			'Przykład zamiany adresów IP na nazwę widzimy na ekranie. <m>'
			'Warto zauważyć że komenda host najpierw zamieniała adres na domenę <m> bezpośrednio z nim związaną w <in-addr.arpa>[in-addr kropka arpa] dla IPv4 lub <ip6.arpa>[ip6 kropka arpa] dla IPv6 <m>'
				'i odpytując DNS o rekord PTR związany z taką domeną <m> uzyskała informacje o nazwie serwera. <m>'
			'Warto także zauważyć że poziomami domen dla IPv4 są zapisane dziesiętnie <m> wartości kolejnych bajtów (oktetów) składających się na adres, <m> a dla IPv6 są to grupy 4bitów zapisanych jako pojedyncza cyfra heksalna. <m>'
			'Rozwiązanie zastosowane dla IPv4 nie pozwala na <m> normalne wydelegowanie obsługi odwrotnego DNS <m> dla sieci o prefixie dłuższym niż 24, <m> co jest problematyczne. <m>'
			'Stosuje się wtedy aliasy typu CNAME. <m>'
			
			'Pomimo funkcjonowania zgodnie z wszystkimi regułami systemu DNS, <m> mechanizm ten bywa określany mianem odwrotnego DNS, <m> gdyż służy do odwrotnej operacji niż typowa dla DNS zamiana nazwy na numer. <m>'
		]
	},
]

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

code_while = r"""
zm=0;
cat /etc/fstab | while read x; do
	zm=13
done
echo $zm
"""

code_while2 = r"""
zm=0;
while read x; do
	zm=13
done < /etc/fstab
echo $zm

zm=0;
while read x; do
	zm=13
done < <$(cat /etc/fstab)
echo $zm
"""

try: clipData
except NameError: clipData = []

clipData += [
	{ 'title': [ "#05.2", "Pętle, warunki", "i funkcje", "w bash'u" ] },
	
	{ 'section': 'pętle' },
	{
		'console': [
			[0.0, ""],
			["for1", eduMovie.runCommandString(r"for x in 1 2  3 abc; do echo $x; done")],
			["for2", eduMovie.runCommandString(r"for x in *; do echo $x; done")],
			["for3", eduMovie.runCommandString(r"for x in /etc/s*.conf; do echo $x; done")],
			["for4", eduMovie.runCommandString(r"for x in `seq 1 5`; do echo $x; done")],
			["for5", eduMovie.runCommandString(r"for x in $(seq 1 2 5); do echo $x; done")],
			["for6", eduMovie.runCommandString(r"for (( i=0 ; $i<=5 ; i++ )) ; do echo $i; done")],
		],
		'text' : [
			'W bashu mamy dostępne dwa podstawowe rodzaje pętli – for i while. <mark name="for1" />'
			
			'Pętla for jest podobna do pętli pythonowej <m> – tu również mamy for jakaś zmienna in lista obiektów. <m>'
			'Tylko że tutaj tej listy nie zapisujemy <m> w nawiasach kwadratowych i elementów nie rozdzielamy przecinkami, <m>'
				'tylko wymieniamy te elementy rozdzielając je spacjami <m> i kończymy średnikiem lub znakiem nowej linii. <m>'
			'Następnie używamy słowa kluczowego <do>[du], <m> które rozpoczyna blok instrukcji wykonywany w ramach pętli. <m>'
			'Blok ten kończymy słowem kluczowym done. <mark name="for2" />'
			
			'Jeżeli jako listę podamy na przykład gwiazdkę, a wiemy że bash <m> pod gwiazdkę podstawia wszystkie pliki nie ukryte z bieżącego katalogu, <m> to pętla taka będzie przebiegała po nazwach tych plików. <mark name="for3" />'
			'Oczywiście nie musimy stosować samej gwiazdki. <m>'
			'Możemy użyć dowolnej ścieżki zawierającej jakieś znaki uogólniające <m> i przechodzić na przykład po plikach z wskazanego katalogu <m> lub z wskazanym rozszerzeniem. <mark name="for4" />'
			
			'Jeżeli chcemy iterować po zakresie liczb całkowitych <m> to podobnie jak w Pythonie mieliśmy range, tutaj mamy seq, <m> który zwraca nam liczby całkowite z podanego zakresu. <m>'
			'Przy czym w przypadku seq podawany przedział jest obustronnie domknięty, <m> czyli pętla wykona się także dla obu krańców przedziału podanych do seq. <mark name="for5" />'
			
			'Możemy też podać krok iteracyjny, <m> ale jest on tutaj drugim a nie trzecim argumentem. <m>'
			'Należy zauważyć że seq musi być podany w ramach backticks <m> lub operatora dolar pojedyncze nawiasy okrągłe. <m>'
			'Wynika to z faktu iż jest on zwykłym programem, który musi zostać <m> uruchomiony, a jego standardowe wyjście podstawione w danym miejscu. <mark name="for6" />'
			
			'Bash pozwala na stosowanie pętli for w stylu C z użyciem podwójnych <m> nawiasów okrągłych, jednak jest to składnia rzadko spotykana. <m>'
		]
	},
	{
		'console': [
			[0.0, eduMovie.runCommandString(r'while [ "$a" != "aaaa" ]; do echo $a; a=${a}a; done')],
			["while2", eduMovie.runCommandString(r"while ! true; do echo x; done")],
			["while3", eduMovie.runCommandString(r"while read x; do echo XX $x XX; done < /etc/networks")],
			["while4", eduMovie.runCommandString(r"while read a b; do echo XX $a --- $b XX; done < /etc/networks")],
			["while5", eduMovie.runCommandString(r'IFS=":"; while read a b c; do echo "XX $a --- $c XX"; done < /etc/passwd | head; unset IFS')],
		],
		'text' : [
			'Drugą pętlą dostępną w bashu jest pętla while, która działa tak jak <m> typowa pętla while – wykonuje swój kod dopóki warunek jest spełniony. <m>'
			'Po słowie kluczowym while ją rozpoczynającym występuje warunek <m> (zakończony średnikiem) po którym występuje blok kodu <m> związany z pętlą ujęty pomiędzy słowami kluczowymi <do>[du] i done. <m>'
			
			'Warunek określony jest przy pomocy komendy, <m> która zostanie uruchomiona i będzie sprawdzony jej kod powrotu. <m>'
			'Jeżeli zakończy się sukcesem (zwróci zero) to warunek jest spełniony, <m> jeżeli zwróci coś nie zerowego to warunek jest nie spełniony i pętla się zakończy. <mark name="while2" />'
			
			'Warunek może być zanegowany poprzez użycie <m> wykrzyknika (wokół którego muszą być spacje). <m>'
			'Użycie wykrzyknika jest wygodne jeżeli sprawdzamy kod powrotu <m> jakiegoś programu, a nie zwykły warunek realizowany <m> komendą test lub nawiasami kwadratowymi. <mark name="while3" />'
			
			'Chyba najczęstszym zastosowaniem pętli while w bashu <m> jest czytanie pliku linia po linii. <m>'
			'Możemy wykorzystać do tego komendę read, która wczytuje <m> pojedynczą linię ze swojego standardowego wejścia <m> i zapisuje ją do zmiennej o nazwie przekazanej jako argument. <m>'
			'Jako że czyta ona jedną linię, to aby móc przeczytać <m> wiele linii używamy pętli while. <m>'
			'Pętla ta zakończy się gdy read zwróci nie zerowy kod powrotu <m> na skutek końca danych w czytanym pliku lub strumieniu. <m>'
			
			'W przykładzie widocznym na ekranie przy pomocy konstrukcji while - read <m> przeczytaliśmy plik networks przekazany na standardowe wejście pętli while. <mark name="while4" />'
			
			'Jeżeli do polecenia read przekażemy kilka nazw zmiennych to dokona <m> ono podziału czytanej linii na pola i kolejne pola zapisze do kolejnych zmiennych. <m>'
			'W ostatniej zmiennej znajdzie się pozostała część linii. <m>'
			'Domyślnym separatorem używanym do podziału linii na pola <m> jest dowolny ciąg białych znaków (spacji lub tabulatorów). <mark name="while5" />'
			
			'Separator ten możemy zmienić przy pomocy zmiennej IFS, <m> tak jak jest to pokazane w przykładzie na ekranie. <m>'
			'Warto zauważyć że w wywołaniu echo dodaliśmy cudzysłów, <m> co jest ważne dla poprawnego wypisania zawartości zmiennej c. <m>'
			
			'Ustawiając IFS, należy pamiętać o przywróceniu wartości <m> domyślnej poprzez usunięcie tej zmiennej (komenda unset), <m>'
				'bo późniejsze działanie różnych poleceń z ustawionym tym <m> separatorem na wartość inną niż domyślna może nas zaskoczyć. <m>'
		]
	},
	{
		'consoleTop': [
			[0.0, eduMovie.clear + eduMovie.code2console(code_while, "sh")],
			[0.0, eduMovie.clear + eduMovie.code2console(code_while2, "sh")],
		],
		'consoleDown': [
			[0.0, eduMovie.runCode(code_while, [], cmd="bash")],
			[0.0, eduMovie.clear + eduMovie.code2console(code_while2, "sh")],
		],
		'text' : [
			'Jako że pętla while bardzo często używana jest w powiązaniu <m> z przekierowaniami strumieni trzeba w tym miejscu zwrócić uwagę, <m>'
				'że przekierowanie standardowego wyjścia na standardowe wejście <m> odbywa się między dwoma różnymi procesami. <m>'
			'Zatem w konstrukcjach typu while read, pętla while może być <m> uruchamiana w procesie potomnym obecnej powłoki, <m>'
				'efektem czego będzie to że w tych przypadkach wykonywane modyfikacje <m> zmiennych wewnątrz takiej pętli nie będą widoczne poza nią. <mark name="code_while2" />'
			'Problem ten można obejść przekazując dane do pętli z pliku. <m>'
			'Jeżeli dane te są wynikiem działania jakiegoś polecenia, <m> możemy skorzystać z pliku tymczasowego <m>'
				'lub ze składni basha pozwalającej na podstawienie <m> standardowego wyjścia polecenia jako pliku. <m>'
			'Możliwe jest też uruchomienie pętli while jako osobnego skryptu <m> lub funkcji bashowej i skorzystanie z kodu powrotu <m> do odebrania informacji z wnętrza pętli. <m>'
		]
	},
]

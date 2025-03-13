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

shenv = {
	"a":"17",
	"d":"13.3"
}

try: clipData
except NameError: clipData = []

clipData += [
	{ 'section': 'operacje matematyczne \n i logiczne' },
	{
		'console': [
			[0.0, eduMovie.runCommandString(r"echo 2 + 2", env=shenv)],
			["math1", eduMovie.runCommandString(r"echo $((2 + 2))", env=shenv)],
			["math2", eduMovie.runCommandString(r"a=17", env=shenv)],
			["math2 + 1", eduMovie.runCommandString(r"echo $((2 + 2*$a ))", env=shenv)],
			["math3 + 1", eduMovie.runCommandString(r"e=$(( 2 + 2*$a )) ; echo e wynosi $e", env=shenv)],
			
			["math4", eduMovie.runCommandString(r"echo $(( 13/5 ))", env=shenv)],
			["math5", eduMovie.runCommandString(r"echo $(( 13%5 ))", env=shenv)],
			
			["let1", eduMovie.runCommandString(r"echo $a; let a++; echo $a", env=shenv)],
			
			["float1", eduMovie.runCommandString(r"d=13.3", env=shenv)],
			["float1 + 1", eduMovie.runCommandString(r"echo $(( $d * 2))", env=shenv)],
			["float1 + 2", eduMovie.runCommandString(r"echo $(( 2.5 * 2))", env=shenv)],
		],
		'text' : [
			'Większość języków programowania gdy każemy im wypisać dwa plus dwa <m> to wypiszą 4, bash potraktuje coś takiego jak napis. <mark name="math1" />'
			
			'Aby użyć operacji matematycznych należy skorzystać ze specjalnego <m> operatora postaci dolar dwa nawiasy okrągłe lewe <m> wyrażenie matematyczne i dwa nawiasy okrągłe prawe. <mark name="math2" />'
			
			'W ramach wyrażenia w tym operatorze możemy odwoływać się do zmiennych <m> oraz (co w bashu jest rzadkością) swobodnie używać spacji. <mark name="math3" />'
			'Wynik takiej operacji możemy przypisać do zmiennej w standardowy sposób <m> (pamiętajmy jednak że wokół znaku równości spacje są niedozwolone). <mark name="math4" />'
			
			'Możemy także wykonać operację dzielenia, jednak będzie to <m> tylko i wyłącznie dzielenie całkowite, czyli dostaniemy część całkowitą wyniku. <mark name="math5" />'
			'Możemy też poznać resztę z dzielenia używając operatora procent. <mark name="let1" />'
			
			'Do operacji arytmetycznych może być też wykorzystywane polecenie let. <m>'
			'Najczęściej jest stosowane do inkrementacji podanej zmiennej, <m> tak jak w przykładzie pokazanym na ekranie. <mark name="float1" />'
			
			'Bash nie rozumie liczb zmiennoprzecinkowych <m> i pomimo że może je przechować w zmiennej nie potrafi na nich operować. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			["float2", eduMovie.runCommandString(r'e=$(python -c "print($d * 2)") ;  echo $e', env=shenv)],
			["float3", eduMovie.runCommandString(r'e=`python -c "print($d * 2)"` ;  echo $e', env=shenv)],
			["float4", eduMovie.runCommandString(r'e=$( x=$(python -c "print(13/3)"); python -c "print($d * $x)" ) ;  echo $e', env=shenv)],
			["callcat", eduMovie.runCommandString(r'e=$( cat /etc/networks ) ;  echo $e', env=shenv)],
			["callcat + 1", eduMovie.runCommandString(r'e=$( cat /etc/networks ) ;  echo "$e"', env=shenv)],
			
		],
		'text' : [
			'Jednak silną stroną basha jest to co w innych językach <m> bywa dość złożone i nie często stosowane, <m>'
				'czyli uruchamianie zewnętrznych poleceń i przekazywanie do nich jakiś danych <m> oraz odbieranie od nich wyników. <mark name="float2" />'
			
			'Możemy zatem użyć innego programu <m> do wykonania operacji zmiennoprzecinkowych. <m>'
			'Na ekranie widzimy użycie Pythona <m> do wykonania operacji zmiennoprzecinkowej na bashowej zmiennej d. <m>'
			'Należy zwrócić uwagę na umieszczenie kodu pythonowego w podwójnych cudzysłowach, <m> co pozwala na podstawienie pod dolar d wartości zmiennej d. <m>'
			'Oraz na umieszczenie całego tego polecenia w pojedynczych nawiasach okrągłych, <m> przed którymi wystepuje znak dolara, <m>'
				'Jest to operator umożliwiający pobranie do zmiennej <m> standardowego wyjścia uruchomionego polecenia, <m> na którym Python wypisał wynik. <mark name="float3" />'
			'Alternatywnym zapisem, widocznym teraz na ekranie, jest użycie backticks. <m>'
			
			'W odróżnieniu od nich, jednak operator dolar nawiasy okrągłe może być zagnieżdżony, <mark name="float4" /> czyli wewnątrz kodu którego wyjście przechwytujemy <m> możemy też definiować zmienną przechwytującą jakieś wyjście. <mark name="callcat" />'
			
			'Warto także zwrócić uwagę na znaczenie cudzysłowów <m> przy odwołaniu się do zmiennych zawierających wiele linii. <m>'
			'Jeżeli wypiszemy taką zmienną bez użycia cudzysłowów <m> to nowe linie zostaną zastąpione przez echo spacjami (podobnie jak <m>'
				'ciąg dowolnej ilości spacji zostanie zastąpiony pojedynczą spacją), <m> a jeżeli zastosujemy cudzysłów zmienna zostanie wypisana w nie zmienionej formie. <m>'
			'Przyczyną tego jest to iż w pierwszym wypadku echo każdy wyraz <m> potraktuje jako osobny swój argument i wypisze go oddzielając od innych argumentów spacją, <m>'
				'a w drugim dostanie jeden argument ze zmienną <m> w oryginalnej postaci i go w takiej postaci wypisze. <m>'
		]
	},
	{
		'console': [
			[0.0, ""],
			["kwadratowe - 1.5", eduMovie.runCommandString(r"[ 0 -lt 3 ]; echo $?", env=shenv)],
			["kwadratowe + 1.5", eduMovie.runCommandString(r"""test "abc" = "def"; echo $?""", env=shenv)],
			["test2", eduMovie.runCommandString(r"test 0 -eq 0 && echo 'zero równa się zero'", env=shenv)],
		],
		'text' : [
			'Można by używać operatora dolar i podwójne nawiasy okrągłe także <m> do obliczania wartości wyrażeń logicznych a nawet bitowych. <m>'
			'Natomiast jest to bardzo rzadko spotykane i do obliczania wartości <m> wyrażeń logicznych typowo stosuje się nawiasy kwadratowe <mark name="kwadratowe" /> lub komendę test (zapisy te są równoważne). <m>'
			
			'Wynika to zapewne z dwóch ich cech. <m>'
			'Po pierwsze wynik testowanego wyrażenia logicznego zwracają jako <m> kod powrotu, co okazuje się bardzo wygodne do łączenia ich z innymi poleceniami. <m>'
			'Po drugie oferują oprócz sprawdzania typowych nierówności i równości <m> także sprawdzanie istnienia / nieistnienia plików itp. <m>'
			
			'Można się też spotkać z operatorem podwójnego nawiasu kwadratowego, <m> ale jest to niestandardowe rozszerzenie basha, <m> którego nie będziemy tu omawiali. <mark name="test2" />'
			
			'Kod powrotu jest wyrażany w sposób typowy dla tej wartości <m> czyli zero oznacza sukces (spełnienie warunku), <m> natomiast coś nie zerowego porażkę (warunek nie spełniony). <m>'
			'Mamy zatem do czynienia z logiką odwróconą. <m>'
			
			'Pełen opis warunków które możemy sprawdzać <m> można znaleźć w man test, warto jednak od razu zauważyć <m>'
				'że prawie wszystkie operacje (za wyjątkiem porównania napisów) <m> określane są jako opcja zaczynająca się od myślnika, <m> na przykład <-lt>[minus l t] oznacza mniejsze niż (less than). <m>'
			
			'Należy też pamiętać że w przypadku nawiasów kwadratowych <m> spacje wokół nich są obowiązkowe – nie możemy nawiasu dokleić do <m> polecenia występującego przed nim, po nim lub do warunku. <m>'
		]
	},
	{ #  wieloliniowe w interaktywnym
		'console': [
			[0.071384, "o", eduMovie.prompt()],
			[0.920981, "o", "e"],
			[1.328904, "o", "="],
			[1.744868, "o", "'"],
			[2.912926, "o", "A"],
			[3.104875, "o", "l"],
			[3.328902, "o", "a"],
			[4.088861, "o", "\r\n"],
			[4.089228, "o", "> "],
			[4.848881, "o", "m"],
			[5.032797, "o", "a"],
			[5.736847, "o", "\r\n"],
			[5.737176, "o", "> "],
			[6.11281, "o", "k"],
			[6.30481, "o", "o"],
			[6.616787, "o", "t"],
			[6.872779, "o", "a"],
			[7.920865, "o", "\r\n"],
			[7.92118, "o", "> "],
			[9.088965, "o", "'"],
			[9.632915, "o", "\r\n"],
			[9.63395, "o", eduMovie.prompt()],
			[10.705002, "o", "e"],
			[10.96089, "o", "c"],
			[11.152874, "o", "h"],
			[11.432917, "o", "o"],
			[11.7849, "o", " "],
			[12.577041, "o", "$"],
			[13.344988, "o", "e"],
			[13.856846, "o", "\r\n"],
			[13.857231, "o", "Ala ma kota\r\n"],
			[13.857694, "o", eduMovie.prompt()],
			[14.641008, "o", "echo $e"],
			[15.209034, "o", "\""],
			[15.464932, "o", "\b"],
			[15.62497, "o", "\b"],
			[15.784907, "o", "\b"],
			[16.129074, "o", "\"$e\"\b\b\b"],
			[16.512932, "o", "\r\n"],
			[16.513324, "o", "Ala\r\nma\r\nkota\r\n\r\n"],
			[16.513926, "o", eduMovie.prompt()],
			
			["blad + 0.072107", "o", eduMovie.prompt()],
			["blad + 1.631328", "o", "e"],
			["blad + 2.423255", "o", "="],
			["blad + 2.903258", "o", "'"],
			["blad + 3.631325", "o", "a"],
			["blad + 3.911212", "o", "b"],
			["blad + 4.29528", "o", "c"],
			["blad + 5.367481", "o", "\""],
			["blad + 5.751265", "o", "\r\n"],
			["blad + 5.751644", "o", "> "],
			["blad + 7.647443", "o", "^C"],
			["blad + 7.648199", "o", eduMovie.prompt()],
		],
		'text' : [
			'Warto zauważyć że bash pozwala na wprowadzanie <m> w trybie interaktywnym poleceń, czy też zmiennych, wieloliniowych. <m>'
			'Oczekiwanie na kontynuację wprowadzania rozpoczętego polecenia <m> bash sygnalizuje zmianą znaku zachęty na pojedynczy znak większości. <m>'
			
			'Często wejście w ten tryb jest jednak wynikiem naszego błędu <mark name="blad" /> i nie chcemy kontynuować wprowadzania tego polecenia. <m>'
			'Możemy wtedy użyć Control C <m> aby przerwać to wprowadzanie i poprawić popełniony błąd. <m>'
			'Przerwane polecenie będzie dostępne w historii linii poleceń. <m>'
		]
	},
]

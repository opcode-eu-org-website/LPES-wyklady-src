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
	{ 'title': [ "#09.1", "Bramki", "logiczne", "" ] },
	
	{ 'comment': 'bramki - intro' },
	{
		'image': [
			[0.0, ""],
			["bramki", eduMovie.circuitjs("bramki", 0, 1)],
			["_not", eduMovie.circuitjs("bramki", 2, 8, [
				("switch", 400, 70), ("wait", 2.1), ("switch", 400, 70), ("wait", 2.1), ("switch", 400, 70)
			])],
			["_and", eduMovie.circuitjs("bramki", 2, 11, [
				("switch", 220, 180), ("switch", 600, 180), ("wait", 1.7), ("switch", 220, 180), ("switch", 600, 180), ("wait", 0.4),
				("switch", 220, 220), ("switch", 600, 220), ("wait", 1.7), ("switch", 220, 180), ("switch", 600, 180),
			])],
		],
		'text' : [
			'Cyfrowość elektroniki polega na reprezentacji sygnałów <m> w formie abstrakcyjnych wartości liczbowych, <m> zamiast bezpośredniej wartości elektrycznych.'
			'Liczby te zazwyczaj zapisywane są w systemie dwójkowym.'
			'Napięcie poniżej jakiejś wartości odpowiada zeru na danej cyfrze, <m> natomiast powyżej jakiegoś poziomu jedynce.'
			'Kolejnymi cyframi są napięcia w różnych miejscach obwodu („na kolejnych przewodach”) <m> lub w na pojedynczym przewodzie w kolejnych jednostkach czasu.'
			'Taka reprezentacja w postaci dyskretnych poziomów napięć, <m> identyfikowanych jako zera i jedynki – wartości logicznego fałszu i prawdy, <m>'
				'pozwala między innymi zwiększyć odporność na zakłócenia <m> i bezstratnie replikować taką cyfrową informację. <mark name="bramki" />'
			
			'Podstawowym elementem elektroniki cyfrowej są bramki logiczne, <m> odpowiadają one znanym nam już z programowania <m> funkcjom logicznym takim jak and, or, xor, not. <m>'
			'Elektronicy bardzo często korzystają z zanegowanych <m> wariantów bramek and i or, czyli nand i nor. <m>'
			'Na ekranie widzimy symulacje przedstawiającą działanie różnych bramek. <mark name="_not" />'
			
			'Na górze mamy bramkę not, która zamienia jedynkę na zero, a zero na jedynkę. <m>'
			
			'Jak widać w elektronice również używa się terminów poziom wysoki lub niski. <m>'
			'Wysoki, H oznacza logiczną prawdę, jedynkę, <m> a poziom niski, L oznacza logiczny fałsz, zero. <m>'
			'Najczęściej z tymi poziomami powiązane są wprost odpowiednie poziomy napięć, <m> czyli poziom zasilania (na przykład 5 lub 3.3 wolta) związany będzie <m> ze stanem wysokim, a poziom masy, zero woltów ze stanem niskim. <m>'
			'Niekiedy jednak można spotkać się z logiką odwróconą, <m> gdzie wysokie napięcie oznacza fałsz, a masa, zero woltów prawdę <m> (tak jak mieliśmy to w przypadku basha). <m>'
			'W niektórych przypadkach poziomy napięć związanych ze stanami logicznymi <m> mogą być jeszcze bardziej dziwne - np. fałsz to napięcie dodatnie, <m> a prawda to napięcie ujemne. <mark name="_and" />'
			
			'Poniżej po lewej stronie mamy bramkę AND, <m> której wyjście będzie w stanie wysokim <m> tylko jeżeli oba wejścia będą w takim stanie. <m>'
			'Po prawej jej stronie jest bramka NAND, czyli AND z dodaną negacją na wyjściu, <m> co na symbolu zaznaczone jest kółkiem przy tym wyprowadzeniu <m>'
				'– tak oznaczane są zanegowane wejścia i wyjścia, <m> co widzieliśmy też w samym symbolu bramki NOT, <m> który składa się z symbolu bufora i właśnie takiej negacji. <m>'
		]
	},
	{
		'image': [
			[0.0, eduMovie.circuitjs("bramki", 2, 6, [
				("switch", 220, 330), ("switch", 600, 330), ("wait", 1.7), ("switch", 220, 330), ("switch", 600, 330), ("wait", 0.4),
				("switch", 220, 290), ("switch", 600, 290), ("wait", 1.7), ("switch", 220, 330), ("switch", 600, 330),
			])],
			["_xor", eduMovie.circuitjs("bramki", 2, 6, [
				("switch", 400, 420), ("wait", 1.7), ("switch", 400, 420), ("wait", 0.4),
				("switch", 400, 460), ("wait", 1.7), ("switch", 400, 420)
			])],
			["wielowej+1.5", eduMovie.circuitjs("bramki_multi", 2, 11, [
				("switch", 200, 210), ("wait", 1.1), ("switch", 200, 310), ("wait", 2.4), ("switch", 200, 290), ("wait", 1.1),
				("switch", 610, 260), ("wait", 2.7), ("switch", 610, 240)
			])],
			["scalone", eduMovie.convertFile('chip.svg', margins=0)],
			["esd", eduMovie.convertFile('esd.svg', margins=0)], # TODO może następny obrazek o podłączanie nieużywanych, antenie i energia związana z niepotrzebnym przełączaniem ...
		],
		'text' : [
			'W kolejnym rzędzie mamy bramkę or, <m> która stan wysoki ma wtedy gdy którekolwiek z wejść lub oba są w stanie wysokim <m> i po prawej jej zanegowany wariant nor. <mark name="_xor" />'
			
			'Na dole znajduje się symbol bramki xor, która stan wysoki na wyjściu <m> ma wtedy gdy tylko jedno z jej wejść jest w stanie wysokim. <mark name="wielowej" />'
			
			'Możemy również korzystać z bramek wielowejściowych, zwłaszcza w przypadku <m> funkcji takich jak and i or jest to dobrze zdefiniowane. <m>'
			'And aby podać stan wysoki na wyjście wymaga aby wszystkie wejścia <m> były w stanie wysokim, or wymaga aby co najmniej jedno z nich <m> było w stanie wysokim. <mark name="scalone" />'
			
			'Bramki tak jak wszystkie układy o których dalej będziemy mówić <m> są realizowane w postaci układów scalonych, <m>'
				'czyli zespołu tranzystorów wykonanych na jednym kawałku krzemu <m> i zamkniętych w jednej wielonóżkowej obudowie. <m>'
			
			'Układy scalone wykonywane są obecnie w technologii <CMOS>[C mos], <m> czyli oparte są na tranzystorach N-MOSFET i P-MOSFET. <m>'
			'Zatem dotyczą ich problemy z izolowaniem i pojemnością bramki, <m> o których mówiliśmy przy omawianiu tego typu tranzystorów. <mark name="esd" />'
			
			'Po pierwsze są one wrażliwe na uszkodzenia elektrostatyczne <m> związane z gromadzeniem ładunku na wejściach. <m>'
			'Często jako zabezpieczenia wejść dodawane są diody nie pozwalające <m> aby pojawił się tam potencjał większy od napięcia zasilania a mniejszy od masy. <m>'
			'Stosuje się też zabezpieczenia związane z rozpraszaniem ładunków <m> elektrostatycznych w trakcie przechowywania i montażu. <m>'
			
			'Należy pamiętać że nieużywane i niepodłączone wejście układu <m> działa zasadniczo jak antena i zbiera jakieś ładunki, <m> dlatego też bardzo często wejścia takie łączymy z poziomem masy lub zasilania. <m>'
			'Co paradoksalnie powoduje też oszczędność energii <m> – nie nastąpi samoistne przełączenie, które mogłoby prowadzić do <m> przełączeń innych tranzystorów wewnątrz układu, które kosztowałyby energię. <m>'
			
			'Wynika to z faktu że zużycie energii przez układy scalone związane jest <m> w dużej mierze właśnie z przeładowywaniem tych pojemności w trakcie zmian jakiegoś <m> sygnału wejściowego, potrzeby przełączenia jakiś tranzystorów. <m>'
		]
	},
]

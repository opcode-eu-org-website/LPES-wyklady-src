v 20130925 2
N 54400 53400 55800 53400 4
{
T 54900 53400 5 10 0 1 0 0 1
netname=ctrl_in1
}
T 54500 53500 9 10 1 0 0 0 1
PWM
C 56700 53300 1 0 1 resistor-2.sym
{
T 56700 53300 5 10 0 0 90 6 1
footprint=acy(100.00mil, pin_flags=none, type=standing)
T 56300 53250 5 10 1 1 180 0 1
refdes=R2
T 56000 53700 5 10 1 1 180 6 1
value=100k
}
C 57200 52300 1 90 0 capacitor-1.sym
{
T 57200 52300 5 10 0 0 0 0 1
footprint=acy(100.00mil, type=block, pin_flags=none, pol=none)
T 56300 52500 5 10 0 0 90 0 1
symversion=0.1
T 56900 53000 5 10 1 1 180 0 1
refdes=C1
T 56900 52600 5 10 1 1 180 0 1
value=100n
}
N 57000 53200 57000 53400 4
C 56900 52000 1 0 0 net-gnd-1.sym
{
T 57100 52250 5 5 0 0 0 0 1
net=GND2:1
}
C 57900 52500 1 0 0 operational_amplifier-3.sym
{
T 57900 52500 5 10 0 1 180 0 1
numslots=2
T 57900 52500 5 10 0 1 180 0 1
slot=2
T 57900 52500 5 10 0 1 180 0 1
slotdef=1:3,2,1,8,4
T 57900 52500 5 10 0 0 180 0 1
footprint=dip(8, pin_ringdia=73.00mil)
T 57900 52500 5 10 0 0 180 0 1
slotdef=2:5,6,7,8,4
T 58225 53650 5 10 1 1 0 6 1
refdes=U2
T 58600 52600 5 10 1 1 180 0 1
value=LM358
}
C 58500 53800 1 0 0 net-pwr-1.sym
{
T 58750 53900 5 5 0 0 0 0 1
net=Vcc2:1
T 58700 54150 5 9 1 1 0 5 1
value=Vcc
}
C 58600 52300 1 0 0 net-gnd-1.sym
{
T 58800 52550 5 5 0 0 0 0 1
net=GND2:1
}
N 59400 53200 61500 53200 4
N 56700 53400 58000 53400 4
N 57800 53000 58000 53000 4
N 57800 52100 57800 53000 4
N 57800 52100 59500 52100 4
N 59500 53200 59500 52100 4
L 53675 52625 53675 53000 3 0 0 0 -1 -1
L 53675 53000 53850 53000 3 0 0 0 -1 -1
L 53850 53000 53850 52625 3 0 0 0 -1 -1
L 53850 52625 54175 52625 3 0 0 0 -1 -1
L 54175 53000 54175 52625 3 0 0 0 -1 -1
L 54175 53000 54375 53000 3 0 0 0 -1 -1
L 54375 53000 54375 52625 3 0 0 0 -1 -1
L 54375 52625 54675 52625 3 0 0 0 -1 -1
L 54675 53000 54675 52625 3 0 0 0 -1 -1
L 54675 53000 54925 53000 3 0 0 0 -1 -1
L 54925 53000 54925 52625 3 0 0 0 -1 -1
L 54925 52625 55175 52625 3 0 0 0 -1 -1
L 55175 53000 55175 52625 3 0 0 0 -1 -1
L 55175 53000 55250 53000 3 0 0 0 -1 -1
L 53675 52625 53600 52625 3 0 0 0 -1 -1
T 59925 53475 9 10 1 0 0 0 2
      analogowy
sygnał napięciowy
A 60400 52800 200 0 180 3 0 0 0 -1 -1
A 60800 52800 200 180 180 3 0 0 0 -1 -1

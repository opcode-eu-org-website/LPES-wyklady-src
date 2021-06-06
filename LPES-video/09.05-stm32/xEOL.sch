v 20130925 2
C 52800 34200 1 0 1 resistor-2.sym
{
T 52500 34500 5 10 1 1 180 2 1
refdes=Rt
}
N 52800 33800 52900 33800 4
N 52900 33100 52900 34300 4
N 52800 33100 52900 33100 4
C 52800 33700 1 0 1 resistor-2.sym
{
T 52500 33500 5 10 1 1 180 2 1
refdes=Ra
}
N 51800 33800 51800 33100 4
N 51800 33100 51900 33100 4
C 49300 35100 1 0 1 net-pwr-1.sym
{
T 49100 35450 5 9 1 1 0 5 1
value=Vcc
}
C 49200 33200 1 0 1 net-gnd-1.sym
C 49000 34100 1 270 1 resistor-2.sym
{
T 49300 34400 5 10 1 1 90 2 1
refdes=Rx
}
C 48100 33900 1 0 0 terminal-end_line.sym
{
T 48525 34150 5 10 1 1 0 3 1
refdes=ADC_in
}
N 48800 34000 51800 34000 4
C 53100 33700 1 90 1 contact-generic.sym
{
T 52400 33000 5 10 1 1 0 5 1
refdes=monitorowany styk
}
N 52800 34300 52900 34300 4
N 51900 34300 51800 34300 4
N 51800 34300 51800 34000 4
N 51900 33800 49100 33800 4
N 49100 35100 49100 35000 4
N 49100 33800 49100 33500 4
N 49100 34100 49100 34000 4
T 50500 33900 9 8 1 0 0 4 1
przewód
B 49300 33700 2400 400 3 0 0 0 -1 -1 0 -1 -1 -1 -1 -1
T 49100 32400 9 10 1 0 0 2 2
stan

T 50750 32050 9 10 1 0 0 2 2
→ Vcc · Rx/(Rx+Rt+Ra)
→ Vcc · Rx/(Rx+Rt)
L 49100 32200 53000 32200 3 20 0 0 -1 -1
T 50750 32400 9 10 1 0 0 2 2
→ wartość napięcia na ADC

T 49100 32050 9 10 1 0 0 2 2
styk rozwarty
styk zwarty
T 50750 31600 9 10 1 0 0 2 2
→ Vcc
→ 0
T 49100 31600 9 10 1 0 0 2 2
przewód przerwany
przewód zwarty

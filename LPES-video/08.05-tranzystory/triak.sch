v 20130925 2
C 46400 47700 1 0 1 triac-1.sym
N 46400 48000 46600 48000 4
C 47200 47700 1 0 1 contact-generic.sym
{
T 47000 48000 5 10 1 1 90 0 1
refdes=Sterowanie
}
N 44200 48900 46000 48900 4
N 45800 48700 45800 48900 4
N 45800 47700 45800 47600 4
N 45800 47600 45450 47600 4
C 45450 47500 1 0 1 resistor-2.sym
{
T 45050 47850 5 10 0 0 0 6 1
device=RESISTOR
T 45450 47300 5 10 1 1 0 6 1
refdes=Obciążenie
}
N 44550 47600 44200 47600 4
C 44000 47850 1 270 1 voltage-1.sym
{
T 44500 47950 5 10 0 0 90 2 1
device=VOLTAGE_SOURCE
}
N 44200 48750 44200 48900 4
N 44200 47850 44200 47600 4
C 42950 47900 1 0 1 triac-1.sym
C 46500 48800 1 90 0 resistor-small.sym
N 46500 48900 46600 48900 4
T 41800 49150 9 10 1 0 0 0 1
Symbol triaka:
T 43800 49150 9 10 1 0 0 0 1
Przykładowa aplikacja:

import math
#Kat w przedziale 0 <= kat < 360:
def anglecheck(x):

    while x < 0:
        x = x + 360
    while x >= 360:
        x = x - 360
    return x

leftwidth = 30
rightwidth = 20
y = 2020
mo = 5
d = 24
phi = 51.47
long = 19.21
#Ile dni do od poczatku i do konca roku
#y = int(input('Rok: '))
#mo = int(input('Miesiac: '))

if mo > 12 and mo < 1:
    quit()
#d = int(input('Dzien: '))
if d > 31 and d < 1:
    quit()
if mo == 2 and d > 29:
    quit()
strefa = 2
he = -0.83333 #Wschod / zachod
he1 = -6 #W/Z cywilny
he2 = -12 #W/Z morski
he3 = -18 #W/Z astronomiczny
print('\n')
#phi = float(input('Latitude (szerokosc): '))
#long = float(input('Longitude (dlugosc): '))
print('\n')
#Lata przestepne
p400 = y % 400
p100 = y % 100
p4 = y % 4

if p400 == 0:
    ildni = int(366)
elif p4 == 0 and p100 != 0:
    ildni = int(366)
else:
    ildni = int(365)

if mo == 2 and ildni == 365 and d == 29:
    quit()

#Miesiace
miechy = {'1': '31', '2': '28', '3': '31', '4': '30', '5': '31', '6': '30', '7': '31', '8': '31', '9': '30', '10': '31', '11': '30', '12': '31'}
miechyp = {'1': '31', '2': '29', '3': '31', '4': '30', '5': '31', '6': '30', '7': '31', '8': '31', '9': '30', '10': '31', '11': '30', '12': '31'}

i = 1
sum = 0
if ildni == 365:
    while i < mo:
        sum = sum + int(miechy[str(i)])
        i = i + 1
    sum = sum + d
    rest = ildni - sum
    print('%s.%s.%s jest to %s dzien roku, do konca roku pozostalo %s.' % (y, mo, d, sum, rest))
if ildni == 366:
    while i < mo:
        sum = sum + int(miechyp[str(i)])
        i = i + 1
    sum = sum + d
    rest = ildni - sum
    print('%s.%s.%s jest to %s dzien roku, do konca roku pozostalo %s.' % (y, mo, d, sum, rest))

#Dni do 01.01.2000
dist = 0
if y >= 2000:
    yg = y - 1
    yd = 2000
    while yg >= 2000:
        # Lata przestepne
        p400 = yg % 400
        p100 = yg % 100
        p4 = yg % 4
        if p400 == 0:
            ildni = int(366)
        elif p4 == 0 and p100 != 0:
            ildni = int(366)
        else:
            ildni = int(365)

        dist = dist + ildni
        yg = yg - 1
    dist = dist + sum - 1.5
    print('Dni do 1.1.2000r.: %s' % (dist))

if y < 2000:
    yg = 2000
    yd = y + 1
    while yd < 2000:
        # Lata przestepne
        p400 = yd % 400
        p100 = yd % 100
        p4 = yd % 4
        if p400 == 0:
            ildni = int(366)
        elif p4 == 0 and p100 != 0:
            ildni = int(366)
        else:
            ildni = int(365)
        dist = dist + ildni
        yd = yd + 1
    dist = -(dist + rest + 1.5)
    print('Dni do 1.1.2000r.: %s\n' % (dist))
print('\n')
i = 0
print('Poprawka[%s]'.center(leftwidth + rightwidth - 5, '#') % (i))
t = (dist) / 36525
#Mean longitude including aberration
L = 280.460 + 36000.770 * t
L = anglecheck(L)
#Mean anomaly
G = 357.528 + 35999.050 * t
G = anglecheck(G)
#eq centre correction
ec = 1.915 * math.sin(math.pi * G / 180) + 0.020 * math.sin(math.pi * 2 * G / 180)
#ecliptic longitude of Sun
lamb = L + ec
#
UT0 = 180
UT = 180
UT1 = 180
UT2 = 180
UT3 = 180
E = -ec + 2.466 * math.sin (math.pi * 2 * lamb / 180) - 0.053 * math.sin(math.pi * 4 * lamb / 180)
GHA = UT - 180 + E
GHA1 = UT1 - 180 + E
GHA2 = UT2 - 180 + E
GHA3 = UT3 - 180 + E
obl = 23.4393 - 0.0130 * t
#Sun declination
delta = 180 * math.asin(math.sin(math.pi * obl / 180) * math.sin(math.pi * lamb / 180)) / math.pi
cosc = (math.sin(math.radians(he)) - math.sin(math.radians(phi)) * math.sin(math.radians(delta))) / (math.cos(math.radians(phi)) * (math.cos(math.radians(delta))))
cosc1 = (math.sin(math.radians(he1)) - math.sin(math.radians(phi)) * math.sin(math.radians(delta))) / (math.cos(math.radians(phi)) * (math.cos(math.radians(delta))))
cosc2 = (math.sin(math.radians(he2)) - math.sin(math.radians(phi)) * math.sin(math.radians(delta))) / (math.cos(math.radians(phi)) * (math.cos(math.radians(delta))))
cosc3 = (math.sin(math.radians(he3)) - math.sin(math.radians(phi)) * math.sin(math.radians(delta))) / (math.cos(math.radians(phi)) * (math.cos(math.radians(delta))))

if cosc > 1:
    correction = 0
if cosc < -1:
    correction = 180
if cosc <=1 and cosc >= -1:
    correction = 180 * math.acos(cosc) / math.pi

if cosc1 > 1:
    correction1 = 0
if cosc1 < -1:
    correction1 = 180
if cosc1 <=1 and cosc1 >= -1:
    correction1 = 180 * math.acos(cosc1) / math.pi

if cosc2 > 1:
    correction2 = 0
if cosc2 < -1:
    correction2 = 180
if cosc2 <=1 and cosc2 >= -1:
    correction2 = 180 * math.acos(cosc2) / math.pi

if cosc3 > 1:
    correction3 = 0
if cosc3 < -1:
    correction3 = 180
if cosc3 <=1 and cosc3 >= -1:
    correction3 = 180 * math.acos(cosc3) / math.pi

UT = UT - (GHA + long + correction)
UT1 = UT1 - (GHA1 + long + correction1)
UT2 = UT2 - (GHA2 + long + correction2)
UT3 = UT3 - (GHA3 + long + correction3)
UTtrans = - (GHA + long)
UTset = UT - (GHA + long - correction)
UT1set = UT1 - (GHA1 + long - correction1)
UT2set = UT2 - (GHA2 + long - correction2)
UT3set = UT3 - (GHA3 + long - correction3)


h = int(UT / 15) + strefa
m = int((UT / 15 - int(UT / 15)) * 60)
s = ((UT / 15 - int(UT / 15)) * 60 - m) * 60

h1 = int(UT1 / 15) + strefa
m1 = int((UT1 / 15 - int(UT1 / 15)) * 60)
s1 = ((UT1 / 15 - int(UT1 / 15)) * 60 - m1) * 60

h2 = int(UT2 / 15) + strefa
m2 = int((UT2 / 15 - int(UT2 / 15)) * 60)
s2 = ((UT2 / 15 - int(UT2 / 15)) * 60 - m2) * 60

h3 = int(UT3 / 15) + strefa
m3 = int((UT3 / 15 - int(UT3 / 15)) * 60)
s3 = ((UT3 / 15 - int(UT3 / 15)) * 60 - m3) * 60

htrans = int(UTtrans / 15) + strefa
mtrans = int((UTtrans / 15 - int(UTtrans / 15)) * 60)
strans = ((UTtrans / 15 - int(UTtrans / 15)) * 60 - mtrans) * 60

hset = int(UTset / 15) + strefa
mset = int((UTset / 15 - int(UTset / 15)) * 60)
sset = ((UTset / 15 - int(UTset / 15)) * 60 - mset) * 60

h1set = int(UT1set / 15) + strefa
m1set = int((UT1set / 15 - int(UT1set / 15)) * 60)
s1set = ((UT1set / 15 - int(UT1set / 15)) * 60 - m1set) * 60

h2set = int(UT2set / 15) + strefa
m2set = int((UT2set / 15 - int(UT2set / 15)) * 60)
s2set = ((UT2set / 15 - int(UT2set / 15)) * 60 - m2set) * 60

h3set = int(UT3set / 15) + strefa
m3set = int((UT3set / 15 - int(UT3set / 15)) * 60)
s3set = ((UT3set / 15 - int(UT3set / 15)) * 60 - m3set) * 60

print('Astr. sunrise: '.ljust(leftwidth, '.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6, '.')) % (h3, m3, s3))
print('Naut. sunrise: '.ljust(leftwidth, '.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6, '.')) % (h2, m2, s2))
print('Civ. sunrise: '.ljust(leftwidth, '.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6, '.')) % (h1, m1, s1))
print('App. sunrise: '.ljust(leftwidth, '.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6, '.')) % (h, m, s))
print('#'.center(leftwidth + rightwidth - 5, '#'))
print('Transit: '.ljust(leftwidth, '.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6, '.')) % (htrans, mtrans, strans))
print('#'.center(leftwidth + rightwidth - 5, '#'))
print('App. sunset: '.ljust(leftwidth, '.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6, '.')) % (hset, mset, sset))
print('Civ. sunset: '.ljust(leftwidth, '.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6, '.')) % (h1set, m1set, s1set))
print('Naut. sunset: '.ljust(leftwidth, '.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6, '.')) % (h2set, m2set, s2set))
print('Astr. sunset: '.ljust(leftwidth, '.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6, '.')) % (h3set, m3set, s3set))
print('#'.center(leftwidth + rightwidth - 5, '#'))
print('\n')
i = 1
UTp = 1
#Poprawka
while abs(UT - UTp) > 0.0001:
    print('Poprawka[%s]'.center(leftwidth + rightwidth - 5,'#') % (i))
    UTp = UT
    t = (dist + UT / 360) / 36525
    #Mean longitude including aberration
    L = 280.460 + 36000.770 * t
    L = anglecheck(L)
    #Mean anomaly
    G = 357.528 + 35999.050 * t
    G = anglecheck(G)
    #eq centre correction
    ec = 1.915 * math.sin(math.pi * G / 180) + 0.020 * math.sin(math.pi * 2 * G / 180)
    #ecliptic longitude of Sun
    lamb = L + ec
    #
    E = -ec + 2.466 * math.sin (math.pi * 2 * lamb / 180) - 0.053 * math.sin(math.pi * 4 * lamb / 180)
    GHA = UT - 180 + E
    GHA1 = UT1 - 180 + E
    GHA2 = UT2 - 180 + E
    GHA3 = UT3 - 180 + E
    obl = 23.4393 - 0.0130 * t
    #Sun declination
    delta = 180 * math.asin(math.sin(math.pi * obl / 180) * math.sin(math.pi * lamb / 180)) / math.pi
    cosc = (math.sin(math.radians(he)) - math.sin(math.radians(phi)) * math.sin(math.radians(delta))) / (math.cos(math.radians(phi)) * (math.cos(math.radians(delta))))
    cosc1 = (math.sin(math.radians(he1)) - math.sin(math.radians(phi)) * math.sin(math.radians(delta))) / (math.cos(math.radians(phi)) * (math.cos(math.radians(delta))))
    cosc2 = (math.sin(math.radians(he2)) - math.sin(math.radians(phi)) * math.sin(math.radians(delta))) / (math.cos(math.radians(phi)) * (math.cos(math.radians(delta))))
    cosc3 = (math.sin(math.radians(he3)) - math.sin(math.radians(phi)) * math.sin(math.radians(delta))) / (math.cos(math.radians(phi)) * (math.cos(math.radians(delta))))

    if cosc > 1:
        correction = 0
    if cosc < -1:
        correction = 180
    if cosc <=1 and cosc >= -1:
        correction = 180 * math.acos(cosc) / math.pi

    if cosc1 > 1:
        correction1 = 0
    if cosc1 < -1:
        correction1 = 180
    if cosc1 <= 1 and cosc1 >= -1:
        correction1 = 180 * math.acos(cosc1) / math.pi

    if cosc2 > 1:
        correction2 = 0
    if cosc2 < -1:
        correction2 = 180
    if cosc2 <= 1 and cosc2 >= -1:
        correction2 = 180 * math.acos(cosc2) / math.pi

    if cosc3 > 1:
        correction3 = 0
    if cosc3 < -1:
        correction3 = 180
    if cosc3 <= 1 and cosc3 >= -1:
        correction3 = 180 * math.acos(cosc3) / math.pi

    UT = UT - (GHA + long + correction)
    UT1 = UT1 - (GHA1 + long + correction1)
    UT2 = UT2 - (GHA2 + long + correction2)
    UT3 = UT3 - (GHA3 + long + correction3)
    UTtrans =  UT - (GHA + long)
    UTset = UT - (GHA + long - correction)
    UT1set = UT1 - (GHA1 + long - correction1)
    UT2set = UT2 - (GHA2 + long - correction2)
    UT3set = UT3 - (GHA3 + long - correction3)

    h = int(UT / 15) + strefa
    m = int((UT / 15 - int(UT / 15)) * 60)
    s = ((UT / 15 - int(UT / 15)) * 60 - m) * 60

    h1 = int(UT1 / 15) + strefa
    m1 = int((UT1 / 15 - int(UT1 / 15)) * 60)
    s1 = ((UT1 / 15 - int(UT1 / 15)) * 60 - m1) * 60

    h2 = int(UT2 / 15) + strefa
    m2 = int((UT2 / 15 - int(UT2 / 15)) * 60)
    s2 = ((UT2 / 15 - int(UT2 / 15)) * 60 - m2) * 60

    h3 = int(UT3 / 15) + strefa
    m3 = int((UT3 / 15 - int(UT3 / 15)) * 60)
    s3 = ((UT3 / 15 - int(UT3 / 15)) * 60 - m3) * 60

    htrans = int(UTtrans / 15) + strefa
    mtrans = int((UTtrans / 15 - int(UTtrans / 15)) * 60)
    strans = ((UTtrans / 15 - int(UTtrans / 15)) * 60 - mtrans) * 60

    hset = int(UTset / 15) + strefa
    mset = int((UTset / 15 - int(UTset / 15)) * 60)
    sset = ((UTset / 15 - int(UTset / 15)) * 60 - mset) * 60

    h1set = int(UT1set / 15) + strefa
    m1set = int((UT1set / 15 - int(UT1set / 15)) * 60)
    s1set = ((UT1set / 15 - int(UT1set / 15)) * 60 - m1set) * 60

    h2set = int(UT2set / 15) + strefa
    m2set = int((UT2set / 15 - int(UT2set / 15)) * 60)
    s2set = ((UT2set / 15 - int(UT2set / 15)) * 60 - m2set) * 60

    h3set = int(UT3set / 15) + strefa
    m3set = int((UT3set / 15 - int(UT3set / 15)) * 60)
    s3set = ((UT3set / 15 - int(UT3set / 15)) * 60 - m3set) * 60

    print('Astr. sunrise: '.ljust(leftwidth,'.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6,'.')) % (h3, m3, s3))
    print('Naut. sunrise: '.ljust(leftwidth,'.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6,'.')) % (h2, m2, s2))
    print('Civ. sunrise: '.ljust(leftwidth,'.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6,'.')) % (h1, m1, s1))
    print('App. sunrise: '.ljust(leftwidth,'.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6,'.')) % (h, m, s))
    print('#'.center(leftwidth + rightwidth - 5,'#'))
    print('Transit: '.ljust(leftwidth,'.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6,'.')) % (htrans, mtrans, strans))
    print('#'.center(leftwidth + rightwidth - 5,'#'))
    print('App. sunset: '.ljust(leftwidth,'.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6,'.')) % (hset, mset, sset))
    print('Civ. sunset: '.ljust(leftwidth,'.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6,'.')) % (h1set, m1set, s1set))
    print('Naut. sunset: '.ljust(leftwidth,'.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6,'.')) % (h2set, m2set, s2set))
    print('Astr. sunset: '.ljust(leftwidth,'.') + ('%sh %sm %0.4fs'.rjust(rightwidth - 6,'.')) % (h3set, m3set, s3set))
    print('#'.center(leftwidth + rightwidth - 5,'#'))
    print('\n')
    i = i + 1
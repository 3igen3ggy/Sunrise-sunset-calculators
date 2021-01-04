import math
y = 2020
mo = 5
d = 14
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

#WLASCIWY PROGRAM Z WIKI.ORG
n = dist
# mean solar noon
J = n - long / 360
#solar mean anomaly
M = (357.5291 + 0.98560028 * J) % 360
#eq. of center
C = 1.9148*math.sin(math.radians(M)) + 2e-2*math.sin(math.radians(2 * M)) + 3e-4 * math.sin(math.radians(3 * M))
#ecliptic longitude
lamb = (M + C + 180 + 102.9372) % 360
#solar trasit
Jtransit = 2451545 + J + 53e-4 * math.sin(math.radians(M)) - 69e-4 * math.sin(math.radians(2 * lamb))
#sun declination
sindelta = (math.sin(math.radians(lamb)) * math.sin(math.radians(23.44)))
delta = math.degrees(math.asin(sindelta))
#hour angle
cosc = ((math.sin(math.radians(-0.833)) - math.sin(math.radians(phi)) * math.sin(math.radians(delta))) / (math.cos(math.radians(phi)) * math.cos(math.radians(delta))))
c = math.degrees(math.acos(cosc))
Jrise = Jtransit - c / 360
Jset = Jtransit + c /360

hrise = (Jrise - int(Jrise)) * 24 + strefa
mrise = (hrise - int(hrise)) * 60
srise = (mrise - int(mrise)) * 60
print(int(hrise))
print(int(mrise))
print(srise)

htran = (Jtransit - int(Jtransit)) * 24 + strefa
mtran = (htran - int(htran)) * 60
stran = (mtran - int(mtran)) * 60
print(int(htran))
print(int(mtran))
print(stran)

hset = (Jset - int(Jset)) * 24 + strefa
mset = (hset - int(hset)) * 60
sset = (mset - int(mset)) * 60
print(int(hset))
print(int(mset))
print(sset)
#print(Jset)
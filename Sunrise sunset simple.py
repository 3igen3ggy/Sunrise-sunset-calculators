import math
import time
#Kat w przedziale 0 <= kat < 360:
def anglecheck(x):

    while x < 0:
        x = x + 360
    while x >= 360:
        x = x - 360
    return x

coordstype = int(input('''Coordinates input:
1. Decimal degrees (51.47, 19.21)
2. D M\' S\'\' (51 28\' 00\'\'N, 19 13\' 00\'\'E)
3. Choose particular city
Choice [1/2/3]: '''))

if coordstype == 1:
    print('''Latitude range: +/-90
Longitude range: +/- 180''')
    sz = float(input('Latitude (N+ S-): '))
    if sz < -90 or sz > 90:
        print('Wrong latitude')
        quit()
    dl = float(input('Longitude (E+ W-): '))
    if dl < -180 or dl > 180:
        print('Wrong longitude')
        quit()
if coordstype == 2:
    print('''Latitude range: 90 N/S
Longitude range: 180 E/W
''')
    szside = input('Lat. side N/S: ')
    dlside = input('Long. side E/W: ')

    szd = float(int(input('Lat. deg: ')))
    szm = float(int(input('Lat. min: ')))
    szs = float(input('Lat. sec: '))

    if sz < -90 or sz > 90:
        print('Wrong latitude')
        quit()

    dld = float(int(input('Long. deg: ')))
    dlm = float(int(input('Long. min: ')))
    dls = float(input('Long. sec: '))

    if dl < -180 or dl > 180:
        print('Wrong longitude')
        quit()

    sides = {'N': 1, 'S': -1, 'E': 1, 'W': -1}
    sz = (szd + szm / 60 + szs / 3600) * sides[szside]
    dl = (dld + dlm / 60 + dls / 3600) * sides[dlside]
########################################################################################################################
#########################TESTING CITIES#########################
if coordstype == 3:
    city = int(input('''Choose city:
    1. ZLW [PL] (51.47, 19.21)
    2. Iqaluit [CND] (63,75, -68.52)
    3. Ushuaia [ARG] (-54.8, -68.3)
    4. Sydney [AUS] (-33.87, 151.2)
    5. New York [USA] (40.66, -73.94)
    6. San Francisco [USA] (37.78, -122.41)
    Choice [1/2/3/4/5/6]: '''))
    if city == 1:
        sz = 51.47
        dl = 19.21
        utc = 2
    if city == 2:
        sz = 63.75
        dl = -68.52
        utc = -2.5
    if city == 3:
        sz = -54.8
        dl = -68.3
        utc = -3
    if city == 4:
        sz = -33.87
        dl = 151.2
        utc = 10.5
    if city == 5:
        sz = 40.66
        dl = -73.94
        utc = -4
    if city == 6:
        sz = 37.78
        dl = -122.41
        utc = -8
    if city != 1 and city != 2 and city != 3 and city != 4 and city != 5 and city != 6:
        print('Wrong city')
        quit()
########################################################################################################################
if coordstype != 1 and coordstype != 2 and coordstype != 3:
    print('Wrong choice')
    quit()

########################################################################################################################
########################################################################################################################
if coordstype != 3:
    utc = int(input('Enter timezone UTC (ranges from -12 to 14). Use full number: '))
if utc <= -12 or utc >= 14:
    print('Wrong UTC')
    quit()

y = int(input('Year: '))
mo = int(input('Month: '))
if mo > 12:
    quit()
d = int(input('Day: '))
if d > 31:
    quit()
if mo == 2 and d > 29:
    quit()

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
    print('''%s.%s.%s is %s day of a year, till end of the year there is %s days left.
    ''' % (y, mo, d, sum, rest))
elif ildni == 366:
    while i < mo:
        sum = sum + int(miechyp[str(i)])
        i = i + 1

    sum = sum + d
    rest = ildni - sum
    print('''%s.%s.%s is %s day of a year, till end of the year there is %s days left.
    ''' % (y, mo, d, sum, rest))
sum = sum + 0.5
dec = 23.44 * math.sin(math.pi * 2 * (sum - 80) / 365.25)

########################################################################################################################
########################################################################################################################
#EOT
ecc = 7.66 * math.sin(math.pi * 2 * (sum - 2) / 365.25)
obl = 9.87 * math.sin(math.pi * 4 * (sum + 10) / 365.25)
eot = ecc + obl

eotem = int(ecc)
eotes = math.fabs(ecc - eotem) * 60

eotom = int(obl)
eotos = math.fabs(obl - eotom) * 60

eotm = int(eot)
eots = math.fabs(eot - eotm) * 60

#Dec
decd = int(dec)
decm = int((dec - decd) * 60)
decs = (((dec - decd) * 60) - decm) * 60

sunalt = 90 - math.fabs(dec - sz)
########################################################################################################################
########################################################################################################################

app = math.sin(math.radians(-0.833))
civ = math.sin(math.radians(-6))
naut = math.sin(math.radians(-12))
astr = math.sin(math.radians(-18))

tran = utc * 15 - dl + 12 * 15 + eot * 15 / 60
tranh = int(tran / 15)
tranm = int((tran / 15 - tranh) * 60)
trans = ((tran / 15 - tranh) * 60 - tranm) * 60

cosca = (app - math.sin(math.radians(sz)) * math.sin(math.radians(dec))) / (math.cos(math.radians(sz)) * math.cos(math.radians(dec)))
coscc = (civ - math.sin(math.radians(sz)) * math.sin(math.radians(dec))) / (math.cos(math.radians(sz)) * math.cos(math.radians(dec)))
coscn = (naut - math.sin(math.radians(sz)) * math.sin(math.radians(dec))) / (math.cos(math.radians(sz)) * math.cos(math.radians(dec)))
coscas = (astr - math.sin(math.radians(sz)) * math.sin(math.radians(dec))) / (math.cos(math.radians(sz)) * math.cos(math.radians(dec)))

if -1 <= cosca <= 1:
    ca = math.degrees(math.acos(cosca))
else:
    ca = str('no')

if -1 <= coscc <= 1:
    cc = math.degrees(math.acos(coscc))
else:
    cc = str('no')

if -1 <= coscn <= 1:
    cn = math.degrees(math.acos(coscn))
else:
    cn = str('no')

if -1 <= coscas <= 1:
    cas = math.degrees(math.acos(coscas))
else:
    cas = str('no')

print('''Sun declination: %.5f
Sun declination: %s %s\' %.2f\'\' ''' % (dec, decd, decm, decs))
print('''EoT (dec min): %.5f, (ecc): %.5f, (obl): %.5f 
EoT (minutes): %s:%.2f, (ecc): %s:%.2f, (obl): %s:%.2f
''' % (eot, ecc, obl, eotm, eots, eotem, eotes, eotom, eotos))
#Sunrise
if isinstance(cas, str) == False:
    setas = tran - cas
    setash = int(setas / 15)
    setasm = int((setas / 15 - setash) * 60)
    setass = ((setas / 15 - setash) * 60 - setasm) * 60
    print('Astronomical sunrise: %s:%s:%.2f' % (setash, setasm, setass))
else:
    print('Astronomical sunrise: --:--:--')

if isinstance(cn, str) == False:
    setn = tran - cn
    setnh = int(setn / 15)
    setnm = int((setn / 15 - setnh) * 60)
    setns = ((setn / 15 - setnh) * 60 - setnm) * 60
    print('Nautical sunrise: %s:%s:%.2f' % (setnh, setnm, setns))
else:
    print('Nautical sunrise: --:--:--')

if isinstance(cc, str) == False:
    setc = tran - cc
    setch = int(setc / 15)
    setcm = int((setc / 15 - setch) * 60)
    setcs = ((setc / 15 - setch) * 60 - setcm) * 60
    print('Civil sunrise: %s:%s:%.2f' % (setch, setcm, setcs))
else:
    print('Civil sunrise: --:--:--')

if isinstance(ca, str) == False:
    seta = tran - ca
    setah = int(seta / 15)
    setam = int((seta / 15 - setah) * 60)
    setas = ((seta / 15 - setah) * 60 - setam) * 60
    print('Apparent sunrise: %s:%s:%.2f' % (setah, setam, setas))
else:
    print('Apparent sunrise: --:--:--')

if sunalt <= 0:
    print('''
Transit time: --:--:--''')
    print('''Sun transit alt: --.--
#####POLAR NIGHT#####
    ''')
if sunalt > 0 and isinstance(ca, str) == False:
    print('''
Transit time: %s:%s:%.2f''' % (tranh, tranm, trans))
    print('''Sun transit alt: %.4f
    ''' % (sunalt))

if sunalt > 0 and isinstance(ca, str) == True:
    print('''
Transit time: %s:%s:%.2f''' % (tranh, tranm, trans))
    print('''Sun transit alt: %.4f
######POLAR DAY######
            ''' % (sunalt))

#Sunset
if isinstance(ca, str) == False:
    seta = tran + ca
    setah = int(seta / 15)
    setam = int((seta / 15 - setah) * 60)
    setas = ((seta / 15 - setah) * 60 - setam) * 60
    print('Apparent sunset: %s:%s:%.2f' % (setah, setam, setas))
else:
    print('Apparent sunset: --:--:--')

if isinstance(cc, str) == False:
    setc = tran + cc
    setch = int(setc / 15)
    setcm = int((setc / 15 - setch) * 60)
    setcs = ((setc / 15 - setch) * 60 - setcm) * 60
    print('Civil sunset: %s:%s:%.2f' % (setch, setcm, setcs))
else:
    print('Civil sunset: --:--:--')

if isinstance(cn, str) == False:
    setn = tran + cn
    setnh = int(setn / 15)
    setnm = int((setn / 15 - setnh) * 60)
    setns = ((setn / 15 - setnh) * 60 - setnm) * 60
    print('Nautical sunset: %s:%s:%.2f' % (setnh, setnm, setns))
else:
    print('Nautical sunset: --:--:--')

if isinstance(cas, str) == False:
    setas = tran + cas
    setash = int(setas / 15)
    setasm = int((setas / 15 - setash) * 60)
    setass = ((setas / 15 - setash) * 60 - setasm) * 60
    print('Astronomical sunset: %s:%s:%.2f' % (setash, setasm, setass))
else:
    print('Astronomical sunrset: --:--:--')
time.sleep(600)
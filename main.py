class Aircraft:
    def __init__(self, name, MLWeight, MWeight, MPayload, S,
                 CD0app, CD2app, CD0clean, CD2clean, Hp,
                 CTDescH, CTDescL, CTDescApp, CT1, CT2, CT3,
                 CF1, CF2):

        self.name = name
        self.MLWeight = MLWeight
        self.MWeight = MWeight
        self.MPayload = MPayload
        self.S = S
        self.CD0app = CD0app
        self.CD2app = CD2app
        self.CD0clean = CD0clean
        self.CD2clean = CD2clean
        self.Hp = Hp
        self.CTDescH = CTDescH
        self.CTDescL = CTDescL
        self.CTDescApp = CTDescApp
        self.CT1 = CT1
        self.CT2 = CT2
        self.CT3 = CT3
        self.CF1 = CF1
        self.CF2 = CF2


# Datos
names = ["B767-300ER", "B777-300", "B737", "A320-212", "A319-131"]

MLWeight = [0.145150E+03, 0.237680E+03, 0.51710E+02, 0.64500E+02, 0.61000E+02]
MWeight = [0.20410E+03, 0.29930E+03, 0.70800E+02, 0.77000E+02, 0.70000E+02]
MPayload = [0.46500E+02, 0.64900E+02, 0.16920E+02, 0.21500E+02, 0.17000E+02]

S = [0.28350E+03, 0.42804E+03, 0.12465E+03, 0.12260E+03, 0.12260E+03]

CD0app = [0.14000E-01, 0.17300E-01, 0.27000E-01, 0.24200E-01, 0.28400E-01]
CD2app = [0.49000E-01, 0.48400E-01, 0.44100E-01, 0.46900E-01, 0.37600E-01]

CD0clean = [0.17400E-01, 0.15700E-01, 0.23500E-01, 0.24000E-01, 0.28000E-01]
CD2clean = [0.45900E-01, 0.42000E-01, 0.44500E-01, 0.37500E-01, 0.31000E-01]

Hp = [26418, 36122, 30152, 12398, 27726]

CTDescH = [0.64359E-1, 0.44239E-1, 0.36336E-1, 0.45711E-1, 0.83084E-1]
CTDescL = [0.55988E-1, 0.41065E-1, 0.53395E-1, 0.27207E-1, 0.51765E-1]
CTDescApp = [0.12475, 0.92921E-1, 0.16440, 0.13981, 0.14767]

CT1 = [.35167E+06, .42577E+06, .14573E+06, .13605E+06, .13900E+06]
CT2 = [.44673E+05, .48987E+05, .55638E+05, .52238E+05, .58900E+05]
CT3 = [.10129E-09, .66146E-10, .14200E-10, .26637E-10, .57200E-14]

CF1 = [.54005E+00, .87843E+00, .94680E+00, .94000E+00, .68800E+00]
CF2 = [.55782E+03, .36897E+04, .10000E+15, .10000E+06, .16700E+04]


# Crear los aircraft
aircrafts = []

for i in range(len(names)):
    aircraft = Aircraft(
        names[i],
        MLWeight[i],
        MWeight[i],
        MPayload[i],
        S[i],
        CD0app[i],
        CD2app[i],
        CD0clean[i],
        CD2clean[i],
        Hp[i],
        CTDescH[i],
        CTDescL[i],
        CTDescApp[i],
        CT1[i],
        CT2[i],
        CT3[i],
        CF1[i],
        CF2[i]
    )

    aircrafts.append(aircraft)

T0 = 288.15
hf = 0
h = hf * 0.3048
P0 = 1013.25
R = 8.314

T = T0 - 1.98*(hf/1000)
P = P0 * ((1-0.0065*(h/T0))**5.2561)

p = (P/R*T)/10000
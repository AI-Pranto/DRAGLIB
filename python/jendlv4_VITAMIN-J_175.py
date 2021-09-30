#!/usr/local/bin/python
from PyNjoy import *
import os

endfb = PyNjoy()
evaluationDir = os.getcwd() + "/jendl40-or-up_20160106/"
endfb.evaluationName = os.getcwd() + "/output/JENDL-4.0"
endfb.execDir = "PyNjoy2016/bld"
endfb.nstr = 17
endfb.iwt = 4
endfb.Espectra = None
endfb.autolib = (22.53556, 1.11377e4, 0.0005)

endfb.legendre = 3
endfb.hmat = "H1_H2O"
endfb.mat = 125
endfb.evaluationFile = evaluationDir + "H001.dat"
endfb.scatteringLaw =  evaluationDir + "tsl-HinH2O.dat"
endfb.scatteringMat = 1
endfb.temperatures = ( 296., 350., 400., 450., 500., 600., 800., 1000. )
endfb.fission = None
endfb.dilutions = None
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.legendre = 1
endfb.hmat = "H2_D2O"
endfb.mat = 128
endfb.evaluationFile = evaluationDir + "H002.dat"
endfb.scatteringLaw = evaluationDir + "tsl-DinD2O.dat"
endfb.scatteringMat = 11
endfb.temperatures = ( 296., 350., 400., 450., 500., 600., 800., 1000. )
endfb.fission = None
endfb.dilutions = None
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "H1_CH2"
endfb.mat = 125
endfb.evaluationFile = evaluationDir + "H001.dat"
endfb.scatteringLaw =  evaluationDir + "tsl-HinCH2.dat"
endfb.scatteringMat = 37
endfb.temperatures = ( 296., 350 )
endfb.fission = None
endfb.dilutions = None
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "H1_ZRH"
endfb.mat = 125
endfb.temperatures = ( 296., 400., 500., 600., 700., 800., 1000., 1200. )
endfb.evaluationFile = evaluationDir + "H001.dat"
endfb.scatteringLaw = evaluationDir + "tsl-HinZrH.dat"
endfb.scatteringMat = 7
endfb.fission = None
endfb.dilutions = None
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Zr90_ZRH"
endfb.mat =  4025
endfb.temperatures = ( 296., 400., 500., 600., 700., 800., 1000., 1200. )
endfb.evaluationFile = evaluationDir + "Zr090.dat"
endfb.scatteringLaw =  evaluationDir + "tsl-ZrinZrH.dat"
endfb.scatteringMat = 58
endfb.fission = None
endfb.dilutions = None
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "C12_GR"
endfb.mat = 625
endfb.temperatures = ( 296., 400., 500., 600., 700., 800., 1000., 1200., 1600., 2000. )
endfb.evaluationFile = evaluationDir + "C000.dat"
endfb.scatteringLaw = evaluationDir + "tsl-graphite.dat"
endfb.scatteringMat = 31
endfb.fission = None
endfb.dilutions = None
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Be9"
endfb.mat = 425
endfb.temperatures = ( 296., 400., 500., 600., 700., 800., 1000., 1200. )
endfb.evaluationFile = evaluationDir + "Be009.dat"
endfb.scatteringLaw =  evaluationDir + "tsl-Be-meta.dat"
endfb.scatteringMat = 26
endfb.fission = None
endfb.dilutions = None
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.scatteringLaw = None
endfb.temperatures = ( 293., 600., 900., 1200., 1500., 3000. )
endfb.fission = None
endfb.dilutions = None

endfb.hmat = "H1"
endfb.mat = 125
endfb.evaluationFile = evaluationDir + "H001.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "H2"
endfb.mat = 128
endfb.evaluationFile = evaluationDir + "H002.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "He3"
endfb.mat = 225
endfb.evaluationFile = evaluationDir + "He003.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "He4"
endfb.mat = 228
endfb.evaluationFile = evaluationDir + "He004.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Li6"
endfb.mat = 325
endfb.evaluationFile = evaluationDir + "Li006.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Li7"
endfb.mat = 328
endfb.evaluationFile = evaluationDir + "Li007.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Be9"
endfb.mat = 425
endfb.evaluationFile = evaluationDir + "Be009.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "B10"
endfb.mat = 525
endfb.evaluationFile = evaluationDir + "B010.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "B11"
endfb.mat = 528
endfb.evaluationFile = evaluationDir + "B011.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "C12"
endfb.mat = 625
endfb.evaluationFile = evaluationDir + "C000.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "N14"
endfb.mat = 725
endfb.evaluationFile = evaluationDir + "N014.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "N15"
endfb.mat = 728
endfb.evaluationFile = evaluationDir + "N015.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "O16"
endfb.mat = 825
endfb.evaluationFile = evaluationDir + "O016.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "F19"
endfb.mat = 925
endfb.evaluationFile = evaluationDir + "F019.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Na23"
endfb.mat = 1125
endfb.evaluationFile = evaluationDir + "Na023.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Mg24"
endfb.mat = 1225
endfb.evaluationFile = evaluationDir + "Mg024.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Mg25"
endfb.mat = 1228
endfb.evaluationFile = evaluationDir + "Mg025.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Mg26"
endfb.mat = 1231
endfb.evaluationFile = evaluationDir + "Mg026.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Al27"
endfb.mat = 1325
endfb.evaluationFile = evaluationDir + "Al027.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Si28"
endfb.mat = 1425
endfb.evaluationFile = evaluationDir + "Si028.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Si29"
endfb.mat = 1428
endfb.evaluationFile = evaluationDir + "Si029.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Si30"
endfb.mat = 1431
endfb.evaluationFile = evaluationDir + "Si030.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "P31"
endfb.mat = 1525
endfb.evaluationFile = evaluationDir + "P031.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "S32"
endfb.mat = 1625
endfb.evaluationFile = evaluationDir + "S032.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "S33"
endfb.mat = 1628
endfb.evaluationFile = evaluationDir + "S033.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "S34"
endfb.mat = 1631
endfb.evaluationFile = evaluationDir + "S034.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "S36"
endfb.mat = 1637
endfb.evaluationFile = evaluationDir + "S036.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cl35"
endfb.mat = 1725
endfb.evaluationFile = evaluationDir + "Cl035.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cl37"
endfb.mat = 1731
endfb.evaluationFile = evaluationDir + "Cl037.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "K39"
endfb.mat = 1925
endfb.evaluationFile = evaluationDir + "K039.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "K40"
endfb.mat = 1928
endfb.evaluationFile = evaluationDir + "K040.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "K41"
endfb.mat = 1931
endfb.evaluationFile = evaluationDir + "K041.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ca40"
endfb.mat = 2025
endfb.evaluationFile = evaluationDir + "Ca040.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ca42"
endfb.mat = 2031
endfb.evaluationFile = evaluationDir + "Ca042.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ca43"
endfb.mat = 2034
endfb.evaluationFile = evaluationDir + "Ca043.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ca44"
endfb.mat = 2037
endfb.evaluationFile = evaluationDir + "Ca044.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ca46"
endfb.mat = 2043
endfb.evaluationFile = evaluationDir + "Ca046.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ca48"
endfb.mat = 2049
endfb.evaluationFile = evaluationDir + "Ca048.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ti46"
endfb.mat = 2225
endfb.evaluationFile = evaluationDir + "Ti046.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ti47"
endfb.mat = 2228
endfb.evaluationFile = evaluationDir + "Ti047.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ti48"
endfb.mat = 2231
endfb.evaluationFile = evaluationDir + "Ti048.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ti49"
endfb.mat = 2234
endfb.evaluationFile = evaluationDir + "Ti049.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ti50"
endfb.mat = 2237
endfb.evaluationFile = evaluationDir + "Ti050.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "V50"
endfb.mat = 2325
endfb.evaluationFile = evaluationDir + "V050.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "V51"
endfb.mat = 2328
endfb.evaluationFile = evaluationDir + "V051.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cr50"
endfb.mat = 2425
endfb.evaluationFile = evaluationDir + "Cr050.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cr52"
endfb.mat = 2431
endfb.evaluationFile = evaluationDir + "Cr052.dat"
endfb.fission = None
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 4.1677
endfb.dilutions = ( 1.e10, 10000.0, 3546.31, 1257.43, 445.8898, 158.1139, 56.0677, 19.8818, 7.0501, 2.5 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.dilutions = None

endfb.hmat = "Cr53"
endfb.mat = 2434
endfb.evaluationFile = evaluationDir + "Cr053.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cr54"
endfb.mat = 2437
endfb.evaluationFile = evaluationDir + "Cr054.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Mn55"
endfb.mat = 2525
endfb.evaluationFile = evaluationDir + "Mn055.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Fe54"
endfb.mat = 2625
endfb.evaluationFile = evaluationDir + "Fe054.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Fe56"
endfb.mat = 2631
endfb.evaluationFile = evaluationDir + "Fe056.dat"
endfb.fission = None
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 3.7243
endfb.dilutions = ( 1.e10, 10000.0, 3546.31, 1257.43, 445.8898, 158.1139, 56.0677, 19.8818, 7.0501, 2.5 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.dilutions = None

endfb.hmat = "Fe57"
endfb.mat = 2634
endfb.evaluationFile = evaluationDir + "Fe057.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Fe58"
endfb.mat = 2637
endfb.evaluationFile = evaluationDir + "Fe058.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Co59"
endfb.mat = 2725
endfb.evaluationFile = evaluationDir + "Co059.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ni58"
endfb.mat = 2825
endfb.evaluationFile = evaluationDir + "Ni058.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ni59"
endfb.mat = 2828
endfb.evaluationFile = evaluationDir + "Ni059.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ni60"
endfb.mat = 2831
endfb.evaluationFile = evaluationDir + "Ni060.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ni61"
endfb.mat = 2834
endfb.evaluationFile = evaluationDir + "Ni061.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ni62"
endfb.mat = 2837
endfb.evaluationFile = evaluationDir + "Ni062.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ni64"
endfb.mat = 2843
endfb.evaluationFile = evaluationDir + "Ni064.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cu63"
endfb.mat = 2925
endfb.evaluationFile = evaluationDir + "Cu063.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cu65"
endfb.mat = 2931
endfb.evaluationFile = evaluationDir + "Cu065.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Zn64"
endfb.mat = 3025
endfb.evaluationFile = evaluationDir + "Zn064.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Zn65"
endfb.mat = 3028
endfb.evaluationFile = evaluationDir + "Zn065.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Zn66"
endfb.mat = 3031
endfb.evaluationFile = evaluationDir + "Zn066.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Zn67"
endfb.mat = 3034
endfb.evaluationFile = evaluationDir + "Zn067.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Zn68"
endfb.mat = 3037
endfb.evaluationFile = evaluationDir + "Zn068.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Zn70"
endfb.mat = 3043
endfb.evaluationFile = evaluationDir + "Zn070.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ga69"
endfb.mat = 3125
endfb.evaluationFile = evaluationDir + "Ga069.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ga71"
endfb.mat = 3131
endfb.evaluationFile = evaluationDir + "Ga071.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "W180"
endfb.mat =  7425
endfb.evaluationFile = evaluationDir + "W180.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "W182"
endfb.mat =  7431
endfb.evaluationFile = evaluationDir + "W182.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "W183"
endfb.mat = 7434
endfb.evaluationFile = evaluationDir + "W183.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "W184"
endfb.mat = 7437
endfb.evaluationFile = evaluationDir + "W184.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "W186"
endfb.mat =  7443
endfb.evaluationFile = evaluationDir + "W186.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pb204"
endfb.mat =  8225
endfb.evaluationFile = evaluationDir + "Pb204.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pb206"
endfb.mat =  8231
endfb.evaluationFile = evaluationDir + "Pb206.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pb207"
endfb.mat =  8234
endfb.evaluationFile = evaluationDir + "Pb207.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pb208"
endfb.mat =  8237
endfb.evaluationFile = evaluationDir + "Pb208.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Bi209"
endfb.mat =  8325
endfb.evaluationFile = evaluationDir + "Bi209.dat"
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Th230"
endfb.mat = 9034
endfb.evaluationFile = evaluationDir + "Th230.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 8.7040
endfb.eFiss = 188.666101
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Th232"
endfb.mat = 9040
endfb.evaluationFile = evaluationDir + "Th232.dat"
endfb.fission = 2 # fission with delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.8699
endfb.eFiss = 197.108389
endfb.dilutions = ( 1.e10, 94.5317612, 56.3173141, 33.5510521, 19.9880447, \
11.9078817, 7.09412289, 4.22632504, 2.51783395, 1.5 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.eFiss = 197.108389
endfb.dilutions = ( 1.e10, 10000.0, 5957.50244, 3549.18335, 2114.42676, \
1259.67004, 750.448669, 447.079956, 266.347961, 158.676849 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pa231"
endfb.mat = 9131
endfb.evaluationFile = evaluationDir + "Pa231.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 8.7266
endfb.eFiss = 194.099942
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pa233"
endfb.mat = 9137
endfb.evaluationFile = evaluationDir + "Pa233.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 9.9950
endfb.eFiss = 194.162901
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "U232"
endfb.mat = 9219
endfb.evaluationFile = evaluationDir + "U232.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 12.0687
endfb.eFiss = 193.044277
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "U233"
endfb.mat = 9222
endfb.evaluationFile = evaluationDir + "U233.dat"
endfb.fission = 2 # fission with delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 12.2989
endfb.eFiss = 199.796183
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "U234"
endfb.mat = 9225
endfb.evaluationFile = evaluationDir + "U234.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.0210
endfb.eFiss = 200.632850
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "U235"
endfb.mat = 9228
endfb.evaluationFile = evaluationDir + "U235.dat"
endfb.fission = 2 # fission with delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.6070
endfb.eFiss = 202.270000
endfb.dilutions = ( 1.e10, 94.5317612, 56.3173141, 33.5510521, 19.9880447, \
11.9078817, 7.09412289, 4.22632504, 2.51783395, 1.5 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.dilutions = ( 1.e10, 10000.0, 5957.50244, 3549.18335, 2114.42676, \
1259.67004, 750.448669, 447.079956, 266.347961, 158.676849 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "U236"
endfb.mat = 9231
endfb.evaluationFile = evaluationDir + "U236.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.9954
endfb.eFiss = 208.679081
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "U237"
endfb.mat = 9234
endfb.evaluationFile = evaluationDir + "U237.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.5000
endfb.eFiss = 196.429642
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "U238"
endfb.mat = 9237
endfb.evaluationFile = evaluationDir + "U238.dat"
endfb.fission = 2 # fission with delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.17103
endfb.eFiss = 209.540012
endfb.dilutions = ( 1.e10, 94.5317612, 56.3173141, 33.5510521, 19.9880447, \
11.9078817, 7.09412289, 4.22632504, 2.51783395, 1.5 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.dilutions = ( 1.e10, 10000.0, 5957.50244, 3549.18335, 2114.42676, \
1259.67004, 750.448669, 447.079956, 266.347961, 158.676849 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Np236"
endfb.mat = 9343
endfb.evaluationFile = evaluationDir + "Np236.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.eFiss = 198.952718
endfb.potential = 12.1427
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Np237"
endfb.mat = 9346
endfb.evaluationFile = evaluationDir + "Np237.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.4369
endfb.eFiss = 205.370480
endfb.branchingN2N = 0.801
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.branchingN2N = None

endfb.hmat = "Np238"
endfb.mat = 9349
endfb.evaluationFile = evaluationDir + "Np238.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.eFiss = 208.699370
endfb.potential = 10.4000
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Np239"
endfb.mat = 9352
endfb.evaluationFile = evaluationDir + "Np239.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.eFiss = 198.519429
endfb.potential = 10.4979
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pu236"
endfb.mat = 9428
endfb.evaluationFile = evaluationDir + "Pu236.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.eFiss = 208.679081
endfb.potential = 11.2458
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pu237"
endfb.mat = 9431
endfb.evaluationFile = evaluationDir + "Pu237.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.5209
endfb.eFiss = 210.593272
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pu238"
endfb.mat = 9434
endfb.evaluationFile = evaluationDir + "Pu238.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.8897
endfb.eFiss = 209.540012
endfb.dilutions = ( 1.e10, 94.5317612, 56.3173141, 33.5510521, 19.9880447, \
11.9078817, 7.09412289, 4.22632504, 2.51783395, 1.5 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.dilutions = ( 1.e10, 10000.0, 5957.50244, 3549.18335, 2114.42676, \
1259.67004, 750.448669, 447.079956, 266.347961, 158.676849 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pu239"
endfb.mat = 9437
endfb.evaluationFile = evaluationDir + "Pu239.dat"
endfb.fission = 2 # fission with delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.8897
endfb.eFiss = 208.018532
endfb.dilutions = ( 1.e10, 158.887822, 100.279413, 63.2896882, \
39.9442369, 25.2101426, 15.9109633, 10.0419406, 6.33780423, 4.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.dilutions = ( 1.e10, 10000.0, 6311.33494, 3983.29436, 2513.99016, \
1586.66319, 1001.39615, 632.014573, 398.885514, 251.749976 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pu240"
endfb.mat = 9440
endfb.evaluationFile = evaluationDir + "Pu240.dat"
endfb.fission = 2 # fission with delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 9.9091
endfb.eFiss = 208.612566
endfb.dilutions = ( 1.e10, 94.5317612, 56.3173141, 33.5510521, 19.9880447, \
11.9078817, 7.09412289, 4.22632504, 2.51783395, 1.5 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.dilutions = ( 1.e10, 10000.0, 5957.50244, 3549.18335, 2114.42676, \
1259.67004, 750.448669, 447.079956, 266.347961, 158.676849 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pu241"
endfb.mat = 9443
endfb.evaluationFile = evaluationDir + "Pu241.dat"
endfb.fission = 2 # fission with delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.2156
endfb.eFiss = 211.237715
endfb.dilutions = ( 1.e10, 94.5317612, 56.3173141, 33.5510521, 19.9880447, \
11.9078817, 7.09412289, 4.22632504, 2.51783395, 1.5 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.dilutions = ( 1.e10, 10000.0, 5957.50244, 3549.18335, 2114.42676, \
1259.67004, 750.448669, 447.079956, 266.347961, 158.676849 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pu242"
endfb.mat = 9446
endfb.evaluationFile = evaluationDir + "Pu242.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.6961
endfb.eFiss = 212.072186
endfb.dilutions = ( 1.e10,  469.546659, 258.807233, 142.650752, \
78.6270025, 43.3380508, 23.8872981, 13.1663284, 7.25708715, 4.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.dilutions = ( 1.e10, 1.e5, 55118.5161, 30380.5178, 16745.2959, \
9229.76155, 5087.30922, 2804.05024, 1545.55137, 851.885253 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pu243"
endfb.mat = 9449
endfb.evaluationFile = evaluationDir + "Pu243.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.2000
endfb.eFiss = 207.499380
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Pu244"
endfb.mat = 9452
endfb.evaluationFile = evaluationDir + "Pu244.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.1000
endfb.eFiss = 208.427244
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Am241"
endfb.mat = 9543
endfb.evaluationFile = evaluationDir + "Am241.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.0329
endfb.eFiss = 211.216798
endfb.branchingNG = 0.115
endfb.dilutions = ( 1.e10, 94.5317612, 56.3173141, 33.5510521, 19.9880447, \
11.9078817, 7.09412289, 4.22632504, 2.51783395, 1.5 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.branchingNG = 0.115
endfb.dilutions = ( 1.e10, 10000.0, 5957.50244, 3549.18335, 2114.42676, \
1259.67004, 750.448669, 447.079956, 266.347961, 158.676849 )
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.branchingNG = None

endfb.hmat = "Am242"
endfb.mat = 9546
endfb.evaluationFile = evaluationDir + "Am242.dat"
endfb.fission = 0 # no fission matrix!!!
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.2000
endfb.eFiss = 215.146730
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Am242m"
endfb.mat = 9547
endfb.evaluationFile = evaluationDir + "Am242m.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.2000
endfb.eFiss = 215.146730
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Am243"
endfb.mat = 9549
endfb.evaluationFile = evaluationDir + "Am243.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.8237
endfb.eFiss = 212.952778
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cm241"
endfb.mat = 9628
endfb.evaluationFile = evaluationDir + "Cm241.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.1788
endfb.eFiss = 219.075406
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cm242"
endfb.mat = 9631
endfb.evaluationFile = evaluationDir + "Cm242.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.2000
endfb.eFiss = 212.786491
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cm243"
endfb.mat = 9634
endfb.evaluationFile = evaluationDir + "Cm243.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.2832
endfb.eFiss = 213.375296
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cm244"
endfb.mat = 9637
endfb.evaluationFile = evaluationDir + "Cm244.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.3200
endfb.eFiss = 217.926766
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cm245"
endfb.mat = 9640
endfb.evaluationFile = evaluationDir + "Cm245.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.3900
endfb.eFiss = 214.624022
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cm246"
endfb.mat = 9643
endfb.evaluationFile = evaluationDir + "Cm246.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.2758
endfb.eFiss = 220.179493
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cm247"
endfb.mat = 9646
endfb.evaluationFile = evaluationDir + "Cm247.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.0000
endfb.eFiss = 218.956599
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cm248"
endfb.mat = 9649
endfb.evaluationFile = evaluationDir + "Cm248.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 10.3971
endfb.eFiss = 221.723145
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Bk249"
endfb.mat = 9752
endfb.evaluationFile = evaluationDir + "Bk249.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.0983
endfb.eFiss = 224.740691
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cf249"
endfb.mat = 9852
endfb.evaluationFile = evaluationDir + "Cf249.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 11.1510
endfb.eFiss = 221.434495
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cf250"
endfb.mat = 9855
endfb.evaluationFile = evaluationDir + "Cf250.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 9.8800
endfb.eFiss = 229.685291
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cf251"
endfb.mat = 9858
endfb.evaluationFile = evaluationDir + "Cf251.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 9.8800
endfb.eFiss = 223.166396
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cf252"
endfb.mat = 9861
endfb.evaluationFile = evaluationDir + "Cf252.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 9.8000
endfb.eFiss = 230.239896
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cf253"
endfb.mat = 9864
endfb.evaluationFile = evaluationDir + "Cf253.dat"
endfb.fission = 1 # fission without delayed neutrons
endfb.ss = (22.53556, 3.206464e5)
endfb.potential = 9.7600
endfb.eFiss = 231.148831
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

# Process the fission products:

endfb.scatteringLaw = None
endfb.legendre = 0
endfb.fission = None
endfb.dilutions = None
endfb.eFiss = None

endfb.hmat = "Ge72"
endfb.mat = 3231
endfb.evaluationFile = evaluationDir + "Ge072.dat"
endfb.makeFp()

endfb.hmat = "Ge73"
endfb.mat = 3234
endfb.evaluationFile = evaluationDir + "Ge073.dat"
endfb.makeFp()

endfb.hmat = "Ge74"
endfb.mat = 3237
endfb.evaluationFile = evaluationDir + "Ge074.dat"
endfb.makeFp()

endfb.hmat = "Ge76"
endfb.mat = 3243
endfb.evaluationFile = evaluationDir + "Ge076.dat"
endfb.makeFp()

endfb.hmat = "As75"
endfb.mat = 3325
endfb.evaluationFile = evaluationDir + "As075.dat"
endfb.makeFp()

endfb.hmat = "Se76"
endfb.mat = 3431
endfb.evaluationFile = evaluationDir + "Se076.dat"
endfb.makeFp()

endfb.hmat = "Se77"
endfb.mat = 3434
endfb.evaluationFile = evaluationDir + "Se077.dat"
endfb.makeFp()

endfb.hmat = "Se78"
endfb.mat = 3437
endfb.evaluationFile = evaluationDir + "Se078.dat"
endfb.makeFp()

endfb.hmat = "Se79"
endfb.mat = 3440
endfb.evaluationFile = evaluationDir + "Se079.dat"
endfb.makeFp()

endfb.hmat = "Se80"
endfb.mat = 3443
endfb.evaluationFile = evaluationDir + "Se080.dat"
endfb.makeFp()

endfb.hmat = "Se82"
endfb.mat = 3449
endfb.evaluationFile = evaluationDir + "Se082.dat"
endfb.makeFp()

endfb.hmat = "Br79"
endfb.mat = 3525
endfb.evaluationFile = evaluationDir + "Br079.dat"
endfb.makeFp()

endfb.hmat = "Br81"
endfb.mat = 3531
endfb.evaluationFile = evaluationDir + "Br081.dat"
endfb.makeFp()

endfb.hmat = "Kr80"
endfb.mat = 3631
endfb.evaluationFile = evaluationDir + "Kr080.dat"
endfb.makeFp()

endfb.hmat = "Kr82"
endfb.mat = 3637
endfb.evaluationFile = evaluationDir + "Kr082.dat"
endfb.makeFp()

endfb.hmat = "Kr83"
endfb.mat = 3640
endfb.evaluationFile = evaluationDir + "Kr083.dat"
endfb.makeFp()

endfb.hmat = "Kr84"
endfb.mat = 3643
endfb.evaluationFile = evaluationDir + "Kr084.dat"
endfb.makeFp()

endfb.hmat = "Kr85"
endfb.mat = 3646
endfb.evaluationFile = evaluationDir + "Kr085.dat"
endfb.makeFp()

endfb.hmat = "Kr86"
endfb.mat = 3649
endfb.evaluationFile = evaluationDir + "Kr086.dat"
endfb.makeFp()

endfb.hmat = "Rb85"
endfb.mat = 3725
endfb.evaluationFile = evaluationDir + "Rb085.dat"
endfb.makeFp()

endfb.hmat = "Rb87"
endfb.mat = 3731
endfb.evaluationFile = evaluationDir + "Rb087.dat"
endfb.makeFp()

endfb.hmat = "Sr86"
endfb.mat = 3831
endfb.evaluationFile = evaluationDir + "Sr086.dat"
endfb.makeFp()

endfb.hmat = "Sr87"
endfb.mat = 3834
endfb.evaluationFile = evaluationDir + "Sr087.dat"
endfb.makeFp()

endfb.hmat = "Sr88"
endfb.mat = 3837
endfb.evaluationFile = evaluationDir + "Sr088.dat"
endfb.makeFp()

endfb.hmat = "Sr89"
endfb.mat = 3840
endfb.evaluationFile = evaluationDir + "Sr089.dat"
endfb.makeFp()

endfb.hmat = "Sr90"
endfb.mat = 3843
endfb.evaluationFile = evaluationDir + "Sr090.dat"
endfb.makeFp()

endfb.hmat = "Y89"
endfb.mat = 3925
endfb.evaluationFile = evaluationDir + "Y089.dat"
endfb.makeFp()

endfb.hmat = "Y90"
endfb.mat = 3928
endfb.evaluationFile = evaluationDir + "Y090.dat"
endfb.makeFp()

endfb.hmat = "Y91"
endfb.mat = 3931
endfb.evaluationFile = evaluationDir + "Y091.dat"
endfb.makeFp()

endfb.hmat = "Zr90"
endfb.mat = 4025
endfb.evaluationFile = evaluationDir + "Zr090.dat"
endfb.fission = None
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 6.8813
endfb.dilutions = ( 1.e10, 10000.0,  3866.97, 1495.35, 578.2475, 223.6068, 86.4682, 33.4370, 12.9300, 5.0 )
endfb.autolib = (4.632489, 3.481068e3, 0.0005)
endfb.pendf()
endfb.gendf()
endfb.draglib()
endfb.autolib = (4.632489, 1.11377e4, 0.0005)

endfb.hmat = "Zr91"
endfb.mat = 4028
endfb.evaluationFile = evaluationDir + "Zr091.dat"
endfb.fission = None
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 6.8813
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Zr92"
endfb.mat = 4031
endfb.evaluationFile = evaluationDir + "Zr092.dat"
endfb.fission = None
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 6.8813
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Zr93"
endfb.mat = 4034
endfb.evaluationFile = evaluationDir + "Zr093.dat"
endfb.makeFp()

endfb.hmat = "Zr94"
endfb.mat = 4037
endfb.evaluationFile = evaluationDir + "Zr094.dat"
endfb.fission = None
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 6.8813
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Zr95"
endfb.mat = 4040
endfb.evaluationFile = evaluationDir + "Zr095.dat"
endfb.makeFp()

endfb.hmat = "Zr96"
endfb.mat = 4043
endfb.evaluationFile = evaluationDir + "Zr096.dat"
endfb.fission = None
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 6.8813
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Nb93"
endfb.mat = 4125
endfb.evaluationFile = evaluationDir + "Nb093.dat"
endfb.makeFp()

endfb.hmat = "Nb94"
endfb.mat = 4128
endfb.evaluationFile = evaluationDir + "Nb094.dat"
endfb.makeFp()

endfb.hmat = "Nb95"
endfb.mat = 4131
endfb.evaluationFile = evaluationDir + "Nb095.dat"
endfb.makeFp()

endfb.hmat = "Mo92"
endfb.mat = 4225
endfb.evaluationFile = evaluationDir + "Mo092.dat"
endfb.makeFp()

endfb.hmat = "Mo94"
endfb.mat = 4231
endfb.evaluationFile = evaluationDir + "Mo094.dat"
endfb.makeFp()

endfb.hmat = "Mo95"
endfb.mat = 4234
endfb.evaluationFile = evaluationDir + "Mo095.dat"
endfb.makeFp()

endfb.hmat = "Mo96"
endfb.mat = 4237
endfb.evaluationFile = evaluationDir + "Mo096.dat"
endfb.makeFp()

endfb.hmat = "Mo97"
endfb.mat = 4240
endfb.evaluationFile = evaluationDir + "Mo097.dat"
endfb.makeFp()

endfb.hmat = "Mo98"
endfb.mat = 4243
endfb.evaluationFile = evaluationDir + "Mo098.dat"
endfb.makeFp()

endfb.hmat = "Mo99"
endfb.mat = 4246
endfb.evaluationFile = evaluationDir + "Mo099.dat"
endfb.makeFp()

endfb.hmat = "Mo100"
endfb.mat = 4249
endfb.evaluationFile = evaluationDir + "Mo100.dat"
endfb.makeFp()

endfb.hmat = "Tc99"
endfb.mat = 4325
endfb.evaluationFile = evaluationDir + "Tc099.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 6.4675
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ru99"
endfb.mat = 4434
endfb.evaluationFile = evaluationDir + "Ru099.dat"
endfb.makeFp()

endfb.hmat = "Ru100"
endfb.mat = 4437
endfb.evaluationFile = evaluationDir + "Ru100.dat"
endfb.makeFp()

endfb.hmat = "Ru101"
endfb.mat = 4440
endfb.evaluationFile = evaluationDir + "Ru101.dat"
endfb.makeFp()

endfb.hmat = "Ru102"
endfb.mat = 4443
endfb.evaluationFile = evaluationDir + "Ru102.dat"
endfb.makeFp()

endfb.hmat = "Ru103"
endfb.mat = 4446
endfb.evaluationFile = evaluationDir + "Ru103.dat"
endfb.makeFp()

endfb.hmat = "Ru104"
endfb.mat = 4449
endfb.evaluationFile = evaluationDir + "Ru104.dat"
endfb.makeFp()

endfb.hmat = "Ru105"
endfb.mat = 4452
endfb.evaluationFile = evaluationDir + "Ru105.dat"
endfb.makeFp()

endfb.hmat = "Ru106"
endfb.mat = 4455
endfb.evaluationFile = evaluationDir + "Ru106.dat"
endfb.makeFp()

endfb.hmat = "Rh103"
endfb.mat = 4525
endfb.evaluationFile = evaluationDir + "Rh103.dat"
endfb.makeFp()

endfb.hmat = "Rh105"
endfb.mat = 4531
endfb.evaluationFile = evaluationDir + "Rh105.dat"
endfb.makeFp()

endfb.hmat = "Pd104"
endfb.mat = 4631
endfb.evaluationFile = evaluationDir + "Pd104.dat"
endfb.makeFp()

endfb.hmat = "Pd105"
endfb.mat = 4634
endfb.evaluationFile = evaluationDir + "Pd105.dat"
endfb.makeFp()

endfb.hmat = "Pd106"
endfb.mat = 4637
endfb.evaluationFile = evaluationDir + "Pd106.dat"
endfb.makeFp()

endfb.hmat = "Pd107"
endfb.mat = 4640
endfb.evaluationFile = evaluationDir + "Pd107.dat"
endfb.makeFp()

endfb.hmat = "Pd108"
endfb.mat = 4643
endfb.evaluationFile = evaluationDir + "Pd108.dat"
endfb.makeFp()

endfb.hmat = "Pd110"
endfb.mat = 4649
endfb.evaluationFile = evaluationDir + "Pd110.dat"
endfb.makeFp()

endfb.hmat = "Ag107"
endfb.mat = 4725
endfb.evaluationFile = evaluationDir + "Ag107.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 5.4739
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ag109"
endfb.mat = 4731
endfb.evaluationFile = evaluationDir + "Ag109.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 5.3316
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ag111"
endfb.mat = 4737
endfb.evaluationFile = evaluationDir + "Ag111.dat"
endfb.makeFp()

endfb.hmat = "Cd106"
endfb.mat = 4825
endfb.evaluationFile = evaluationDir + "Cd106.dat"
endfb.makeFp()

endfb.hmat = "Cd108"
endfb.mat = 4831
endfb.evaluationFile = evaluationDir + "Cd108.dat"
endfb.makeFp()

endfb.hmat = "Cd110"
endfb.mat = 4837
endfb.evaluationFile = evaluationDir + "Cd110.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 5.1762
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Cd111"
endfb.mat = 4840
endfb.evaluationFile = evaluationDir + "Cd111.dat"
endfb.makeFp()

endfb.hmat = "Cd112"
endfb.mat = 4843
endfb.evaluationFile = evaluationDir + "Cd112.dat"
endfb.makeFp()

endfb.hmat = "Cd113"
endfb.mat = 4846
endfb.evaluationFile = evaluationDir + "Cd113.dat"
endfb.makeFp()

endfb.hmat = "Cd114"
endfb.mat = 4849
endfb.evaluationFile = evaluationDir + "Cd114.dat"
endfb.branchingNG = 0.079383
endfb.makeFp()
endfb.branchingNG = None

endfb.hmat = "Cd116"
endfb.mat = 4855
endfb.evaluationFile = evaluationDir + "Cd116.dat"
endfb.makeFp()

endfb.hmat = "In113"
endfb.mat = 4925
endfb.evaluationFile = evaluationDir + "In113.dat"
endfb.makeFp()

endfb.hmat = "In115"
endfb.mat = 4931
endfb.evaluationFile = evaluationDir + "In115.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 5.0439
endfb.dilutions = ( 1.e10, 10000.0, 3549.18335, 1259.67004, 447.079956, \
158.676849, 56.3173141, 19.9880447, 7.09412289, 2.51783395 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Sn112"
endfb.mat = 5025
endfb.evaluationFile = evaluationDir + "Sn112.dat"
endfb.makeFp()

endfb.hmat = "Sn114"
endfb.mat = 5031
endfb.evaluationFile = evaluationDir + "Sn114.dat"
endfb.makeFp()

endfb.hmat = "Sn115"
endfb.mat = 5034
endfb.evaluationFile = evaluationDir + "Sn115.dat"
endfb.makeFp()

endfb.hmat = "Sn116"
endfb.mat = 5037
endfb.evaluationFile = evaluationDir + "Sn116.dat"
endfb.makeFp()

endfb.hmat = "Sn117"
endfb.mat = 5040
endfb.evaluationFile = evaluationDir + "Sn117.dat"
endfb.makeFp()

endfb.hmat = "Sn118"
endfb.mat = 5043
endfb.evaluationFile = evaluationDir + "Sn118.dat"
endfb.makeFp()

endfb.hmat = "Sn119"
endfb.mat = 5046
endfb.evaluationFile = evaluationDir + "Sn119.dat"
endfb.makeFp()

endfb.hmat = "Sn120"
endfb.mat = 5049
endfb.evaluationFile = evaluationDir + "Sn120.dat"
endfb.makeFp()

endfb.hmat = "Sn122"
endfb.mat = 5055
endfb.evaluationFile = evaluationDir + "Sn122.dat"
endfb.makeFp()

endfb.hmat = "Sn123"
endfb.mat = 5058
endfb.evaluationFile = evaluationDir + "Sn123.dat"
endfb.makeFp()

endfb.hmat = "Sn124"
endfb.mat = 5061
endfb.evaluationFile = evaluationDir + "Sn124.dat"
endfb.makeFp()

endfb.hmat = "Sn126"
endfb.mat = 5067
endfb.evaluationFile = evaluationDir + "Sn126.dat"
endfb.makeFp()

endfb.hmat = "Sb121"
endfb.mat = 5125
endfb.evaluationFile = evaluationDir + "Sb121.dat"
endfb.makeFp()

endfb.hmat = "Sb123"
endfb.mat = 5131
endfb.evaluationFile = evaluationDir + "Sb123.dat"
endfb.makeFp()

endfb.hmat = "Sb124"
endfb.mat = 5134
endfb.evaluationFile = evaluationDir + "Sb124.dat"
endfb.makeFp()

endfb.hmat = "Sb125"
endfb.mat = 5137
endfb.evaluationFile = evaluationDir + "Sb125.dat"
endfb.makeFp()

endfb.hmat = "Sb126"
endfb.mat = 5140
endfb.evaluationFile = evaluationDir + "Sb126.dat"
endfb.makeFp()

endfb.hmat = "Te120"
endfb.mat = 5225
endfb.evaluationFile = evaluationDir + "Te120.dat"
endfb.makeFp()

endfb.hmat = "Te122"
endfb.mat = 5231
endfb.evaluationFile = evaluationDir + "Te122.dat"
endfb.makeFp()

endfb.hmat = "Te123"
endfb.mat = 5234
endfb.evaluationFile = evaluationDir + "Te123.dat"
endfb.makeFp()

endfb.hmat = "Te124"
endfb.mat = 5237
endfb.evaluationFile = evaluationDir + "Te124.dat"
endfb.makeFp()

endfb.hmat = "Te125"
endfb.mat = 5240
endfb.evaluationFile = evaluationDir + "Te125.dat"
endfb.makeFp()

endfb.hmat = "Te126"
endfb.mat = 5243
endfb.evaluationFile = evaluationDir + "Te126.dat"
endfb.branchingNG = 0.091528
endfb.makeFp()
endfb.branchingNG = None

endfb.hmat = "Te127m"
endfb.mat = 5247
endfb.evaluationFile = evaluationDir + "Te127m.dat"
endfb.makeFp()

endfb.hmat = "Te128"
endfb.mat = 5249
endfb.evaluationFile = evaluationDir + "Te128.dat"
endfb.branchingNG = 0.031894
endfb.makeFp()
endfb.branchingNG = None

endfb.hmat = "Te129m"
endfb.mat = 5253
endfb.evaluationFile = evaluationDir + "Te129m.dat"
endfb.makeFp()

endfb.hmat = "Te130"
endfb.mat = 5255
endfb.evaluationFile = evaluationDir + "Te130.dat"
endfb.makeFp()

endfb.hmat = "Te132"
endfb.mat = 5261
endfb.evaluationFile = evaluationDir + "Te132.dat"
endfb.makeFp()

endfb.hmat = "I127"
endfb.mat = 5325
endfb.evaluationFile = evaluationDir + "I127.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 4.5239
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "I129"
endfb.mat = 5331
endfb.evaluationFile = evaluationDir + "I129.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 5.8221
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "I130"
endfb.mat = 5334
endfb.evaluationFile = evaluationDir + "I130.dat"
endfb.makeFp()

endfb.hmat = "I131"
endfb.mat = 5337
endfb.evaluationFile = evaluationDir + "I131.dat"
endfb.makeFp()

endfb.hmat = "I135"
endfb.mat = 5349
endfb.evaluationFile = evaluationDir + "I135.dat"
endfb.makeFp()

endfb.hmat = "Xe128"
endfb.mat = 5437
endfb.evaluationFile = evaluationDir + "Xe128.dat"
endfb.makeFp()

endfb.hmat = "Xe129"
endfb.mat = 5440
endfb.evaluationFile = evaluationDir + "Xe129.dat"
endfb.makeFp()

endfb.hmat = "Xe130"
endfb.mat = 5443
endfb.evaluationFile = evaluationDir + "Xe130.dat"
endfb.makeFp()

endfb.hmat = "Xe131"
endfb.mat = 5446
endfb.evaluationFile = evaluationDir + "Xe131.dat"
endfb.makeFp()

endfb.hmat = "Xe132"
endfb.mat = 5449
endfb.evaluationFile = evaluationDir + "Xe132.dat"
endfb.makeFp()

endfb.hmat = "Xe133"
endfb.mat = 5452
endfb.evaluationFile = evaluationDir + "Xe133.dat"
endfb.makeFp()

endfb.hmat = "Xe134"
endfb.mat = 5455
endfb.evaluationFile = evaluationDir + "Xe134.dat"
endfb.makeFp()

endfb.hmat = "Xe135"
endfb.mat = 5458
endfb.evaluationFile = evaluationDir + "Xe135.dat"
endfb.makeFp()

endfb.hmat = "Xe136"
endfb.mat = 5461
endfb.evaluationFile = evaluationDir + "Xe136.dat"
endfb.makeFp()

endfb.hmat = "Cs133"
endfb.mat = 5525
endfb.evaluationFile = evaluationDir + "Cs133.dat"
endfb.makeFp()

endfb.hmat = "Cs134"
endfb.mat = 5528
endfb.evaluationFile = evaluationDir + "Cs134.dat"
endfb.makeFp()

endfb.hmat = "Cs135"
endfb.mat = 5531
endfb.evaluationFile = evaluationDir + "Cs135.dat"
endfb.makeFp()

endfb.hmat = "Cs136"
endfb.mat = 5534
endfb.evaluationFile = evaluationDir + "Cs136.dat"
endfb.makeFp()

endfb.hmat = "Cs137"
endfb.mat = 5537
endfb.evaluationFile = evaluationDir + "Cs137.dat"
endfb.makeFp()

endfb.hmat = "Ba134"
endfb.mat = 5637
endfb.evaluationFile = evaluationDir + "Ba134.dat"
endfb.makeFp()

endfb.hmat = "Ba135"
endfb.mat = 5640
endfb.evaluationFile = evaluationDir + "Ba135.dat"
endfb.makeFp()

endfb.hmat = "Ba136"
endfb.mat = 5643
endfb.evaluationFile = evaluationDir + "Ba136.dat"
endfb.makeFp()

endfb.hmat = "Ba137"
endfb.mat = 5646
endfb.evaluationFile = evaluationDir + "Ba137.dat"
endfb.makeFp()

endfb.hmat = "Ba138"
endfb.mat = 5649
endfb.evaluationFile = evaluationDir + "Ba138.dat"
endfb.makeFp()

endfb.hmat = "Ba140"
endfb.mat = 5655
endfb.evaluationFile = evaluationDir + "Ba140.dat"
endfb.makeFp()

endfb.hmat = "La138"
endfb.mat = 5725
endfb.evaluationFile = evaluationDir + "La138.dat"
endfb.makeFp()

endfb.hmat = "La139"
endfb.mat = 5728
endfb.evaluationFile = evaluationDir + "La139.dat"
endfb.makeFp()

endfb.hmat = "La140"
endfb.mat = 5731
endfb.evaluationFile = evaluationDir + "La140.dat"
endfb.makeFp()

endfb.hmat = "Ce140"
endfb.mat = 5837
endfb.evaluationFile = evaluationDir + "Ce140.dat"
endfb.makeFp()

endfb.hmat = "Ce141"
endfb.mat = 5840
endfb.evaluationFile = evaluationDir + "Ce141.dat"
endfb.makeFp()

endfb.hmat = "Ce142"
endfb.mat = 5843
endfb.evaluationFile = evaluationDir + "Ce142.dat"
endfb.makeFp()

endfb.hmat = "Ce143"
endfb.mat = 5846
endfb.evaluationFile = evaluationDir + "Ce143.dat"
endfb.makeFp()

endfb.hmat = "Ce144"
endfb.mat = 5849
endfb.evaluationFile = evaluationDir + "Ce144.dat"
endfb.makeFp()

endfb.hmat = "Pr141"
endfb.mat = 5925
endfb.evaluationFile = evaluationDir + "Pr141.dat"
endfb.makeFp()

endfb.hmat = "Pr142"
endfb.mat = 5928
endfb.evaluationFile = evaluationDir + "Pr142.dat"
endfb.makeFp()

endfb.hmat = "Pr143"
endfb.mat = 5931
endfb.evaluationFile = evaluationDir + "Pr143.dat"
endfb.makeFp()

endfb.hmat = "Nd142"
endfb.mat = 6025
endfb.evaluationFile = evaluationDir + "Nd142.dat"
endfb.makeFp()

endfb.hmat = "Nd143"
endfb.mat = 6028
endfb.evaluationFile = evaluationDir + "Nd143.dat"
endfb.makeFp()

endfb.hmat = "Nd144"
endfb.mat = 6031
endfb.evaluationFile = evaluationDir + "Nd144.dat"
endfb.makeFp()

endfb.hmat = "Nd145"
endfb.mat = 6034
endfb.evaluationFile = evaluationDir + "Nd145.dat"
endfb.makeFp()

endfb.hmat = "Nd146"
endfb.mat = 6037
endfb.evaluationFile = evaluationDir + "Nd146.dat"
endfb.makeFp()

endfb.hmat = "Nd147"
endfb.mat = 6040
endfb.evaluationFile = evaluationDir + "Nd147.dat"
endfb.makeFp()

endfb.hmat = "Nd148"
endfb.mat = 6043
endfb.evaluationFile = evaluationDir + "Nd148.dat"
endfb.makeFp()

endfb.hmat = "Nd150"
endfb.mat = 6049
endfb.evaluationFile = evaluationDir + "Nd150.dat"
endfb.makeFp()

endfb.hmat = "Pm147"
endfb.mat = 6149
endfb.evaluationFile = evaluationDir + "Pm147.dat"
endfb.branchingNG = 0.470
endfb.makeFp()
endfb.branchingNG = None

endfb.hmat = "Pm148"
endfb.mat = 6152
endfb.evaluationFile = evaluationDir + "Pm148.dat"
endfb.makeFp()

endfb.hmat = "Pm148m"
endfb.mat = 6153
endfb.evaluationFile = evaluationDir + "Pm148m.dat"
endfb.makeFp()

endfb.hmat = "Pm149"
endfb.mat = 6155
endfb.evaluationFile = evaluationDir + "Pm149.dat"
endfb.makeFp()

endfb.hmat = "Pm151"
endfb.mat = 6161
endfb.evaluationFile = evaluationDir + "Pm151.dat"
endfb.makeFp()

endfb.hmat = "Sm147"
endfb.mat = 6234
endfb.evaluationFile = evaluationDir + "Sm147.dat"
endfb.makeFp()

endfb.hmat = "Sm148"
endfb.mat = 6237
endfb.evaluationFile = evaluationDir + "Sm148.dat"
endfb.makeFp()

endfb.hmat = "Sm149"
endfb.mat = 6240
endfb.evaluationFile = evaluationDir + "Sm149.dat"
endfb.makeFp()

endfb.hmat = "Sm150"
endfb.mat = 6243
endfb.evaluationFile = evaluationDir + "Sm150.dat"
endfb.makeFp()

endfb.hmat = "Sm151"
endfb.mat = 6246
endfb.evaluationFile = evaluationDir + "Sm151.dat"
endfb.makeFp()

endfb.hmat = "Sm152"
endfb.mat = 6249
endfb.evaluationFile = evaluationDir + "Sm152.dat"
endfb.makeFp()

endfb.hmat = "Sm153"
endfb.mat = 6252
endfb.evaluationFile = evaluationDir + "Sm153.dat"
endfb.makeFp()

endfb.hmat = "Sm154"
endfb.mat = 6255
endfb.evaluationFile = evaluationDir + "Sm154.dat"
endfb.makeFp()

endfb.hmat = "Eu151"
endfb.mat = 6325
endfb.evaluationFile = evaluationDir + "Eu151.dat"
endfb.makeFp()

endfb.hmat = "Eu152"
endfb.mat = 6328
endfb.evaluationFile = evaluationDir + "Eu152.dat"
endfb.makeFp()

endfb.hmat = "Eu153"
endfb.mat = 6331
endfb.evaluationFile = evaluationDir + "Eu153.dat"
endfb.makeFp()

endfb.hmat = "Eu154"
endfb.mat = 6334
endfb.evaluationFile = evaluationDir + "Eu154.dat"
endfb.makeFp()

endfb.hmat = "Eu155"
endfb.mat = 6337
endfb.evaluationFile = evaluationDir + "Eu155.dat"
endfb.makeFp()

endfb.hmat = "Eu156"
endfb.mat = 6340
endfb.evaluationFile = evaluationDir + "Eu156.dat"
endfb.makeFp()

endfb.hmat = "Eu157"
endfb.mat = 6343
endfb.evaluationFile = evaluationDir + "Eu157.dat"
endfb.makeFp()

endfb.hmat = "Gd152"
endfb.mat = 6425
endfb.evaluationFile = evaluationDir + "Gd152.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 8.0425
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Gd154"
endfb.mat = 6431
endfb.evaluationFile = evaluationDir + "Gd154.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 6.6723
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Gd155"
endfb.mat = 6434
endfb.evaluationFile = evaluationDir + "Gd155.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 6.3376
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Gd156"
endfb.mat = 6437
endfb.evaluationFile = evaluationDir + "Gd156.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.3792
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Gd157"
endfb.mat = 6440
endfb.evaluationFile = evaluationDir + "Gd157.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 6.6063
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Gd158"
endfb.mat = 6443
endfb.evaluationFile = evaluationDir + "Gd158.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.6454
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Gd160"
endfb.mat = 6449
endfb.evaluationFile = evaluationDir + "Gd160.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.0241
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.dilutions = None

endfb.hmat = "Tb159"
endfb.mat = 6525
endfb.evaluationFile = evaluationDir + "Tb159.dat"
endfb.makeFp()

endfb.hmat = "Tb160"
endfb.mat = 6528
endfb.evaluationFile = evaluationDir + "Tb160.dat"
endfb.makeFp()

endfb.hmat = "Dy160"
endfb.mat = 6637
endfb.evaluationFile = evaluationDir + "Dy160.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 6.9861
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Dy161"
endfb.mat = 6640
endfb.evaluationFile = evaluationDir + "Dy161.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.0121
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Dy162"
endfb.mat = 6643
endfb.evaluationFile = evaluationDir + "Dy162.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 4.5681
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Dy163"
endfb.mat = 6646
endfb.evaluationFile = evaluationDir + "Dy163.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.0639
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Dy164"
endfb.mat = 6649
endfb.evaluationFile = evaluationDir + "Dy164.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.0897
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Hf174"
endfb.mat = 7225
endfb.evaluationFile = evaluationDir + "Hf174.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.1385
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Hf176"
endfb.mat = 7231
endfb.evaluationFile = evaluationDir + "Hf176.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.1935
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Hf177"
endfb.mat = 7234
endfb.evaluationFile = evaluationDir + "Hf177.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.2202
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Hf178"
endfb.mat = 7237
endfb.evaluationFile = evaluationDir + "Hf178.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.2469
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Hf179"
endfb.mat = 7240
endfb.evaluationFile = evaluationDir + "Hf179.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.2736
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Hf180"
endfb.mat = 7243
endfb.evaluationFile = evaluationDir + "Hf180.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.3004
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.hmat = "Ta181"
endfb.mat = 7328
endfb.evaluationFile = evaluationDir + "Ta181.dat"
endfb.ss = (22.53556, 1.858471e4)
endfb.potential = 7.6454
endfb.dilutions = ( 1.e10, 10000.0, 4216.96552, 1778.27959, 749.894278, \
316.227791, 133.352152,  56.2341357, 23.7137381, 10.0 )
endfb.pendf()
endfb.gendf()
endfb.draglib()

endfb.dilutions = None

endfb.hmat = "Ho165"
endfb.mat = 6725
endfb.evaluationFile = evaluationDir + "Ho165.dat"
endfb.makeFp()

endfb.hmat = "Er166"
endfb.mat = 6837
endfb.evaluationFile = evaluationDir + "Er166.dat"
endfb.makeFp()

endfb.hmat = "Er167"
endfb.mat = 6840
endfb.evaluationFile = evaluationDir + "Er167.dat"
endfb.makeFp()

# Process the burnup chain:

endfb.fissionFile = evaluationDir.joinpath('jendl40-or-up-fy_20120914').rglob('*NF.dat')
endfb.decayFile =   evaluationDir.joinpath('JENDL-4-PA').rglob('*.dat')
endfb.burnup()

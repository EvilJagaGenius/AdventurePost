#Scene pack for APTalk
#Includes: Po-Koro, all of MNOG Po-Wahi, Onu-Koro, Ta-Koro
#TTG
print('Loading scenes')

#Some rules for editing:
#Scene images are to be placed in the SceneImgs folder, in .png format.
#NPC images are to be placed in the NPC_Imgs folder, in .png format.
#Item images are to be in the ItemImgs folder, should look somewhat like a square, and be in .bmp format with an odd, solid color surrounding the item.
#Platformer levels are in the APPLElvls folder, in .bmp format.
#And try not to look at the combination lock doors, as that would be cheating...
finished = False

import APtalk
from APtalk import *

#Start Po-Wahi
startScene = Scene('Beach.png', 'startScene')
poRoad1 = Scene('Img2.png', 'poRoad1')
poRoad2 = Scene('Img3.png', 'poRoad2')
poRoad3 = Scene('PoWahi3.png', 'poRoad3')
poRoad4 = Scene('PoWahi4.png', 'poRoad4')
poRoad5 = Scene('PoWahi5.png', 'poRoad5')
poRoad6 = Scene('PoWahi6.png', 'poRoad6')
poRoad7 = Scene('PoWahi7.png', 'poRoad7')
poRoad8 = Scene('PoWahi8.png', 'poRoad8')
poRoad9 = Scene('OutOfPoKoro.png', 'poRoad9')
poRoad10 = Scene('PoWahi10.png', 'poRoad10')
poRoad11 = Scene('PoWahi11.png', 'poRoad11')
poRoad12 = Scene('PoWahi12.png', 'poRoad12')
poRoad13 = Scene('PoWahi13.png', 'poRoad13')
poBeach1 = Scene('PoWahi2.png', 'poBeach1')
poBeach2 = Scene('PoWahi1.png', 'poBeach2')
poBeach3 = Scene('BackFromXRoad.png', 'poBeach3')
poXRoad1 = Scene('XRoad1.png', 'poXRoad1')
poXRoad1_L = Scene('XRoad1_Left.png', 'poXRoad1_L')
poXRoad1_FL = Scene('XRoad1_FarLeft.png', 'poXRoad1_FL')
poXRoad1_R = Scene('XRoad1_Right.png', 'poXRoad1_R')
poXRoad1_FR = Scene('XRoad1_FarRight.png', 'poXRoad1_FR')
poXRoad2_FB = Scene('HafuFromBeach_Far.png', 'poXRoad2_FB')
poXRoad2_FPK = Scene('HafuFromPoKoro_Far.png', 'poXRoad2_FPK')
poXRoad2_BtOW = Scene('HafuFromBeach.png', 'poXRoad2_BtOW')
poXRoad2_BtPK = Scene('PoKoro_XRoad2.png', 'poXRoad2_BtPK')
poXRoad2_PKtB = Scene('HafuFromPoKoro.png', 'poXRoad2_PKtB')
poXRoad2_PKtOW = Scene('OnuWahi_XRoad2.png', 'poXRoad2_PKtOW')
poXRoad2_OWtB = Scene('OKtoBeach.png', 'poXRoad2_OWtB')
poXRoad2_OWtPK = Scene('OKtoPK.png', 'poXRoad2_OWtPK')
poKoroGate_VF = Scene('PoKoro_VeryFar.png', 'poKoroGate_VF')
poKoroGate_F = Scene('PoKoro_Far.png', 'poKoroGate_F')
poKoroGate_C = Scene('PoKoroGate_Close.png', 'poKoroGate_C')
poKoroGate_VC = Scene('PoKoroGate_VeryClose.png', 'poKoroGate_VC')
poKoroGate_I = Scene('PoKoroGate_Inside.png', 'poKoroGate_I')
poKoro1 = Scene('PoKoro1.png', 'poKoro1')
poKoro2 = Scene('PoKoro2.png', 'poKoro2')
poKoro3 = Scene('PoKoro3.png', 'poKoro3')
poKoro4 = Scene('PoKoro4.png', 'poKoro4')
poGuardStairs_U = Scene('PoStairs2.png', 'poGuardStairs_U')
poGuardStairs_D = Scene('LightMine9.png', 'poGuardStairs_D')
poTunnel1 = Scene('PoWahiTunnel.png', 'poTunnel1')
poTunnel2 = Scene('PoWahiTunnel.png', 'poTunnel2')
quarry_L = Scene('QuarryLeft.png', 'quarry_L')
quarry_R = Scene('QuarryRight.png', 'quarry_R')
quarry_F = Scene('QuarryFar.png', 'quarry_F')
quarry_C = Scene('QuarryClose.png', 'quarry_C')
stoneField1 = Scene('StoneField1.png', 'stoneField1')
stoneField2 = Scene('StoneField2.png', 'stoneField2')
stoneField3 = Scene('StoneField3.png', 'stoneField3')
stoneField4 = Scene('StoneField4.png', 'stoneField4')
stoneField5 = Scene('StoneField5.png', 'stoneField5')
Midak_F = Scene('MidakFar.png', 'Midak_F')
Midak_R = Scene('MidakRight.png', 'Midak_R')
Midak_L = Scene('MidakLeft.png', 'Midak_L')
#End Po-Wahi, start Onu-Koro Po-Wahi Highway
onuTunnel1 = Scene('OnuTunnel1.png', 'onuTunnel1')
onuTunnel_PW = Scene('TunnelToPW.png', 'onuTunnel_PW')
onuTunnel2 = Scene('OnuTunnel2.png', 'onuTunnel2')
onuTunnel3 = Scene('OnuTunnel3.png', 'onuTunnel3')
onuTunnel4 = Scene('OnuTunnel4.png', 'onuTunnel4')
onuTunnel5 = Scene('OnuTunnel5.png', 'onuTunnel5')
onuTunnel6 = Scene('OnuTunnel6.png', 'onuTunnel6')
onuTunnel7 = Scene('OnuTunnel7.png', 'onuTunnel7')
onuTunnel8 = Scene('OnuTunnel8.png', 'onuTunnel8')
onuTunnel9 = Scene('OnuTunnel9.png', 'onuTunnel9')
onuTunnel10 = Scene('OnuTunnel10.png', 'onuTunnel10')
onuTunnel11 = Scene('OnuTunnel11.png', 'onuTunnel11')
#End highway, start Onu-Koro
onuKoro1 = Scene('OnuKoro1.png', 'onuKoro1')
onuKoro2 = Scene('OnuKoro2.png', 'onuKoro2')
onuKoro3 = Scene('OnuKoro3.png', 'onuKoro3')
onuKoro4 = Scene('OnuKoro4.png', 'onuKoro4')
onuKoro5 = Scene('OnuKoro5.png', 'onuKoro5')
onuKoro6 = Scene('OnuKoro6.png', 'onuKoro6')
onuKoro7 = Scene('OnuKoro7.png', 'onuKoro7')
onuKoro8 = Scene('OnuKoro8.png', 'onuKoro8')
onuKoro9 = Scene('OnuKoro9.png', 'onuKoro9')
onuKoro10 = Scene('OnuKoro10.png', 'onuKoro10')
onuKoro11 = Scene('NuparusLab.png', 'onuKoro11')
onuKoro12 = Scene('OnuKoro12.png', 'onuKoro12')
onuKoro13 = Scene('OnuKoro13.png', 'onuKoro13')
onuKoro14 = Scene('OnuKoro14.png', 'onuKoro14')
onuKoro15 = Scene('OnuKoro15.png', 'onuKoro15')
onuKoro16 = Scene('OnuKoro16.png', 'onuKoro16')
onuMarket_L = Scene('OnuMarketL.png', 'onuMarket_L')
onuMarket_R = Scene('OnuMarketR.png', 'onuMarket_R')
WhenuasHut = Scene('WhenuasHut.png', 'WhenuasHut')
OnepusHut = Scene('OnepusHut.png', 'OnepusHut')
#End Onu-Koro, start Great Mine
onuTunnel12 = Scene('OnuTunnel12.png', 'onuTunnel12')
onuTunnel13 = Scene('OnuTunnel10.png', 'onuTunnel13')
onuTunnel14 = Scene('OnuTunnel14.png', 'onuTunnel14')
onuTunnel15 = Scene('OnuTunnel15.png', 'onuTunnel15')
onuTunnel16 = Scene('OnuTunnel16.png', 'onuTunnel16')
onuTunnel17 = Scene('OnuTunnel17.png', 'onuTunnel17')
onuTunnel18 = Scene('OnuTunnel18.png', 'onuTunnel18')
greatMine1 = Scene('GreatMine1.png', 'greatMine1')
greatMine2 = Scene('GreatMine2.png', 'greatMine2')
greatMine3 = Scene('GreatMine3.png', 'greatMine3')
ProspectorsLedge = Scene('ProspectorsLedge.png', 'ProspectorsLedge')
onuElevator1 = Scene('OnuElevator1.png', 'onuElevator1')
onuElevator2 = Scene('OnuElevator2.png', 'onuElevator2')
onuElevator3 = Scene('OnuElevator3.png', 'onuElevator3')
#End Great Mine, start Onu-Koro to crossroad
#Tunnels 19-27 are Onu-Koro to the Le-Ta-Koro crossroad
onuTunnel19 = Scene('OnuTunnel19.png', 'onuTunnel19')
onuTunnel20 = Scene('OnuTunnel10.png', 'onuTunnel20')
onuTunnel21 = Scene('OnuTunnel21.png', 'onuTunnel21')
onuTunnel22 = Scene('OnuTunnel22.png', 'onuTunnel22')
onuTunnel23 = Scene('OnuTunnel23.png', 'onuTunnel23')
onuTunnel24 = Scene('OnuTunnel24.png', 'onuTunnel24')
onuTunnel25 = Scene('OnuTunnel25.png', 'onuTunnel25')
onuTunnel26 = Scene('OnuTunnel26.png', 'onuTunnel26')
onuTunnel27 = Scene('OnuTunnel27.png', 'onuTunnel27')
#Tunnels 28-36 are crossroad to Ta-Koro
onuTunnel28 = Scene('OnuTunnel28.png', 'onuTunnel28')
onuTunnel29 = Scene('OnuTunnel29.png', 'onuTunnel29')
onuTunnel30 = Scene('OnuTunnel30.png', 'onuTunnel30')
onuTunnel31 = Scene('OnuTunnel31.png', 'onuTunnel31')
onuTunnel32 = Scene('OnuTunnel31.png', 'onuTunnel32')
onuTunnel33 = Scene('OnuTunnel22.png', 'onuTunnel33')
onuTunnel34 = Scene('OnuTunnel34.png', 'onuTunnel34')
onuTunnel35 = Scene('OnuTunnel35.png', 'onuTunnel35')
onuTunnel36 = Scene('OnuTunnel36.png', 'onuTunnel36')
#Lightstone mine
lightMine1 = Scene('LightMine1.png', 'lightMine1')
lightMine2 = Scene('LightMine2.png', 'lightMine2')
lightMine3 = Scene('LightMine3.png', 'lightMine3')
lightMine4 = Scene('LightMine4.png', 'lightMine4')
lightMine5 = Scene('LightMine5.png', 'lightMine5')
lightMine6 = Scene('LightMine6.png', 'lightMine6')
lightMine7 = Scene('LightMine7.png', 'lightMine7')
lightMine8 = Scene('LightMine8.png', 'lightMine8')
lightMine9 = Scene('LightMine9.png', 'lightMine9')
lightMine10 = Scene('LightMine10.png', 'lightMine10')
lightMine11 = Scene('LightMine11.png', 'lightMine11')
lightMine12 = Scene('LightMine12.png', 'lightMine12')
lightMine13 = Scene('LightMine13.png', 'lightMine13')
#Flooded with lava, will be constructed into a bottleneck
lightMine14 = Scene('LightMine14.png', 'lightMine14')
lightMine15 = Scene('LightMine15.png', 'lightMine15')
lightMine16 = Scene('LightMine16.png', 'lightMine16')
lightMine6_2 = Scene('LightMine6.png', 'lightMine6_2')
lightMine4_2 = Scene('LightMine4.png', 'lightMine4_2')
#Actual Onu-Koro crossroad
onuXRoad_LT = Scene('OnuXRoad_LeTa.png', 'onuXRoad_LT')
onuXRoad_L = Scene('OnuXRoad_Le.png', 'onuXRoad_L')
onuXRoad_OR = Scene('OnuXRoad_OnuR.png', 'onuXRoad_OR')
onuXRoad_OT = Scene('OnuXRoad_OnuTa.png', 'onuXRoad_OT')
#Tunnels 37-45 are crossroad to Le-Koro
onuTunnel37 = Scene('OnuTunnel37.png', 'onuTunnel37')
onuTunnel38 = Scene('OnuTunnel38.png', 'onuTunnel38')
onuTunnel39 = Scene('OnuTunnel39.png', 'onuTunnel39')
onuTunnel40 = Scene('OnuTunnel40.png', 'onuTunnel40')
onuTunnel41 = Scene('OnuTunnel41.png', 'onuTunnel41')
onuTunnel42 = Scene('OnuTunnel42.png', 'onuTunnel42')
onuTunnel43 = Scene('OnuTunnel41.png', 'onuTunnel43')
onuTunnel44 = Scene('OnuTunnel44.png', 'onuTunnel44')
onuTunnel45 = Scene('OnuTunnel45.png', 'onuTunnel45')
onuTunnel46 = Scene('OnuTunnel46.png', 'onuTunnel46')
#Le-Koro digsite
leDig1 = Scene('LeDig1.png', 'leDig1')
leDig2 = Scene('LeDig2.png', 'leDig2')
leDig3 = Scene('LeDig3.png', 'leDig3')
#Ta-Koro
taKoro1 = Scene('TaKoro1.png', 'taKoro1')
taKoro2 = Scene('TaKoro2.png', 'taKoro2')
taKoro3 = Scene('TaKoro3.png', 'taKoro3')
taKoro4 = Scene('TaKoro4.png', 'taKoro4')
taKoro5 = Scene('TaKoro5.png', 'taKoro5')
taKoro6 = Scene('TaKoro6.png', 'taKoro6')
taKoro7 = Scene('TaKoro7.png', 'taKoro7')
taKoro8 = Scene('TaKoro8.png', 'taKoro8')
taKoro9 = Scene('TaKoro9.png', 'taKoro9')
taKoro10 = Scene('TaKoro10.png', 'taKoro10')
taKoro11 = Scene('TaKoro11.png', 'taKoro11')
taKoro12 = Scene('TaKoro12.png', 'taKoro12')
TKCableCar = Scene('TKCableCar.png', 'TKCableCar')
JalasHut1 = Scene('JalasHut1.png', 'JalasHut1')
JalasHut2 = Scene('JalasHut2.png', 'JalasHut2')
VakamasHut = Scene('VakamasHut.png', 'VakamasHut')
#Ta-Wahi, the Beach.  Missing the telescope and the giant mouth.
taWahi1 = Scene('TaWahi1.png', 'taWahi1')
taWahi2 = Scene('TaWahi2.png', 'taWahi2')
taWahi3 = Scene('TaWahi3.png', 'taWahi3')
taWahi4 = Scene('TaWahi4.png', 'taWahi4')
taWahi5 = Scene('TaWahi5.png', 'taWahi5')
taWahi6 = Scene('TaWahi6.png', 'taWahi6')
taWahi7 = Scene('TaWahi7.png', 'taWahi7')
taWahi8 = Scene('TaWahi8.png', 'taWahi8')
taWahi9 = Scene('TaWahi9.png', 'taWahi9')
taWahi10 = Scene('TaWahi10.png', 'taWahi10')
#Ko-Wahi tunnels, fortress, etc.
tunnelEntrance = Scene('TunnelEntrance.png', 'tunnelEntrance')
note = Scene('Note.png', 'note')
fortressFar = Scene('TheFortress.png', 'fortressFar')
fortressEntrance = Scene('FortressEntrance.png', 'fortressEntrance')
fortress1 = Scene('Fortress1.png', 'fortress1')
fortress2 = Scene('Fortress2.png', 'fortress2')
fortress3 = Scene('Fortress3.png', 'fortress3')
fortress4_R = Scene('Fortress4.png', 'fortress4_R')
fortress4_L = Scene('Fortress4.png', 'fortress4_L')
fortress5 = Scene('Fortress5.png', 'fortress5')
fortress6 = Scene('Fortress6.png', 'fortress6')
fortress7 = Scene('Fortress7.png', 'fortress7')
fortress8 = Scene('Fortress8.png', 'fortress8')
fortress9 = Scene('Fortress9.png', 'fortress9')
fortress10 = Scene('Fortress10.png', 'fortress10')
fortress11 = Scene('Fortress11.png', 'fortress11')
fortress12 = Scene('Fortress12.png', 'fortress12')
fortress13 = Scene('Fortress13.png', 'fortress13')
fortress14 = Scene('Fortress14.png', 'fortress14')
fortress15 = Scene('Fortress15.png', 'fortress15')
fortress16 = Scene('Fortress16.png', 'fortress16')
fortress17 = Scene('Fortress17.png', 'fortress17')
fortress18 = Scene('Fortress18.png', 'fortress18')
fortress19 = Scene('Fortress19.png', 'fortress19')
fortress20 = Scene('Fortress20.png', 'fortress20')
fortress21 = Scene('Fortress21.png', 'fortress21')
fortress22 = Scene('Fortress22.png', 'fortress22')
fortress23 = Scene('Fortress23.png', 'fortress23')
fortress24 = Scene('Fortress24.png', 'fortress24')
fortress25 = Scene('Fortress25.png', 'fortress25')
fortress26 = Scene('Fortress26.png', 'fortress26')

#Miscellaneous
TradersHut = Scene('TradersHut.png', 'TradersHut')
TradersHut_Outside = Scene('TradersHut_Outside.png', 'TradersHut_Outside')
PiatarasHut = Scene('PiatarasHut.png', 'PiatarasHut')
OnewasHut = Scene('Onewa.png', 'OnewasHut')
poBoat = Scene('PoWahiBoat.png', 'poBoat')
Gadjati_Koli = Scene('Gadjati.png', 'Gadjati_Koli')
koliField = Scene('Epena_KoliField.png', 'koliField')

#Combination locks
Bomb = Lock('337','Bomb')
elevatorLock = Lock('5887930', 'elevatorLock')

#APPLE levels
Lvl1 = Level('Level1.bmp', 'Lvl1', 'Level1.txt', 'Img2.png')

Lvl2 = Level('Level2.bmp', 'Lvl2', 'Level2.txt', 'Img2.png')

Lvl3 = Level('Level3.bmp', 'Lvl3', 'Level3.txt', 'OnuTunnel17.png', ONUWAHI)

Lvl4 = Level('Level4.bmp', 'Lvl4', 'Level4.txt', 'OnuTunnel46.png', KOWAHI)

Lvl5 = Level('Level5.bmp', 'Lvl5', 'Level5.txt', 'Fortress2.png', KOWAHI)

#CutChapters, in chronological order
chap1 = CutChapter('chapter1.txt', 'chap1', '', 'Post1.ogg')
chap2 = CutChapter('chapter2.txt', 'chap2', 'player.add(APtalk.Piataras_Letter)', 'Post2.ogg')
chap3 = CutChapter('chapter3.txt', 'chap3', '', 'Post3.ogg')
Kylae_Duel = CutChapter('Kylae_Duel.txt', 'Kylae_Duel')
Kylae_Duel_pt2 = CutChapter('Kylae_Duel_pt2.txt', 'Kylae_Duel_pt2')
chap4 = CutChapter('chapter4.txt', 'chap4', 'APtalk.onuKoro3.addHotSpot(APtalk.chap5, pygame.Rect(100,60,330,260), False, player); APtalk.onuKoro3.delHotSpot(APtalk.onuTunnel11, player); APtalk.Kaj.editWords("kaj2.txt", player); APtalk.OKCrab.editWords("OKCrab2.txt", player)', 'Post4.ogg')
chap5 = CutChapter('chapter5.txt', 'chap5', '', 'Post5.ogg')
chap6_pt1 = CutChapter('chapter6_pt1.txt', 'chap6_pt1', 'APtalk.lightMine1.addHotSpot(APtalk.lightMine14, pygame.Rect(400,140,80,260), False, player); APtalk.lightMine1.delHotSpot(APtalk.lightMine3, player); APtalk.lightMine2.addHotSpot(APtalk.lightMine14, pygame.Rect(60,150,80,250), False, player), APtalk.lightMine2.delHotSpot(APtalk.lightMine3, player); APtalk.Onepu.editWords("onepu4.txt", player);APtalk.onuKoro3.addHotSpot(APtalk.onuTunnel11, pygame.Rect(100,60,330,260), False, player); APtalk.onuKoro3.delHotSpot(APtalk.chap5, player)', 'Post6_pt1.ogg')
chap6_pt2 = CutChapter('chapter6_pt2.txt', 'chap6_pt2', 'APtalk.Damek.editWords("damek2.txt", player); APtalk.Lab.editWords("lab2.txt", player)', 'Post6_pt2.ogg')
chap7_pt1 = CutChapter('chapter7_pt1.txt', 'chap7_pt1', '', 'Post7_pt1.ogg')
chap7_pt2 = CutChapter('chapter7_pt2.txt', 'chap7_pt2', '', 'Post7_pt2.ogg')
fall = CutChapter('fall.txt', 'fall', 'player.delCompanion(APtalk.cDamek); player.delCompanion(APtalk.cNuparu)')
regroup = CutChapter('regroup.txt', 'regroup', 'player.addCompanion(APtalk.cDamek); APtalk.cDamek.editWords("cDamek3.txt", player); player.addCompanion(APtalk.cNuparu); APtalk.cNuparu.editWords("cNuparu2.txt", player); APtalk.fortress14.delHotSpot(self, player); APtalk.fortress14.addHotSpot(APtalk.fortress15, pygame.Rect(140,100,340,200), False, player)')
chap8 = CutChapter('chapter8.txt', 'chap8', 'APtalk.TradersHut.addHotSpot(APtalk.TradersHut_Outside, pygame.Rect(500,80,100,160))')
fortressReturn = CutChapter('FortressReturn.txt', 'fortressReturn')
NuparusTale = CutChapter('NuparusTale.txt', 'NuparusTale')

#NPCs
Gadjati = NPC('Gadjati', None, 'gadjati.txt')
Pekka = NPC('Pekka', 'Pekka.png', 'pekka.txt')
Boat = NPC('Boat', None, 'boat.txt')
Hafu = NPC('Hafu', 'Hafu.png', 'hafu.txt')
Onewa = NPC('Onewa', 'OnewaTalk.png', 'onewa.txt')
Ahkmou = NPC('Ahkmou', 'OxTalk.png', 'ahkmou.txt')
HusiGang = NPC('HusiGang', None, 'husiGang.txt')
Epena = NPC('Epena', 'Epena.png', 'epena.txt')
Midak = NPC('Midak', 'Midak.png', 'midak.txt')
OKCrab = NPC('OKCrab', 'OKCrab.png', 'OKCrab.txt')
PWCrab = NPC('PWCrab', 'PWCrab.png', 'PWCrab.txt')
Onepu = NPC('Onepu', 'Onepu.png', 'onepu.txt')
Damek = NPC('Damek', None, 'damek.txt')
Whenua = NPC('Whenua', 'Whenua.png', 'whenua.txt')
Prospector = NPC('Prospector', 'Prospector.png', 'prospector.txt')
Kelati = NPC('Kelati', None, 'kelati.txt')
Kaj = NPC('Kaj', None, 'kaj.txt')
Dashka = NPC('Dashka', None, 'dashka.txt')
Taipu = NPC('Taipu', None, 'taipu.txt')
Megasphere = NPC('Megasphere', None, 'megasphere.txt')
Lab = NPC('Lab', None, 'lab.txt')
Nuparu = NPC('Nuparu', None, 'nuparu.txt')
UssalryHQ = NPC('UssalryHQ', None, 'ussalryHQ.txt')
Kailani = NPC('Kailani', None, 'kailani.txt')
Vohon = NPC('Vohon', None, 'vohon.txt')
Jala = NPC('Jala', 'Jala.png', 'jala.txt')
Vakama = NPC('Vakama', 'Vakama.png', 'vakama.txt')
Agni = NPC('Agni', None, 'agni.txt')
OKElevator = NPC('OKElevator', None, 'OKElevator.txt')
KWElevator = NPC('KWElevator', None, 'KWElevator.txt')
closet = NPC('closet', None, 'closet.txt')
KOdGuard = NPC('KOdGuard', None, 'KOdGuard.txt')
Rama = NPC('Rama', None, 'rama.txt')
Trader = NPC('Trader', None, 'trader.txt')
FortressNuparu = NPC('FortressNuparu', None, 'nuparu2.txt', 'NuparuSprite.png')
FortressDamek = NPC('FortressDamek', None, 'damek3.txt', 'DamekSprite.png')
Nuhrii = NPC('Nuhrii', None, 'nuhrii.txt', 'NuhriiSprite.png')
#Comapnions
cDamek = Companion('cDamek', 'cDamek.txt', 'CDamek.png', 'Damek')
cNuparu = Companion('cNuparu', 'cNuparu.txt', 'CNuparu.png', 'Nuparu')

#Items
Widgets = InventoryItem('Widgets.bmp', 'Widgets', None, 999)
Lightstone = InventoryItem('Lightstone.bmp', 'Lightstone')
Koli_Ball = InventoryItem('KoliBall.bmp', 'Koli_Ball', 'Koli Ball')
JalasRing = InventoryItem('JalasRing.bmp', "JalasRing", "Jala's Ring")
OnepusRing = InventoryItem('OnepusRing.bmp', "OnepusRing", "Onepu's Ring")
TranqDart = InventoryItem('TranqDart.bmp', 'TranqDart', '???')
Plate = Plate()
Disk = InventoryItem('Disk.png', 'Disk')
HammerHatchet = InventoryItem('HammerHatchet.png', 'HammerHatchet', 'Hammer-Hatchet')
Empty_Bottle = Empty_Bottle()
Water_Bottle = Water_Bottle()
Pure_Water = Pure_Water()
Piataras_Letter = PiatarasLetter()
print('Items created!')

centerRect = pygame.Rect(100, 200, 300, 100)

startScene.addHotSpot(poRoad1, pygame.Rect(460, 200, 90, 100))
startScene.returnSpot(poBoat)

poRoad1.addHotSpot(poRoad2, centerRect)
poRoad1.returnSpot(poBeach1)

poBeach1.addHotSpot(poBoat, centerRect)
poBeach1.returnSpot(poRoad1)

poRoad2.addHotSpot(poXRoad1, centerRect)
poRoad2.returnSpot(poBeach2)

poBeach2.addHotSpot(poBeach1, centerRect)
poBeach2.returnSpot(poRoad2)

poXRoad1.addHotSpot(poRoad3, pygame.Rect(50, 100, 100, 300))
poXRoad1.addHotSpot(quarry_F, pygame.Rect(450, 100, 100, 300))
poXRoad1.returnSpot(poBeach3)

quarry_F.addHotSpot(quarry_C, centerRect)
quarry_F.returnSpot(poXRoad1_R)

quarry_C.addHotSpot(poTunnel1, centerRect)
quarry_C.returnSpot(poXRoad1_FR)

quarry_L.addHotSpot(poTunnel2, leftRect)
quarry_L.addHotSpot(quarry_R, rightRect)
quarry_L.addHotSpot(Lvl1, centerRect)

quarry_R.addHotSpot(poTunnel2, rightRect)
quarry_R.addHotSpot(quarry_L, leftRect)

poTunnel1.returnSpot(poRoad8)
poTunnel1.addHotSpot(quarry_L, centerRect)

poTunnel2.addHotSpot(poRoad8, centerRect)
poTunnel2.returnSpot(quarry_L)

poRoad3.addHotSpot(poRoad4, centerRect)
poRoad3.returnSpot(poXRoad1_L)

poXRoad1_L.addHotSpot(poBeach2, pygame.Rect(WX-150, 100, 100, 300))
poXRoad1_L.addHotSpot(quarry_F, pygame.Rect(50, 100, 100, 300))
poXRoad1_L.returnSpot(poRoad3)

poXRoad1_FL.addHotSpot(poXRoad1_L, centerRect)
poXRoad1_FL.returnSpot(poRoad4)

poXRoad1_R.addHotSpot(poBeach2, pygame.Rect(50, 100, 100, 300))
poXRoad1_R.addHotSpot(poRoad3, pygame.Rect(WX-150, 100, 100, 300))
poXRoad1_R.returnSpot(quarry_F)

poXRoad1_FR.addHotSpot(poXRoad1_R, centerRect)
poXRoad1_FR.returnSpot(quarry_C)

poRoad4.addHotSpot(poXRoad2_FB, centerRect)
poRoad4.returnSpot(poXRoad1_FL)

poXRoad2_FB.addHotSpot(poXRoad2_BtOW, centerRect)
poXRoad2_FB.returnSpot(poRoad5)

poXRoad2_BtOW.addHotSpot(poRoad6, leftRect)
poXRoad2_BtOW.addHotSpot(poXRoad2_BtPK, rightRect)
poXRoad2_BtOW.addHotSpot(poRoad10, pygame.Rect(50, 100, 100, 200))

poXRoad2_BtPK.addHotSpot(poRoad6, rightRect)
poXRoad2_BtPK.addHotSpot(poXRoad2_BtOW, leftRect)
poXRoad2_BtPK.addHotSpot(poKoroGate_VF, pygame.Rect(WX-150, 100, 100, 200))

poKoroGate_VF.addHotSpot(poKoroGate_F, centerRect)
poKoroGate_VF.returnSpot(poXRoad2_PKtB)

poKoroGate_F.addHotSpot(poKoroGate_C, centerRect)
poKoroGate_F.returnSpot(poXRoad2_FPK)

poKoroGate_C.addHotSpot(poKoroGate_VC, centerRect)
poKoroGate_C.returnSpot(poRoad7)

poKoroGate_VC.addHotSpot(poKoro1, centerRect)
poKoroGate_VC.returnSpot(poRoad9)

poKoroGate_I.addHotSpot(poRoad9, centerRect)
poKoroGate_I.addHotSpot(poKoro4, leftRect)
poKoroGate_I.addHotSpot(poKoro1, rightRect)

poRoad7.addHotSpot(poXRoad2_FPK, centerRect)
poRoad7.returnSpot(poKoroGate_C)

poRoad8.addHotSpot(poXRoad1_FR, centerRect)
poRoad8.returnSpot(poTunnel1)

poRoad9.addHotSpot(poRoad7, centerRect)
poRoad9.returnSpot(poKoroGate_VC)

poRoad10.addHotSpot(poRoad11, centerRect)
poRoad10.returnSpot(poRoad12)

poRoad11.addHotSpot(stoneField1, centerRect)
poRoad11.returnSpot(poRoad13)

poRoad12.addHotSpot(poXRoad2_OWtB, centerRect)
poRoad12.returnSpot(poRoad10)

poRoad13.addHotSpot(poRoad12, centerRect)
poRoad13.returnSpot(poRoad11)

poXRoad2_FPK.addHotSpot(poXRoad2_PKtB, centerRect)
poXRoad2_FPK.returnSpot(poKoroGate_F)

poXRoad2_PKtB.addHotSpot(poKoroGate_VF, leftRect)
poXRoad2_PKtB.addHotSpot(poXRoad2_PKtOW, rightRect)
poXRoad2_PKtB.addHotSpot(poRoad6, pygame.Rect(50, 200, 100, 200))
poXRoad2_PKtB.addNPC(Hafu, pygame.Rect(WX-200, 225, 100, 100))

poXRoad2_PKtOW.addHotSpot(poKoroGate_VF, rightRect)
poXRoad2_PKtOW.addHotSpot(poXRoad2_PKtB, leftRect)
poXRoad2_PKtOW.addHotSpot(poRoad10, pygame.Rect(350, 150, 200, 150))

poXRoad2_OWtB.addHotSpot(poRoad10, rightRect)
poXRoad2_OWtB.addHotSpot(poRoad6, pygame.Rect(100, 150, 200, 150))
poXRoad2_OWtB.addHotSpot(poXRoad2_OWtPK, leftRect)
poXRoad2_OWtB.addNPC(Hafu, pygame.Rect(WX-150, 200, 100, 100))

poXRoad2_OWtPK.addHotSpot(poRoad10, leftRect)
poXRoad2_OWtPK.addHotSpot(poKoroGate_VF, pygame.Rect(50, 150, 150, 150))
poXRoad2_OWtPK.addHotSpot(poXRoad2_OWtB, rightRect)

poRoad6.addHotSpot(poRoad5, centerRect)
poRoad6.returnSpot(poXRoad2_BtOW)

poRoad5.addHotSpot(poXRoad1_FL, centerRect)
poRoad5.returnSpot(poRoad4)

poBeach3.addHotSpot(poBeach2, centerRect)
poBeach3.returnSpot(poXRoad1)

poKoro1.addHotSpot(koliField, pygame.Rect(450, 150, 100, 200))
poKoro1.addHotSpot(OnewasHut, pygame.Rect(170, 200, 100, 100))
poKoro1.addHotSpot(poKoroGate_I, leftRect)
poKoro1.addHotSpot(poKoro2, rightRect)
poKoro1.addNPC(HusiGang, pygame.Rect(300, 200, 160, 100))

poKoro2.addHotSpot(poKoro1, leftRect)
poKoro2.addHotSpot(poKoro4, rightRect)
poKoro2.addNPC(Ahkmou, pygame.Rect(250, 225, 100, 100))
poKoro2.addItem(Koli_Ball, pygame.Rect(500, 340, 50, 50))

poKoro3.addHotSpot(poKoroGate_I, pygame.Rect(375, 180, 150, 150))
poKoro3.addHotSpot(koliField, leftRect)
poKoro3.addHotSpot(Gadjati_Koli, rightRect)

poKoro4.addHotSpot(poKoro2, leftRect)
poKoro4.addHotSpot(poKoroGate_I, rightRect)
poKoro4.addHotSpot(poGuardStairs_U, pygame.Rect(210,150,170,170))

poGuardStairs_U.addHotSpot(PiatarasHut, pygame.Rect(250,50,60,130))
poGuardStairs_U.returnSpot(poKoro4)

poGuardStairs_D.addHotSpot(poKoro2, pygame.Rect(260,200,60,130))
poGuardStairs_D.returnSpot(PiatarasHut)

PiatarasHut.addHotSpot(chap2, pygame.Rect(50,150,150,150))
PiatarasHut.returnSpot(poGuardStairs_D)

OnewasHut.returnSpot(poKoro1)
OnewasHut.addNPC(Onewa, pygame.Rect(150, 70, 200, 300))

poBoat.returnSpot(startScene)

Gadjati_Koli.addNPC(Gadjati, pygame.Rect(290, 180, 150, 150))
Gadjati_Koli.addHotSpot(koliField, rightRect)
Gadjati_Koli.addHotSpot(poKoro3, leftRect)

koliField.addHotSpot(Gadjati_Koli, leftRect)
koliField.addHotSpot(poKoro3, rightRect)
koliField.addNPC(Epena, pygame.Rect(320, 190, 100, 200))

stoneField1.returnSpot(poRoad13)
stoneField1.addHotSpot(stoneField2, centerRect)

stoneField2.addHotSpot(Midak_F, centerRect)
stoneField2.returnSpot(stoneField3)

stoneField4.addHotSpot(stoneField3, centerRect)
stoneField4.returnSpot(stoneField2)

stoneField3.addHotSpot(poRoad13, centerRect)
stoneField3.returnSpot(stoneField1)

stoneField5.addHotSpot(stoneField4, centerRect)
stoneField5.returnSpot(Midak_F)

Midak_F.addHotSpot(Midak_L, centerRect)
Midak_F.returnSpot(stoneField4)

Midak_L.addHotSpot(stoneField5, leftRect)
Midak_L.addHotSpot(Midak_R, rightRect)
Midak_L.addNPC(Midak, pygame.Rect(230, 240, 150, 150))

Midak_R.addHotSpot(onuTunnel1, pygame.Rect(280,70,220,320))
Midak_R.addHotSpot(Midak_L, leftRect)
Midak_R.addHotSpot(stoneField5, rightRect)
Midak_R.addNPC(PWCrab, pygame.Rect(50,270,175,125))

onuTunnel1.addHotSpot(onuTunnel2, centerRect)
onuTunnel1.returnSpot(onuTunnel_PW)

onuTunnel_PW.addHotSpot(stoneField5, centerRect)
onuTunnel_PW.returnSpot(onuTunnel1)

onuTunnel2.addHotSpot(onuTunnel4, centerRect)
onuTunnel2.returnSpot(onuTunnel3)

onuTunnel3.addHotSpot(onuTunnel_PW, centerRect)
onuTunnel3.returnSpot(onuTunnel2)

onuTunnel4.addHotSpot(onuTunnel6, centerRect)
onuTunnel4.returnSpot(onuTunnel5)

onuTunnel5.addHotSpot(onuTunnel3, pygame.Rect(50,75,200,200))
onuTunnel5.returnSpot(onuTunnel4)

onuTunnel6.addHotSpot(onuTunnel8, centerRect)
onuTunnel6.returnSpot(onuTunnel7)

onuTunnel7.addHotSpot(onuTunnel5, centerRect)
onuTunnel7.returnSpot(onuTunnel6)

onuTunnel8.addHotSpot(onuTunnel10, centerRect)
onuTunnel8.returnSpot(onuTunnel9)

onuTunnel9.addHotSpot(onuTunnel7, centerRect)
onuTunnel9.returnSpot(onuTunnel8)

onuTunnel10.addHotSpot(onuKoro1, centerRect)
onuTunnel10.returnSpot(onuTunnel11)

onuTunnel11.addHotSpot(onuTunnel9, centerRect)
onuTunnel11.returnSpot(onuTunnel10)

onuTunnel12.addHotSpot(onuTunnel14, centerRect)
onuTunnel12.returnSpot(onuTunnel13)

onuTunnel13.addHotSpot(onuKoro16, centerRect)
onuTunnel13.returnSpot(onuTunnel12)

onuTunnel14.addHotSpot(onuTunnel16, centerRect)
onuTunnel14.returnSpot(onuTunnel15)

onuTunnel15.addHotSpot(onuTunnel13, centerRect)
onuTunnel15.returnSpot(onuTunnel14)

onuTunnel16.addHotSpot(greatMine1, centerRect)
onuTunnel16.returnSpot(onuTunnel17)

onuTunnel17.addHotSpot(onuTunnel15, centerRect)
onuTunnel17.returnSpot(onuTunnel16)

onuTunnel18.addHotSpot(onuTunnel17, pygame.Rect(100,50,400,300))
onuTunnel18.returnSpot(greatMine1)

onuTunnel19.addHotSpot(onuTunnel21, centerRect)
onuTunnel19.returnSpot(onuTunnel20)

onuTunnel20.addHotSpot(onuKoro13, centerRect)
onuTunnel20.returnSpot(onuTunnel19)

onuTunnel21.addHotSpot(onuTunnel23, centerRect)
onuTunnel21.returnSpot(onuTunnel22)

onuTunnel22.addHotSpot(onuTunnel20, centerRect)
onuTunnel22.returnSpot(onuTunnel21)

onuTunnel23.addHotSpot(onuTunnel25, centerRect)
onuTunnel23.returnSpot(onuTunnel24)

onuTunnel24.addHotSpot(onuTunnel22, centerRect)
onuTunnel24.returnSpot(onuTunnel23)

onuTunnel25.addHotSpot(onuXRoad_LT, centerRect)
onuTunnel25.returnSpot(onuTunnel26)

onuTunnel26.addHotSpot(onuTunnel24, centerRect)
onuTunnel26.returnSpot(onuTunnel25)

onuTunnel27.addHotSpot(onuTunnel26, centerRect)
onuTunnel27.returnSpot(onuXRoad_LT)

onuTunnel28.addHotSpot(onuTunnel29, centerRect)
onuTunnel28.addHotSpot(onuXRoad_OR, leftRect)
onuTunnel28.addHotSpot(onuXRoad_L, rightRect)

onuTunnel29.addHotSpot(lightMine1, centerRect)
onuTunnel29.returnSpot(onuTunnel30)

onuTunnel30.addHotSpot(onuXRoad_OR, centerRect)
onuTunnel30.returnSpot(onuTunnel29)

onuTunnel31.addHotSpot(onuTunnel30, centerRect)
onuTunnel31.returnSpot(lightMine1)

onuTunnel32.addHotSpot(onuTunnel33, centerRect)
onuTunnel32.returnSpot(lightMine2)

onuTunnel33.addHotSpot(onuTunnel35, centerRect)
onuTunnel33.returnSpot(onuTunnel34)

onuTunnel34.addHotSpot(lightMine2, centerRect)
onuTunnel34.returnSpot(onuTunnel33)

onuTunnel35.addHotSpot(taKoro1, pygame.Rect(240,140,140,140))
onuTunnel35.returnSpot(onuTunnel36)

onuTunnel36.addHotSpot(onuTunnel34, centerRect)
onuTunnel36.returnSpot(onuTunnel35)

onuTunnel37.addHotSpot(onuTunnel38, centerRect)
onuTunnel37.returnSpot(onuXRoad_OT)

onuTunnel38.returnSpot(onuTunnel39)
onuTunnel38.addHotSpot(onuTunnel40, centerRect)

onuTunnel39.addHotSpot(onuXRoad_OT, centerRect)
onuTunnel39.returnSpot(onuTunnel38)

onuTunnel40.addHotSpot(onuTunnel42, centerRect)
onuTunnel40.returnSpot(onuTunnel41)

onuTunnel41.addHotSpot(onuTunnel39, centerRect)
onuTunnel41.returnSpot(onuTunnel40)

onuTunnel42.addHotSpot(leDig1, centerRect)
onuTunnel42.returnSpot(onuTunnel43)

onuTunnel43.addHotSpot(onuTunnel39, centerRect)
onuTunnel43.returnSpot(onuTunnel42)

onuTunnel45.addHotSpot(tunnelEntrance, centerRect)
onuTunnel45.returnSpot(onuElevator3)

onuTunnel46.addHotSpot(onuElevator3, centerRect)
onuTunnel46.returnSpot(tunnelEntrance)

leDig1.addHotSpot(leDig2, pygame.Rect(250,50,300,300))
leDig1.returnSpot(onuTunnel43)

leDig2.addNPC(Taipu, pygame.Rect(270,140,150,300))
leDig2.addHotSpot(leDig3, rightRect)

leDig3.addHotSpot(onuTunnel43, pygame.Rect(50,50,210,300))
leDig3.addHotSpot(leDig2, leftRect)

lightMine1.addHotSpot(lightMine3, pygame.Rect(400,140,80,260))
lightMine1.addHotSpot(onuTunnel32, pygame.Rect(50,100,200,230))
lightMine1.returnSpot(onuTunnel31)

lightMine2.addHotSpot(lightMine3, pygame.Rect(60,150,80,250))
lightMine2.addHotSpot(onuTunnel31, pygame.Rect(300,100,250,250))
lightMine2.returnSpot(onuTunnel32)

lightMine3.addHotSpot(lightMine5, pygame.Rect(250,150,100,150))
lightMine3.returnSpot(lightMine4)

lightMine4.addHotSpot(onuTunnel31, pygame.Rect(50,50,250,300))
lightMine4.addHotSpot(onuTunnel32, pygame.Rect(300,50,250,300))
lightMine4.returnSpot(lightMine3)

lightMine5.addHotSpot(lightMine7, pygame.Rect(250,100,100,150))
lightMine5.returnSpot(lightMine6)

lightMine6.addHotSpot(lightMine4, pygame.Rect(250,150,100,150))
lightMine6.returnSpot(lightMine5)

lightMine7.addNPC(Kaj, pygame.Rect(190,230,190,170))
lightMine7.addHotSpot(lightMine9, pygame.Rect(470,120,80,200))
lightMine7.returnSpot(lightMine8)

lightMine8.addHotSpot(lightMine6, pygame.Rect(230,100,100,150))
lightMine8.returnSpot(lightMine7)

lightMine9.addHotSpot(lightMine10, pygame.Rect(260,200,60,130))
lightMine9.returnSpot(lightMine7)

lightMine10.addHotSpot(lightMine11, leftRect)
lightMine10.addHotSpot(lightMine12, rightRect)

lightMine11.addHotSpot(lightMine10, rightRect)
lightMine11.addHotSpot(lightMine13, leftRect)

lightMine12.addHotSpot(lightMine10, leftRect)
lightMine12.addHotSpot(lightMine13, rightRect)

lightMine13.addHotSpot(lightMine7, pygame.Rect(260,0,60,130))
lightMine13.returnSpot(lightMine10)

lightMine14.addHotSpot(lightMine15, pygame.Rect(250,150,100,150))
lightMine14.returnSpot(lightMine4_2)

lightMine15.addHotSpot(lightMine6_2, rightRect)
lightMine15.addHotSpot(lightMine16, leftRect)

lightMine16.addHotSpot(lightMine15, rightRect)
lightMine16.addHotSpot(lightMine6_2, leftRect)

lightMine6_2.addHotSpot(lightMine16, rightRect)
lightMine6_2.addHotSpot(lightMine15, leftRect)
lightMine6_2.addHotSpot(lightMine4_2, pygame.Rect(250,150,100,150))

lightMine4_2.addHotSpot(onuTunnel31, pygame.Rect(50,50,250,300))
lightMine4_2.addHotSpot(onuTunnel32, pygame.Rect(300,50,250,300))
lightMine4_2.returnSpot(lightMine14)

onuXRoad_LT.addHotSpot(onuTunnel37, pygame.Rect(380,100,170,220))
onuXRoad_LT.addHotSpot(onuTunnel28, pygame.Rect(50,110,170,220))
onuXRoad_LT.returnSpot(onuTunnel27)

onuXRoad_OR.addHotSpot(onuTunnel27, pygame.Rect(230,90,320,230))
onuXRoad_OR.addHotSpot(onuXRoad_L, leftRect)
onuXRoad_OR.addHotSpot(onuTunnel28, rightRect)

onuXRoad_L.addHotSpot(onuTunnel37, pygame.Rect(125,120,225,200))
onuXRoad_L.addHotSpot(onuXRoad_OR, rightRect)
onuXRoad_L.addHotSpot(onuTunnel28, leftRect)

onuXRoad_OT.addHotSpot(onuTunnel27, pygame.Rect(50,70,190,260))
onuXRoad_OT.addHotSpot(onuTunnel28, pygame.Rect(410,120,140,200))
onuXRoad_OT.returnSpot(onuTunnel37)

greatMine1.addHotSpot(greatMine2, pygame.Rect(360,180,150,150))
greatMine1.returnSpot(onuTunnel18)

greatMine2.addHotSpot(ProspectorsLedge, pygame.Rect(410,130,100,100))
greatMine2.addHotSpot(onuElevator1, pygame.Rect(50,170,150,150))
greatMine2.returnSpot(greatMine3)

greatMine3.addHotSpot(onuTunnel18, centerRect)
greatMine3.returnSpot(greatMine2)

onuElevator1.addNPC(OKElevator, pygame.Rect(300,60,100,100))
onuElevator1.returnSpot(greatMine2)

onuElevator2.addNPC(KWElevator, pygame.Rect(300,60,100,100))
onuElevator2.returnSpot(onuTunnel45)

onuElevator3.addHotSpot(onuElevator2, pygame.Rect(130,160,200,200))
onuElevator3.returnSpot(onuTunnel45)

ProspectorsLedge.addNPC(Prospector, pygame.Rect(160,190,200,150))
ProspectorsLedge.returnSpot(greatMine2)

onuKoro1.addHotSpot(onuKoro3, leftRect)
onuKoro1.addHotSpot(onuKoro2, rightRect)
onuKoro1.addHotSpot(OnepusHut, pygame.Rect(50,270,75,75))
onuKoro1.addHotSpot(onuKoro4, pygame.Rect(170,150,130,120))
onuKoro1.addNPC(Damek, pygame.Rect(390,240,160,160))

onuKoro2.addHotSpot(onuKoro1, leftRect)
onuKoro2.addHotSpot(onuKoro3, rightRect)
onuKoro2.addNPC(Damek, pygame.Rect(110,240,190,160))
onuKoro2.addNPC(Lab, pygame.Rect(480,265,60,60))

onuKoro3.addHotSpot(onuKoro2, leftRect)
onuKoro3.addHotSpot(onuKoro1, rightRect)
onuKoro3.addHotSpot(onuTunnel11, pygame.Rect(100,60,230,260))
onuKoro3.addNPC(OKCrab, pygame.Rect(350,250,175,125))

onuKoro4.addHotSpot(onuKoro7, pygame.Rect(50,70,250,300))
onuKoro4.addHotSpot(onuKoro8, pygame.Rect(300,70,250,300))
onuKoro4.addHotSpot(onuMarket_R, leftRect)
onuKoro4.addHotSpot(onuMarket_L, rightRect)

onuKoro5.addHotSpot(onuMarket_L,pygame.Rect(50,150,250,150))
onuKoro5.addHotSpot(onuMarket_R,pygame.Rect(300,150,250,150))
onuKoro5.addHotSpot(onuKoro8, leftRect)
onuKoro5.addHotSpot(onuKoro6, rightRect)

onuKoro6.addHotSpot(onuKoro14, pygame.Rect(420,150,100,150))
onuKoro6.addHotSpot(onuKoro5, leftRect)
onuKoro6.addHotSpot(onuKoro7, rightRect)

onuKoro7.addHotSpot(onuKoro9, pygame.Rect(130,130,100,100))
onuKoro7.addHotSpot(onuKoro8, rightRect)
onuKoro7.addHotSpot(onuKoro6, leftRect)

onuKoro8.addHotSpot(WhenuasHut, pygame.Rect(360,180,100,100))
onuKoro8.addHotSpot(onuKoro7, leftRect)
onuKoro8.addHotSpot(onuKoro5, rightRect)

onuKoro9.addNPC(Kelati, pygame.Rect(220,250,120,100))
onuKoro9.addHotSpot(onuTunnel19, pygame.Rect(375,120,175,200))
onuKoro9.addHotSpot(onuKoro10, rightRect)
onuKoro9.addHotSpot(onuKoro12, leftRect)

onuKoro10.addHotSpot(onuTunnel19, pygame.Rect(50,110,300,200))
onuKoro10.addHotSpot(onuKoro9, leftRect)
onuKoro10.addHotSpot(onuKoro13, rightRect)

onuKoro11.addNPC(Nuparu, pygame.Rect(370,180,150,150))
onuKoro11.returnSpot(onuKoro2)

onuKoro12.addHotSpot(onuKoro14, pygame.Rect(410,190,100,150))
onuKoro12.addHotSpot(onuKoro13, leftRect)
onuKoro12.addHotSpot(onuKoro9, rightRect)

onuKoro13.addHotSpot(onuKoro5, centerRect)
onuKoro13.addHotSpot(onuKoro12, rightRect)
onuKoro13.addHotSpot(onuKoro10, leftRect)

onuKoro14.addHotSpot(onuTunnel12, pygame.Rect(50,120,300,200))
onuKoro14.addHotSpot(onuKoro16, leftRect)
onuKoro14.addHotSpot(onuKoro15, rightRect)

onuKoro15.addHotSpot(onuKoro9, pygame.Rect(70,150,100,150))
onuKoro15.addHotSpot(onuKoro16, rightRect)
onuKoro15.addHotSpot(onuKoro14, leftRect)

onuKoro16.addHotSpot(onuKoro8, centerRect)
onuKoro16.addHotSpot(onuKoro15, leftRect)
onuKoro16.addHotSpot(onuKoro14, rightRect)

onuMarket_R.addNPC(UssalryHQ, pygame.Rect(450,260,100,100))
onuMarket_R.addNPC(Vohon, pygame.Rect(170,270,80,80))
onuMarket_R.addHotSpot(onuKoro3, pygame.Rect(50,150,100,100))
onuMarket_R.addHotSpot(onuMarket_L, leftRect)
onuMarket_R.addHotSpot(onuKoro4, rightRect)

onuMarket_L.addNPC(Kailani, pygame.Rect(290,260,80,80))
onuMarket_L.addNPC(Megasphere, pygame.Rect(410,250,100,100))
onuMarket_L.addNPC(Dashka, pygame.Rect(80,280,120,120))
onuMarket_L.addHotSpot(onuMarket_R, rightRect)
onuMarket_L.addHotSpot(onuKoro4, leftRect)

taKoro1.addHotSpot(taKoro2, centerRect)
taKoro1.returnSpot(onuTunnel36)

taKoro2.addHotSpot(VakamasHut, pygame.Rect(460,160,70,130))
taKoro2.addHotSpot(taKoro3, pygame.Rect(240,180,60,60))
taKoro2.returnSpot(taKoro6)

taKoro3.addHotSpot(taKoro7, pygame.Rect(250,80,160,200))
taKoro3.addHotSpot(taKoro4, leftRect)
taKoro3.addHotSpot(taKoro5, rightRect)

taKoro4.addHotSpot(taKoro3, rightRect)
taKoro4.addHotSpot(taKoro5, leftRect)
taKoro4.addNPC(Agni, pygame.Rect(390,230,160,170))

taKoro5.addHotSpot(VakamasHut, pygame.Rect(80,190,100,210))
taKoro5.addHotSpot(taKoro6, pygame.Rect(390,170,60,60))
taKoro5.addHotSpot(taKoro3, leftRect)
taKoro5.addHotSpot(taKoro4, rightRect)

taKoro6.addHotSpot(onuTunnel36, pygame.Rect(180,120,250,220))
taKoro6.returnSpot(taKoro2)

taKoro7.addHotSpot(taWahi10, pygame.Rect(135,70,265,230))
taKoro7.addHotSpot(JalasHut1, pygame.Rect(70,200,65,140))
taKoro7.returnSpot(taKoro8)

taKoro8.addHotSpot(taKoro5, centerRect)
taKoro8.returnSpot(taKoro7)

taKoro10.addHotSpot(taKoro12, leftRect)
taKoro10.addHotSpot(taWahi10, rightRect)

taKoro12.addHotSpot(taKoro8, pygame.Rect(100,100,280,200))
taKoro12.addHotSpot(JalasHut1, pygame.Rect(390,170,50,100))
taKoro12.addHotSpot(taWahi10, leftRect)
taKoro12.addHotSpot(taKoro10, rightRect)

taWahi1.addHotSpot(taWahi5, centerRect)
taWahi1.returnSpot(taWahi9)

taWahi2.addHotSpot(taWahi9, pygame.Rect(100,100,400,200))
taWahi2.returnSpot(taWahi5)

taWahi5.addHotSpot(taWahi7, centerRect)
taWahi5.returnSpot(taWahi2)

taWahi7.addHotSpot(taWahi6, rightRect)

taWahi6.addHotSpot(taWahi2, pygame.Rect(400,140,150,200))
taWahi6.addHotSpot(taWahi7, leftRect)

taWahi9.addHotSpot(taKoro12, centerRect)
taWahi9.returnSpot(taWahi1)

taWahi10.addHotSpot(taKoro12, rightRect)
taWahi10.addHotSpot(taKoro10, leftRect)
taWahi10.addHotSpot(taWahi1, centerRect)

VakamasHut.addNPC(Vakama, pygame.Rect(190,160,200,210))
VakamasHut.returnSpot(taKoro5)

JalasHut1.addHotSpot(taKoro7, pygame.Rect(0,80,140,230))
JalasHut1.addHotSpot(JalasHut2, rightRect)

JalasHut2.addNPC(Jala, pygame.Rect(120,170,100,170))
JalasHut2.addHotSpot(JalasHut1, leftRect)

tunnelEntrance.addHotSpot(fortressFar, pygame.Rect(90,100,250,300))
tunnelEntrance.addHotSpot(note, pygame.Rect(400,100,100,100))
tunnelEntrance.returnSpot(onuTunnel46)

note.returnSpot(tunnelEntrance)

fortressFar.addHotSpot(fall, centerRect)

fortressEntrance.addHotSpot(Lvl4, centerRect)

fortress1.addHotSpot(fortress2, pygame.Rect(230,80,130,200))

fortress2.addHotSpot(fortress5, pygame.Rect(230,90,120,140))
fortress2.addHotSpot(fortress4_R, rightRect)
fortress2.addHotSpot(fortress4_L, leftRect)

fortress3.addHotSpot(fortress1, centerRect)
fortress3.addHotSpot(fortress4_R, leftRect)
fortress3.addHotSpot(fortress4_L, rightRect)

fortress4_R.addNPC(closet, pygame.Rect(230,40,140,300))
fortress4_R.addHotSpot(fortress2, leftRect)
fortress4_R.addHotSpot(fortress3, rightRect)

fortress4_L.addNPC(closet, pygame.Rect(230,40,140,300))
fortress4_L.addHotSpot(fortress2, rightRect)
fortress4_L.addHotSpot(fortress3, leftRect)

fortress5.addHotSpot(fortress10, pygame.Rect(230,100,140,250))
fortress5.addHotSpot(fortress6, leftRect)
fortress5.addHotSpot(fortress7, rightRect)

fortress6.addHotSpot(fortress5, rightRect)
fortress6.addHotSpot(fortress9, leftRect)

fortress7.addHotSpot(fortress5, leftRect)
fortress7.addHotSpot(fortress9, rightRect)

fortress8.returnSpot(fortress10)

fortress9.addHotSpot(fortress3, pygame.Rect(230,90,120,140))
fortress9.addHotSpot(fortress6, rightRect)
fortress9.addHotSpot(fortress7, leftRect)

fortress10.addHotSpot(fortress8, pygame.Rect(200,70,200,200))
fortress10.addHotSpot(fortress12, pygame.Rect(450,50,150,350))
fortress10.addHotSpot(fortress11, leftRect)

fortress11.addHotSpot(fortress10, rightRect)
fortress11.addHotSpot(fortress13, leftRect)

fortress12.addNPC(KOdGuard, pygame.Rect(150,190,200,100))
fortress12.addHotSpot(fortress13, rightRect)
fortress12.addHotSpot(fortress10, leftRect)

fortress13.addHotSpot(fortress9, pygame.Rect(140,100,340,200))
fortress13.returnSpot(fortress10)

fortress14.addHotSpot(regroup, pygame.Rect(140,100,340,200))
fortress14.returnSpot(fortress10)

fortress15.addHotSpot(fortress17, leftRect)

fortress17.addHotSpot(fortress18, pygame.Rect(150,100,300,250))
fortress17.returnSpot(fortress15)

fortress18.addHotSpot(fortress20, pygame.Rect(200,100,170,170))
fortress18.returnSpot(fortress19)

fortress19.addHotSpot(fortress15, pygame.Rect(150,100,300,250))
fortress19.returnSpot(fortress18)

fortress20.addHotSpot(fortress22, pygame.Rect(270,130,100,100))
fortress20.returnSpot(fortress21)

fortress21.addHotSpot(fortress19, pygame.Rect(150,100,300,250))
fortress21.returnSpot(fortress20)

fortress22.addHotSpot(chap7_pt1, pygame.Rect(140,100,340,200))

fortress23.addHotSpot(fortress24, leftRect)
fortress23.addHotSpot(fortress26, rightRect)
fortress23.addHotSpot(fortress25, pygame.Rect(330,140,100,150))

fortress24.returnSpot(fortress23)
fortress24.addNPC(Nuhrii, pygame.Rect(200,200,150,120))

fortress25.returnSpot(fortress23)
fortress25.addNPC(FortressNuparu, pygame.Rect(300,200,100,100))

fortress26.returnSpot(fortress23)
fortress26.addNPC(FortressDamek, pygame.Rect(300,200,150,120))

TradersHut.addNPC(Trader, pygame.Rect(325,150,100,100))

TradersHut_Outside.returnSpot(TradersHut)
TradersHut_Outside.addNPC(Rama, pygame.Rect(200,120,200,150))

OnepusHut.returnSpot(onuKoro1)
OnepusHut.addNPC(Onepu, pygame.Rect(140,160,320,220))

WhenuasHut.returnSpot(onuKoro8)
WhenuasHut.addNPC(Whenua, pygame.Rect(300,200,200,190))

startScene.addNPC(Pekka, pygame.Rect(375,225,100,100))
poBoat.addNPC(Boat, centerRect)
poXRoad2_BtOW.addNPC(Hafu, pygame.Rect(150,225,100,100))


Lvl1.addTarget(startScene)
Lvl2.addTarget(startScene)
Lvl3.addTarget(Kylae_Duel)
Lvl4.addTarget(fortress1)
Lvl5.addTarget(chap7_pt2)
chap1.addTarget(startScene)
chap2.addTarget(poKoro2)
chap3.addTarget(Lvl3)
chap4.addTarget(onuKoro4)
chap5.addTarget(onuKoro4)
chap6_pt1.addTarget(lightMine14)
chap6_pt2.addTarget(OnepusHut)
chap7_pt1.addTarget(Lvl5)
chap7_pt2.addTarget(TradersHut)
Kylae_Duel.addTarget(Kylae_Duel_pt2)
Kylae_Duel_pt2.addTarget(Bomb)
fall.addTarget(fortressEntrance)
regroup.addTarget(fortress15)
chap8.addTarget(TradersHut)
fortressReturn.addTarget(fortress23)
NuparusTale.addTarget(fortress25)
Bomb.addTargets(chap4, Kylae_Duel_pt2)
elevatorLock.addTargets(onuElevator2, onuElevator1)

finished = True

print('Done with scenes')

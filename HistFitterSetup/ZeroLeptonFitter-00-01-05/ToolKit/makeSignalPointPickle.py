#!/usr/bin/env python

import pickle

outfile = open('signalPointPickle.pkl','wb')
pointdict = {};

pointdict['SS_direct'] = {
    370700: (200,0),
    370701: (400,0),
    370702: (400,375),
    370703: (425,375),
    370704: (400,350),
    370705: (400,300),
    370706: (500,475),
    370707: (500,450),
    370708: (500,400),
    370709: (600,0),
    370710: (600,500),
    370711: (600,400),
    370712: (600,575),
    370713: (600,550),
    370714: (800,100),
    370715: (800,300),
    370716: (800,500),
    370717: (800,600),
    370718: (900,0),
    370719: (900,100),
    370720: (900,200),
    370721: (900,300),
    370722: (900,400),
    370723: (800,0),
    370724: (800,200),
    370725: (800,400),
    370726: (900,500),
    370727: (900,600),
    370728: (1000,100),
    370729: (1000,300),
    370730: (1000,500),
    370731: (1000,600),
    370732: (1100,0),
    370733: (1100,100),
    370734: (1100,200),
    370735: (1100,300),
    370736: (1000,0),
    370737: (1000,200),
    370738: (1000,400),
    370739: (1100,400),
    370740: (1100,500),
    370741: (1100,600),
    370742: (1200,100),
    370743: (1200,300),
    370744: (1200,400),
    370745: (1200,500),
    370746: (1200,600),
    370747: (1300,0),
    370748: (1300,100),
    370749: (1200,0),
    370750: (1200,200),
    370751: (1300,200),
    370752: (1300,300),
    370753: (1300,400),
    370754: (1300,500),
    370755: (1300,600),
    370756: (1400,100),
    370757: (1400,200),
    370758: (1400,300),
    370759: (1400,400),
    370760: (1400,500),
    370761: (1400,600),
    370762: (1400,0),
    370763: (1500,0),
    370764: (1500,100),
    370765: (1500,200),
    370766: (1500,300),
    370767: (1500,400),
    370768: (1500,500),
    370769: (1500,600),
    370770: (1600,100),
    370771: (1600,200),
    370772: (1600,300),
    370773: (1600,400),
    370774: (1600,500),
    370775: (1600,0),
    370776: (1600,600),
    370777: (200,100),
    370778: (200,175),
    370779: (200,150),
    370780: (300,0),
    370781: (300,100),
    370782: (300,200),
    370783: (300,275),
    370784: (300,250),
    370785: (400,100),
    370786: (400,200),
    370787: (500,0),
    370788: (500,100),
    370789: (500,200),
    370790: (500,300),
    370791: (600,100),
    370792: (600,200),
    370793: (600,300),
    370794: (700,0),
    370795: (700,100),
    370796: (700,200),
    370797: (700,300),
    370798: (700,400),
    370799: (700,500),
    370800: (700,600),
    370801: (600,300),
    370802: (600,500),
    370803: (650,250),
    370804: (650,450),
    370805: (700,200),
    370806: (700,400),
    370807: (750,150),
    370808: (750,350),
    370809: (800,100),
    370810: (800,300),
    370811: (850,50),
    370812: (850,250),
    370813: (900,0),
    370814: (900,200),
    370815: (950,150),
    370816: (1000,100),
    370817: (1050,50),
    370818: (1100,0),
    }

pointdict['GG_direct'] = {
    370900: (200,0),
    370901: (400,0),
    370902: (600,0),
    370903: (612,587),
    370904: (625,575),
    370905: (650,550),
    370906: (700,500),
    370907: (712,687),
    370908: (725,675),
    370909: (750,650),
    370910: (800,0),
    370911: (800,600),
    370912: (812,787),
    370913: (825,775),
    370914: (850,550),
    370915: (850,750),
    370916: (900,500),
    370917: (900,700),
    370918: (912,887),
    370919: (925,875),
    370920: (950,650),
    370921: (950,850),
    370922: (1000,0),
    370923: (1000,600),
    370924: (1000,800),
    370925: (1050,550),
    370926: (1050,750),
    370927: (1100,100),
    370928: (1100,300),
    370929: (1100,500),
    370930: (1100,700),
    370931: (1100,900),
    370932: (1150,50),
    370933: (1150,250),
    370934: (1150,450),
    370935: (1150,650),
    370936: (1150,850),
    370937: (1200,0),
    370938: (1200,200),
    370939: (1200,400),
    370940: (1200,600),
    370941: (1200,800),
    370942: (1250,150),
    370943: (1250,350),
    370944: (1250,550),
    370945: (1250,750),
    370946: (1300,100),
    370947: (1300,300),
    370948: (1300,500),
    370949: (1300,700),
    370950: (1300,900),
    370951: (1350,50),
    370952: (1350,250),
    370953: (1350,450),
    370954: (1350,650),
    370955: (1350,850),
    370956: (1400,0),
    370957: (1400,200),
    370958: (1400,400),
    370959: (1400,600),
    370960: (1400,800),
    370961: (1450,150),
    370962: (1450,350),
    370963: (1450,550),
    370964: (1450,750),
    370965: (1500,100),
    370966: (1500,300),
    370967: (1500,500),
    370968: (1500,700),
    370969: (1500,900),
    370970: (1550,50),
    370971: (1550,250),
    370972: (1550,450),
    370973: (1550,650),
    370974: (1550,850),
    370975: (1600,0),
    370976: (1600,200),
    370977: (1600,400),
    370978: (1600,600),
    370979: (1600,800),
    370980: (1650,150),
    370981: (1650,350),
    370982: (1650,550),
    370983: (1650,750),
    370984: (1700,100),
    370985: (1700,300),
    370986: (1700,500),
    370987: (1700,700),
    370988: (1700,900),
    370989: (1750,50),
    370990: (1750,250),
    370991: (1750,450),
    370992: (1750,650),
    370993: (1750,850),
    370994: (1800,0),
    370995: (1800,200),
    370996: (1800,400),
    370997: (1800,600),
    370998: (1800,800),
    370999: (1850,150),
    371000: (1850,350),
    371001: (1850,550),
    371002: (1850,750),
    371003: (1900,100),
    371004: (1900,300),
    371005: (1900,500),
    371006: (1900,700),
    371007: (1900,900),
    371008: (1950,50),
    371009: (1950,250),
    371010: (1950,450),
    371011: (1950,650),
    371012: (1950,850),
    371013: (2000,0),
    371014: (2000,200),
    371015: (2000,400),
    371016: (2000,600),
    371017: (2000,800),
    371018: (112,87),
    371019: (125,75),
    371020: (150,50),
    371021: (212,187),
    371022: (225,175),
    371023: (250,150),
    371024: (300,100),
    371025: (312,287),
    371026: (325,275),
    371027: (350,50),
    371028: (350,250),
    371029: (400,200),
    371030: (412,387),
    371031: (425,375),
    371032: (450,150),
    371033: (450,350),
    371034: (500,100),
    371035: (500,300),
    371036: (512,487),
    371037: (525,475),
    371038: (550,50),
    371039: (550,250),
    371040: (550,450),
    371041: (600,200),
    371042: (600,400),
    371043: (650,150),
    371044: (650,350),
    371045: (662,637),
    371046: (675,625),
    371047: (700,100),
    371048: (700,300),
    371049: (700,600),
    371050: (750,50),
    371051: (750,250),
    371052: (750,450),
    371053: (750,550),
    371054: (762,737),
    371055: (775,725),
    371056: (800,200),
    371057: (800,400),
    371058: (800,500),
    371059: (800,700),
    371060: (850,150),
    371061: (850,350),
    371062: (850,450),
    371063: (850,650),
    371064: (862,837),
    371065: (875,825),
    371066: (900,100),
    371067: (900,300),
    371068: (900,400),
    371069: (900,600),
    371070: (900,800),
    371071: (950,50),
    371072: (950,250),
    371073: (950,350),
    371074: (950,450),
    371075: (950,550),
    371076: (950,750),
    371077: (1000,200),
    371078: (1000,300),
    371079: (1000,400),
    371080: (1000,500),
    371081: (1000,700),
    371082: (1012,987),
    371083: (1025,975),
    371084: (1050,150),
    371085: (1050,250),
    371086: (1050,350),
    371087: (1050,450),
    371088: (1050,650),
    371089: (1050,950),
    371090: (1100,200),
    371091: (1100,400),
    371092: (1100,600),
    371093: (1150,150),
    371094: (1150,350),
    371095: (1150,550),
    371096: (1200,100),
    371097: (1200,300),
    371098: (1200,500),
    371099: (1200,1000),
    371100: (1250,50),
    371101: (1250,250),
    371102: (1250,450),
    371103: (1250,950),
    371104: (1300,0),
    371105: (1300,200),
    371106: (1300,400),
    371107: (1350,150),
    371108: (1350,350),
    371109: (1400,100),
    371110: (1400,300),
    371111: (1400,1000),
    371112: (1450,50),
    371113: (1450,250),
    371114: (1450,950),
    371115: (1500,0),
    371116: (1500,200),
    371117: (1550,150),
    371118: (1600,100),
    371119: (1600,1000),
    371120: (1650,50),
    371121: (1650,950),
    371122: (1700,0),
    371123: (1800,1000),
    371124: (1850,950),
    371125: (2000,1000),
    406000: (1500,0),    
    }

pointdict['GG_onestepCC'] = {
    371500:(237,226,215),
    371501:(265,225,185),
    371502:(317,306,295),
    371503:(345,305,265),
    371504:(397,386,375),
    371505:(425,385,345),
    371506:(477,466,455),
    371507:(505,465,425),
    371508:(557,546,535),
    371509:(585,545,505),
    371510:(637,626,615),
    371511:(665,625,585),
    371512:(717,706,695),
    371513:(745,625,505),
    371514:(745,705,665),
    371515:(785,705,625),
    371516:(797,786,775),
    371517:(825,785,745),
    371518:(877,866,855),
    371519:(905,705,505),
    371520:(905,865,825),
    371521:(945,785,625),
    371522:(957,946,935),
    371523:(985,865,745),
    371524:(985,945,905),
    371525:(1025,945,865),
    371526:(1037,1026,1015),
    371527:(1065,1025,985),
    371528:(1065,545,25),
    371529:(1065,785,505),
    371530:(1105,625,145),
    371531:(1105,865,625),
    371532:(1145,705,265),
    371533:(1145,945,745),
    371534:(1185,1025,865),
    371535:(1185,785,385),
    371536:(1225,1105,985),
    371537:(1225,625,25),
    371538:(1225,865,505),
    371539:(1265,705,145),
    371540:(1265,945,625),
    371541:(1305,1025,745),
    371542:(1305,785,265),
    371543:(1345,1105,865),
    371544:(1345,865,385),
    371545:(1385,1185,985),
    371546:(1385,705,25),
    371547:(1385,945,505),
    371548:(1425,1025,625),
    371549:(1425,785,145),
    371550:(1465,1105,745),
    371551:(1465,865,265),
    371552:(1505,1185,865),
    371553:(1505,945,385),
    371554:(1545,1025,505),
    371555:(1545,1265,985),
    371556:(1545,785,25),
    371557:(1585,1105,625),
    371558:(1585,865,145),
    371559:(1625,1185,745),
    371560:(1625,945,265),
    371561:(1665,1025,385),
    371562:(1665,1265,865),
    371563:(265,145,25),
    371564:(305,225,145),
    371565:(425,225,25),
    371566:(465,305,145),
    371567:(505,385,265),
    371568:(545,465,385),
    371569:(585,305,25),
    371570:(625,385,145),
    371571:(665,465,265),
    371572:(705,545,385),
    371573:(745,385,25),
    371574:(785,465,145),
    371575:(825,545,265),
    371576:(865,625,385),
    371577:(905,465,25),
    371578:(945,545,145),
    371579:(985,625,265),
    371580:(1025,705,385),
    371581:(1705,1105,505),
    371582:(1705,1345,985),
    371583:(1705,865,25),
    371584:(1745,1185,625),
    371585:(1745,945,145),
    371586:(1785,1025,265),
    371587:(1785,1265,745),
    371588:(1825,1105,385),
    371589:(1825,1345,865),
    371590:(1865,1185,505),
    371591:(1865,945,25),
    371592:(1905,1025,145),
    371593:(1905,1265,625),
    371594:(1945,1105,265),
    371595:(1945,1345,745),
    371596:(1985,1185,385),
    371597:(2025,1025,25),
    371598:(2025,1265,505),
    371650:(1000,70,60),
    371651:(1000,110,60),
    371652:(1000,160,60),
    371653:(1000,260,60),
    371654:(1000,460,60),
    371655:(1000,660,60),
    371656:(1000,800,60),
    371657:(1000,860,60),
    371658:(1000,900,60),
    371659:(1000,950,60),
    371660:(1000,990,60),
    371661:(1200,70,60),
    371662:(1200,110,60),
    371663:(1200,160,60),
    371664:(1200,260,60),
    371665:(1200,460,60),
    371666:(1200,660,60),
    371667:(1200,860,60),
    371668:(1200,1000,60),
    371669:(1200,1060,60),
    371670:(1200,1100,60),
    371671:(1200,1150,60),
    371672:(1200,1190,60),
    371673:(1400,70,60),
    371674:(1400,110,60),
    371675:(1400,160,60),
    371676:(1400,260,60),
    371677:(1400,460,60),
    371678:(1400,660,60),
    371679:(1400,860,60),
    371680:(1400,1060,60),
    371681:(1400,1200,60),
    371682:(1400,1260,60),
    371683:(1400,1300,60),
    371684:(1400,1350,60),
    371685:(1400,1390,60),
    371686:(1600,70,60),
    371687:(1600,110,60),
    371688:(1600,160,60),
    371689:(1600,260,60),
    371690:(1600,460,60),
    371691:(1600,660,60),
    371692:(1600,860,60),
    371693:(1600,1060,60),
    371694:(1600,1260,60),
    371695:(1600,1400,60),
    371696:(1600,1460,60),
    371697:(1600,1500,60),
    371698:(1600,1550,60),
    371699:(1600,1590,60),
    371700:(200,70,60),
    371701:(200,100,60),
    371702:(200,110,60),
    371703:(200,150,60),
    371704:(200,160,60),
    371705:(200,190,60),
    371706:(400,70,60),
    371707:(400,110,60),
    371708:(400,160,60),
    371709:(400,200,60),
    371710:(400,260,60),
    371711:(400,300,60),
    371712:(400,350,60),
    371713:(400,390,60),
    371714:(600,70,60),
    371715:(600,110,60),
    371716:(600,160,60),
    371717:(600,260,60),
    371718:(600,400,60),
    371719:(600,460,60),
    371720:(600,500,60),
    371721:(600,550,60),
    371722:(600,590,60),
    371723:(800,70,60),
    371724:(800,110,60),
    371725:(800,160,60),
    371726:(800,260,60),
    371727:(800,460,60),
    371728:(800,600,60),
    371729:(800,660,60),
    371730:(800,700,60),
    371731:(800,750,60),
    371732:(800,790,60),
    371733:(1300,70,60),
    371734:(1300,110,60),
    371735:(1300,160,60),
    371736:(1300,260,60),
    371737:(1300,460,60),
    371738:(1300,660,60),
    371739:(1300,860,60),
    371740:(1300,1060,60),
    371741:(1300,1100,60),
    371742:(1300,1200,60),
    371743:(1300,1250,60),
    371744:(1300,1260,60),
    371745:(1300,1290,60),
    371746:(1500,70,60),
    371747:(1500,110,60),
    371748:(1500,160,60),
    371749:(1500,260,60),
    371750:(1500,460,60),
    371751:(1500,660,60),
    371752:(1500,860,60),
    371753:(1500,1060,60),
    371754:(1500,1260,60),
    371755:(1500,1300,60),
    371756:(1500,1400,60),
    371757:(1500,1450,60),
    371758:(1500,1460,60),
    371759:(1500,1490,60),
    371760:(1800,70,60),
    371761:(1800,110,60),
    371762:(1800,160,60),
    371763:(1800,260,60),
    371764:(1800,460,60),
    371765:(1800,660,60),
    371766:(1800,860,60),
    371767:(1800,1060,60),
    371768:(1800,1260,60),
    371769:(1800,1460,60),
    371770:(1800,1600,60),
    371771:(1800,1660,60),
    371772:(1800,1700,60),
    371773:(1800,1750,60),
    371774:(1800,1790,60),
    371775:(2000,70,60),
    371776:(2000,110,60),
    371777:(2000,160,60),
    371778:(2000,260,60),
    371779:(2000,460,60),
    371780:(2000,660,60),
    371781:(2000,860,60),
    371782:(2000,1060,60),
    371783:(2000,1260,60),
    371784:(2000,1460,60),
    371785:(2000,1660,60),
    371786:(2000,1800,60),
    371787:(2000,1860,60),
    371788:(2000,1900,60),
    371789:(2000,1950,60),
    371790:(2000,1990,60),

}

pointdict['Gtt'] = {
    }

pickle.dump(pointdict,outfile)
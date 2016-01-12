import socket, struct

def double_quote(word):
    double_q = '"' # double quote
    return double_q + word + double_q

def quote(word):
    q = "'" #  quote
    return q + word + q


def isp_lookup(ip_txt):

    packedIP = socket.inet_aton(ip_txt)
    ip = struct.unpack("!L", packedIP)[0]
    if ip in range( 3167817728 , 3167821823 +1): return "ITC" # 188.209.16.0 , 188.209.31.255
    if ip in range( 3167821824 , 3167825919 +1): return "ITC" # 188.209.32.0 , 188.209.47.255
    if ip in range( 3167830016 , 3167834111 +1): return "ITC" # 188.209.64.0 , 188.209.79.255
    if ip in range( 3167911936 , 3167928319 +1): return "ITC" # 188.210.128.0 , 188.210.191.255
    if ip in range( 3167903744 , 3167911935 +1): return "ITC" # 188.210.96.0 , 188.210.127.255
    if ip in range( 3167977472 , 3167985663 +1): return "ITC" # 188.211.128.0 , 188.211.159.255
    if ip in range( 3167989760 , 3167993855 +1): return "ITC" # 188.211.176.0 , 188.211.191.255
    if ip in range( 3167993856 , 3168002047 +1): return "ITC" # 188.211.192.0 , 188.211.223.255
    if ip in range( 3167952896 , 3167961087 +1): return "ITC" # 188.211.32.0 , 188.211.63.255
    if ip in range( 3167961088 , 3167977471 +1): return "ITC" # 188.211.64.0 , 188.211.127.255
    if ip in range( 3168051200 , 3168059391 +1): return "ITC" # 188.212.160.0 , 188.212.191.255
    if ip in range( 3168063488 , 3168067583 +1): return "ITC" # 188.212.208.0 , 188.212.223.255
    if ip in range( 3168067584 , 3168071679 +1): return "ITC" # 188.212.224.0 , 188.212.239.255
    if ip in range( 3168026624 , 3168034815 +1): return "ITC" # 188.212.64.0 , 188.212.95.255
    if ip in range( 3168112640 , 3168116735 +1): return "ITC" # 188.213.144.0 , 188.213.159.255
    if ip in range( 3168120832 , 3168124927 +1): return "ITC" # 188.213.176.0 , 188.213.191.255
    if ip in range( 3168100352 , 3168108543 +1): return "ITC" # 188.213.96.0 , 188.213.127.255
    if ip in range( 3168182272 , 3168190463 +1): return "ITC" # 188.214.160.0 , 188.214.191.255
    if ip in range( 3168239616 , 3168243711 +1): return "ITC" # 188.215.128.0 , 188.215.143.255
    if ip in range( 3168247808 , 3168255999 +1): return "ITC" # 188.215.160.0 , 188.215.191.255
    if ip in range( 3168256000 , 3168264191 +1): return "ITC" # 188.215.192.0 , 188.215.223.255
    if ip in range( 3281133568 , 3281141759 +1): return "ITC" # 195.146.32.0 , 195.146.63.255
    if ip in range( 3654942720 , 3655073791 +1): return "ITC" # 217.218.0.0 , 217.219.255.255
    if ip in range( 45088768 , 46137343 +1): return "ITC" # 2.176.0.0 , 2.191.255.255
    if ip in range( 521048064 , 521052159 +1): return "ITC" # 31.14.144.0 , 31.14.159.255
    if ip in range( 521031680 , 521035775 +1): return "ITC" # 31.14.80.0 , 31.14.95.255
    if ip in range( 631009280 , 631013375 +1): return "ITC" # 37.156.112.0 , 37.156.127.255
    if ip in range( 631013376 , 631017471 +1): return "ITC" # 37.156.128.0 , 37.156.143.255
    if ip in range( 778305536 , 778371071 +1): return "ITC" # 46.100.0.0 , 46.100.255.255
    if ip in range( 99090432 , 99614719 +1): return "ITC" # 5.232.0.0 , 5.239.255.255
    if ip in range( 1297162240 , 1297166335 +1): return "ITC" # 77.81.32.0 , 77.81.47.255
    if ip in range( 1311113216 , 1311244287 +1): return "ITC" # 78.38.0.0 , 78.39.255.255
    if ip in range( 1354694656 , 1354760191 +1): return "ITC" # 80.191.0.0 , 80.191.255.255
    if ip in range( 1438187520 , 1438253055 +1): return "ITC" # 85.185.0.0 , 85.185.255.255
    if ip in range( 1439485952 , 1439490047 +1): return "ITC" # 85.204.208.0 , 85.204.223.255
    if ip in range( 1439453184 , 1439457279 +1): return "ITC" # 85.204.80.0 , 85.204.95.255
    if ip in range( 1449676800 , 1449680895 +1): return "ITC" # 86.104.80.0 , 86.104.95.255
    if ip in range( 1449680896 , 1449684991 +1): return "ITC" # 86.104.96.0 , 86.104.111.255
    if ip in range( 1449754624 , 1449758719 +1): return "ITC" # 86.105.128.0 , 86.105.143.255
    if ip in range( 1449889792 , 1449893887 +1): return "ITC" # 86.107.144.0 , 86.107.159.255
    if ip in range( 1449873408 , 1449877503 +1): return "ITC" # 86.107.80.0 , 86.107.95.255
    if ip in range( 1507573760 , 1507590143 +1): return "ITC" # 89.219.192.0 , 89.219.255.255
    if ip in range( 1507540992 , 1507557375 +1): return "ITC" # 89.219.64.0 , 89.219.127.255
    if ip in range( 1495576576 , 1495580671 +1): return "ITC" # 89.36.176.0 , 89.36.191.255
    if ip in range( 1495543808 , 1495547903 +1): return "ITC" # 89.36.48.0 , 89.36.63.255
    if ip in range( 1495556096 , 1495560191 +1): return "ITC" # 89.36.96.0 , 89.36.111.255
    if ip in range( 1495658496 , 1495662591 +1): return "ITC" # 89.37.240.0 , 89.37.255.255
    if ip in range( 1495683072 , 1495687167 +1): return "ITC" # 89.38.80.0 , 89.38.95.255
    if ip in range( 1495855104 , 1495859199 +1): return "ITC" # 89.40.240.0 , 89.40.255.255
    if ip in range( 1538883584 , 1538891775 +1): return "ITC" # 91.185.128.0 , 91.185.159.255
    if ip in range( 1567948800 , 1567956991 +1): return "ITC" # 93.117.0.0 , 93.117.31.255
    if ip in range( 1567956992 , 1567961087 +1): return "ITC" # 93.117.32.0 , 93.117.47.255
    if ip in range( 1567973376 , 1567981567 +1): return "ITC" # 93.117.96.0 , 93.117.127.255
    if ip in range( 1568047104 , 1568055295 +1): return "ITC" # 93.118.128.0 , 93.118.159.255
    if ip in range( 1568055296 , 1568059391 +1): return "ITC" # 93.118.160.0 , 93.118.175.255
    if ip in range( 1568038912 , 1568047103 +1): return "ITC" # 93.118.96.0 , 93.118.127.255
    if ip in range( 1568088064 , 1568096255 +1): return "ITC" # 93.119.32.0 , 93.119.63.255
    if ip in range( 1568096256 , 1568104447 +1): return "ITC" # 93.119.64.0 , 93.119.95.255
    if ip in range( 2548957184 , 2549088255 +1): return "Shatel" # 151.238.0.0 , 151.239.255.255
    if ip in range( 2549088256 , 2549612543 +1): return "Shatel" # 151.240.0.0 , 151.247.255.255
    if ip in range( 523763712 , 524025855 +1): return "Shatel" # 31.56.0.0 , 31.59.255.255
    if ip in range( 1425080320 , 1425096703 +1): return "Shatel" # 84.241.0.0 , 84.241.63.255
    if ip in range( 1427046400 , 1427062783 +1): return "Shatel" # 85.15.0.0 , 85.15.63.255
    if ip in range( 1588985856 , 1589116927 +1): return "Shatel" # 94.182.0.0 , 94.183.255.255
    if ip in range( 42991616 , 43253759 +1): return "Irancell" # 2.144.0.0 , 2.147.255.255
    if ip in range( 91226112 , 92274687 +1): return "Irancell" # 5.112.0.0 , 5.127.255.255
    iif ip in range( 3002892288 , 3002908671 +1): return "MABNA" # 178.252.128.0 , 178.252.191.255
    if ip in range( 532185088 , 532201471 +1): return "MABNA" # 31.184.128.0 , 31.184.191.255
    if ip in range( 628277248 , 628293631 +1): return "MABNA" # 37.114.192.0 , 37.114.255.255
    if ip in range( 635240448 , 635256831 +1): return "MABNA" # 37.221.0.0 , 37.221.63.255
    if ip in range( 97910784 , 98041855 +1): return "MABNA" # 5.214.0.0 , 5.215.255.255
    if ip in range( 98041856 , 98172927 +1): return "MABNA" # 5.216.0.0 , 5.217.255.255
    if ip in range( 98172928 , 98238463 +1): return "MABNA" # 5.218.0.0 , 5.218.255.255
    if ip in range( 98271232 , 98303999 +1): return "MABNA" # 5.219.128.0 , 5.219.255.255
    if ip in range( 98254848 , 98271231 +1): return "MABNA" # 5.219.64.0 , 5.219.127.255
    if ip in range( 98304000 , 98566143 +1): return "MABNA" # 5.220.0.0 , 5.223.255.255
    if ip in range( 1361031168 , 1361035263 +1): return "Sharif-University" # 81.31.176.0 , 81.31.191.255
    if ip in range( 3641380864 , 3641384959 +1): return "Afranet" # 217.11.16.0 , 217.11.31.255
    if ip in range( 521039872 , 521043967 +1): return "Afranet" # 31.14.112.0 , 31.14.127.255
    if ip in range( 523182080 , 523190271 +1): return "Afranet" # 31.47.32.0 , 31.47.63.255
    if ip in range( 778469376 , 778473471 +1): return "Afranet" # 46.102.128.0 , 46.102.143.255
    if ip in range( 1315815424 , 1315819519 +1): return "Afranet" # 78.109.192.0 , 78.109.207.255
    if ip in range( 1336901632 , 1336918015 +1): return "Afranet" # 79.175.128.0 , 79.175.191.255
    if ip in range( 1347092480 , 1347096575 +1): return "Afranet" # 80.75.0.0 , 80.75.15.255
    if ip in range( 1364889600 , 1364893695 +1): return "Afranet" # 81.90.144.0 , 81.90.159.255
    if ip in range( 1449664512 , 1449668607 +1): return "Afranet" # 86.104.32.0 , 86.104.47.255
    if ip in range( 1567744000 , 1567748095 +1): return "Afranet" # 93.113.224.0 , 93.113.239.255
    if ip in range( 532779008 , 532783103 +1): return "Arian-Rasaneh-Pars" # 31.193.144.0 , 31.193.159.255
    if ip in range( 3162406912 , 3162415103 +1): return "Arian-Rasaneh-Pars" # 188.126.128.0 , 188.126.159.255
    if ip in range( 1603198976 , 1603203071 +1): return "Armaghan-Rahe-Talaie" # 95.142.224.0 , 95.142.239.255
    if ip in range( 520585216 , 520589311 +1): return "Aryan-Sat" # 31.7.128.0 , 31.7.143.255
    if ip in range( 3586326528 , 3586334719 +1): return "Arya-Sepehr" # 213.195.0.0 , 213.195.31.255
    if ip in range( 1318723584 , 1318731775 +1): return "Arya-Sepehr-Ettelarasan-Tehran" # 78.154.32.0 , 78.154.63.255
    if ip in range( 1319018496 , 1319026687 +1): return "Arya-Sepehr-Ettelarasan-Tehran" # 78.158.160.0 , 78.158.191.255
    if ip in range( 1843494912 , 1843511295 +1): return "Asiatech" # 109.225.128.0 , 109.225.191.255
    if ip in range( 2151788544 , 2151792639 +1): return "Asiatech" # 128.65.176.0 , 128.65.191.255
    if ip in range( 3001991168 , 3001995263 +1): return "Asiatech" # 178.238.192.0 , 178.238.207.255
    if ip in range( 520577024 , 520585215 +1): return "Asiatech" # 31.7.96.0 , 31.7.127.255
    if ip in range( 624918528 , 624951295 +1): return "Asiatech" # 37.63.128.0 , 37.63.255.255
    if ip in range( 781123584 , 781139967 +1): return "Asiatech" # 46.143.0.0 , 46.143.63.255
    if ip in range( 781156352 , 781172735 +1): return "Asiatech" # 46.143.128.0 , 46.143.191.255
    if ip in range( 781139968 , 781156351 +1): return "Asiatech" # 46.143.64.0 , 46.143.127.255
    if ip in range( 782516224 , 782532607 +1): return "Asiatech" # 46.164.64.0 , 46.164.127.255
    if ip in range( 94437376 , 94470143 +1): return "Asiatech" # 5.161.0.0 , 5.161.127.255
    if ip in range( 94470144 , 94502911 +1): return "Asiatech" # 5.161.128.0 , 5.161.255.255
    if ip in range( 100270080 , 100302847 +1): return "Asiatech" # 5.250.0.0 , 5.250.127.255
    if ip in range( 87367680 , 87375871 +1): return "Asiatech" # 5.53.32.0 , 5.53.63.255
    if ip in range( 1333723136 , 1333755903 +1): return "Asiatech" # 79.127.0.0 , 79.127.127.255
    if ip in range( 1599225856 , 1599242239 +1): return "Asiatech" # 95.82.64.0 , 95.82.127.255
    if ip in range( 96903168 , 96911359 +1): return "Asiatech" # 5.198.160.0 , 5.198.191.255
    if ip in range( 85327872 , 85360639 +1): return "Asitech" # 5.22.0.0 , 5.22.127.255
    if ip in range( 3156344832 , 3156410367 +1): return "Asre-Enteghal-Dadeha" # 188.34.0.0 , 188.34.255.255
    if ip in range( 1358794752 , 1358798847 +1): return "Azadnet-Rasaneh" # 80.253.144.0 , 80.253.159.255
    if ip in range( 1508589568 , 1508605951 +1): return "Azadnet-Rasaneh" # 89.235.64.0 , 89.235.127.255
    if ip in range( 1533689856 , 1533698047 +1): return "Badr-Rayan-Jonoob" # 91.106.64.0 , 91.106.95.255
    if ip in range( 622882816 , 622886911 +1): return "Baran" # 37.32.112.0 , 37.32.127.255
    if ip in range( 1835999232 , 1836007423 +1): return "Behin-Saman-Gostar" # 109.111.32.0 , 109.111.63.255
    if ip in range( 1843806208 , 1843822591 +1): return "Boomerang-Rayaneh" # 109.230.64.0 , 109.230.127.255
    if ip in range( 2156658688 , 2156691455 +1): return "Bozorg-Net-e-Aria" # 128.140.0.0 , 128.140.127.255
    if ip in range( 1599111168 , 1599127551 +1): return "Bozorg-Net-e-Aria" # 95.80.128.0 , 95.80.191.255
    if ip in range( 1475903488 , 1475911679 +1): return "CallWithMe" # 87.248.128.0 , 87.248.159.255
    if ip in range( 1361043456 , 1361051647 +1): return "Chapar-Rasaneh" # 81.31.224.0 , 81.31.255.255
    if ip in range( 1547546624 , 1547550719 +1): return "Arian-Rasaneh-Pars" # 92.61.176.0 , 92.61.191.255
    if ip in range( 85377024 , 85385215 +1): return "Dadeh-Pardazan" # 5.22.192.0 , 5.22.223.255
    if ip in range( 1839366144 , 1839398911 +1): return "DATAK" # 109.162.128.0 , 109.162.255.255
    if ip in range( 1364951040 , 1364955135 +1): return "DATAK" # 81.91.128.0 , 81.91.143.255
    if ip in range( 1364955136 , 1364959231 +1): return "DATAK" # 81.91.144.0 , 81.91.159.255
    if ip in range( 3587162112 , 3587178495 +1): return "DATAK" # 213.207.192.0 , 213.207.255.255
    if ip in range( 1538801664 , 1538809855 +1): return "DATAK" # 91.184.64.0 , 91.184.95.255
    if ip in range( 1586208768 , 1586216959 +1): return "DATAK" # 94.139.160.0 , 94.139.191.255
    if ip in range( 1052835840 , 1052844031 +1): return "DP-IRAN" # 62.193.0.0 , 62.193.31.255
    if ip in range( 637403136 , 637534207 +1): return "Esfahan-Telecom" # 37.254.0.0 , 37.255.255.255
    if ip in range( 98238464 , 98254847 +1): return "Esfahan-Telecom" # 5.219.0.0 , 5.219.63.255
    if ip in range( 2765586432 , 2765619199 +1): return "Fanava-Group" # 164.215.128.0 , 164.215.255.255
    if ip in range( 1596325888 , 1596391423 +1): return "Fanava-Group" # 95.38.0.0 , 95.38.255.255
    if ip in range( 1318920192 , 1318928383 +1): return "Fanava-Group" # 78.157.32.0 , 78.157.63.255
    if ip in range( 1507676160 , 1507680255 +1): return "Fanava-Group" # 89.221.80.0 , 89.221.95.255
    if ip in range( 3558981632 , 3558989823 +1): return "Fanavaran-Ettelaaat-Dibagaran-Karaj" # 212.33.192.0 , 212.33.223.255
    if ip in range( 1842061312 , 1842069503 +1): return "Farahoosh-Dena" # 109.203.160.0 , 109.203.191.255
    if ip in range( 2955837440 , 2955845631 +1): return "Farahoosh-Dena" # 176.46.128.0 , 176.46.159.255
    if ip in range( 531247104 , 531251199 +1): return "Farahoosh-Dena" # 31.170.48.0 , 31.170.63.255
    if ip in range( 1581940736 , 1581957119 +1): return "Farahoosh-Dena" # 94.74.128.0 , 94.74.191.255
    if ip in range( 774275072 , 774283263 +1): return "Farhang-Azma" # 46.38.128.0 , 46.38.159.255
    if ip in range( 3557834752 , 3557842943 +1): return "Farhang-Azma" # 212.16.64.0 , 212.16.95.255
    if ip in range( 3562012672 , 3562020863 +1): return "Farhang-Azma" # 212.80.0.0 , 212.80.31.255
    if ip in range( 96337920 , 96403455 +1): return "Fars-Telecom" # 5.190.0.0 , 5.190.255.255
    if ip in range( 2548563968 , 2548826111 +1): return "Fars-Telecom" # 151.232.0.0 , 151.235.255.255
    if ip in range( 3564683264 , 3564691455 +1): return "Hamara-System-Tabriz" # 212.120.192.0 , 212.120.223.255
    if ip in range( 787808256 , 787841023 +1): return "Hamara-System-Tabriz" # 46.245.0.0 , 46.245.127.255
    if ip in range( 1599160320 , 1599176703 +1): return "Hamara-System-Tabriz" # 95.81.64.0 , 95.81.127.255
    if ip in range( 90578944 , 90583039 +1): return "Hamshahri" # 5.102.32.0 , 5.102.47.255
    if ip in range( 3563028480 , 3563032575 +1): return "Hesabgar" # 212.95.128.0 , 212.95.143.255
    if ip in range( 3644887040 , 3644891135 +1): return "Homa-Idea-Process" # 217.64.144.0 , 217.64.159.255
    if ip in range( 3562422272 , 3562430463 +1): return "Homaye-Jahan-Nama" # 212.86.64.0 , 212.86.95.255
    if ip in range( 2959417344 , 2959421439 +1): return "IRAN" # 176.101.32.0 , 176.101.47.255
    if ip in range( 528658432 , 528662527 +1): return "IRAN" # 31.130.176.0 , 31.130.191.255
    if ip in range( 781459456 , 781463551 +1): return "IRAN" # 46.148.32.0 , 46.148.47.255
    if ip in range( 1412415488 , 1412431871 +1): return "IRAN" # 84.47.192.0 , 84.47.255.255
    if ip in range( 1542692864 , 1542696959 +1): return "IRAN" # 91.243.160.0 , 91.243.175.255
    if ip in range( 1568538624 , 1568555007 +1): return "IRAN" # 93.126.0.0 , 93.126.63.255
    if ip in range( 2959532032 , 2959540223 +1): return "IRAN" # 176.102.224.0 , 176.102.255.255
    if ip in range( 2960867328 , 2960883711 +1): return "IRAN" # 176.123.64.0 , 176.123.127.255
    if ip in range( 3000434688 , 3000451071 +1): return "IRAN" # 178.215.0.0 , 178.215.63.255
    if ip in range( 3000754176 , 3000758271 +1): return "IRAN" # 178.219.224.0 , 178.219.239.255
    if ip in range( 3247931392 , 3247939583 +1): return "IRAN" # 193.151.128.0 , 193.151.159.255
    if ip in range( 3580751872 , 3580755967 +1): return "IRAN" # 213.109.240.0 , 213.109.255.255
    if ip in range( 3651952640 , 3651960831 +1): return "IRAN" # 217.172.96.0 , 217.172.127.255
    if ip in range( 1485250560 , 1485254655 +1): return "IRAN" # 88.135.32.0 , 88.135.47.255
    if ip in range( 3585081344 , 3585089535 +1): return "Iranian-Research-Org" # 213.176.0.0 , 213.176.31.255
    if ip in range( 3585089536 , 3585097727 +1): return "Iranian-Research-Org" # 213.176.32.0 , 213.176.63.255
    if ip in range( 3585097728 , 3585114111 +1): return "Iranian-Research-Org" # 213.176.64.0 , 213.176.127.255
    if ip in range( 1044152320 , 1044185087 +1): return "Iranian-Research-Org" # 62.60.128.0 , 62.60.255.255
    if ip in range( 2956496896 , 2956500991 +1): return "Irianian-ITC" # 176.56.144.0 , 176.56.159.255
    if ip in range( 1294237696 , 1294270463 +1): return "IRIB" # 77.36.128.0 , 77.36.255.255
    if ip in range( 3642306560 , 3642310655 +1): return "IRNA" # 217.25.48.0 , 217.25.63.255
    if ip in range( 1360797696 , 1360801791 +1): return "IsIran" # 81.28.32.0 , 81.28.47.255
    if ip in range( 1360801792 , 1360805887 +1): return "IsIran" # 81.28.48.0 , 81.28.63.255
    if ip in range( 1836761088 , 1836769279 +1): return "Jahan-Ruye-Khat" # 109.122.192.0 , 109.122.223.255
    if ip in range( 1844359168 , 1844363263 +1): return "Khalij-Ettela-Resan-Jonoub" # 109.238.176.0 , 109.238.191.255
    if ip in range( 1833484288 , 1833488383 +1): return "Khalij-Ettela-Resan-Jonoub" # 109.72.192.0 , 109.72.207.255
    if ip in range( 2957197312 , 2957201407 +1): return "Khalij-Ettela-Resan-Jonoub" # 176.67.64.0 , 176.67.79.255
    if ip in range( 1567490048 , 1567555583 +1): return "Laser" # 93.110.0.0 , 93.110.255.255
    f ip in range( 2760540160 , 2760556543 +1): return "MCC" # 164.138.128.0 , 164.138.191.255
    if ip in range( 3169124352 , 3169157119 +1): return "MCC" # 188.229.0.0 , 188.229.127.255
    if ip in range( 520257536 , 520290303 +1): return "MCC" # 31.2.128.0 , 31.2.255.255
    if ip in range( 629211136 , 629276671 +1): return "MCC" # 37.129.0.0 , 37.129.255.255
    if ip in range( 775094272 , 775127039 +1): return "MCC" # 46.51.0.0 , 46.51.127.255
    if ip in range( 97517568 , 97648639 +1): return "MCC" # 5.208.0.0 , 5.209.255.255
    if ip in range( 97648640 , 97714175 +1): return "MCC" # 5.210.0.0 , 5.210.255.255
    if ip in range( 97714176 , 97779711 +1): return "MCC" # 5.211.0.0 , 5.211.255.255
    if ip in range( 97779712 , 97910783 +1): return "MCC" # 5.212.0.0 , 5.213.255.255
    if ip in range( 1446445056 , 1446510591 +1): return "MCC" # 86.55.0.0 , 86.55.255.255
    if ip in range( 1506017280 , 1506082815 +1): return "MCC" # 89.196.0.0 , 89.196.255.255
    if ip in range( 1506148352 , 1506181119 +1): return "MCC" # 89.198.0.0 , 89.198.127.255
    if ip in range( 1506181120 , 1506213887 +1): return "MCC" # 89.198.128.0 , 89.198.255.255
    if ip in range( 1506213888 , 1506279423 +1): return "MCC" # 89.199.0.0 , 89.199.255.255
    if ip in range( 1543176192 , 1543241727 +1): return "MCC" # 91.251.0.0 , 91.251.255.255
    if ip in range( 1598029824 , 1598062591 +1): return "MCC" # 95.64.0.0 , 95.64.127.255
    if ip in range( 90832896 , 90898431 +1): return "MCC" # 5.106.0.0 , 5.106.255.255
    if ip in range( 1844379648 , 1844383743 +1): return "Mehvar-Machine" # 109.239.0.0 , 109.239.15.255
    if ip in range( 774004736 , 774012927 +1): return "MellatInsurance" # 46.34.96.0 , 46.34.127.255
    if ip in range( 788242432 , 788250623 +1): return "METANET-SEPAHAN" # 46.251.160.0 , 46.251.191.255
    if ip in range( 1836769280 , 1836777471 +1): return "MIHAN" # 109.122.224.0 , 109.122.255.255
    if ip in range( 781172736 , 781189119 +1): return "MIHAN" # 46.143.192.0 , 46.143.255.255
    if ip in range( 1835835392 , 1835843583 +1): return "MobinNet" # 109.108.160.0 , 109.108.191.255
    if ip in range( 1842053120 , 1842061311 +1): return "MobinNet" # 109.203.128.0 , 109.203.159.255
    if ip in range( 2197798912 , 2197815295 +1): return "MobinNet" # 130.255.192.0 , 130.255.255.255
    if ip in range( 2994929664 , 2994995199 +1): return "MobinNet" # 178.131.0.0 , 178.131.255.255
    if ip in range( 3162136576 , 3162144767 +1): return "MobinNet" # 188.122.96.0 , 188.122.127.255
    if ip in range( 3167862784 , 3167866879 +1): return "MobinNet" # 188.209.192.0 , 188.209.207.255
    if ip in range( 3167928320 , 3167932415 +1): return "MobinNet" # 188.210.192.0 , 188.210.207.255
    if ip in range( 3167895552 , 3167899647 +1): return "MobinNet" # 188.210.64.0 , 188.210.79.255
    if ip in range( 3167944704 , 3167948799 +1): return "MobinNet" # 188.211.0.0 , 188.211.15.255
    if ip in range( 3168022528 , 3168026623 +1): return "MobinNet" # 188.212.48.0 , 188.212.63.255
    if ip in range( 3168092160 , 3168096255 +1): return "MobinNet" # 188.213.64.0 , 188.213.79.255
    if ip in range( 630984704 , 630988799 +1): return "MobinNet" # 37.156.16.0 , 37.156.31.255
    if ip in range( 627179520 , 627212287 +1): return "MobinNet" # 37.98.0.0 , 37.98.127.255
    if ip in range( 87293952 , 87359487 +1): return "MobinNet" # 5.52.0.0 , 5.52.255.255
    if ip in range( 1046904832 , 1046908927 +1): return "MobinNet" # 62.102.128.0 , 62.102.143.255
    if ip in range( 1358036992 , 1358041087 +1): return "MobinNet" # 80.242.0.0 , 80.242.15.255
    if ip in range( 1441775616 , 1441783807 +1): return "MobinNet" # 85.239.192.0 , 85.239.223.255
    if ip in range( 1449852928 , 1449857023 +1): return "MobinNet" # 86.107.0.0 , 86.107.15.255
    if ip in range( 1449906176 , 1449910271 +1): return "MobinNet" # 86.107.208.0 , 86.107.223.255
    if ip in range( 1495597056 , 1495601151 +1): return "MobinNet" # 89.37.0.0 , 89.37.15.255
    if ip in range( 1495990272 , 1495994367 +1): return "MobinNet" # 89.43.0.0 , 89.43.15.255
    if ip in range( 1496133632 , 1496137727 +1): return "MobinNet" # 89.45.48.0 , 89.45.63.255
    if ip in range( 1535475712 , 1535508479 +1): return "MobinNet" # 91.133.128.0 , 91.133.255.255
    if ip in range( 1550979072 , 1550983167 +1): return "MobinNet" # 92.114.16.0 , 92.114.31.255
    if ip in range( 1567993856 , 1567997951 +1): return "MobinNet" # 93.117.176.0 , 93.117.191.255
    if ip in range( 1583710208 , 1583714303 +1): return "MobinNet" # 94.101.128.0 , 94.101.143.255
    if ip in range( 1583738880 , 1583742975 +1): return "MobinNet" # 94.101.240.0 , 94.101.255.255
    if ip in range( 97091584 , 97124351 +1): return "MobinNet" # 5.201.128.0 , 5.201.255.255
    if ip in range( 1334099968 , 1334108159 +1): return "Morva-System" # 79.132.192.0 , 79.132.223.255
    if ip in range( 3652063232 , 3652067327 +1): return "National-Iranian-Oil" # 217.174.16.0 , 217.174.31.255
    if ip in range( 3164471296 , 3164602367 +1): return "Neda-Gostar-Saba" # 188.158.0.0 , 188.159.255.255
    if ip in range( 1503985664 , 1504018431 +1): return "Neda-Gostar-Saba" # 89.165.0.0 , 89.165.127.255
    if ip in range( 1495916544 , 1495920639 +1): return "Neda-Gostar-Saba" # 89.41.224.0 , 89.41.239.255
    if ip in range( 1588596736 , 1588600831 +1): return "Neda-Gostar-Saba" # 94.176.16.0 , 94.176.31.255
    if ip in range( 1588604928 , 1588609023 +1): return "Neda-Gostar-Saba" # 94.176.48.0 , 94.176.63.255
    if ip in range( 1588613120 , 1588617215 +1): return "Neda-Gostar-Saba" # 94.176.80.0 , 94.176.95.255
    if ip in range( 1505280000 , 1505288191 +1): return "Neda" # 89.184.192.0 , 89.184.223.255
    if ip in range( 3650277376 , 3650281471 +1): return "Neda-Rayaneh" # 217.146.208.0 , 217.146.223.255
    if ip in range( 3645030400 , 3645034495 +1): return "Neda-Rayaneh" # 217.66.192.0 , 217.66.207.255
    if ip in range( 3645034496 , 3645038591 +1): return "Neda-Rayaneh" # 217.66.208.0 , 217.66.223.255
    if ip in range( 1315897344 , 1315901439 +1): return "Neda-Rayaneh" # 78.111.0.0 , 78.111.15.255
    if ip in range( 1346859008 , 1346863103 +1): return "Neda-Rayaneh" # 80.71.112.0 , 80.71.127.255
    if ip in range( 1475846144 , 1475854335 +1): return "Neda-Rayaneh" # 87.247.160.0 , 87.247.191.255
    if ip in range( 3002925056 , 3002941439 +1): return "Oracle-Investment" # 178.253.0.0 , 178.253.63.255
    if ip in range( 1402191872 , 1402208255 +1): return "Oracle-Investment" # 83.147.192.0 , 83.147.255.255
    if ip in range( 1592885248 , 1592901631 +1): return "Oracle-Investment" # 94.241.128.0 , 94.241.191.255
    if ip in range( 1538965504 , 1538973695 +1): return "Oracle-Investment" # 91.186.192.0 , 91.186.223.255
    if ip in range( 3167846400 , 3167862783 +1): return "Pardazesh-Pishrafteh-Rasaneie" # 188.209.128.0 , 188.209.191.255
    if ip in range( 3170697216 , 3170729983 +1): return "Pardazesh-Pishrafteh-Rasaneie" # 188.253.0.0 , 188.253.127.255
    if ip in range( 3563032576 , 3563036671 +1): return "Pardazesh-Pishrafteh-Rasaneie" # 212.95.144.0 , 212.95.159.255
    if ip in range( 788094976 , 788103167 +1): return "Pardazesh-Pishrafteh-Rasaneie" # 46.249.96.0 , 46.249.127.255
    if ip in range( 1383272448 , 1383276543 +1): return "Pardazesh-Pishrafteh-Rasaneie" # 82.115.16.0 , 82.115.31.255
    if ip in range( 3162071040 , 3162079231 +1): return "Pardaz-Gostar-Ertebatat-Berelian" # 188.121.96.0 , 188.121.127.255
    if ip in range( 622854144 , 622862335 +1): return "Pardaz-Gostar-Ertebatat-Berelian" # 37.32.0.0 , 37.32.31.255
    if ip in range( 1583722496 , 1583726591 +1): return "Pardaz-Gostar-Ertebatat-Berelian" # 94.101.176.0 , 94.101.191.255
    if ip in range( 1841889280 , 1841897471 +1): return "Pardis-Ettela-Resaan-Sepehr" # 109.201.0.0 , 109.201.31.255
    if ip in range( 1360916480 , 1360920575 +1): return "Pardis-Ettela-Resaan-Sepehr" # 81.29.240.0 , 81.29.255.255
    if ip in range( 97009664 , 97017855 +1): return "ParsFonounOfogh" # 5.200.64.0 , 5.200.95.255
    if ip in range( 3170172928 , 3170238463 +1): return "ParsOnline" # 188.245.0.0 , 188.245.255.255
    if ip in range( 3587776512 , 3587784703 +1): return "ParsOnline" # 213.217.32.0 , 213.217.63.255
    if ip in range( 622526464 , 622591999 +1): return "ParsOnline" # 37.27.0.0 , 37.27.255.255
    if ip in range( 774488064 , 774504447 +1): return "ParsOnline" # 46.41.192.0 , 46.41.255.255
    if ip in range( 775847936 , 775880703 +1): return "ParsOnline" # 46.62.128.0 , 46.62.255.255
    if ip in range( 88997888 , 89063423 +1): return "ParsOnline" # 5.78.0.0 , 5.78.255.255
    if ip in range( 1382268928 , 1382285311 +1): return "ParsOnline" # 82.99.192.0 , 82.99.255.255
    if ip in range( 1533149184 , 1533280255 +1): return "ParsOnline" # 91.98.0.0 , 91.99.255.255
    if ip in range( 3651858432 , 3651862527 +1): return "Petiak-System" # 217.170.240.0 , 217.170.255.255
    if ip in range( 774135808 , 774143999 +1): return "PiroozLeen" # 46.36.96.0 , 46.36.127.255
    if ip in range( 1307418624 , 1307426815 +1): return "Pishgaman-Kavir-Yazd" # 77.237.160.0 , 77.237.191.255
    if ip in range( 1426669568 , 1426685951 +1): return "Pishgaman-Kavir-Yazd" # 85.9.64.0 , 85.9.127.255
    if ip in range( 1836941312 , 1836949503 +1): return "Pishgaman-Tejarat-Sayar" # 109.125.128.0 , 109.125.159.255
    if ip in range( 97124352 , 97189887 +1): return "PishgamanToseehErtebatat" # 5.202.0.0 , 5.202.255.255
    if ip in range( 1836949504 , 1836957695 +1): return "Pishgaman-Toseeh-Ertebatat" # 109.125.160.0 , 109.125.191.255
    if ip in range( 630759424 , 630767615 +1): return "RahanetZanjan" # 37.152.160.0 , 37.152.191.255
    if ip in range( 773849088 , 773857279 +1): return "RasanehAvabarid" # 46.32.0.0 , 46.32.31.255
    if ip in range( 2996633600 , 2996649983 +1): return "RasanehEsfahanNet" # 178.157.0.0 , 178.157.63.255
    if ip in range( 3560103936 , 3560112127 +1): return "Rasaneh-Esfahan-Net" # 212.50.224.0 , 212.50.255.255
    if ip in range( 788013056 , 788021247 +1): return "Rased-Maral-Ava-Jonoob" # 46.248.32.0 , 46.248.63.255
    if ip in range( 1833623552 , 1833627647 +1): return "Rased-Maral-Ava-Jonoob" # 109.74.224.0 , 109.74.239.255
    if ip in range( 786432000 , 786563071 +1): return "Rayaneh-Danesh-Golestan" # 46.224.0.0 , 46.225.255.255
    if ip in range( 97026048 , 97058815 +1): return "Rayaneh-Danesh-Golestan" # 5.200.128.0 , 5.200.255.255
    if ip in range( 1296908288 , 1296924671 +1): return "Rayaneh-Danesh-Golestan" # 77.77.64.0 , 77.77.127.255
    if ip in range( 1533837312 , 1533845503 +1): return "Rayaneh-Gostar-Farzanegan-Ahwaz" # 91.108.128.0 , 91.108.159.255
    if ip in range( 1307959296 , 1307963391 +1): return "Research-Institute-Petroleum" # 77.245.224.0 , 77.245.239.255
    if ip in range( 1298677760 , 1298694143 +1): return "Respina" # 77.104.64.0 , 77.104.127.255
    if ip in range( 1307394048 , 1307402239 +1): return "Respina" # 77.237.64.0 , 77.237.95.255
    if ip in range( 785448960 , 785514495 +1): return "Respina" # 46.209.0.0 , 46.209.255.255
    if ip in range( 94371840 , 94437375 +1): return "Respina" # 5.160.0.0 , 5.160.255.255
    if ip in range( 1559412736 , 1559420927 +1): return "Respina" # 92.242.192.0 , 92.242.223.255
    if ip in range( 3167784960 , 3167789055 +1): return "Rightel" # 188.208.144.0 , 188.208.159.255
    if ip in range( 3167789056 , 3167797247 +1): return "Rightel" # 188.208.160.0 , 188.208.191.255
    if ip in range( 3167805440 , 3167813631 +1): return "Rightel" # 188.208.224.0 , 188.208.255.255
    if ip in range( 3167764480 , 3167772671 +1): return "Rightel" # 188.208.64.0 , 188.208.95.255
    if ip in range( 3586334720 , 3586338815 +1): return "Rightel" # 213.195.32.0 , 213.195.47.255
    if ip in range( 629735424 , 629800959 +1): return "Rightel" # 37.137.0.0 , 37.137.255.255
    if ip in range( 630829056 , 630833151 +1): return "Rightel" # 37.153.176.0 , 37.153.191.255
    if ip in range( 630992896 , 630996991 +1): return "Rightel" # 37.156.48.0 , 37.156.63.255
    if ip in range( 97017856 , 97026047 +1): return "Rightel" # 5.200.96.0 , 5.200.127.255
    if ip in range( 1297203200 , 1297211391 +1): return "Rightel" # 77.81.192.0 , 77.81.223.255
    if ip in range( 1495269376 , 1495277567 +1): return "Rightel" # 89.32.0.0 , 89.32.31.255
    if ip in range( 1495293952 , 1495298047 +1): return "Rightel" # 89.32.96.0 , 89.32.111.255
    if ip in range( 1495433216 , 1495441407 +1): return "Rightel" # 89.34.128.0 , 89.34.159.255
    if ip in range( 1495408640 , 1495416831 +1): return "Rightel" # 89.34.32.0 , 89.34.63.255
    if ip in range( 1495908352 , 1495916543 +1): return "Rightel" # 89.41.192.0 , 89.41.223.255
    if ip in range( 1496285184 , 1496293375 +1): return "Rightel" # 89.47.128.0 , 89.47.159.255
    if ip in range( 1496268800 , 1496272895 +1): return "Rightel" # 89.47.64.0 , 89.47.79.255
    if ip in range( 1567756288 , 1567760383 +1): return "Rightel" # 93.114.16.0 , 93.114.31.255
    if ip in range( 92700672 , 92717055 +1): return "Rightel" # 5.134.128.0 , 5.134.191.255
    if ip in range( 629207040 , 629211135 +1): return "SABZ-KHAZAR" # 37.128.240.0 , 37.128.255.255
    if ip in range( 773148672 , 773152767 +1): return "SABZ-KHAZAR" # 46.21.80.0 , 46.21.95.255
    if ip in range( 1835868160 , 1835876351 +1): return "SABZ-KHAZAR" # 109.109.32.0 , 109.109.63.255
    if ip in range( 2668912640 , 2668916735 +1): return "SABZ-KHAZAR" # 159.20.96.0 , 159.20.111.255
    if ip in range( 2953592832 , 2953596927 +1): return "SABZ-KHAZAR" # 176.12.64.0 , 176.12.79.255
    if ip in range( 2967277568 , 2967281663 +1): return "SABZ-KHAZAR" # 176.221.16.0 , 176.221.31.255
    if ip in range( 1502642176 , 1502658559 +1): return "SABZ-KHAZAR" # 89.144.128.0 , 89.144.191.255
    if ip in range( 86163456 , 86171647 +1): return "Samaneh-Sama-Pishro" # 5.34.192.0 , 5.34.223.255
    if ip in range( 1434812416 , 1434845183 +1): return "Sepanta-Communication" # 85.133.128.0 , 85.133.255.255
    if ip in range( 774021120 , 774029311 +1): return "Sepehr-Ava" # 46.34.160.0 , 46.34.191.255
    if ip in range( 2151784448 , 2151788543 +1): return "Shabakeh-Gostar-Dorna" # 128.65.160.0 , 128.65.175.255
    if ip in range( 3168157696 , 3168161791 +1): return "Shabakeh" # 188.214.64.0 , 188.214.79.255
    if ip in range( 1835966464 , 1835974655 +1): return "Shabdiz-Telecom" # 109.110.160.0 , 109.110.191.255
    if ip in range( 1599209472 , 1599225855 +1): return "Shahrad-Net" # 95.82.0.0 , 95.82.63.255
    if ip in range( 1446576128 , 1446608895 +1): return "Shahrad" # 86.57.0.0 , 86.57.127.255
    if ip in range( 1546780672 , 1546797055 +1): return "Shahrad" # 92.50.0.0 , 92.50.63.255
    if ip in range( 622022656 , 622026751 +1): return "Shahriyar" # 37.19.80.0 , 37.19.95.255
    if ip in range( 636162048 , 636166143 +1): return "Shahriyar" # 37.235.16.0 , 37.235.31.255
    if ip in range( 3588857856 , 3588866047 +1): return "Sharif-University" # 213.233.160.0 , 213.233.191.255
    if ip in range( 520568832 , 520577023 +1): return "Sharif-University" # 31.7.64.0 , 31.7.95.255
    if ip in range( 1361027072 , 1361031167 +1): return "Sharif-University" # 81.31.160.0 , 81.31.175.255
    if ip in range( 2997714944 , 2997747711 +1): return "Shiraz-Hamyar" # 178.173.128.0 , 178.173.255.255
    if ip in range( 1054629888 , 1054638079 +1): return "Soroush-Rasanheh" # 62.220.96.0 , 62.220.127.255
    if ip in range( 1359740928 , 1359773695 +1): return "Soroush-Rasanheh" # 81.12.0.0 , 81.12.127.255
    if ip in range( 1466630144 , 1466695679 +1): return "Soroush-Rasanheh" # 87.107.0.0 , 87.107.255.255
    if ip in range( 3163062272 , 3163095039 +1): return "Ariana-Gostar-Spadana" # 188.136.128.0 , 188.136.255.255
    if ip in range( 522002432 , 522010623 +1): return "Ariana-Gostar-Spadana" # 31.29.32.0 , 31.29.63.255
    if ip in range( 633290752 , 633298943 +1): return "Ariana-Gostar-Spadana" # 37.191.64.0 , 37.191.95.255
    if ip in range( 1358610432 , 1358614527 +1): return "Tapash-Rayane-Ahvaz" # 80.250.192.0 , 80.250.207.255
    if ip in range( 3269525504 , 3269591039 +1): return "Theoretical-Physics" # 194.225.0.0 , 194.225.255.255
    if ip in range( 1589116928 , 1589149695 +1): return "Theoretical-Physics" # 94.184.0.0 , 94.184.127.255
    if ip in range( 1589149696 , 1589182463 +1): return "Theoretical-Physics" # 94.184.128.0 , 94.184.255.255
    if ip in range( 3002044416 , 3002048511 +1): return "Toloe-Rayaneh-Loghman" # 178.239.144.0 , 178.239.159.255
    if ip in range( 3001819136 , 3001823231 +1): return "Toos-Ashena" # 178.236.32.0 , 178.236.47.255
    if ip in range( 3583213568 , 3583221759 +1): return "Tosee-Resan-Pasargad" # 213.147.128.0 , 213.147.159.255
    if ip in range( 1346760704 , 1346764799 +1): return "Tosee-Resan-Pasargad" # 80.69.240.0 , 80.69.255.255
    if ip in range( 1547612160 , 1547616255 +1): return "Tosee-Resan-Pasargad" # 92.62.176.0 , 92.62.191.255
    if ip in range( 3159048192 , 3159064575 +1): return "Toseh-Ertebatat-Homa" # 188.75.64.0 , 188.75.127.255
    if ip in range( 1315860480 , 1315864575 +1): return "TSTonline" # 78.110.112.0 , 78.110.127.255
    if ip in range( 3162079232 , 3162087423 +1): return "TSTonline" # 188.121.128.0 , 188.121.159.255
    if ip in range( 1439039488 , 1439055871 +1): return "TSTonline" # 85.198.0.0 , 85.198.63.255
    if ip in range( 3161866240 , 3161882623 +1): return "University-Tehran" # 188.118.64.0 , 188.118.127.255
    if ip in range( 1346547712 , 1346551807 +1): return "University-Tehran" # 80.66.176.0 , 80.66.191.255
    return "OTHERS" #

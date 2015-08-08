
# Module for sh commands
import os

# USB Vendor ID
Acer = '0502'
Asus = '0b05'
Dell = '413c'
Foxconn = '0489'
Fujitsu = '04c5'
Garmin_Asus = '091e'
Google = '18d1'
Haier = '201E'
Hisense = '109b'
HTC = '0bb4'
Huawei = '12d1'
K_Touch = '24e3'
KT_Tech = '2116'
Kyocera = '0482'
Lenovo = '17ef'
LG = '1004'
Motorola = '22b8'
MTK = '0e8d'
NEC = '0409'
Nook = '2080'
Nvidia = '0955'
OTGV = '2257'
Pantech = '10a9'
Pegatron = '1d4d'
Philips = '0471'
PMC_Sierra = '04da'
Qualcomm = '05c6'
SK_Telesys = '1f53'
Samsung = '04e8'
Sharp = '04dd'
Sony = '054c'
Sony_Ericsson = '0fce'
Teleepoch = '2340'
Toshiba = '0930'
ZTE = '19d2'

vendor = raw_input("Insert the name: ")

#################################################################################################
if (vendor == "Acer" or vendor == "acer"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Acer)

#################################################################################################

elif (vendor == "Asus" or vendor == "asus"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Asus)

#################################################################################################

elif (vendor == "Dell" or vendor == "dell"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Dell)

#################################################################################################

elif (vendor == "Foxconn" or vendor == "foxconn"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Foxconn)

#################################################################################################

elif (vendor == "Fujitsu" or vendor == "fujitsu"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Fujitsu)

#################################################################################################

elif (vendor == "Garmin-Asus" or vendor == "garmin-asus"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Garmin_Asus)

#################################################################################################

elif (vendor == "Google" or vendor == "google"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Google)

#################################################################################################

elif (vendor == "Haier" or vendor == "haier"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Haier)

#################################################################################################

elif (vendor == "Hisense" or vendor == "hisense"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Hisense)

#################################################################################################

elif (vendor == "HTC" or vendor == "htc"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (HTC)

#################################################################################################

elif (vendor == "Huawei" or vendor == "huawei"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Huawei)

#################################################################################################

elif (vendor == "K-Touch" or vendor == "k-touch"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (K_Touch)

#################################################################################################

elif (vendor == "KT Tech" or vendor == "kt tech"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (KT_Tech)

#################################################################################################

elif (vendor == "Kyocera" or vendor == "kyocera"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Kyocera)

#################################################################################################

elif (vendor == "Lenovo" or vendor == "lenovo"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Lenovo)

#################################################################################################

elif (vendor == "LG" or vendor == "lg"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (LG)

#################################################################################################

elif (vendor == "Motorola" or vendor == "motorola"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Motorola)

#################################################################################################

elif (vendor == "MTK" or vendor == "mtk"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (MTK)

#################################################################################################

elif (vendor == "NEC" or vendor == "nec"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (NEC)

#################################################################################################

elif (vendor == "Nook" or vendor == "nook"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Nook)

#################################################################################################

elif (vendor == "Nvidia" or vendor == "nvidia"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Nvidia)

#################################################################################################

elif (vendor == "OTGV" or vendor == "otgv"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (OTGV)

#################################################################################################

elif (vendor == "Pantech" or vendor == "pantech"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Pantech)

#################################################################################################

elif (vendor == "Pegatron" or vendor == "pegatron"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Pegatron)

#################################################################################################

elif (vendor == "Philips" or vendor == "philips"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Philips)

#################################################################################################

elif (vendor == "PMC-Sierra" or vendor == "pmc-sierra"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (PMC_Sierra)

#################################################################################################

elif (vendor == "Qualcomm" or vendor == "qualcomm"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Qualcomm)

#################################################################################################

elif (vendor == "SK-Telesys" or vendor == "sk-telesys"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (SK_Telesys)

#################################################################################################

elif (vendor == "Samsung" or vendor == "samsung"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Samsung)

#################################################################################################

elif (vendor == "Sharp" or vendor == "sharp"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Sharp)

#################################################################################################

elif (vendor == "Sony" or vendor == "sony"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Sony)

#################################################################################################

elif (vendor == "Sony-Ericsson" or vendor == "sony-ericsson"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Sony_Ericsson)

#################################################################################################

elif (vendor == "Teleepoch" or vendor == "teleepoch"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Teleepoch)

#################################################################################################

elif (vendor == "Toshiba" or vendor == "toshiba"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (Toshiba)

#################################################################################################

elif (vendor == "ZTE" or vendor == "zte"):

    device = 'SUBSYSTEM=="usb", ATTR{idVendor}=="%s", MODE="0666", GROUP="plugdev"' % (ZTE)

#################################################################################################

# Creating the file in /etc/udev/rules.d/51-android.rules
file = open('/etc/udev/rules.d/51-android.rules', 'w')
file.write(device)
file.close()

# Giving permissions to 51-android.rules file
os.system("chmod a+r /etc/udev/rules.d/51-android.rules")

os.system("echo Script created by Mirko Buttazzo ---> mirko9662@gmail.com")

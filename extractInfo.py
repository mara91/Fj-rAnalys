import xml.etree.ElementTree as ET
import os

os.chdir(r'C:\GISN24\Projekt')
tree = ET.parse('MTD_MSIL1C.xml')
root = tree.getroot()

for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
    print Quality_Indicators_Info.text

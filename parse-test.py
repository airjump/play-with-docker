from lxml import etree
root = etree.parse("fruits.xml").getroot()

for name in root.findall("item/name"):
    etree.dump(name)

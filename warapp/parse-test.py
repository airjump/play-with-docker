from lxml import etree
root = etree.parse("fruits.xml").getroot()

for name in root.findall("item/name"):
    etree.dump(name)

for name in root.findall("item/count"):
    etree.dump(count)

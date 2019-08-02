from lxml import etree
tree = etree.parse("sample.xml")
root = tree.getroot()
print root.find("a").text

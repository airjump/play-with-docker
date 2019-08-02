from lxml import etree
tree = etree.parse("sample.xml")
print etree.tostring(tree)

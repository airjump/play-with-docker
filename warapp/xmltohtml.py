import lxml.html
from lxml import etree
 
xslt_doc = etree.parse("test-xslt.xslt")
xslt_transformer = etree.XSLT(xslt_doc)
 
source_doc = etree.parse("toc-test.xml")
output_doc = xslt_transformer(source_doc)
 
print(str(output_doc))
output_doc.write("output-toc.html", pretty_print=True)

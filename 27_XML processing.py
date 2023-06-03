# XML module in python

# Analyse xml documents in python

# Analizing a sample xml document  

import xml.etree.ElementTree as etree

tree = etree.parse(r"C:\Users\pc\Desktop\test.xml")     # Parse a xml
root = tree.getroot()                                   # Get root element of xml    
print(root)

print(root.tag)                                         # Get root element tag of xml   
print(root.attrib)                                      # Get root element attributes of xml  
print(root.getchildren)                                 # Get child elements tag of root 

for child in root:                                      # Get child elements tag of root by for loop  
    print(child.tag)

print(tree.findall("author"))                           # Search and find specific element in xml document 
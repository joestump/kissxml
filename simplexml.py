try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree  as ET

class XMLTree(object):
    nodes = {}

    def __init__(self, node):
        self.node = node
        for n in node:
            if len(n.getchildren()):
                self.nodes[n.tag] = XMLTree(n)
            else:
                self.nodes[n.tag] = XMLNode(n)

    def __getattr__(self, attr):
        return self.nodes[attr]

    def __getitem__(self, key):
        return self.node.attrib.get(key)

    def __len__(self):
        return len(self.nodes)

class XMLNode(object):
    def __init__(self, node):
        self.node = node

    def __getitem__(self, key):
        return self.node.attrib.get(key)

    def __unicode__(self):
        return self.node.text

    def __repr__(self):
        return self.__unicode__()

def parse(file):
    tree = ET.parse(file)
    return XMLTree(tree.getroot())

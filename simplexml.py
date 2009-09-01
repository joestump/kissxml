try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree  as ET

class XMLTree(object):
    nodes = {}

    def __init__(self, node):
        self.node = node
        for n in node:
            if n.tag in self.nodes:
                if len(self.nodes[n.tag]) == 1:
                    self.nodes[n.tag] = [self.nodes[n.tag]]
            else:
                self.nodes[n.tag] = None

            if len(n.getchildren()):
                wrapper = XMLTree
            else:
                wrapper = XMLNode

            if self.nodes[n.tag] != None and len(self.nodes[n.tag]):
                self.nodes[n.tag].append(wrapper(n))
            else:
                self.nodes[n.tag] = wrapper(n)

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

    def __len__(self):
        return 1

def parse(file):
    tree = ET.parse(file)
    return XMLTree(tree.getroot())

if __name__ == "__main__":
    xml = parse("fixture.xml")
    print xml.name
    print xml.hair["style"] 
    print xml.like

    print len(xml.name)
    print len(xml.like)

    for like in xml.like:
        print "I like %s." % like

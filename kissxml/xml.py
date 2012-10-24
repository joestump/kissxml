class XMLTree(object):
    def __init__(self, node):
        self.nodes = {}
        self.node = node
        for n in node:
            if len(n.getchildren()):
                xmlnode = XMLTree(n)
            else:
                xmlnode = XMLNode(n)
            if n.tag in self.nodes:
                if isinstance(self.nodes[n.tag], (XMLTree, XMLNode)):
                    self.nodes[n.tag] = [self.nodes[n.tag], xmlnode]
                else:
                    self.nodes[n.tag].append(xmlnode)
            else:
                self.nodes[n.tag] = xmlnode

    def __unicode__(self):
        return unicode(dict((k, str(v)) for k, v in self.nodes.iteritems()))

    def __str__(self):
        return unicode(self).encode('utf-8')

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
        return self.node.text or ''

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __repr__(self):
        return self.__unicode__()

    def __len__(self):
        return 1

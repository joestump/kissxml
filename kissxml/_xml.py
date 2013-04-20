try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class FactoryNode(object):
    _classes = {}

    @classmethod
    def create_class(cls, node, parent):
        key = (node, parent)
        if not key in cls._classes:
            cls._classes[key] = type(node.tag, (parent,), {})
        return cls._classes[key]

    @classmethod
    def create_instance(cls, node, parent):
        return cls.create_class(node, parent)(node)


class XMLTree(object):
    def __init__(self, node):
        self.nodes = {}
        self.node = node
        for n in node:
            if len(n.getchildren()):
                xmlnode = FactoryNode.create_instance(n, XMLTree)
            else:
                xmlnode = XMLNode(n)
            if n.tag in self.nodes:
                if isinstance(self.nodes[n.tag], (XMLTree, XMLNode)):
                    self.nodes[n.tag] = [self.nodes[n.tag], xmlnode]
                else:
                    self.nodes[n.tag].append(xmlnode)
            else:
                self.nodes[n.tag] = xmlnode

    def trait_names(self):
        """
        used to work with tabs in ipython and ipdb
        """
        return self.nodes

    def __unicode__(self):
        return unicode(dict((k, str(v)) for k, v in self.nodes.iteritems()))

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __getattr__(self, attr):
        return self.nodes[attr]

    def __getitem__(self, key):
        if (isinstance(key, int)):
            return self.node.attrib.keys()[key]
        return self.node.attrib.get(key)

    def __len__(self):
        return len(self.nodes)

    def __repr__(self):
        return unicode(self.node).encode('utf-8')

    @property
    def tag_name(self):
        return unicode(self.node.tag).encode('utf-8')


class XMLNode(object):
    def __init__(self, node):
        self.node = node

    def __getitem__(self, key):
        if (isinstance(key, int)):
            return self.node.attrib.keys()[key]
        return self.node.attrib.get(key)

    def __unicode__(self):
        return self.node.text or ''

    def __str__(self):
        return unicode(self).encode('utf-8')

    def __int__(self):
        return int(self.node.text)

    def __repr__(self):
        return self.__unicode__()

    def __len__(self):
        return 1

    def __eq__(self, value):
        if isinstance(value, str) or isinstance(value, unicode):
            return unicode(self) == value

        if isinstance(value, int):
            try:
                return value == int(self)
            except (ValueError, TypeError):
                return False

        if isinstance(value, self.__class__):
            return value.node.text == self.node.text

        return False


def parse(file):
    tree = ET.parse(file)
    return XMLTree(tree.getroot())


def parsestring(s):
    return parse(StringIO(s))

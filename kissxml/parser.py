from . import XMLTree

try:
    import cElementTree as ET
except ImportError:
    try:
        import lxml.etree as ET
    except ImportError:
        try:
            import elementtree.ElementTree as ET
        except ImportError:
            import xml.etree.ElementTree as ET  # Python 2.5


try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


def parse_file(file):
    tree = ET.parse(file)
    return XMLTree(tree.getroot())
parse = parse_file

def parse_string(s):
    return parse(StringIO(s))
parsestring = parse_string

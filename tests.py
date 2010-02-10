import unittest
import simplexml

class TestSimpleXML(unittest.TestCase):
    def assertXMLHasProperties(self, xml, properties):
        for propname, value in properties.iteritems():
            if isinstance(value, tuple):
                value, attrs = value
            else:
                value, attrs = value, {}
            actual = getattr(xml, propname)
            if isinstance(actual, simplexml.XMLTree):
                self.assertTrue(isinstance(value, dict), 'Expected dictionary, got %s (value: %s)' % (type(actual), actual))
                self.assertXMLHasProperties(actual, value)
            elif isinstance(actual, list):
                for idx, item in enumerate(actual):
                    self.assertEquals(value[idx], str(item), 'Expected node value "%s", got "%s"' % (value[idx], item))
            else:
                self.assertEquals(value, str(actual), 'Expected node value "%s", got "%s"' % (value, actual))
            for attrname, attrvalue in attrs.iteritems():
                actualattr = getattr(xml, propname)[attrname]
                self.assertEquals(attrvalue, actualattr, 'Expected attribute value "%s", got "%s"' % (attrvalue, actualattr))

    def test_simplexml(self):
        for name, vals in self.get_tests().iteritems():
            self.assertXMLHasProperties(simplexml.parsestring(vals[1]), vals[0])

    def get_tests(self):
        # Dictionary of tests, keyed by test name.
        # Values: (<expected_value>, <xml>)
        #   <expected_value>: dict(<node>=<value>) or dict(<node>=(<value>,<attrs>)).
        return {
            'basic': ({'name': 'Joe Stump', 'hair': ('Brown', {'style': 'buzzed'}), 'like': ['Beer', 'Bikes', 'Computers']}, '<?xml version="1.0"?><test><name>Joe Stump</name><hair style="buzzed">Brown</hair><like>Beer</like><like>Bikes</like><like>Computers</like></test>'),
            'subitem_name_conflict': ({'type': 'Foo', 'properties': {'type': 'properties', 'foo': 'bar'}}, '<?xml version="1.0"?><item><type>Foo</type><properties><type>properties</type><foo>bar</foo></properties></item>')
        }


if __name__ == '__main__':
    unittest.main()

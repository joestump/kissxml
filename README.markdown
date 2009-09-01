# Overview

When I started working in Python I'd heard rumors that parsing XML was kind of a pain in the ass. Coming from PHP I had SimpleXML that worked perfectly fine for 99% of the XML parsing I had to do. When it finally came to needing to parse some simplistic XML documents I decided to write this small wrapper around [ElementTree](http://effbot.org/zone/element-index.htm).

# Usage

    from simplexml import parse
    xml = parse("person.xml")
    print xml.name.first
    print xml.name.last
    print xml.name["origin"]

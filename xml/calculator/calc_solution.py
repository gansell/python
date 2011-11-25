
"""
An XML driven calculator using custom lxml.etree element classes.

Examples::

    >>> try:
    ...   from io import BytesIO
    ... except ImportError:
    ...   from cStringIO import StringIO as BytesIO

    >>> tree = generate_calc_xml()
    >>> print(tree.to_term())
    (1.0 + 2.0 + 1.5 * 2 * (2 + 3.5 * 4))

    >>> xml = etree.tostring(tree)
    >>> calculate(BytesIO(xml))
    51.0

    >>> tree = generate_calc_var_xml()
    >>> print(tree.to_term())
    (1.0 + 2.0 + x + 1.5 * 2 * (2 + x + 3 * 5.0 * y))

    >>> xml = etree.tostring(tree)
    >>> calculate(BytesIO(xml), {'x': 2.0, 'y': 3.0})
    152.0
    >>> calculate(BytesIO(xml), {'x': 3.0, 'y': 2.0})
    111.0
"""

from lxml import etree

# custom element classes

parser = etree.XMLParser()

class add(etree.ElementBase):
    PARSER = parser
    def calculate(self, variables={}):
        value = 0.0
        for operand in self:
            value += operand.calculate(variables)
        return value

    def to_term(self):
        return '(%s)' % ' + '.join(operand.to_term() for operand in self)

class mul(etree.ElementBase):
    PARSER = parser
    def calculate(self, variables={}):
        value = 1.0
        for operand in self:
            value *= operand.calculate(variables)
        return value

    def to_term(self):
        return ' * '.join(operand.to_term() for operand in self)

class num(etree.ElementBase):
    PARSER = parser
    def calculate(self, variables={}):
        return float(self.text)

    def to_term(self):
        return self.text

class var(etree.ElementBase):
    PARSER = parser
    def calculate(self, variables={}):
        return variables[self.text]

    def to_term(self):
        return self.text


# configure parser and class lookup

ns_lookup = etree.ElementNamespaceClassLookup()
# quick way to register all subclasses of ElementBase in this module:
ns_lookup.get_namespace(None).update(vars())

parser.set_element_class_lookup(ns_lookup)


# calculate the result of a document

def calculate(file, variables={}):
    term = etree.parse(file, parser).getroot()
    return term.calculate(variables)


# generate example documents

def generate_calc_xml():
    return add( num('1.0'), num('2.0'),
                mul( num('1.5'), num('2'),
                     add( num('2'),
                          mul( num('3.5'), num('4') ),
                          ),
                     ),
                )

def generate_calc_var_xml():
    return add( num('1.0'), num('2.0'), var('x'),
                mul( num('1.5'), num('2'),
                     add( num('2'), var('x'),
                          mul( num('3'), num('5.0'), var('y') ),
                          ),
                     ),
                )

def gen():
    tree = generate_calc_xml()
    etree.ElementTree(tree).write('calc.xml', pretty_print=True)
    etree.ElementTree(generate_calc_var_xml()).write('calc_var.xml', pretty_print=True)


if __name__ == '__main__':
    gen()

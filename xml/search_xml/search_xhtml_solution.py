
from collections import Counter  # Py2.7+ or Py3.2+
import random
import re

from lxml import etree
from lxml.cssselect import CSSSelector

XHTML_NAMESPACE = "http://www.w3.org/1999/xhtml"
## or use this:
# from lxml.html import XHTML_NAMESPACE

################################################################################
# generic page processing

def parse_xhtml_page(url):
    # DTD defines entity names, e.g. "&amp;"
    parser = etree.XMLParser(load_dtd=True, remove_comments=True, remove_pis=True)
    return etree.parse(url, parser)

def process(tree, find_headings):
    headings = find_headings(tree)

    # count headings
    counts = Counter(heading.tag for heading in headings)
    print(sorted(counts.items()))

    # print headings (in their tag context)
    for heading in headings:
        print(etree.tostring(heading))

    # modify heading text
    for heading in random.sample(headings, min(len(headings), 5)):
        heading.text = 'random change'

    # save locally (and try to find a suitable name based on the finder type)
    tree.write('page_%s.xhtml' % getattr(find_headings, '__name__', type(find_headings).__name__))


################################################################################
# tag search implementations

find_headings_with_css = CSSSelector(
    ','.join('x|h%d,x|H%d' % (i,i) for i in range(1,7)),
    namespaces = {'x': XHTML_NAMESPACE})

find_headings_with_xpath = etree.XPath(
    '|'.join('//x:h%d|//x:H%d' % (i,i) for i in range(1,7)),
    namespaces = {'x': XHTML_NAMESPACE})

find_headings_with_etxpath = etree.ETXPath(
    '|'.join('//{%(ns)s}h%(i)d|//{%(ns)s}H%(i)d' % {'ns': XHTML_NAMESPACE, 'i': i}
             for i in range(1,7)))

def find_headings_with_iter(tree):
    is_heading = re.compile(r'\{%s\}[hH][1-6]$' % XHTML_NAMESPACE).match
    return [ el for el in tree.iter() if is_heading(el.tag) ]


################################################################################
# main program (dynamically looks up search implementations in the module)

if __name__ == '__main__':
    tree = parse_xhtml_page('http://en.wikipedia.org/wiki/XML')
    #tree = parse_xhtml_page('http://www.w3.org/TR/REC-xml/')
    #tree = parse_xhtml_page('http://lxml.de/')

    for name, value in sorted(globals().items()):
        if name.startswith('find_headings_with_') and hasattr(value, '__call__'):
            finder_function = value
            print('Processing tree with %s' % type(finder_function))
            process(tree, finder_function)

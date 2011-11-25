################################################################################
## Solution for "searching XML with XPath" exercise.
##
## Presents different ways to search an XML document using different
## path languages: XPath, ElementPath and CSS selectors.
################################################################################

from lxml import etree, cssselect

def et_ok(f):
    f.ET_OK = True
    return f

################################################################################
# XPath

def xpath_iter_city_names(tree):
    for el in tree.xpath('//city'):
        yield el.text

def xpath_iter_city_names_alt2(tree):
    for name in tree.xpath('//city/text()'):
        yield name

_cxpath_city_names = etree.XPath('//city')
def cxpath_iter_city_names(tree):
    for el in _cxpath_city_names(tree):
        yield el.text

_cxpath_city_names_alt2 = etree.XPath('//city/text()')
def cxpath_iter_city_names_alt2(tree):
    for name in _cxpath_city_names_alt2(tree):
        yield name


################################################################################
# ElementPath

@et_ok
def findall_iter_city_names(tree):
    for el in tree.findall('//city'):
        yield el.text

@et_ok
def iterfind_iter_city_names(tree):
    for el in tree.iterfind('//city'):
        yield el.text


################################################################################
# CSSSelect

_cssselect_city_names = cssselect.CSSSelector('city')
def cssselect_iter_city_names(tree):
    for el in _cssselect_city_names(tree):
        yield el.text


################################################################################
# different ways to traverse an XML tree

@et_ok
def iter_city_names_navigate(tree):
    for entry in tree.getroot():
        for el in entry:
            if el.tag == 'city':
                yield el.text

@et_ok
def iter_city_names_recursive(tree):
    def iter_names(el):
        if el.tag == 'city':
            yield el.text
        for child in el:
            for name in iter_names(child):
                yield name

    for name in iter_names(tree.getroot()):
        yield name

@et_ok
def iter_city_names_etiter(tree):
    for el in tree.iter('city'):
        yield el.text


################################################################################
# main program

if __name__ == '__main__':
    # find all defined names in this module that contain an 'iter_'
    # and point to callable things
    functions = []
    for name, value in globals().items():
        if 'iter_' in name and hasattr(value, '__call__'):
            functions.append(value)

    import timeit

    def run_benchmark(function, tree):
        def bench(func=function, repeat=100):
            for i in range(repeat):
                list(func(tree))
        return min(timeit.repeat(bench, number=10, repeat=3))

    # run lxml benchmarks
    print('Using lxml ...')
    tree = etree.parse('../cityindex.xml')

    for func in functions:
        print('%s: %.3f ms' % (func.__name__, run_benchmark(func, tree)))

    # run ET benchmarks
    import xml.etree.ElementTree as ET
    print('Using ElementTree ...')
    tree = ET.parse('../cityindex.xml')

    for func in functions:
        if not getattr(func, 'ET_OK', False):
            continue
        print('%s: %.3f ms' % (func.__name__, run_benchmark(func, tree)))

    # run cET benchmarks
    import xml.etree.cElementTree as ET
    print('Using cElementTree ...')
    tree = ET.parse('../cityindex.xml')

    for func in functions:
        if not getattr(func, 'ET_OK', False):
            continue
        print('%s: %.3f ms' % (func.__name__, run_benchmark(func, tree)))

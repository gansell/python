################################################################################
## Solution for "searching XML" exercise.
##
## Presents different ways to traverse an XML document, using either
## the plain ElementTree API or lxml specific parsing and serialising.
################################################################################


################################################################################
# parsing and serialising with lxml.etree and ElementTree

def in_and_out_with_lxml(file='cityindex.xml'):
    from lxml import etree

    # remove newlines and other non-content to save space
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file, parser)

    # serialise, just to see the result
    tree.write('lxml_result.xml')
    tree.write('lxml_result_utf8.xml', encoding='utf8')
    tree.write('lxml_result_pp.xml', pretty_print=True)
    tree.write('lxml_result_c14n.xml', method='c14n')

    return tree


def in_and_out_with_et(file='cityindex.xml'):
    import xml.etree.ElementTree as ET
    tree = ET.parse(file)

    # serialise, just to see the result
    tree.write('ET_result.xml')
    tree.write('ET_result_utf8.xml', encoding='utf8')

    return tree


################################################################################
# different ways to traverse an XML tree

def iter_city_names_navigate(tree):
    for entry in tree.getroot():
        for el in entry:
            if el.tag == 'city':
                yield el.text

def iter_city_names_recursive(tree):
    def iter_names(el):
        if el.tag == 'city':
            yield el.text
        for child in el:
            for name in iter_names(child):
                yield name

    for name in iter_names(tree.getroot()):
        yield name

def iter_city_names_etiter(tree):
    for el in tree.iter('city'):
        yield el.text


################################################################################
# main program

if __name__ == '__main__':
    print('Using lxml ...')
    tree = in_and_out_with_lxml('../cityindex.xml')

    print('Tree navigation:')
    print(', '.join(iter_city_names_navigate(tree)))

    print('Recursion:')
    print(', '.join(iter_city_names_recursive(tree)))

    print('iter():')
    print(', '.join(iter_city_names_etiter(tree)))

    print('Using ElementTree ...')
    tree = in_and_out_with_et('../cityindex.xml')

    print('Tree navigation:')
    print(', '.join(iter_city_names_navigate(tree)))

    print('Recursion:')
    print(', '.join(iter_city_names_recursive(tree)))

    print('iter():')
    print(', '.join(iter_city_names_etiter(tree)))

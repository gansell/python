
import xml.etree.cElementTree as cET
import xml.etree.ElementTree as ET
import lxml.etree as etree


def build_factory(elem, ET=cET):
    def generate_elem(append, elem, level):
        var = "e" + str(level)
        arg = repr(elem.tag)
        if elem.attrib:
            arg += ", **%r" % elem.attrib
        if level == 1:
            append(" e1 = Element(%s)" % arg)
        else:
            append(" %s = SubElement(e%d, %s)" % (
                                   var, level-1, arg))
        if elem.text:
            append(" %s.text = %r" % (var, elem.text))
        if elem.tail:
            append(" %s.tail = %r" % (var, elem.tail))
        for e in elem:
            generate_elem(append, e, level+1)

    # generate code for a function that creates a tree
    output = ["def element_factory():"]
    generate_elem(output.append, elem, 1)
    output.append(" return e1")
    code = "\n".join(output)

    # create function object
    namespace = {
        "Element"    : ET.Element,
        "SubElement" : ET.SubElement
        }
    exec code in namespace
    return namespace["element_factory"]


##################
# benchmark code

from copy import deepcopy

template_xml = '''\
<eintrag>
  <stadt />
  <land />
</eintrag>
'''

template_ET    =    ET.fromstring(template_xml)
template_cET   =   cET.fromstring(template_xml)
template_etree = etree.fromstring(template_xml)

def factory_ET(template=template_ET):
    return build_factory(template, ET)

def factory_cET(template=template_cET):
    return build_factory(template, cET)

def factory_etree(template=template_etree):
    return build_factory(template, etree)


def parse_template_ET(template=template_xml):
    return ET.fromstring(template)

def parse_template_cET(template=template_xml):
    return cET.fromstring(template)

def parse_template_etree(template=template_xml):
    return etree.fromstring(template)


def deepcopy_ET(template=template_ET):
    return deepcopy(template)

def deepcopy_cET(template=template_cET):
    return deepcopy(template)

def deepcopy_etree(template=template_etree):
    return deepcopy(template)


def make_efactory(ET):
    if ET is etree:
        # lxml.etree
        import lxml.builder
        return lxml.builder.E
        # lxml.objectify
        import lxml.objectify as builder
        return builder.ElementMaker(annotate=False)
    else:
        import builder
        return builder.ElementMaker(ET=ET)

def efactory_plain(E, count):
    eintrag, stadt, land = E.eintrag, E.stadt, E.land
    root = E.root(
        *[ eintrag( stadt,
                    land )
           for _ in xrange(count) ]
        )
    return root

def efactory_text(E, count):
    eintrag, stadt, land = E.eintrag, E.stadt, E.land
    root = E.root(
        *[ eintrag( stadt('abcdefg'),
                    land('abcdefg') )
           for _ in xrange(count) ]
        )
    return root

def efactory_attributes(E, count):
    eintrag, stadt, land = E.eintrag, E.stadt, E.land
    root = E.root(
        *[ eintrag( stadt(test='toast', toast='test'),
                    land(test='toast', toast='test') )
           for _ in xrange(count) ]
        )
    return root

def efactory_text_attributes(E, count):
    eintrag, stadt, land = E.eintrag, E.stadt, E.land
    root = E.root(
        *[ eintrag( stadt('abcdefg', test='toast', toast='test'),
                    land('abcdefg', test='toast', toast='test') )
           for _ in xrange(count) ]
        )
    return root


def benchmark(with_text=False, with_attributes=False):
    from timeit import repeat

    max_count = 4000

    template_root = cET.fromstring(template_xml)
    if with_text:
        for el in template_root[:]:
            el.text = 'abcdefg'
    if with_attributes:
        for el in template_root[:]:
            el.set('test', 'toast')
            el.set('toast', 'test')

    def _deepcopy():
        return deepcopy(element)

    def _parse():
        return et_lib.fromstring(xml)

    if with_text:
        if with_attributes:
            def _efactory():
                return efactory_text_attributes(efactory, i)
        else:
            def _efactory():
                return efactory_text(efactory, i)
    elif with_attributes:
        def _efactory():
            return efactory_attributes(efactory, i)
    else:
        def _efactory():
            return efactory_plain(efactory, i)

    i = 1
    while True:
        root = cET.Element('root')
        root[:] = [ template_root ] * i
        count = len(list(root.getiterator()))
        if count > max_count:
            break
        print('%02d) XML size: %d' % (i, count))

        xml = cET.tostring(root)
        root = None

        i *= 2

        timings = []
        for et_lib, repeat_count in zip([ET,cET,etree], [3,4,4]):
            print("Timings for %s" % et_lib.__name__)

            element = et_lib.fromstring(xml)
            factory = build_factory(element, et_lib)
            efactory = make_efactory(et_lib)

            if i > 1000:
                repeat_count = int((repeat_count+1) / 2)

            times = tuple(
                min(repeat(func, repeat=repeat_count, number=1000))
                for func in (_deepcopy, _parse, factory, _efactory)
                )

            print(('%.1f '*len(times)) % times)
            timings.append(times)

        formatted = '%8d  %s' % (count, '  '.join(
            ' '.join('%6.3f' % t for t in times) for times in timings))

        print(formatted)

        with open('bench.txt', 'a') as f:
            f.write('\t'.join(formatted.split()))
            f.write('\n')

if __name__ == '__main__':
    print("Timings without text and without attributes:")
    benchmark(with_text=False, with_attributes=False)
    print("Timings with text and attributes:")
    benchmark(with_text=True, with_attributes=True)

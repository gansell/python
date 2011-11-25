# $Id$
# The E elementtree builder.
#
# Fredrik Lundh, November 2006.
#

# based on:
#   http://effbot.org/zone/element-lib.htm#append
#   http://www.tothink.com/python/ElementBuilder/

try:
    import xml.etree.cElementTree as ET
except ImportError:
    try:
        import cElementTree as ET
    except ImportError:
        import elementtree.ElementTree as ET

try:
    from functools import partial
except ImportError:
    # fake it for pre-2.5 releases
    def partial(func, tag):
        return lambda *args, **kwargs: func(tag, *args, **kwargs)

try:
    basestring
except:
    basestring = str, unicode

class _C:
    pass

class ElementMaker(object):

    def __init__(self, typemap=None, ET=ET):
        self.ET = ET

	# initialize type map for this element factory

	if typemap:
	    typemap = typemap.copy()
	else:
	    typemap = {}
	
	def add_text(elem, item):
	    if len(elem):
		elem[-1].tail = (elem[-1].tail or "") + item
	    else:
		elem.text = (elem.text or "") + item
	typemap[str] = typemap[unicode] = add_text

	def add_dict(elem, item):
	    attrib = elem.attrib
	    for k, v in item.items():
		if isinstance(v, basestring):
		    attrib[k] = v
		else:
		    attrib[k] = typemap[type(v)](None, v)
	typemap[dict] = add_dict

	def add_elem(elem, item):
	    elem.append(item)
	t = type(ET.Element("tag"))
	if t is not type(_C()):
	    typemap[t] = add_elem

	self._typemap = typemap

	# print typemap

    def __call__(self, tag, *children, **attrib):
        ET = self.ET

	get = self._typemap.get

        elem = ET.Element(tag)
	if attrib:
	    get(dict)(elem, attrib)

        for item in children:
            if callable(item):
                item = item()
	    t = get(type(item))
	    if t is None:
		if ET.iselement(item):
		    elem.append(item)
		    continue
		raise TypeError("bad argument type: %r" % item)
	    else:
		v = t(elem, item)
		if v:
		    get(type(v))(elem, v)

        return elem

    def __getattr__(self, tag):
        return partial(self, tag)

# create factory object
E = ElementMaker()

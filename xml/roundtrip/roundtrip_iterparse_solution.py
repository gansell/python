
from copy import deepcopy
from lxml import etree


def build_region_index(url='../cityindex.xml', etree=etree):
    regions = {}
    for _,entry in etree.iterparse(url, tag='entry'):
        regions[(entry.findtext('city'), entry.findtext('country'))] = entry.findtext('region')
        entry.clear()
    return regions


def parse_with_region(person_list_file='../personlist.xml', etree=etree):
    """
    Augment document while parsing.
    """
    region_element = etree.Element('region')

    region_index = build_region_index(etree=etree)

    context = etree.iterparse(person_list_file, tag='person')
    for _, person in context:
        # find city and country of each person
        city = person.findtext('address/city')
        country = person.findtext('address/country')
        if not city or not country:
            continue

        # insert region tag
        region_element.text = region_index.get((city,country))
        city_el = person.find('address/city')
        city_el.addnext(deepcopy(region_element))

    # return parsed root element
    return context.root


def augment_with_region(in_file='../personlist.xml', out_file='personlist_with_region_iterparse.xml', etree=etree):
    """
    Try to minimise memory overhead by serialising as the data comes in.
    """
    region_element = etree.Element('region')

    region_index = build_region_index(etree=etree)

    context = etree.iterparse(in_file, tag='person')

    with open(out_file, 'w') as out:
        out.write('<personlist>\n')

        for _, person in context:
            # find city and country of each person
            city = person.findtext('address/city')
            country = person.findtext('address/country')
            if not city or not country:
                continue

            # insert region tag
            region_element.text = region_index.get((city,country))
            city_el = person.find('address/city')
            city_el.addnext(deepcopy(region_element))

            # serialise into target file
            out.write(etree.tostring(person))

            # clear processed content
            person.clear()

        out.write('\n</personlist>')


if __name__ == '__main__':
    # iterparse in to memory
    person_list_root = parse_with_region()
    etree.ElementTree(person_list_root).write('personlist_with_region.xml', encoding='utf-8')

    # iterparse back into file
    augment_with_region()

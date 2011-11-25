
from copy import deepcopy
from lxml import etree

def parse_person_list(url='../personlist.xml'):
    return etree.parse(url)

def parse_city_index(url='../cityindex.xml'):
    return etree.parse(url)


def insert_region(tree):
    person_list = tree.getroot()
    if person_list.tag != 'personlist':
        raise ValueError("unexpected XML format: expected personlist, found '%s'" % person_list.tag)

    city_list = parse_city_index().getroot()
    empty_region = person_list.makeelement('region')

    for person in person_list:
        # find city and country of each person
        city = person.findtext('address/city')
        country = person.findtext('address/country')
        if not city or not country:
            continue

        # find a corresponding region
        region = None
        for el in city_list:
            if el.findtext('city') == city and el.findtext('country') == country:
                region = el.find('region')
                if region is not None:
                    break

        # insert region tag
        if region is None:
            region = empty_region
        city_el = person.find('address/city')
        city_el.addnext(deepcopy(region))


if __name__ == '__main__':
    person_list = parse_person_list()
    insert_region(person_list)
    person_list.write('personlist_with_region.xml', encoding='utf-8')

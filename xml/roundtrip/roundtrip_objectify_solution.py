
from copy import deepcopy
from lxml import etree, objectify


def parse_with_region(person_list_file='../personlist.xml', city_index_file='../cityindex.xml'):
    """
    Augment document while parsing.
    """
    tree = objectify.parse(person_list_file)
    city_index = objectify.parse(city_index_file).getroot().entry

    person_list = tree.getroot()
    region_element = person_list.makeelement('region')

    for person in person_list.person:
        # find city and country of each person
        city = person.address.city
        country = person.address.country

        region = region_element
        for entry in city_index:
            if entry.city == city and entry.country == country:
                region = entry.region
                break

        # insert region tag after city tag
        city.addnext(deepcopy(region))

        # change birth date to April 1st if born in December
        if person.birthday.month == 'December':
            birthday = person.birthday
            birthday.day = 1
            birthday.month = 'April'
            birthday.month.set('number', '4')

    # return processed tree
    objectify.deannotate(tree)
    etree.cleanup_namespaces(tree)
    return tree


if __name__ == '__main__':
    tree = parse_with_region()
    tree.write('personlist_with_region_objectify.xml',
               encoding='utf-8', pretty_print=True)

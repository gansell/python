# coding: utf8
from __future__ import unicode_literals

import itertools

from lxml import etree
from lxml import objectify

firstnames = (
    'Hubert', 'Johannes', 'Sven', 'Georg', 'Peter',
    )
lastnames = (
    'Hottentott', 'Berger', 'Hohensiel', 'Gravenkamp', 'Anderson',
    )
titles = itertools.cycle([
    '', 'Dr.', 'Dr.Ing.', '', 'Prof.', '', 'Prof. Dr.', '', '', '',
    ])
streets = (
    'Ringstr.', 'Mutzenbacherplatz', 'Habichtgasse', 'Ablatusweg',
    )
zip_city_countries = (
    ('1190', 'Wien', 'Österreich', 'A'),
    ('81537', 'München', 'Deutschland', 'D'),
    ('20095', 'Hamburg', 'Deutschland', 'D'),
    ('49074', 'Osnabrück', 'Deutschland', 'D'),
    ('8004', 'Zürich', 'Schweiz', 'CH'),
    )
months = (
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
    )
birthdays = (
    itertools.cycle(range(1, 28, 3)),
    itertools.cycle(range(1, 12)),
    itertools.cycle(range(1956, 2007, 3)),
    )

def gen_people():
    person_id = 1
    people = objectify.Element('personlist')
    for zipcode, city, country, prefix in zip_city_countries:
        for street in streets:
            for lastname in lastnames:
                for firstname in firstnames:
                    title = next(titles)
                    day, month, year = map(next, birthdays)
                    person = objectify.SubElement(people, 'person', id='p%d' % person_id)
                    person_id += 1

                    person.firstname = firstname
                    person.lastname = lastname
                    person.title = title

                    address = objectify.SubElement(person, 'address')
                    address.street = street
                    address.zip = zipcode
                    address.city = city
                    address.country = country
                    address.country.set('zip-prefix', prefix)

                    birthday = objectify.SubElement(person, 'birthday')
                    birthday.day = day
                    birthday.month = months[month]
                    birthday.month.set('number', str(month))
                    birthday.year = year

    return people

def main():
    people = gen_people()
    objectify.deannotate(people)
    etree.cleanup_namespaces(people)
    etree.ElementTree(people).write('personlist.xml', encoding='utf8', pretty_print=True)

if __name__ == '__main__':
    main()

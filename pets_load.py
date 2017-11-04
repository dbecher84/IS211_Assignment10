#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""load the pet database"""

import sqlite3


PERSON = ((1, 'James', 'Smith', 41),
          (2, 'Diana', 'Greene', 23),
          (3, 'Sara', 'White', 27),
          (4, 'William', 'Gibson', 23))

PETS = ((1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1))

PERSON_PET = ((1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6))


CONN = sqlite3.connect('pets.db')
C = CONN.cursor()

for item in PERSON:
    C.execute('INSERT INTO person VALUES (?,?,?,?)', item)

for item in PETS:
    C.execute('INSERT INTO pet VALUES (?,?,?,?,?)', item)

for item in PERSON_PET:
    C.execute('INSERT INTO person_pet VALUES (?,?)', item)

CONN.commit()

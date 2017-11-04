#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""create a pet database"""

import sqlite3

DB = sqlite3.connect('pets.db')

try:
    CURSOR = DB.cursor()
    CURSOR.executescript('''
                         CREATE TABLE person(
                         id INTEGER PRIMARY KEY,
                         first_name TEXT,
                         last_name TEXT,
                         age INTEGER);

                         CREATE TABLE pet(
                             id INTEGER PRIMARY KEY,
                             name TEXT,
                             breed TEXT,
                             age INTEGER,
                             dead INTEGER);
                
                         CREATE TABLE person_pet(
                             person_id INTEGER,
                                pet_id INTEGER)''')
    DB.commit()

except Exception:
    DB.close()

finally:
    DB.close()

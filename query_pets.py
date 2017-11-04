#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""search the pet database"""


import sqlite3
import sys



CONN = sqlite3.connect('pets.db')

C = CONN.cursor()

def query_pets():
    """searches the pets database for the entered id and returns that users info"""
    query_id = raw_input('Enter the ID of the person to view. Enter -1 to exit. ')

    if query_id == '-1':
        sys.exit()

    else:
        try:
            C.execute('SELECT first_name, last_name, age FROM person WHERE id = ?', query_id)
            person_info = C.fetchall()

            C.execute('SELECT pet_id FROM person_pet WHERE person_id = ?', query_id)
            working_pet_id = C.fetchall()

            pet_info = []
            count = 0
            for item in working_pet_id:
                C.execute('SELECT name, breed, age, dead FROM pet WHERE id = ?',
                          working_pet_id[count])
                count += 1
                pet_info.append(C.fetchall())

            print '{} {} age {} is the owner of:'.format(person_info[0][0],
                                                         person_info[0][1],
                                                         person_info[0][2])

            count = 0
            while count < len(pet_info):
                for item in pet_info:
                    if pet_info[count][0][3] == 0:
                        print '{} a {} who is {} years old.'.format(item[0][0],
                                                                    item[0][1],
                                                                    item[0][2])
                    if pet_info[count][0][3] == 1:
                        print '{} a {} who lived to be {} years old.'.format(item[0][0],
                                                                             item[0][1],
                                                                             item[0][2])
                    count += 1

            query_pets()

        except IndexError:
            print 'Not a valid user ID'
            query_pets()


if __name__ == "__main__":
    query_pets()

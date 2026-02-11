#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from python.starwars_characters import get_film_characters


class TestStarWarsCharacters(unittest.TestCase):
    def test_fetch_with_stub(self):
        data = {
            'https://swapi-api.alx-tools.com/api/films/1/': {
                'characters': ['char-1', 'char-2']
            },
            'char-1': {'name': 'Luke Skywalker'},
            'char-2': {'name': 'C-3PO'},
        }

        def fetch_json(url):
            return data[url]

        self.assertEqual(
            get_film_characters(1, fetch_json=fetch_json),
            ['Luke Skywalker', 'C-3PO'],
        )


if __name__ == '__main__':
    unittest.main()

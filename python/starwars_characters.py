# -*- coding: utf-8 -*-
# @Time : 2026/02/11
# @Author : AllisonOge
# @Describe: fetch Star Wars film characters in API order.

import json
from urllib.request import urlopen


def _default_fetch_json(url):
    with urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


def get_film_characters(film_id, fetch_json=None):
    """Return character names for a Star Wars film in listed order.

    Mental roadmap:
    1. Fetch film payload first.
    2. Read ``characters`` URLs from that payload.
    3. Fetch each character URL in given sequence.
    4. Collect ``name`` values in the same order.

    Toy example:
    film has characters [urlA, urlB]
    urlA -> Luke, urlB -> Leia
    output -> [Luke, Leia] (order preserved).
    Why effective:
    The film payload order is the desired display order, so sequential fetch
    preserves expected output.
    """
    if fetch_json is None:
        fetch_json = _default_fetch_json

    film_url = f"https://swapi-api.alx-tools.com/api/films/{film_id}/"
    film = fetch_json(film_url)
    names = []
    for character_url in film.get("characters", []):
        character = fetch_json(character_url)
        names.append(character.get("name"))
    return names

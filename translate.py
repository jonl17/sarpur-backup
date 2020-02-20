#!/usr/bin/env python
# -*- coding: utf-8 -*-

special_characters = {
    "á": "a",
    "é": "e",
    "í": "i",
    "ó": "o",
    "ú": "u",
    "ý": "y",
    "æ": "ae",
    "ö": "o",
    "/": "_",
}

special_chars = {"&#8217;": "'", "&#8211;": "-"}


def replace_icelandic(aString):

    new_string = aString
    for letter in aString:
        for stafur in special_characters.keys():
            if letter == stafur:
                new_string = new_string.replace(letter, special_characters[letter])
    return new_string


def clean_special_characets(aString):
    return aString.replace("&#8217;", "'").replace("&#8211;", "-")

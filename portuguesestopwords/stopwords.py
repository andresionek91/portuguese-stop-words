#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unicodedata
import pkg_resources

DB_FILE = pkg_resources.resource_filename('portuguesestopwords', '/stopwords.txt')


def unaccent(string):
    """
    Receives a string and return it without accents
    :param string: accented string
    :return: unaccented string
    """

    text = unicodedata.normalize('NFD', string)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")

    return str(text)


class PortugueseStopWords:
    """
    Generates a list of Portuguese stop words
    """

    def __init__(self):
        self.words = open(DB_FILE, encoding='utf-8').read()

    def get(self):
        """
        returns a list of unique stop words
        :return: list
        """

        return list(set(self.words.split('\n')))

    def get_unaccented(self):
        """
        returns a list of unique unaccented stop words
        :return: list
        """

        word_list = self.words.split('\n')
        word_list = [unaccent(w) for w in word_list]

        return list(set(word_list))

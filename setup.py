#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
# from setuptools.command.install import install as _install


# class Install(_install):
#     def run(self):
#         #_install.do_egg_install(self)
#         import nltk
#         nltk.download('stopwords')

setup(
    name='Portuguese Stop Words',
    version='0.1',
    packages=find_packages(),
    package_data={'portuguesestopwords': ['*.txt']},
    keywords='nlp stopwords portuguese natural language processing words',
    url='https://github.com/andresionek91/portuguese-stop-words',
    classifiers=['Development Status :: 3 - Alpha', 'Programming Language :: Python :: 3.6'],
    author='Andre Sionek',
    author_email='andresionek91@gmail.com',
    description='Provides list of portuguese stop words. With or without accents.'
)

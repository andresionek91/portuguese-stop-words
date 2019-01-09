# Portuguese Stop Words
Provides list of portuguese stop words. With or without accents.

## Installation or Upgrade
To install the portuguese Stop Words just execute the following:
~~~
pip install git+https://www.github.com/andresionek91/portuguese-stop-words --upgrade
~~~

## What does this it do?

### Generates Stop Words
Use it to generate a list of portuguese stop words. They might be both accented 
or unaccented. Useful for *Natural Language Processing* algorithms.

~~~
>>> from portuguesestopwords.stopwords import PortugueseStopWords
>>>
>>> # Returns a list of stop words 
>>> PortugueseStopWords().get()
['está', 'que', 'quando', 'temos', 'tua', 'vocês', 'éramos', ... ]

>>> PortugueseStopWords().get_unaccented()
['houveramos', 'quem', 'houveram', 'nossos', 'serei', ... ]
~~~

Stop Words database from [António Lopes](https://github.com/alopes): https://gist.github.com/alopes/5358189

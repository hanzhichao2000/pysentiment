pysentiment
===========

This is a library for sentiment analysis in dictionary framework. 
Two dictionaris are provided in the library, namely, Harvard IV-4 and 
Loughran and McDonald Financial Sentiment Dictionaries, which are sentiment
dictionaries for general and financial sentiment analysis.

See also http://www.wjh.harvard.edu/~inquirer/ and https://www3.nd.edu/~mcdonald/Word_Lists.html .

Install
```````
::

    easy_install pysentiment

Usage
`````

::

    >>> import pysentiment as ps
    >>> hiv4 = ps.HIV4()
    >>> tokens = hiv4.tokenize(text)  # text can be tokenized by other ways
                                      # however, dict in HIV4 is preprocessed
                                      # by the default tokenizer in the library
    >>> score = hiv4.get_score(tokens)


``HIV4`` is a subclass for ``pysentiment.base.BaseDict``. ``BaseDict`` can be inherited by implmenting ``init_dict`` to initialize ``_posset`` and ``_negset`` for the dictionary
to calculate 'positive' or 'negative' scores for terms.


Contributions
`````````````
Bug-fixes / features are always welcome.

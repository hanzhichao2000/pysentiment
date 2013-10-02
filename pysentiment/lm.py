import pandas as pd
from pysentiment.base import STATIC_PATH, BaseDict


class LM(BaseDict):
    '''
    Dictionary class for
    Loughran and McDonald Financial Sentiment Dictionaries.
    
    See also https://www3.nd.edu/~mcdonald/Word_Lists.html
    
    The terms for the dictionary are stemmed by the default tokenizer.
    '''
    
    PATH = '%s/LM.csv' % STATIC_PATH
    
    def init_dict(self):
        data = pd.read_csv(self.PATH)
        for category in ['Positive', 'Negative']:
            terms = data['Word'][data[category] > 0]
            if category == 'Positive':
                for t in terms:
                    t = self.tokenize(t)
                    if len(t) > 0:
                        self._posset.add(t[0])
            else:
                for t in terms:
                    t = self.tokenize(t)
                    if len(t) > 0:
                        self._negset.add(t[0])
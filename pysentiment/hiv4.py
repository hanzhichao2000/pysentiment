import pandas as pd
from pysentiment.base import STATIC_PATH, BaseDict


class HIV4(BaseDict):
    '''
    Dictionary class for Harvard IV-4. 
    See also http://www.wjh.harvard.edu/~inquirer/
    
    The terms for the dictionary are stemmed by the default tokenizer.
    '''
    
    PATH = '%s/HIV-4.csv' % STATIC_PATH
    
    def init_dict(self):
        data = pd.read_csv(self.PATH)
        for category in ['Positiv', 'Negativ']:
            terms = data['Entry'][data[category] == category]
            if category == 'Positiv':
                for t in terms:
                    t = self.tokenize(t)
                    if len(t) > 0:
                        self._posset.add(t[0])
            else:
                for t in terms:
                    t = self.tokenize(t)
                    if len(t) > 0:
                        self._negset.add(t[0])
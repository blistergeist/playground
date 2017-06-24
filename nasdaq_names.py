import requests
import pandas as pd
from bs4 import BeautifulSoup
import nltk
# from tqdm import tqdm

class NasdaqNames:
    def __init__(self):
        self.url = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ'

    def get_download_url(self):
        r = requests.get(self.url)
        if not r.ok:
            code = '{} {}'.format(r.status_code, r.reason)
            raise requests.HTTPError(code)
        soup = BeautifulSoup(r.text, 'lxml')
        for a in soup.find_all('a', href=True):
            if 'companies-by-industry.aspx?exchange=NASDAQ&render=download' in a['href']:
                # print(a['href'])
                self.url += a['href']
        print(self.url)

    def create_names_df(self):
        self.get_download_url()
        df = pd.read_csv(self.url)
        # print(df.iloc[0]['Symbol'])
        # print(df.iloc[0]['Name'])
        self.namesRaw = list(df.iloc[:]['Name'])
        print(df.iloc[:]['Name'][200:250])
        print(self.namesRaw)

    def extract_name_features(self):
        stopWords = ['Inc', 'Corp', 'Ltd', 'L.P.', '.', ',']

def main():
    ndNames = NasdaqNames()
    names = ndNames.create_names_df()
    # print(names)
    # extract names as features
    # set up stopwords to remove things like ', Inc.' and ' LLC'
    # save names as list of ngrams


if __name__ == '__main__':
    main()
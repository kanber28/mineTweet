import twint
import pandas as pd

class ScrapKeyword():
    def __init__(self, keyword, limit, lang):
        self.twitter = twint.Config()
        self.twitter.Search = keyword

        self.twitter.Store_csv = True
        self.twitter.Output = keyword+".csv"
        self.twitter.Limit = limit
        self.twitter.Lang = lang
        twint.run.Search(self.twitter)

        self.result = pd.read_csv(keyword+".csv")

    def showResult(self):
        return self.result


  


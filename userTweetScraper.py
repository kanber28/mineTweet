import twint
import pandas as pd

class userTweetScrap():

  def __init__(self, username, limit):
      self.username = username
      self.limit = limit
  

  def tweetScraper(self):
    twitter = twint.Config()
    twitter.Username = self.username
    twitter.Limit = self.limit
    twitter.Store_csv = True
    twitter.Output = self.username+".csv"
    twitter.Lang = "en"
    twint.run.Search(twitter)
    result = pd.read_csv(self.username+".csv")
    
    return result

  def followersScraper(self):
    twitter = twint.Config()
    twitter.Username = self.username
    twitter.Limit = self.limit
    twitter.Store_csv = True
    twitter.Output = self.username+".csv"
    twitter.Lang = "en"
    twint.run.Followers(twitter)
    result = pd.read_csv(self.username+"Followers.csv")
    
    return result

  def followingScraper(self):
    twitter = twint.Config()
    limit = self.limit
    twitter.Username = self.username
    twitter.Limit = limit
    twitter.Store_csv = True
    twitter.Output = self.username+".csv"
    twitter.Lang = "en"
    twint.run.Following(twitter)
    result = pd.read_csv(self.username+".csv")
    
    return result
  
  


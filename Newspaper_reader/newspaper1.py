import json
import requests
def say(str):
    from win32com.client import Dispatch
    d= Dispatch('SAPI.SpVoice')
    d.Speak(str)


if __name__=='__main__':

    say('Good Morining everyone')

    #891a65af17e749a4a853d7ba31f1f98a
    #http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-14&sortBy=publishedAt&apiKey=API_KEY
    url="http://newsapi.org/v2/everything?q=bitcoin&from=2020-06-14&sortBy=publishedAt&apiKey=891a65af17e749a4a853d7ba31f1f98a"
    url2 = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d"

    news=requests.get(url2).text
    #print(news)
    l=json.loads(news)
    print(l)
    til=l['articles']

    print(til)
    for article in til:
        say(article['title'])
        print(article['title'])
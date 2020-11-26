#search engine using google
# https://www.google.com/maps/search/
query = input('Enter what you want to search ')
url = r"https://www.google.com/maps/search/"
#url = url+query


import webbrowser
url2 = r"https://www.google.com/maps/dir/"
src=input('enter source location ')
dest=input('enter destination ')
url2 = url2 +src +r"/" +dest
webbrowser.open(url2)


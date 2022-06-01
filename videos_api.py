import requests
from bs4 import BeautifulSoup

def value_to_float(x):
  if type(x) == float or type(x) == int:
      return x
  if 'K' in x:
      if len(x) > 1:
          return int(float(x.replace('K', '')) * 1000)
      return 1000
  if 'M' in x:
      if len(x) > 1:
          return int(float(x.replace('M', '')) * 1000000)
      return 1000000
  if 'B' in x:
      return int(float(x.replace('B', '')) * 1000000000)
  return x

def get_videos(username):
  links = []
  images = []
  views = []
  response = []
  url = "https://www.tiktok.com/@" + username
  html = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
  soup = BeautifulSoup(html.content, 'html.parser')
  div = soup.find("div", class_="tiktok-1qb12g8-DivThreeColumnContainer eegew6e2")
  divs = div.find_all("div", class_ = "tiktok-x6y88p-DivItemContainerV2 e19c29qe7")
  for div in divs:
    sub = div.find('div', class_="tiktok-x6f6za-DivContainer-StyledDivContainerV2 e1gitlwo0")
    img = sub.find('img')
    a = sub.find('a')
    view = sub.find('strong')
    view = view.text
    view = value_to_float(view)
    links.append(a['href'])
    images.append(img['src'])
    views.append(view)
    
  x = 0
  for link in links:
    html = requests.get(link, headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"})
    soup = BeautifulSoup(html.content, 'html.parser')
    div = soup.find('div', class_ = "tiktok-ln2tr4-DivActionItemContainer ean6quk0")
    if div:
      tabs = div.find_all('strong', class_ = "tiktok-wxn977-StrongText edu4zum2")
      if len(tabs):
        likes = tabs[0].text
        likes = value_to_float(likes)
        comments = tabs[1].text
        comments = value_to_float(comments)
        shares = tabs[2].text
        shares = value_to_float(shares)
      else:
        likes = 0
        comments = 0
        shares = 0
      obj = {}
      obj["url"] = link
      obj["img"] = images[x]
      obj["views"] = views[x]
      obj["likes"] = likes
      obj["comments"] = comments
      obj["shares"] = shares
      response.append(obj)
    x += 1

  return response

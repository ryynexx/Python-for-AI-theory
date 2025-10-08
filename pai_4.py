import requests
from bs4 import BeautifulSoup

#url of the wikipedia page to scrape
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

#send a get request to the url and get the html content
response = requests.get(url)
html_content = response.content

#response.status_code
#creare a BeatifulSoup object tp parse the html

soup = BeautifulSoup(html_content, 'html.parser')

#find the page title
title = soup.find("h1",{"class": "firstHeading"})
print(f"Title:{title}")

#extract the introduction paragraph
intro_para = soup.find('p').text
print(f'Introduction: {intro_para}')

#find all section headings
section_headings = [heading.text for heading in soup.find_all("span", {"class": "mw-headline"})]
print("Section Headings:")
for heading in section_headings:
    print(f" - {heading}")

#extract the infobox
infobox = soup.find("table", {"class":"infobox vevent"})
if infobox:
    print("\nInfobox:")
    for row in infobox.find_all('tr'):
        th = row.find("th")
        td = row.find("td")
        if th and td:
            print(f"{th.text.strip()}: {td.text.strip()}")

#find all external links
external_links = [link.get("href") for link in soup.find_all("a",{"class": "external text"})]
print("\nExternal Links:")
for link in external_links:
    print(f" - {link}")

#find all images 
images = [img.get("src") for img in soup.find_all("img")]
print("\nImages:")
for image in images:
    print(f"- https://en.wikipedia.org{image}")
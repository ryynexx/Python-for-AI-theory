from urllib.request import urlopen
url = 'https://www.annualreviews.org/content/journals/10.1146/annurev.psych.55.090902.141927'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/91.04472.124 Safari/537.36'}
page = urlopen(url).read()
print(page[:500]) #first 50 bytes
print(page[:500].decode('utf-8')) #first 50 bytes

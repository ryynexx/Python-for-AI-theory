from urllib.request import urlopen

datafile_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
explore_data =urlopen(datafile_url).read()
print(explore_data[:20])
from urllib.request import urlopen

datafile_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

#open the url and read data
with urlopen(datafile_url) as response:
    #read the entire content
    csv_data = response.read().decode('utf-8') #decode to convert bytes to string

#split the data into lines
lines = csv_data.splitlines()

#loop through each line and print it 
for line in lines:
    print(line)
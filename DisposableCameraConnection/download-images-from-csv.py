## Assuming a csv file has:
## Image Name (ImageID) in column 1 (line[0])
## Full Resolution URL (OriginalURL) in column 3 (line[2])

import sys
import urllib
import csv
import os.path

csv_filename = sys.argv[1]
url_column = int(sys.argv[2])
folder_name = sys.argv[3]
append_url = "https://images.weserv.nl/?&il&af&url="

data = []

with open(csv_filename+".csv".format(csv_filename), 'r') as read_file, open( folder_name + 'url.csv', 'w') as write_file:
    writer = csv.writer(write_file)
    for line in csv.reader(read_file):
        if (line[url_column] != "") & ("//" in line[url_column]):
            filename = line[url_column].split('/')[-1]
            if os.path.isfile("fullres/" + filename):
                print "Image skipped for {0}".format(line[0])
            else:
                if line[url_column] != '':
                    fileuri = folder_name + "/" + filename
                    urllib.urlretrieve(append_url + line[url_column], fileuri)
                    writer.writerow([line[0],line[1],line[2], line[url_column], ["./" + fileuri]])
                    print "Image saved for {0}".format(filename)
                else:
                    print "No result for {0}".format(filename)
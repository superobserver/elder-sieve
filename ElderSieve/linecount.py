import collections

#run this program from command line as "pylinecount.py >> count.txt


with open('composite2.csv') as infile:
    counts = collections.Counter(l.strip() for l in infile)
for line, count in counts.most_common():
    print line, count

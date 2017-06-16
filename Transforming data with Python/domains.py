import read
from collections import Counter
df = read.load_data()

counts = df['url'].value_counts()
print(counts[:100])

for name, row in counts.items():
    print("{0}: {1}".format(name,row))
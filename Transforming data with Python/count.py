import read
import pandas as pd
from collections import Counter
 
df = read.load_data()
s=""
for i in df['headline']:
    s += str(i).lower()

print(Counter(s.split()).most_common(100))
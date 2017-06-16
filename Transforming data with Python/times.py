import read
from dateutil.parser import parse
import datetime
df = read.load_data()

def parsing(column):
    par_col = parse(column)
    return par_col.hour
        
df['hour'] = df['submission_time'].apply(parsing)
print(df['hour'].value_counts())

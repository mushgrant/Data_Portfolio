import pandas as pd
def load_data():
    df = pd.read_csv('hn_stories.csv')
    print(df.head())
    df.columns = ['submission_time', 'upvotes', 'url','headline']
    print(df.head())
    return df
if __name__== "__main__":
        
   load_data()
        
        
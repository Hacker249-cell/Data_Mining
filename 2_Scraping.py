import pandas as pd
# Step 1: Load Twitter dataset
df = pd.read_csv("/content/Twitter_Data.csv")

# Step 2: Display first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Step 3: Display dataset columns
print("\nColumns in dataset:")
print(df.columns)

# Step 4: Extract tweet text column
if df.columns[0] != 'text':
    df.rename(columns={df.columns[0]: 'text'}, inplace=True)

tweets = df['text']

# Step 5: Display sample scraped tweets
print("\nSample Tweets:\n")
for i in range(5):
    print("Tweet", i+1, ":", tweets.iloc[i])
    print("-" * 40)

# Step 6: Total tweets collected
print("\nTotal Tweets Scraped:", len(tweets))
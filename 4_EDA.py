import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load dataset
df = pd.read_csv("Twitter_Data.csv")

# Use correct column
col = 'clean_text' if 'clean_text' in df.columns else df.columns[0]

# Basic info
print("Total Tweets:", len(df))

# Sentiment
def sentiment(text):
    p = TextBlob(str(text)).sentiment.polarity
    return "Positive" if p > 0 else "Negative" if p < 0 else "Neutral"

df['sentiment'] = df[col].apply(sentiment)

# Show sample
print(df[[col, 'sentiment']].head())

# Plot sentiment
df['sentiment'].value_counts().plot(kind='bar')
plt.title("Sentiment Analysis")
plt.show()

# Plot tweet length
df[col].astype(str).apply(len).plot(kind='hist')
plt.title("Tweet Length")
plt.show()
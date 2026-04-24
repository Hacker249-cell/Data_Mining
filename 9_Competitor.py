import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Load dataset
df = pd.read_csv("Twitter_Data.csv")

# Use correct column
col = 'clean_text' if 'clean_text' in df.columns else df.columns[0]

# Create competitor labels (example)
def get_brand(text):
    text = str(text).lower()
    if "amazon" in text:
        return "Amazon"
    elif "flipkart" in text:
        return "Flipkart"
    else:
        return "Other"

df['brand'] = df[col].apply(get_brand)

# Sentiment
def sentiment(text):
    p = TextBlob(str(text)).sentiment.polarity
    return "Positive" if p > 0 else "Negative" if p < 0 else "Neutral"

df['sentiment'] = df[col].apply(sentiment)

# Compare competitors
result = df.groupby(['brand','sentiment']).size().unstack()

print(result)

# Plot comparison
result.plot(kind='bar')
plt.title("Competitor Sentiment Comparison")
plt.show()
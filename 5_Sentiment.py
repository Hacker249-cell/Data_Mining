import pandas as pd
from textblob import TextBlob

# Step 1: Sample social media content (text-based)
data = {
    'text': [
        "AI is transforming business",
        "Marketing strategies are evolving",
        "Startup growth is amazing",
        "Business is facing challenges",
        "New technology trends in market"
    ]
}

df = pd.DataFrame(data)

# Step 2: Sentiment Analysis
def sentiment(text):
    p = TextBlob(text).sentiment.polarity
    return "Positive" if p > 0 else "Negative" if p < 0 else "Neutral"

df['sentiment'] = df['text'].apply(sentiment)

# Step 3: Topic / Keyword Extraction (simple)
df['topic'] = df['text'].str.extract('(business|marketing|startup|technology)', expand=False)

# Step 4: Display results
print(df)
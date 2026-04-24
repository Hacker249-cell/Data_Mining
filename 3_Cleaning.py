import pandas as pd
import re
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

# Load dataset
df = pd.read_csv("Twitter_Data.csv")

# Ensure text column
df.columns = ['text'] + list(df.columns[1:])

# Stopwords
stop_words = set(stopwords.words('english'))

# Clean + remove stopwords in ONE step
def clean(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|@\w+|#\w+|[^a-z\s]', '', text)
    words = text.split()
    return " ".join([w for w in words if w not in stop_words])

# Apply cleaning
df['clean_text'] = df['text'].apply(clean)

# Show result
print(df[['text', 'clean_text']].head())

# Save file
df.to_csv("cleaned_twitter_data.csv", index=False)
print("Cleaned dataset saved!")
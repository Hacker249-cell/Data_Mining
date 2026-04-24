import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("7817_1.csv")
df = df[['reviews.text','reviews.rating']].dropna()

df['sentiment'] = df['reviews.rating'].apply(lambda x: "positive" if x >= 4 else "negative")

df['sentiment'].value_counts().plot(kind='bar')
plt.title("Before Model")
plt.show()

X = TfidfVectorizer().fit_transform(df['reviews.text'])
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

pd.Series(y_pred).value_counts().plot(kind='bar')
plt.title("After Model")
plt.show()
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Dữ liệu mẫu
X = ["I love this", "I hate this"]
y = ["positive", "negative"]

# Chuyển văn bản thành vector
vectorizer = TfidfVectorizer()
X_transformed = vectorizer.fit_transform(X)

# Huấn luyện mô hình
model = LogisticRegression()
model.fit(X_transformed, y)

# Lưu mô hình và vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
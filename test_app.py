import pytest
import pandas as pd
import pickle
import os
import tempfile

def test_read_input_csv():
    # Tạo file CSV tạm trong thư mục tạm của hệ thống
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as temp_file:
        test_data = pd.DataFrame({
            "time": ["2023-01-01", "2023-01-02"],
            "sales": [100, 200]
        })
        test_data.to_csv(temp_file.name, index=False)
        temp_csv_path = temp_file.name

    # Kiểm tra đọc file
    df = pd.read_csv(temp_csv_path)
    assert len(df) == 2, "CSV should have 2 rows"
    assert "time" in df.columns, "CSV should have 'time' column"
    assert "sales" in df.columns, "CSV should have 'sales' column"
    os.remove(temp_csv_path)

def test_sentiment_prediction():
    try:
        model = pickle.load(open("model.pkl", "rb"))
        vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    except FileNotFoundError:
        pytest.skip("Model or vectorizer file not found")

    test_text = "I love this product"
    X_transformed = vectorizer.transform([test_text])
    prediction = model.predict(X_transformed)[0]
    assert prediction in ["positive", "negative"], "Prediction should be 'positive' or 'negative'"
    assert prediction == "positive", "Expected 'positive' for positive text"
from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load both models and transformers
model_low = joblib.load('random_forest_segment1.pkl')    # For low spenders
model_high = joblib.load('random_forest_segment2.pkl')   # For high spenders

transformer_1 = joblib.load('transformer_segment1.pkl')  # Transformer for segment 1
transformer_2 = joblib.load('transformer_segment2.pkl')  # Transformer for segment 2

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user input
        data = {
            'Gender': request.form['Gender'],
            'Age': request.form['Age'],
            'Occupation': int(request.form['Occupation']),
            'City_Category': request.form['City_Category'],
            'Stay_In_Current_City_Years': request.form['Stay_In_Current_City_Years'],
            'Marital_Status': int(request.form['Marital_Status']),
            'Product_Category_1': int(request.form['Product_Category_1']),
            'Product_Category_2': int(request.form.get('Product_Category_2') or 0),
            'Product_Category_3': int(request.form.get('Product_Category_3') or 0),
        }

        # Calculate Total_Product
        data['Total_Product'] = (
            data['Product_Category_1'] +
            data['Product_Category_2'] +
            data['Product_Category_3']
        )

        df = pd.DataFrame([data])

        # Segmentation based on Total_Product
        if data['Total_Product'] <= 3:
            transformed = transformer_1.transform(df)
            prediction = model_low.predict(transformed)
        else:
            transformed = transformer_2.transform(df)
            prediction = model_high.predict(transformed)

        return render_template(
            'index.html',
            prediction_text=f"Predicted Purchase: ₹{int(prediction[0])}"
        )

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

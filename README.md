# Black Friday Sales Prediction

This project uses machine learning models to predict user spending on Black Friday sales based on various features such as demographics and product categories. The goal is to create a predictive model to help businesses target customers more effectively during sales events.

## Project Overview

The project consists of the following components:

1. **Data Preprocessing**: Cleaning and preparing the data, including feature engineering and handling missing values.
2. **Model Training**: Using Random Forest models to predict customer spending, segmented into two categories:
   - Users spending ≤ 10k
   - Users spending between 10k–25k
3. **Model Deployment**: The model is deployed as a web application using Flask to make real-time predictions.

## Features

- Gender
- Age
- Occupation
- City Category
- Stay in Current City Years
- Marital Status
- Product Categories (3 categories)
- Total Product (sum of all product categories)

## Requirements

To run this project locally, you'll need the following:

- Python 3.7 or above
- Flask
- Scikit-learn
- Pandas
- Joblib
- NumPy
- Git Large File Storage (LFS) (for model files)

Install dependencies using:

```bash
pip install -r requirements.txt





# Model Files
# The trained models are available in this repository, but they have been excluded from regular Git due to their large size. They are tracked using Git Large File Storage (LFS).

# Future Enhancements
# Model optimization and hyperparameter tuning.

# Deployment to cloud platforms such as AWS or Heroku.

# Integration with a front-end UI for better user interaction.



# Acknowledgments
# Abhay Gupta - For guiding me through the project and providing valuable insights.


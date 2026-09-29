# House Price Prediction

**CODTECH Internship Project**

- **Intern ID:** CT-6212
- **Full Name:** Rahul Yadav
- **Project Name:** House Price Prediction
- **No. of Weeks:** 4
- **Project Scope:** Data cleaning, exploratory analysis, visualization and machine-learning-based house price prediction.

## Objective
Build a regression model that predicts house prices from property characteristics such as area, bedrooms, bathrooms, age, parking and location score.

## Dataset
`data/house_prices.csv` is a reproducible dummy dataset created for this project. CODTECH guidance permits dummy/public datasets for Data Science & Analytics projects.

## Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Workflow
1. Load the dataset.
2. Remove duplicates and missing rows.
3. Explore the data and visualize price distribution.
4. Split the data into training and testing sets.
5. Train a Random Forest Regression model.
6. Evaluate using MAE, RMSE and R².
7. Visualize predictions and feature importance.

## Model Result
Using the included reproducible dataset and a fixed random seed:
- MAE: 12.44 lakh
- RMSE: 15.55 lakh
- R²: 0.9757

> These metrics are specific to this included dummy dataset and should not be interpreted as real-estate market accuracy.

## Repository Structure
```text
house-price-prediction/
├── data/
│   └── house_prices.csv
├── outputs/
│   ├── actual_vs_predicted.png
│   ├── feature_importance.png
│   └── price_distribution.png
├── src/
│   └── house_price_prediction.py
├── docs/
│   └── project_documentation.md
├── house_price_prediction.ipynb
├── requirements.txt
└── README.md
```

## How to Run
```bash
pip install -r requirements.txt
python src/house_price_prediction.py
```

For notebook use:
```bash
jupyter notebook
```

## Author
Rahul Yadav — CODTECH Intern ID CT-6212

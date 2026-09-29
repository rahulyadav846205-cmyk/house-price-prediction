# Project Documentation

## 1. Project Scope
This project demonstrates an end-to-end machine learning workflow for predicting house prices.

## 2. Data Preparation
The dataset contains 500 records and the following features:
- area_sqft
- bedrooms
- bathrooms
- house_age_years
- parking_spaces
- location_score
- price_lakh (target)

Duplicate and missing records are removed before training.

## 3. Exploratory Analysis
The project includes:
- House-price distribution chart
- Actual-vs-predicted chart
- Feature-importance chart

## 4. Model
A Random Forest Regressor is used because it can model nonlinear relationships and interactions among numeric property features.

## 5. Evaluation
- Mean Absolute Error (MAE): 12.44 lakh
- Root Mean Squared Error (RMSE): 15.55 lakh
- R² Score: 0.9757

## 6. Conclusion
The project successfully demonstrates data cleaning, visualization, regression modelling and evaluation in a single reproducible workflow. The included dataset is synthetic and intended for educational/internship demonstration.

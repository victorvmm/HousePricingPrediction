# HousePricingPrediction
This project applies Machine Learning techniques to predict house prices in Ames, Iowa (USA), using a dataset with multiple structural and qualitative features of residential properties. The goal is to compare different regression models and evaluate their performance in predicting housing prices.

# Technologies and libraries

- Python: 3.12.3
- Scikit-learn: 1.8.0
- XGBoost: 3.2.0
- Pandas: 3.0.2
- Numpy: 2.4.4
- MatPlotLib: 3.10.8

# Files

- data_description.txt: 
Describes all variables, explaining each element and its classification. 

- HouseInfo.csv:
Contains all labeled data

- test.csv:
Contains non-labeled data, utilized to test the model

- DataPreparation.ipynb:
Data preprocessing was performed in this file, including handling missing values, encoding categorical variables, feature selection (removal of low-impact or potentially bias-inducing features), ensuring consistency between training and test datasets.

-  Model.ipynb:
Contains all prediction models. The models selected were Support Vector Machine (SVR), XGBoost, Random Forest and AdaBoost, based on the size of the dataset and the amount of variables, meaning it required more complex models, capable of makinn more accurate predictions in high-dimensional and non-linear spaces. Hyperparameters were optimized using GridSearchCV in two stages: coarse search (broad parameter ranges) and fine search (refined search around the best values). Models were evaluated by R² score and relation between MAE and sale price mean.

# Models final parameters

Support Vector Machine:
- C: 11
- gamma: 0.0005
- kernel: rbf

XGBoost:
- n_estimators: 1000
- learning_rate: 0.05
- max_depth: 3
- gamma: 0

Random Forest:
- n_estimators: 400
- max_depth: 30
- min_samples_split: 2
- bootstrap: False
- max_features: sqrt

AdaBoost:
- n_estimators: 400
- learning_rate: 0.1
- estimator: DecisionTreeRegressor(max_depth=3)
- loss: exponential

# Results
The best-performing models were:

- XGBoost
- - R² Score: 0.91
- - Relative MAE: 8.8%
- Random Forest
- - R² Score: 0.89
- - Relative MAE: 9.2%

These results indicate strong predictive performance, with ensemble methods outperforming other models.

- Visualization:

Bar plots were used to compare predictions from different models, highlighting differences in predicted prices for selected houses.

# Sources
The train and test datasets used in this project, as well as the data description .txt, comes from the Kaggle competition:
"House Prices: Advanced Regression Techniques"

It includes:
- 79 explanatory variables describing house features
- A target variable: SalePrice

Dataset URL: 
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques


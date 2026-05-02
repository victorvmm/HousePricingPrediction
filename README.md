# HousePricingPrediction
This project applies Machine Learning techniques to predict house prices in Ames, Iowa (USA), using a dataset with multiple structural and qualitative features of residential properties. The goal is to compare different regression models and evaluate their performance in predicting housing prices.

# Technologies and libraries

- Python: 3.12.4
- Scikit-learn: 1.4.0
- XGBoost: 
- Pandas: 
- Numpy: 
- MatPlotLib:

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
Contains all prediction models. The models chosen were Support Vector Machine (SVR), XGBoost, Random Forest and AdaBoost. These models were chosen based on the size of the dataset and the amount of variables, meaning it required more complex models, capable of predicting more accurately in high-dimensional and non-linear spaces. Hyperparameters were optimized using GridSearchCV in two stages: coarse search (broad parameter ranges) and fine search (refined search around the best values).

# Models description

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
- 

AdaBoost:
- 

# Results
The best-performing models were:

- XGBoost
- - R² Score: 0.91
- - Relative MAE: 8.8%
- Random Forest
- - R² Score: 0.89
- - Relative MAE: 9.4%

These results indicate strong predictive performance, with ensemble methods outperforming other models.

- Visualization:

Bar plots were used to compare predictions from different models, highlighting differences in predicted prices for selected houses.

# Sources
The dataset used in this project comes from the Kaggle competition:
"House Prices: Advanced Regression Techniques"

It includes:

79 explanatory variables describing house features
A target variable: SalePrice

Project URL: 

https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques


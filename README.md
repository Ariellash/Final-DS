# Property Price Prediction - DS Final Project
Final project for DS certificate

The goal of the project is to build the model that predicts the price of the property according to provided data. The project consists of 3 main steps:
1. Data preparation
2. Feature analisys and preparation
3. Model building, validation and saving for production use


## This is regression task, Metrics that were used for this purpose is RMSE. 

For testing model on local host do the following:
1. Download PriceProd.py, Client.py, model.pkl, test_example.json to you localhost
2. Open PyCharm and open the Project with saved files
3. Prepare Pycharm environemnt: install all the required packages
4. Run PriceProd.py
5. Run Client.py
6. PyCharm Console will display the predicted Price


The Project contains of 3 notebooks:
1. DataPeparation notebook which prepares data for feature and model process, treats missing and invalid values, converts objects to numerical types
2. FeaturePreparation notebook adds additional features by stacking and analyses by vizualization.
Parameteres for 3 basic stacking algorithms(LinearRegression, DecisionTreeRegressor, RandomForestRegressor) are recieved from RandomizedSearchCV process and the fourth algorithm AdaBoostRegressor got its parameters from hyperopt process
3. FinalModel train and validates the Final model. The Model that was used for regression is xgb.XGBRegressor with parameters recieved after hyperopt process. And was validated with kfold crossvalidation.

The prepoduction scripts that uses model.pkl save on localhost - PriceProd.py using Flask and Client.py that takes the test_example.json and sends it to PriceProd.py which returns the Price prediction.




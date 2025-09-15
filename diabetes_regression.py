import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data[:, np.newaxis, 2]

#train and test
#slicing
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_Y_train = diabetes.target[:-20]
diabetes_Y_test = diabetes.target[-20:]
#making model finally
model = linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_Y_train)
diabetes_Y_predicted = model.predict(diabetes_X_test)

print("Mean squared error is: ", mean_squared_error(diabetes_Y_test, diabetes_Y_predicted))
print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)
print("R² Score: ", r2_score(diabetes_Y_test, diabetes_Y_predicted))
#make legend and make graph easy to read
plt.scatter(diabetes_X_test, diabetes_Y_test,color='blue', label = 'actual')
plt.plot(diabetes_X_test, diabetes_Y_predicted, color='red', linewidth=2, label='Predicted')
plt.title('Diabetes Progression Prediction using Linear Regression')
plt.xlabel('Feature Value (3rd feature)')
plt.ylabel('Disease Progression')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

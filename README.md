# Linear_Regression( Diabetes )
PROBLEM STATEMENT 
Diabetes is a chronic medical condition that requires careful monitoring and management. Predicting the progression of diabetes can help healthcare professionals provide timely interventions. This project focuses on building a simple linear regression model to predict diabetes progression based on a single feature from the diabetes dataset.
WORKFLOW
1.  Loading of data:
The diabetes dataset was loaded from scikit-learn, containing various clinical measurements and a target variable representing disease progression.

2. Selection of feature:
For simplicity, only one feature (the third feature in the dataset) was selected to train the model.

3. Data splitting:
The data was split into training and testing sets. The last 20 samples were used for testing, and the remaining samples were used for training the model.

4. Model training:
A linear regression model was trained on the training data to learn the relationship between the selected feature and diabetes progression.

5. Model evaluation:
The model’s performance was evaluated using Mean Squared Error (MSE) and the coefficient of determination (R² score) on the test data.

6. Graph :
A scatter plot of actual versus predicted values was created to visually assess the model’s predictions.

Results

Mean Squared Error: It measures the average squared difference between predicted and actual values. A lower value indicates better accuracy.
R² Score: It represents the proportion of variance in the target variable explained by the model. Values closer to 1 indicate a better fit.


Intercept: The value of the target variable when the feature is zero.

The accompanying plot displays actual test data points alongside the model’s predicted values, illustrating the quality of the fit.

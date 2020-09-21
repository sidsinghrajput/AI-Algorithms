## Linear Regression

In Linear Regression, the relationship between the input variables (x) and output variable (y) is expressed as an equation of the form y = a + bx.
Thus, the goal of linear regression is to find out the values of coefficients a and b. Here, a is the intercept and b is the slope of the line.

## Formula for Linear Regression
y = θ1 + θ2.x

While training the model we are given :
x: input training data (univariate – one input variable(parameter))
y: labels to data (supervised learning)

When training the model – it fits the best line to predict the value of y for a given value of x. The model gets the best regression fit line by finding the best θ1 and θ2 values.
θ1: intercept
θ2: coefficient of x

## Gradient Descent

To update θ1 and θ2 values in order to reduce Cost function (minimizing RMSE value) and achieving the best fit line the model uses Gradient Descent.
The idea is to start with random θ1 and θ2 values and then iteratively updating the values, reaching minimum cost.

rm(list=ls())

#Load package with Boston(corrected) dataset
library(pdp)

#dataset summary
help(boston)

#variable names, top portion of the data
names(boston)
head(boston)

#Delete 2 variables: longitude ["lon"] and latidude ["lat"]
boston$lon <- NULL
boston$lat <- NULL
#Check the remaining variable names 
names(boston)

# Training and test subsets.
set.seed(42)
train = sample(1:nrow(boston), nrow(boston)*0.5)
test = (-train)

boston_train <- boston[train, ]
boston_test  <- boston[test, ]

X_train <- model.matrix(cmedv ~ 0 + ., data = boston_train)
X_test  <- model.matrix(cmedv ~ 0 + ., data = boston_test)

Y_train <- boston_train$cmedv
Y_test  <- boston_test$cmedv


#SOLUTION FROM HERE
#SOLUTION FROM HERE
#SOLUTION FROM HERE
#SOLUTION FROM HERE

#Ridge
(grid <- 10^seq(10, -2, length = 13))
library(glmnet)





#LM
model_linear <- lm(cmedv ~ ., data = boston_train)
summary(model_linear)

Y_hat <- predict(model_linear, newdata = boston_test)
MSE_lm <- mean((Y_test - Y_hat)^2)

print(sprintf("Linear model test MSE= %10.4f", MSE_lm))

#Ridge
(grid <- 10^seq(10, -5, length = 21))
library(glmnet)

model_ridge <- glmnet(X_train, Y_train, alpha = 0, lambda = grid)
dim(coef(model_ridge))

set.seed (42)
cv.out <- cv.glmnet(X_train, Y_train, alpha = 0)
plot(cv.out)
bestlam <- cv.out$lambda.min
bestlam

Y_hat <- predict(model_ridge, s = bestlam, newx = X_test)
MSE_ridge <- mean((Y_test - Y_hat)^2)
print(sprintf("Ridge regression test MSE= %10.4f", MSE_ridge))

#Lasso
model_lasso <- glmnet(X_train, Y_train, alpha = 1, lambda=grid)

set.seed (42)
cv.out <- cv.glmnet(X_train, Y_train, alpha = 1)
plot(cv.out)

bestlam <- cv.out$lambda.min
bestlam

Y_hat <- predict(model_lasso, s = bestlam, newx = X_test)
MSE_lasso <- mean((Y_test - Y_hat)^2)
print(sprintf("Lasso regression test MSE= %10.4f", MSE_lasso))

print(predict(model_lasso, type = "coefficients", s = bestlam))
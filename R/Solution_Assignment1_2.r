rm(list=ls())
library(ISLR2)

#dataset summary
help(Wage)

#variable names, top portion of the data
names(Wage)
head(Wage)

#Original sample size (3000 obs.)
dim(Wage)

#Reduction to 1000, and check of new sample size (1000 obs.)
Wage1000 <- Wage[1:1000,]
dim(Wage1000)

#The original variable names
names(Wage1000)

#Delete “region” and “wage”
Wage1000$region <- NULL
Wage1000$wage   <- NULL

# checking that “region” and “wage” were actually deleted 
names(Wage1000)

# Training and test subsets, 50% and 50%.
set.seed(42)
train = sample(1:nrow(Wage1000), nrow(Wage1000)*0.5)
test = (-train)

Wage1000_train <- Wage1000[train, ]
Wage1000_test  <- Wage1000[test, ]

#Subsets of explanatory variables X
X_train <- model.matrix(logwage ~ 0 + ., data = Wage1000_train)
X_test  <- model.matrix(logwage ~ 0 + ., data = Wage1000_test)

#Subsets of Y
Y_train <- Wage1000_train$logwage
Y_test  <- Wage1000_test$logwage

#SOLUTION FROM HERE
#SOLUTION FROM HERE
#SOLUTION FROM HERE
#SOLUTION FROM HERE

#LM
model_linear <- lm(logwage ~ ., data = Wage1000_train)
summary(model_linear)

Y_hat <- predict(model_linear, newdata = Wage1000_test)
MSE_lm <- mean((Y_test - Y_hat)^2)

print(sprintf("Linear model test MSE= %10.4f", MSE_lm))

#Ridge
(grid <- 10^seq(10, -2, length = 13))
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
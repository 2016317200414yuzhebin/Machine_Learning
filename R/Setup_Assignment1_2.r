rm(list=ls())
library(ISLR2)
options(digits=6)

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

#Delete $B!H(Bregion$B!I(B and $B!H(Bwage$B!I(B
Wage1000$region <- NULL
Wage1000$wage   <- NULL

# checking that $B!H(Bregion$B!I(B and $B!H(Bwage$B!I(B were actually deleted 
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

attach(Wage1000)
glm.fit2 <- glm(logwage ~ ., data = Wage1000, subset = train)
mean((logwage - predict(glm.fit2, Wage1000))[-train]^2)

library(glmnet)
grid <- 10^seq(10, -2)
ridge.mod <- cv.glmnet(X_train, Y_train, alpha = 0, lambda = grid, thresh=1e-12)
lambda.best = ridge.mod$lambda.min
ridge.pred = predict(ridge.mod, newx = X_test, s = lambda.best)
mean((Y_test - ridge.pred)^2)

grid <- 10^seq(10, -2)
lasso.mod <- cv.glmnet(X_train, Y_train, alpha = 1, lambda = grid, thresh=1e-12)
lasso.lambda.best = lasso.mod$lambda.min
lasso.pred = predict(lasso.mod, newx = X_test, s = lasso.lambda.best)
mean((Y_test - lasso.pred)^2)

lasso.coef <- predict(lasso.mod, type = "coefficients",s = lasso.lambda.best)
lasso.coef[lasso.coef == 0]


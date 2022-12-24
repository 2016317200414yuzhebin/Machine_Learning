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

attach(boston)
glm.fit <- glm(cmedv ~ ., data = boston, subset = train)
mean((cmedv - predict(glm.fit, boston))[-train]^2)

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
ridge.coef <- predict(ridge.mod, type = "coefficients",s = lambda.best)
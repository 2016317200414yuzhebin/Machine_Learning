#Load and split the College data
rm(list = ls())

library(ISLR2)
head(College)
# This copies the College dataset to R environment, and give it a new name ($B!H(Bdata$B!I(B)
data <- College
names(data)

data$Accept.Rate = data$Accept / data$Apps

#Drop 5 predictors
data$Apps         <- NULL
data$Accept       <- NULL
data$Enroll       <- NULL
data$Top25perc    <- NULL
data$perc.alumni  <- NULL

#1 Random seed and number of folds
cv_folds     <-  5
my_seed      <-  42
train_share  <-  0.75

#2 Training and test subsets
set.seed(my_seed)
train = sample(1:nrow(data), nrow(data)*train_share)
test = (-train)

data_train <- data[train, ]
data_test  <- data[test, ]

X_train <- model.matrix(Grad.Rate ~ 0 + ., data = data_train)
X_test  <- model.matrix(Grad.Rate ~ 0 + ., data = data_test)

Y_train <- data_train$Grad.Rate
Y_test  <- data_test$Grad.Rate

#3 Setup for Cross-validation and training 
library(caret)
# Setup for k-fold cross varidation
my_control <- trainControl(method = 'cv', 
                           number = cv_folds) 

#Grid for hyperparameter Lambda
Lambda_n <- 100
(lambda_grid <- 10^seq(5, -5, length = Lambda_n))
(lambda_grid = c(0, lambda_grid))

#Grid for hyperparameter Alpha
Alpha_n <- 100
(alpha_grid = (0:Alpha_n)/Alpha_n)

#Final grid for Elastic net
grid_elastic_net = expand.grid(alpha  =  alpha_grid, 
                               lambda = lambda_grid)
head(grid_elastic_net)
dim(grid_elastic_net)

#Final grid for Ridge
grid_ridge = expand.grid(alpha  =  0, 
                        lambda = lambda_grid)
head(grid_ridge)
dim(grid_ridge)

#Final grid for Lasso
grid_lasso = expand.grid(alpha  =  1, 
                         lambda = lambda_grid)
head(grid_lasso)
dim(grid_lasso)

#A special function to extract RMSE vector (just use it as it is)
get_best_result = function(caret_fit) {
  best = which(rownames(caret_fit$results) == rownames(caret_fit$bestTune))
  best_result = caret_fit$results[best, ]
  rownames(best_result) = NULL
  best_result
}

# Algorithms start from here
#LM
#################################
#       Linear model            #
#################################

set.seed(my_seed)
model_lm =  train(Grad.Rate ~ ., data = data_train, method='lm', trControl = my_control)
model_lm
summary(model_lm)

# RMSE for training dataset
(RMSE_train_lm <- get_best_result(model_lm))
(RMSE_train_lm <- RMSE_train_lm[2])

# RMSE for testing dataset
#First, prediction
pred_lm <- predict(model_lm, data_test)

#Second, prediction errors
(RMSE_test_lm <-  postResample(pred_lm, Y_test))
(RMSE_test_lm <- RMSE_test_lm[1])

print(sprintf("Linear model test RMSE = %10.4f", RMSE_test_lm))

#Elastic net
####################################
#            Elastic Net           #
####################################
set.seed(my_seed)
model_en =  train(Grad.Rate ~ ., data = data_train, method="glmnet", 
                  trControl = my_control, tuneGrid = grid_elastic_net,
                  preProc = c("center", "scale"))
model_en

#Best alpha and lambda
model_en$bestTune$alpha
model_en$bestTune$lambda

# RMSE for training dataset
(RMSE_train_en <- get_best_result(model_en))
(RMSE_train_en <- RMSE_train_en[3])

# RMSE for testing dataset
pred_en <- predict(model_en, data_test)
(RMSE_test_en <- postResample(pred_en, Y_test))
(RMSE_test_en <- RMSE_test_en[1])

print(sprintf("EN regression test RMSE = %10.4f", RMSE_test_en))

####################################
#               Ridge              #
####################################
set.seed(my_seed)
model_ridge =  train(Grad.Rate ~ ., data = data_train, method="glmnet", 
                     trControl = my_control, tuneGrid = grid_ridge,
                     preProc = c("center", "scale"))
plot(model_ridge)
model_ridge

#Best alpha and lambda
model_ridge$bestTune$alpha
model_ridge$bestTune$lambda

# RMSE for training dataset
(RMSE_train_ridge <- get_best_result(model_ridge))
(RMSE_train_ridge <- RMSE_train_ridge[3])

# RMSE for testing dataset
pred_ridge <- predict(model_ridge, data_test)
(RMSE_test_ridge <- postResample(pred_ridge, Y_test))
(RMSE_test_ridge <- RMSE_test_ridge[1])

print(sprintf("Ridge regression test RMSE= %10.4f", RMSE_test_ridge))

####################################
#              Lasso               #
####################################
set.seed(my_seed)
model_lasso =  train(Grad.Rate ~ ., data = data_train, method="glmnet", 
                     trControl = my_control, tuneGrid = grid_lasso,
                     preProc = c("center", "scale"))
plot(model_lasso)
model_lasso

#Best alpha and lambda
model_lasso$bestTune$alpha
model_lasso$bestTune$lambda

# RMSE for training dataset
(RMSE_train_lasso <- get_best_result(model_lasso))
(RMSE_train_lasso <- RMSE_train_lasso[3])

# RMSE for testing dataset
pred_lasso <- predict(model_lasso, data_test)
(RMSE_test_lasso <- postResample(pred_lasso, Y_test))
(RMSE_test_lasso <- RMSE_test_lasso[1])

print(sprintf("Lasso regression test RMSE = %10.4f", RMSE_test_lasso))

print("###############################")
print("###############################")
print("#8 FINAL RESULT: training error")
print("###############################")
print("###############################")

print(sprintf("Linear model = %10.4f", RMSE_train_lm))
print(sprintf("Ridge        = %10.4f", RMSE_train_ridge))
print(sprintf("Lasso        = %10.4f", RMSE_train_lasso))
print(sprintf("Elastic net  = %10.4f", RMSE_train_en))

print("###############################")
print("###############################")
print("#9 FINAL RESULT: testing error")
print("###############################")
print("###############################")

print(sprintf("Linear model = %10.4f", RMSE_test_lm))
print(sprintf("Ridge        = %10.4f", RMSE_test_ridge))
print(sprintf("Lasso        = %10.4f", RMSE_test_lasso))
print(sprintf("Elastic net  = %10.4f", RMSE_test_en))
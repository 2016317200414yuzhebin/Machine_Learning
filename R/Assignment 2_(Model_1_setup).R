rm(list=ls())

# Step 1 
# Random seed and number of folds
cv_folds     <- 5
my_seed      <- 42
train_share  <- 0.75

library(readxl)
dataset <- read_excel("D:/R/Economist_data_2022.xlsx",sheet = "Data")
dim(dataset)

#check for missing data
dataset <- na.omit(dataset)
dim(dataset)

#variable names, top portion of the data
names(dataset)
head(dataset)

#Model 1 (no country_id)
#Delete 1 variable: country_id
dataset$country_id <- NULL

#Check the remaining variable names 
names(dataset)

# Step 2
# Training and test subsets
set.seed(my_seed)
train = sample(1:nrow(dataset), nrow(dataset)*train_share)
test = (-train)

dataset_train <- dataset[train, ]
dataset_test  <- dataset[test, ]

X_train <- model.matrix(gdp ~ 0 + ., data = dataset_train)
X_test  <- model.matrix(gdp ~ 0 + ., data = dataset_test)

Y_train <- dataset_train$gdp
Y_test  <- dataset_test$gdp

# Step 3
# Setup for Cross-validation and training 
library(caret)
# There are k cross-folds
my_control <- trainControl(method = 'cv', 
                           number = cv_folds) 

(lambda_grid <- 10^seq(5, -5, length = 100))
(lambda_grid = c(0, lambda_grid))

# Step 4
# Elastic Net
# "alpha" is a mixing parameter between Lasso and Ridge regressions
# alpha=1: lasso regression (default) 
# alpha=0: ridge regression 

# alpha in the range [0,1], 
ElasticNetMax <- 10
(alpha_grid = (0:ElasticNetMax)/ElasticNetMax)

grid_elastic_net = expand.grid(alpha  =  alpha_grid, 
                               lambda = lambda_grid)
grid_elastic_net
dim(grid_elastic_net)

# Step 5
# Bagging
#!!!!!Bagging requires no hyperparameters!!!
# Available models (search for "bag")
# https://topepo.github.io/caret/available-models.html

modelLookup('treebag')

# Step 6
# Random Forest
# Available models (search for "bag")
# https://topepo.github.io/caret/available-models.html
modelLookup('rf')

(rf_max <- ncol(X_train)-1)

#In random forest, here we use EACH predictor in X (from 1 to rf_max)
RFGrid <-  expand.grid(mtry = seq(1, rf_max))   
RFGrid
dim(RFGrid)

#A smaller subset of predictors, every second predictor in X (from 1 to rf_max)
#RFGrid <-  expand.grid(mtry = seq(1, rf_max, by = 2))   
#RFGrid
#dim(RFGrid)

# Step 7 
# Gradient Boosting Machine
# Available models (search for "gbm")
# https://topepo.github.io/caret/available-models.html
modelLookup('gbm')

gbmGrid <-  expand.grid(n.trees           = seq(100, 500, by = 100),
                        interaction.depth = seq(1, 5, by = 2),
                        shrinkage         = c(0.010, 0.025, 0.050),
                        n.minobsinnode    = seq(1, 11, by = 5)) 
dim(gbmGrid)

# Step 8
# A special function to extract RMSE vector (just use it as it is)
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
model_lm =  train(gdp ~ ., data = dataset_train,
                  method = "lm",
                  trControl = my_control)
model_lm
summary(model_lm)

# RMSE for training dataset
(RMSE_train_lm <- get_best_result(model_lm))
(RMSE_train_lm <- RMSE_train_lm[2])

# RMSE for testing dataset
#First, prediction
pred_lm <- predict(model_lm, dataset_test)

#Second, prediction errors
(RMSE_test_lm <-  postResample(pred_lm, Y_test))
(RMSE_test_lm <- RMSE_test_lm[1])

print(sprintf("Linear model test RMSE = %10.4f", RMSE_test_lm))

#Elastic net
####################################
#            Elastic Net           #
####################################
set.seed(my_seed)
model_en =  train(gdp ~ ., data = dataset_train,
                  method = "glmnet", 
                  trControl = my_control,
                  tuneGrid = grid_elastic_net,
                  preProc = c("center", "scale"))
model_en

#Best alpha and lambda
model_en$bestTune$alpha
model_en$bestTune$lambda

# RMSE for training dataset
(RMSE_train_en <- get_best_result(model_en))
(RMSE_train_en <- RMSE_train_en[3])

# RMSE for testing dataset
pred_en <- predict(model_en, dataset_test)
(RMSE_test_en <- postResample(pred_en, Y_test))
(RMSE_test_en <- RMSE_test_en[1])

print(sprintf("EN regression test RMSE = %10.4f", RMSE_test_en))

#Bagging
####################################
#              Bagging             #
####################################
set.seed(my_seed)
model_bag =  train(gdp ~ ., data = dataset_train,
                   method = "treebag", 
                   trControl = my_control)

# RMSE for training dataset
(RMSE_train_bag <- get_best_result(model_bag))
(RMSE_train_bag <- RMSE_train_bag[2])

# RMSE for testing dataset
pred_bag <- predict(model_bag, dataset_test)
(RMSE_test_bag <- postResample(pred_bag, Y_test))
(RMSE_test_bag <- RMSE_test_bag[1])

#Random Forest
####################################
#          Random Forest           #
####################################
set.seed(my_seed)
model_rf  =  train(gdp ~ ., data = dataset_train, 
                   method = "rf", 
                   trControl = my_control,
                   tuneGrid = RFGrid)

# RMSE for training dataset
(RMSE_train_rf <- get_best_result(model_rf))
(RMSE_train_rf <- RMSE_train_rf[2])

# RMSE for testing dataset
pred_rf <- predict(model_rf, dataset_test)
(RMSE_test_rf <- postResample(pred_rf, Y_test))
(RMSE_test_rf <- RMSE_test_rf[1])

#Boosting
####################################
#           Boosting(GBM)          #
####################################
set.seed(my_seed)
model_bt  =  train(gdp ~ ., data = dataset_train, 
                   method = "gbm", 
                   trControl = my_control,
                   tuneGrid = gbmGrid,
                   verbose = FALSE)

# RMSE for training dataset
(RMSE_train_bt <- get_best_result(model_bt))
(RMSE_train_bt <- RMSE_train_bt[5])

# RMSE for testing dataset
pred_bt <- predict(model_bt, dataset_test)
(RMSE_test_bt <- postResample(pred_bt, Y_test))
(RMSE_test_bt <- RMSE_test_bt[1])

print("###############################")
print("###############################")
print("#8 FINAL RESULT: training error")
print("###############################")
print("###############################")
print(sprintf("Linear model  = %10.4f", RMSE_train_lm))
print(sprintf("Elastic net   = %10.4f", RMSE_train_en))
print(sprintf("Bagging       = %10.4f", RMSE_train_bag))
print(sprintf("Random Forest = %10.4f", RMSE_train_rf))
print(sprintf("Boosting(GBM) = %10.4f", RMSE_train_bt))

print("###############################")
print("###############################")
print("#9 FINAL RESULT: testing error")
print("###############################")
print("###############################")
print(sprintf("Linear model  = %10.4f", RMSE_test_lm))
print(sprintf("Elastic net   = %10.4f", RMSE_test_en))
print(sprintf("Bagging       = %10.4f", RMSE_test_bag))
print(sprintf("Random Forest = %10.4f", RMSE_test_rf))
print(sprintf("Boosting(GBM) = %10.4f", RMSE_test_bt))

#Now start plot analysis

library("DALEX")
library("randomForest")
library("archivist")
library("ggplot2")

#maximum number of variables in variable-importance plots
max_vars <- 10
set.seed(my_seed)
explainer_rf <- DALEX::explain(model = model_rf, 
                               data = dataset_train[,-1], 
                               y = dataset_train$gdp, 
                               label = "Random Forest")

#plot for Random Forest
####################################
#            plot (VIP)            #
####################################
set.seed(my_seed)
vip_rf <- model_parts(explainer = explainer_rf, 
                      loss_function = loss_root_mean_square)

plot(vip_rf, max_vars = max_vars) + ggtitle("Mean variable-importance for Random Forest", "")

####################################
#            plot (PDP)            #
####################################
set.seed(my_seed)
pdp_rf <- model_profile(explainer = explainer_rf, 
                        variables = "expect_m")

plot(pdp_rf) + ggtitle("Partial-dependence profiles for Random Forest", "")

set.seed(my_seed)
pdp_rf_expectancy <- model_profile(explainer = explainer_rf, 
                                  variables = c("expect_m", "expect_w"))

plot(pdp_rf_expectancy) + ggtitle("Partial-dependence profiles for Random Forest", "")

#XGBoost
####################################
#              XGBoost             #
####################################
library(caret)
modelLookup('xgbTree')

#Note that there are 7 hyperparameters:
#1: nrounds          
#2: max_depth        
#3: eta              
#4: gamma            
#5: min_child_weight 
#6: subsample        
#7: colsample_bytree 

#Number of parameter combinantions 
xgb_combinations <- 200 #9 minutes on fast PC

#Complete grid of hyperparameters
xgbGrid <-  expand.grid(nrounds          = seq(100, 500, by = 200),
                        max_depth        = seq(3, 5, by = 2),
                        eta              = c(0.010, 0.025, 0.050),
                        gamma            = seq(2, 10, by = 2),
                        min_child_weight = seq(1, 11, by = 5),
                        subsample        = seq(0.25, 1.00, by = 0.25),
                        colsample_bytree = seq(0.25, 0.75, by = 0.25))

#Note that the complete grid has 3240 combinantions

#We randomly select only a portion of the complete grid
# Random selection (sample WITHOUT replacement)
set.seed(my_seed)
smpl <- sample(1:nrow(xgbGrid), xgb_combinations,replace = FALSE)
xgbGrid <- xgbGrid[smpl,]

set.seed(my_seed)
model_xgb  =  train(gdp ~ ., data = dataset_train, 
                    method = 'xgbTree', 
                    trControl = my_control,
                    tuneGrid = xgbGrid,
                    verbose = FALSE,
                    verbosity = 0)

##1.1 RMSE for training dataset
(RMSE_train_xgb <- get_best_result(model_xgb))
(RMSE_train_xgb <- RMSE_train_xgb[8])

#1.2 RMSE for testing dataset
pred_xgb <- predict(model_xgb, dataset_test)
(RMSE_test_xgb <- postResample(pred_xgb, Y_test))
(RMSE_test_xgb <- RMSE_test_xgb[1])

#Best hyperparameters
model_xgb$bestTune

print("###############################")
print("###############################")
print("#8 FINAL RESULT: training error")
print("###############################")
print("###############################")
print(sprintf("Random Forest = %10.4f", RMSE_train_rf))
print(sprintf("Boosting(GBM) = %10.4f", RMSE_train_bt))
print(sprintf("XGBoost       = %10.4f", RMSE_train_xgb))

print("###############################")
print("###############################")
print("#9 FINAL RESULT: testing error")
print("###############################")
print("###############################")
print(sprintf("Random Forest = %10.4f", RMSE_test_rf))
print(sprintf("Boosting(GBM) = %10.4f", RMSE_test_bt))
print(sprintf("XGBoost       = %10.4f", RMSE_test_xgb))

#plot for XGBoost
####################################
#            plot (PDP)            #
####################################
set.seed(my_seed)
explainer_xgb <- DALEX::explain(model = model_xgb, 
                               data = dataset_train[,-1], 
                               y = dataset_train$gdp, 
                               label = "XGBoost")

set.seed(my_seed)
vip_xgb <- model_parts(explainer = explainer_xgb, 
                       loss_function = loss_root_mean_square)

plot(vip_xgb, max_vars = max_vars) + ggtitle("Mean variable-importance for XGBoost", "")

set.seed(my_seed)
pdp_xgb <- model_profile(explainer = explainer_xgb, 
                        variables = "expect_m")

plot(pdp_rf, pdp_xgb) + ggtitle("Partial-dependence profiles for Random Forest and XGBoost") 
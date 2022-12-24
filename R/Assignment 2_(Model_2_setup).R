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

#Model 2: Keep "country_id" and convert it to dummy variables
dataset$country_id <- factor(dataset$country_id)
#Convert time to dummy variables too
dataset$year  <- factor(dataset$year)

#Check the remaining variable names 
str(dataset)
dim(dataset)

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
# "alpha" is a mixing parameter between Lass and Ridge regressions
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
RFGrid <-  expand.grid(mtry = seq(1, rf_max, by = 2))   
RFGrid
dim(RFGrid)

# Step 7 
# Gradient Boosting Machine
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
library("archivist")
library("ggplot2")

#maximum number of variables in variable-importance plots
max_vars <- 10
set.seed(my_seed)
explainer_en <- DALEX::explain(model = model_en, 
                               data = dataset_train[,-1], 
                               y = dataset_train$gdp, 
                               label = "Elastic net")

#plot for Random Forest
####################################
#            plot (VIP)            #
####################################
set.seed(my_seed)
vip_en <- model_parts(explainer = explainer_en, 
                      loss_function = loss_root_mean_square)

plot(vip_en, max_vars = max_vars) + ggtitle("Mean variable-importance for Elastic net", "")

####################################
#            plot (PDP)            #
####################################
set.seed(my_seed)
pdp_en <- model_profile(explainer = explainer_en, 
                        variables = "country_id")

plot(pdp_en) + ggtitle("Partial-dependence profiles for Elastic net", "")
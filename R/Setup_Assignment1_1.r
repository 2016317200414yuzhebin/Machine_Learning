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

lm.fit <- lm(logwage ~ age + health + education + health_ins, data = Wage1000)
summary(lm.fit)
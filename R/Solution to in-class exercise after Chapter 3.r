#10a.
library(ISLR2)
head(Carseats)
# This copies the carseats dataset to R environment, and give it a new name (“data”)
data <- Carseats
?Carseats

summary(Carseats)

##      Sales         CompPrice       Income       Advertising   
##  Min.   : 0.00   Min.   : 77   Min.   : 21.0   Min.   : 0.00  
##  1st Qu.: 5.39   1st Qu.:115   1st Qu.: 42.8   1st Qu.: 0.00  
##  Median : 7.49   Median :125   Median : 69.0   Median : 5.00  
##  Mean   : 7.50   Mean   :125   Mean   : 68.7   Mean   : 6.63  
##  3rd Qu.: 9.32   3rd Qu.:135   3rd Qu.: 91.0   3rd Qu.:12.00  
##  Max.   :16.27   Max.   :175   Max.   :120.0   Max.   :29.00  
##    Population      Price      ShelveLoc        Age         Education   
##  Min.   : 10   Min.   : 24   Bad   : 96   Min.   :25.0   Min.   :10.0  
##  1st Qu.:139   1st Qu.:100   Good  : 85   1st Qu.:39.8   1st Qu.:12.0  
##  Median :272   Median :117   Medium:219   Median :54.5   Median :14.0  
##  Mean   :265   Mean   :116                Mean   :53.3   Mean   :13.9  
##  3rd Qu.:398   3rd Qu.:131                3rd Qu.:66.0   3rd Qu.:16.0  
##  Max.   :509   Max.   :191                Max.   :80.0   Max.   :18.0  
##  Urban       US     
##  No :118   No :142  
##  Yes:282   Yes:258  
##                     
##                     
##                     
## 

attach(Carseats)
model1 = lm(Sales~Education + Price + Urban + US)
summary(model1)

model2 = lm(Sales~Price + US)
summary(model2)



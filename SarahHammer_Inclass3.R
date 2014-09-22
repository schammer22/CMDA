#Sarah Hammer
#CMDA 3654
#In class assignment 3

getwd()
setwd("/Users/sarahhammer/Documents/CMDA")

#reload the insurance data (new version of the file)

load("exampleData1.rData")

temp <- merge(medianincome, custdata)
summary(temp)

custdata$norm.income <- custdata$income/temp$Median.Income
summary(custdata$norm.income)

# Normalizing the income can be useful, because the cost of living and incomes
# fluctuate depending on location. Wages vary from state to state, so a high income in
# a certain state may be considered low in others.

#30% of gp values are below 0.30 and 70% of the values are above 0.30.
#Split the dataset according to values of gp. (percentages are approximate)
testSet <- subset(custdata, custdata$gp <= 0.3)
trainingSet <- subset(custdata, custdata$gp > 0.3)
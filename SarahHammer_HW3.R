#Sarah Hammer
#CMDA 3654
# HW 3
# Team 4

getwd()
setwd("/Users/sarahhammer/Documents/CMDA")

library("ggplot2");

# Part 1 - Load data
load("StockSentiment.RData")

# Part 2 - Numeric vs Factors
# Numeric values will be the values like open, high, low, close, and volume that have more information while
# the variable Polairty gives us more information as either Positive or Negative.

# Part 3
summary(stockData$Open)
summary(stockData$Date)
summary(stockData$Volume)
summary(twitterData$Positive)
summary(twitterData$Negative)
summary(twitterData$Date)

# Part 4

# TODO need to learn how to convert dates
ggplot(data=subset(stockData, Stock == "AAPL"), aes(x=Date, y=Open)) + geom_line() + theme_bw() + ggtitle("Apple Stock Values Over Time")

ggplot(data=twitterData, aes(x=Positive)) + geom_bar() + theme_bw() + ggtitle("Positive Polarity Against Negative Polarity")

ggplot(data=subset(twitterData, Query == "kindle2"), aes(x=Positive)) + geom_bar() + theme_bw() + ggtitle("Positive Polarity Against Negative Polarity for the Kindle 2")

# Part 5
# No missing values in the data

# Part 6
# Create a factor denoting if the obs is positive or negative
twitterData$Positive <- ifelse(twitterData$Polarity == 4, TRUE, FALSE);
twitterData$Negative <- ifelse(twitterData$Polarity == 0, TRUE, FALSE);

# Need to figure out how to convert the data for stockData$Date

# Need to match Queries to companies.

# Part 7
save(stockData, twitterData, file="TransformedData.RData")

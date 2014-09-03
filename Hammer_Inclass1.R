#In class assignment 1

#set working directory
getwd()
setwd("/Users/sarahhammer/Documents/CMDA")

#imports cars1 dataset
mydatacars1<- read.table('cars1.csv', sep=',', header=T)

#outputs dimension of data frame
dim(mydatacars1)

#assigns the value of cell [2,2] to variable
var1 <- mydatacars1[2,2]
var1

#gets variable names of datasets
names(mydatacars1)

#outputs first column
mydatacars1[,1]
#outputs second column
mydatacars1[,2]

#assigns column 1 to variable SPEED
SPEED <- mydatacsv[,1]
SPEED

#outputs value of row 15
mydatacars1[15,]

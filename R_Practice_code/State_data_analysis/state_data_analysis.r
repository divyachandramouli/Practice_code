getwd()
setwd('C:/Users/cdivy/Desktop/Coursework/DAND/Term_2/EDA_using_R')

# Read stateData into a variable called statesInfo (a dataframe)
statesInfo <- read.csv('stateData.csv')

#Retrieve subset of data for North east states , states like Connecticut with state.region = 1
stateSubset <- subset(statesInfo,state.region==1)
head(stateSubset,2)
dim(stateSubset)

# Another way to subset the dataframe - dataSet[ROWS,COLUMNS]
# To get all columns, leave it blank

stateSubsetBracket <-statesInfo[statesInfo$state.region ==1, ]
head(stateSubsetBracket,2)
dim(stateSubsetBracket)




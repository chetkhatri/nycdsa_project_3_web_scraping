setwd('~/Desktop/nycdsa/project_3_web_scraping/')
# library(data.table)
# library(Hmisc)
library(dplyr)
library(ggplot2)
library(reshape2)
library(ggfortify)

####################### Import data and transformation #######################
##############################################################################

df = read.csv("./df_state_count.csv", stringsAsFactors = FALSE)  

arrange(df, count)       # Use arrange from plyr package
df = df[ order(df$count), ]   # Use built-in R functions
rownames(df) <- 1:nrow(df)
 
####################### Bar charts ###########################################
##############################################################################

ggplot(df, aes(state, count)) +  
  geom_bar(aes(fill=Visitor),stat="identity") +
  labs(title= 'National Parks in US', x='',y='# of Nationa Parks') +
  coord_flip() 

 

library(igraph)
library(netrw)


g<-read.graph("temp1.txt",format="ncol",directed=T)

lpg<-page.rank(g)
sort(unlist(lpg$vector),decreasing=TRUE)[1:11]

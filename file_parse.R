
#create a temp file and replace all \t\t with \t due to r restriction and import
file = "actress_movies.txt"
x <- readLines(file)
y <- gsub( "\t\t", "\t", x,fixed=TRUE )
cat(y, file="actress_movies_1.txt", sep="\n")

actress<- read.delim("actress_movies_1.txt",sep="\t", header=FALSE, colClasses = "character",fill=TRUE)

file = "actor_movies.txt"
x <- readLines(file)
y <- gsub( "\t\t", "\t", x,fixed=TRUE )
cat(y, file="actor_movies_1.txt", sep="\n")

actor<- read.delim("actor_movies_1.txt",sep="\t", header=FALSE, colClasses = "character",fill=TRUE)


#remove all actors and actresses with < 10 movies 
vec=c()
for( i in 1:dim(actor)[1])
{
if(sum(actor[i,]!="")<11)
{
  vec=append(vec,i)
  if(i%%10000==0)
    {print(i)}
}
}
cleanactors <- actor[-vec, ]
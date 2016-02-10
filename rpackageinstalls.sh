## Expects R to be present ( 3.2 +)
## This line will install the following packages

sudo R -e 'for(x in c("httr","infuser","rjson","data.table","arm","forecast","zoo","DescTools","mixtools")) install.packages(x,repo="https://cran.cnr.berkeley.edu/",dep=TRUE)'


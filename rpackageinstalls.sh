## Expects R to be present ( 3.2 +), running this 
## Rscript -e 'cat(sprintf("%s.%s\\n",R.version["major"],R.version["minor"]))'
## will return the R version
## This line will install the following packages

sudo Rscript -e 'for(x in c("httr","infuser","rjson","data.table","arm","forecast","zoo","DescTools","mixtools")) install.packages(x,repo="https://cran.cnr.berkeley.edu/",dep=TRUE)'


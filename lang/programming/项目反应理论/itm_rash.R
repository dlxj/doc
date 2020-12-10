#detach("package:eRm")
#install.packages("ltm")
library("ltm")
setwd("D:\\workcode\\algo")
getwd()
answers <- read.csv("answers_rasch.csv")
#head(answers)

ct = cbind( ncol(answers)+1, 1) # 区分度(斜率) 固定为1
dim(ct)

o <- rasch(answers, constraint=ct)
co <- coef(o, TRUE, TRUE) # 提取参数，type 是list 或matrix
dim(co)
class(co)
co
write.table(co,file="test.txt") # 存参数
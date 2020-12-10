#detach("package:eRm")
#install.packages("ltm")
library("ltm")
setwd("D:\\workcode\\algo")
getwd()
#answers <- read.csv("answers_2PL.csv")

#ddd<- read.csv("answers_2PL.csv")
ddd<- read.csv('lsat.csv')

#ddd<-read.fwf("c2_2pl.dat", widths=c(10,rep(1,20)))  # read fixed width data format
# 前10 列是person identification
dim(ddd) #2.2_2
#数据维度是：(1000*21)，默认列名是：V1 到V21
#第一列是person index

#ddd <- ddd[,-1] # 2.2_3 
#去掉第一列，只取 V2到V21
#用head(ddd) 或 names(ddd) 来验证这一点

#names(ddd) <- paste("It",1:20, sep="") #2.2_4
#列名重命名为：It1 到It20

mod.2pl <- ltm(ddd~z1, IRT.param=T) #2. 2_5
mod.2pl$conv #2. 2_6

summary(mod.2pl) #2.2_7
co <- coef(mod.2pl) #2.2_8
co



#head(answers)

#ct = cbind( ncol(answers)+1, 1) # 区分度(斜率) 固定为1
#dim(ct)

#o <- rasch(answers) # constraint=ct
# o <- PL2.rasch<-rasch(answers)
# co <- coef(o, TRUE, TRUE) # 提取参数，type 是list 或matrix
# dim(co)
# class(co)
# co
# write.table(co,file="test.txt") # 存参数
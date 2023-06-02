heart <- read.csv("D:\\Important Documents\\GSSoC'23\\heart.csv")
summary(heart)

heart$sex <- as.factor(heart$sex)
heart$cp <- as.factor(heart$cp)
heart$restecg <- as.factor(heart$restecg)
heart$fbs <- as.factor(heart$fbs)
heart$exang <- as.factor(heart$exang)
heart$slope <- as.factor(heart$slope)
heart$ca <- as.factor(heart$ca)
heart$thal <- as.factor(heart$thal)
summary(heart)


x <- sample(1:nrow(heart), 0.8 * nrow(heart))
train <- heart[x,]
test <- heart[-x,]

model <- glm(target~., data=train, family=binomial)

pred <- predict(model, newdata=test, type="response")
pred

pchisq(model$null.deviance - model$deviance,
	model$df.null - model$df.residual,
	lower.tail=FALSE)

library(pROC)
plot(roc(test$target, pred))
auc(roc(test$target, pred))
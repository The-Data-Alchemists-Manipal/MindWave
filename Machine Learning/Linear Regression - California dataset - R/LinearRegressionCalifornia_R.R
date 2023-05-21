df <- read.csv("housing.csv")
df <- na.omit(df)
df$ocean_proximity <- as.factor(df$ocean_proximity)
set.seed(2023)
x <- sample(1:nrow(df), 0.8 * nrow(df))
train <- df[x,]
test <- df[-x,]

model <- lm(median_house_value ~ latitude + housing_median_age + population + median_income + ocean_proximity,
            data = train)
summary(model)

pred <- predict(model,
	newdata = data.frame(latitude=test$latitude,
			housing_median_age=test$housing_median_age,
			population=test$population,
			median_income=test$median_income,
			ocean_proximity=test$ocean_proximity)
)

sum((test$median_house_value - pred)^2)/nrow(test)

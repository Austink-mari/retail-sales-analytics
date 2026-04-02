library(tidyverse)
library(forecast) 
library(tseries) 
library(lubridate)
df <- read_csv("~/.spyder-py3/Codes/MP_Retail/theme_park_retail_sales.csv")
monthly <- df %>% mutate (order_date= ymd(order_date)) %>%
  mutate (year_month =floor_date(order_date, "month")) %>% 
  group_by(year_month) %>%
  summarize( total_revenue = sum(net_revenue), total_orders =n(),
    avg_satisfaction =mean(customer_satisfaction))
print(monthly)

ts()
frequency=12
revenue_ts <- ts ( monthly$total_revenue, start= c(2024,1), frequency=12)
plot(revenue_ts, main='Montly Revenue Time Series', ylab='Revenue ($)', xlab='Time', col='#0072CE',lwd=2)

decomp <- decompose(revenue_ts)
plot(decomp)

fit <- auto.arima(revenue_ts, seasonal=TRUE, D=1)
summary(fit)
checkresiduals(fit)

fit2 <- ets(revenue_ts, model = "AAA")
fc2 <- forecast(fit2, h = 6)
plot(fc2)

fc <- forecast(fit, h=6)
plot(fc, main='6-Month Revenue Forecast', ylab='Revenue ($)', xlab='Time', col='darkblue',lwd=2)
legend('topleft', legend=c('Observed','Forecast','80% CI','95% CI'),
       col=c('darkblue','darkblue','#AACCEE','#DDEEFF'), lwd=c(2,2,8,8))



df = df |> mutate(is_weekend=ifelse (day_of_week %in% c('Saturday','Sunday'),'Weekend','Weekday'))
weekend_rev <- df |> filter(is_weekend == 'Weekend') |>
  pull(net_revenue)
weekday_rev <- df |> filter(is_weekend=='Weekday') |> pull(net_revenue)
test_result <- t.test(weekend_rev, weekday_rev) 
print(test_result)

discounted <- df %>% filter(discount_pct > 0) %>% pull(returned)
full_price <- df %>% filter(discount_pct == 0) %>% pull(returned)

test2 <- t.test(discounted, full_price)
print(test2)


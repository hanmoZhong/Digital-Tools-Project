# Digital-Tools-Project
# Which of the G10 currencies is the riskiest to hold for an American resident?

## Reproducibility

Our group’s files are stored in the folder named “Main”. Within the folder you can find:

Crawl_Data: 

Crawl_data.py: python file used to reproducibly crawl data from FRED 

crawl_list_11.6.csv: csv file exported from database, from 2021.11.08 to 2022.11.08.

currency_data_11.6.db: exchange rate database we build, from 2021.11.08 to 2022.11.08.

Presentation: Presentation Powerpoint using LaTex

Digital_Tools_Final_Presentaion: latex code for writting Presentaion PowerPoint and png/jpg files.

app.ipynb: interactive app (Jupyter notebook) describing the main finding

Digital_tools_report.pdf: The final report using LaTex via online overleaf.

Digital-tools-report.zip: All images, reference and tex for writting report.

The user can reproduce our research by running this Jupyter Noteboook, can choose other currencies to look at(not just G10 currencies) by change the URL code when buiding the dataset in the code.
```
ROOT_URL_DEXSDUS="https://api.stlouisfed.org/fred/series/observationsseries_id=DEXSDUS&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
ROOT_URL_DEXUSNZ="https://api.stlouisfed.org/fred/series/observationsseries_id=DEXUSNZ&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
ROOT_URL_DEXCAUS="https://api.stlouisfed.org/fred/series/observationsseries_id=DEXCAUS&api_key=4f7fcecc2234fbd09478ce8b8f0a3725&file_type=json"
```


## Project Structure
### 1.Data Source

We collect G10 currency from FRED Data, an open economic datasource. We take G10 currency to U.S dollar daily spot exchange rate data from 2021/11/08 to 2022/10/28 which is one year before our research project begins.

The G10 currencies are: Australian dollar(al), Pound sterling(uk), Euro(eu), Swiss franc(sz), Norwegian krone(no), Japanese yen(jp),Canadian dollar(ca), New Zealand dollar(nz), Swedish krona(sd) and USD which we use as a base currency since our investor is an American resident.

* Data Crawl

We build a Database which allow users to crawl from FRED Data website to get the latest 1 year G10 currency echange rate to USD dollar.

* Data Processing

We now have a dataset which contains the daily exchange rate of each G10 currency to USD Dollar. 
To deal with missing values due to holidays we use code
```
df = df.replace('.', np.nan) # replace missing values with nan
df_ret = df.pct_change(fill_method='ffill') # calculate return
```
to get a return dataset called df_ret.


### 2.Analysis Structure

Which G10 currency is the riskiest for an American resident to hold? We want to figure out the question in this setting by looking at the riskiness of each asset. We refer to IMF's working paper "Exchange Rate Risk Measurement and Management:Issues and Approaches for Firms" and follow the measurement of exchange rate risk discussed in the paper. We also calculate the price volatility for each currency.

* VaR Calculation

The VaR calculation depends on 3 parameters:
  * The holding period, i.e., the length of time over which the foreign exchange position is planned to be held. In our setting the holding period is 1 day.
  * The confidence level at which the estimate is planned to be made. In our setting the confidence level at 95 percent.
  * The unit of currency to be used for the denomination of the VaR. We use USD dollar as the base currency.

To calculate VaR, we use 3 different widely-used models:
  * Historical Simulation

  The historical simulation is the simplest method of calculation. For each currency we plot historical return distribution and calculate VaR at 5% level.

<p align="center">
  <img src="https://user-images.githubusercontent.com/103332502/207389480-5deecc36-dc1f-40e2-b70c-34b7e7385875.png" />
</p>


  * Variance-Covariance model

  The variance – covariance model assumes that (1)the change in the value of a firm’s total foreign exchange position is a linear combination of all the changes in the values of individual foreign exchange positions, so that also the total currency return is linearly dependent on all individual currency returns; and (2)the currency returns are jointly normally distributed. Since in our setting we only allow investor to trade one single currency, in this model we only need to assume the return of each currency is normally distributed.
  For each currency we plot normally distributed historical return and calculate VaR at 5% level.
  
  <p align="center">
  <img src="https://user-images.githubusercontent.com/103332502/207391751-a41baf1a-866e-47d9-a8aa-746c53aebe9c.png" />
</p>
  
  
  * Monte Carlo Simulation
  
  We use Monte-carlo simulation to simulate the price and return for each currency, for computing simplicity and plot readability we run 10 times simulations, but we can change the time whenever we want. We then calculate VaR of return for each currency simulation. Below we show a price and return simulation for Japanese yen.
  
<p float="left">
  <img src="https://user-images.githubusercontent.com/103332502/207393192-318fd34b-e205-489b-94b5-45e51128786e.png"  />
  <img src="https://user-images.githubusercontent.com/103332502/207393760-e17377c1-e71b-4477-ba74-03ce87e0cb18.png"  /> 
</p>

* Results

We calculate VaR value for each nine currency under 3 different models, the table below shows the results:
  <p align="center">
  <img src="https://user-images.githubusercontent.com/103332502/207396522-3e3026d6-33ff-4357-9b8e-9f3b104f6891.png" />
</p>

We see Norwegian Krone is the riskiest asset under all three method, and it has the probability of 5% of losing 1.3% in one day in the fisrt two methods and the probability of 5% of losing 1.9% in one day.

* Volatility

The second way to measure riskiness is to look at volatility, which measures the dispersion of the returns.

  <p align="center">
  <img src="https://user-images.githubusercontent.com/103332502/207399427-20c23a7b-d2e1-4c53-bc1b-583087676579.png" />
</p>

By the calculating results we see that Japanese yen has the highest volatility, which means it is relatively riskier than other currencies.

* Variance-Covariance Matrix

We also plot a Variance-Covariance Matrix for the nine currencies to see the correlation.

  <p align="center">
  <img src="https://user-images.githubusercontent.com/103332502/207399989-3359dd7f-a010-4c72-9185-3205f841b9ae.png" />
</p>

We can see all the G10 currencies' exchange to USD are highly correlated, and Swiss Franc has a negative correlation with all other currencies. This gives us intuition that it's hard to do risk diversification using only G10 currencies since they are highly correlated, also the investor can use swiss franc to hedge against risk.

## Data Source
[https://fred.stlouisfed.org](https://fred.stlouisfed.org)


## References
[Exchange Rate Risk Measurement and Management:Issues and Approaches for Firms](https://www.imf.org/en/Publications/WP/Issues/2016/12/31/Exchange-Rate-Risk-Measurement-and-Management-Issues-and-Approaches-for-Firms-20120)

## Authors
baiyun.yuan@uzh.ch

hanmo.zhong@uzh.ch

yidan.chen@uzh.ch

jingshu.yang@uzh.ch

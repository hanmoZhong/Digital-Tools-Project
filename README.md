# Digital-Tools-Project
# Which of the G10 currencies is the riskiest to hold for an American resident?

## Project Structure
### 1.Data Source

We collect G10 currency from FRED Data, an open economic datasource. We take G10 currency to U.S dollar daily sopt exchange rate data from 2021/11/08 to 2022/10/28 which is one year before our research project begins.

The G10 currencies are: Australian dollar(al), Pound sterling(uk), Euro(eu), Swiss franc(sz), Norwegian krone(no), Japanese yen(jp),Canadian dollar(ca), New Zealand dollar(nz), Swedish krona(sd) and USD which we use as a base currency since our investor is an American resident.

* Data Crawl
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
  
  ![return density plot](https://user-images.githubusercontent.com/103332502/207389480-5deecc36-dc1f-40e2-b70c-34b7e7385875.png)


  * Variance-Covariance model
  * Monte Carlo Simulation

* Volatility

## Reproducibility
```
code blocks for commands
```

## Data Source
[https://fred.stlouisfed.org](https://fred.stlouisfed.org)


## References
[Exchange Rate Risk Measurement and Management:Issues and Approaches for Firms](https://www.imf.org/en/Publications/WP/Issues/2016/12/31/Exchange-Rate-Risk-Measurement-and-Management-Issues-and-Approaches-for-Firms-20120)

## Authors
baiyun.yuan@uzh.ch

hanmo.zhong@uzh.ch

yidan.chen@uzh.ch

jingshu.yang@uzh.ch

an informative README file briefly explaining the main finding, and indicating any information needed to reproduce the findings:

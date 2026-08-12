# Black-Scholes_Engine
A Python execution of the Black-Scholes options pricing model

## Overview
This project ingests historical price series and option chain data to dynamically determine asset volatility and calculate theoretical European Call and Put prices

### Key Features
* **Automated Volatility Calculation:** Analyzes historical spot prices and determines annualized historical volatility, $\sigma$
* **Closed-Form Option Pricing:** Calculates theoretical European Call ($C$) and put ($P$) valuations
* **Data Parsing Pipeline:** Ingests CSV market data and option chains via Pandas

  ---
  
## Mathematical Formulation
The engine uses the Black-Scholes-Merton model assuming lognormal distribution of underlying stock prices:

$$C(S, t) = S_0 N(d_1) - K e^{-rt} N(d_2)$$

$$P(S, t) = C + K e^{-rt} - S_0$$

Where $d_1$ and $d_2$ are defined as:

$$d_1 = \frac{\ln(S_0 / K) + \left(r + \frac{\sigma^2}{2}\right)T}{\sigma \sqrt{T}}$$

$$d_2 = d_1 - \sigma \sqrt{T}$$

* **$S_0$**: Current spot price
* **$K$**: Strike price
* **$r$**: Risk-free interest rate
* **$\sigma$**: Annualized volatility
* **$T$**: Time to maturity (in annualized years)
* **$N(\cdot)$**: Standard normal cumulative distribution function (CDF)

  ---
  
## Tech Stack & Dependencies

* **Language:** Python 3.x
* **Environment:** Jupyter Notebook / Anaconda
* **Libraries:**
  * `numpy` - Array manipulations & vectorization
  * `scipy` - Cumulative distribution function ('scipy.stats.norm')
  * `pandas` - Market data parsing and dataframe manipulation

---

## Getting Started

### Prerequisites
Ensure you have Python and Jupyter installed. All dependencies can be installed via pip:

```bash
pip install numpy scipy pandas
```

### Usage
1. Download the .py file from the repository
2. Download your market data files ('ExampleHistory.csv' and 'ExampleOChain.csv')
3. Open the file, adjust all parameters and file names, and run the file

""" 
METRICS:
    ROE(by_year): net_income(symbol) / total_average_shareholders_equity(symbol)
    EPS: DPS / EPS

CRITERIAS:
  -- Criterio 1: Dividend yield > 5%, Rentabilidad del dividendo > 5 %
    -- DividendYield = Dividend Per Share / Price Per Share
    -- DividendPayOut = DPS / PPS
    -- dividendYield_Calculated = stockadvancedtats_ttmDividendRate[1]/stock_price[1]

  -- Criterio 2: DGR > 5% , Tasa de crecimiento del dividendo > 5% 
    --log(dividends_amountyear_Y1[1],dividends_amountyear_Y2[1])

  -- Criterio 3: PayOut entre 30% y 60%
    -- DividendPayOut = Dividend Per Share / Earning Per Share
    -- DividendPayOut = DPS / EPS

  -- Criterio 4: ROE superior al 12 %, en los últimos 3 años
    -- ROE = NetIncome / Total Average Shareholder's Equity

  -- Criterio 5: Flujos de caja, positivos y en aumento en los últimos 3 años
  -- Criterio 6: Tesoreria y equivalentes, positivos y en aumento en los últimos 3 años
  -- Criterio 7: Indice de covertura de Deuda de al menos 3:1
    -- Debt Coverange Ratio = Net Income / Interest expense

  -- Criterio 8: Debt to Equity Ratio < 40 %
    -- Debt/Equity = Total Liabilities / Total Shareholder's Equity
    -- según gurufucus Debt/Equity = (Current Debt + Debt long) / Total Shareholder's Equity
    -- según morningstar Debt/Equity = Debt long / Total Shareholder's Equity
  
  -- Criterio 9: 
    -- Current Ratio = Activos corrientes/ Pasivos corrientes  > 0.95
    ---Total Current Assets / Total Current Liabilities
"""

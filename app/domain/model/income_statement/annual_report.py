from typing import Optional
from dataclasses import dataclass


@dataclass
class AnnualReport:
    """
    Represents an annual financial report for a company.

    Attributes:
        fiscalDateEnding (str): The end date of the fiscal period (e.g., "2023-12-31").
        reportedCurrency (str): The currency used for reporting (e.g., "USD").
        grossProfit (str): The gross profit for the fiscal year.
        totalRevenue (str): The total revenue for the fiscal year.
        costOfRevenue (str): The cost of revenue for the fiscal year.
        costofGoodsAndServicesSold (str): The cost of goods and services sold.
        operatingIncome (str): The operating income for the fiscal year.
        sellingGeneralAndAdministrative (str): Total selling, general, and administrative expenses.
        researchAndDevelopment (str): Research and development expenses.
        operatingExpenses (str): Total operating expenses.
        investmentIncomeNet (Optional[str]): Net investment income (may be None).
        netInterestIncome (str): Net interest income.
        interestIncome (str): Total interest income.
        interestExpense (str): Total interest expense.
        nonInterestIncome (str): Non-interest income.
        otherNonOperatingIncome (str): Other non-operating income.
        depreciation (str): Depreciation expenses.
        depreciationAndAmortization (str): Depreciation and amortization expenses.
        incomeBeforeTax (str): Income before tax.
        incomeTaxExpense (str): Income tax expense.
        interestAndDebtExpense (str): Interest and debt expense.
        netIncomeFromContinuingOperations (str): Net income from continuing operations.
        comprehensiveIncomeNetOfTax (str): Comprehensive income net of tax.
        ebit (str): Earnings before interest and taxes.
        ebitda (str): Earnings before interest, taxes, depreciation, and amortization.
        netIncome (str): Net income.
    """

    fiscalDateEnding: str
    reportedCurrency: str
    grossProfit: str
    totalRevenue: str
    costOfRevenue: str
    costofGoodsAndServicesSold: str
    operatingIncome: str
    sellingGeneralAndAdministrative: str
    researchAndDevelopment: str
    operatingExpenses: str
    investmentIncomeNet: Optional[str]  # Use Optional for fields that can be None
    netInterestIncome: str
    interestIncome: str
    interestExpense: str
    nonInterestIncome: str
    otherNonOperatingIncome: str
    depreciation: str
    depreciationAndAmortization: str
    incomeBeforeTax: str
    incomeTaxExpense: str
    interestAndDebtExpense: str
    netIncomeFromContinuingOperations: str
    comprehensiveIncomeNetOfTax: str
    ebit: str
    ebitda: str
    netIncome: str

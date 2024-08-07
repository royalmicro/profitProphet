from typing import Optional
from dataclasses import dataclass


@dataclass
class AnnualReport:
    """
    A class to represent an annual financial report of a company.

    Attributes
    ----------
    fiscalDateEnding : str
        The end date of the fiscal period.
    reportedCurrency : str
        The currency in which the financials are reported.
    totalAssets : str
        The total assets of the company.
    totalCurrentAssets : str
        The total current assets of the company.
    cashAndCashEquivalentsAtCarryingValue : str
        The value of cash and cash equivalents at the carrying value.
    cashAndShortTermInvestments : str
        The value of cash and short-term investments.
    inventory : str
        The value of the company's inventory.
    currentNetReceivables : str
        The value of current net receivables.
    totalNonCurrentAssets : str
        The total non-current assets of the company.
    propertyPlantEquipment : str
        The value of property, plant, and equipment.
    accumulatedDepreciationAmortizationPPE : Optional[str]
        The accumulated depreciation and amortization of PPE (Property, Plant, and Equipment).
    intangibleAssets : str
        The value of intangible assets.
    intangibleAssetsExcludingGoodwill : str
        The value of intangible assets excluding goodwill.
    goodwill : str
        The value of goodwill.
    investments : str
        The value of investments.
    longTermInvestments : str
        The value of long-term investments.
    shortTermInvestments : str
        The value of short-term investments.
    otherCurrentAssets : str
        The value of other current assets.
    otherNonCurrentAssets : Optional[str]
        The value of other non-current assets.
    totalLiabilities : str
        The total liabilities of the company.
    totalCurrentLiabilities : str
        The total current liabilities of the company.
    currentAccountsPayable : str
        The value of current accounts payable.
    deferredRevenue : str
        The value of deferred revenue.
    currentDebt : str
        The value of current debt.
    shortTermDebt : str
        The value of short-term debt.
    totalNonCurrentLiabilities : str
        The total non-current liabilities of the company.
    capitalLeaseObligations : str
        The value of capital lease obligations.
    longTermDebt : str
        The value of long-term debt.
    currentLongTermDebt : str
        The value of current long-term debt.
    longTermDebtNoncurrent : str
        The value of long-term debt that is non-current.
    shortLongTermDebtTotal : str
        The total of short and long-term debt.
    otherCurrentLiabilities : str
        The value of other current liabilities.
    otherNonCurrentLiabilities : str
        The value of other non-current liabilities.
    totalShareholderEquity : str
        The total shareholder equity.
    treasuryStock : str
        The value of treasury stock.
    retainedEarnings : str
        The value of retained earnings.
    commonStock : str
        The value of common stock.
    commonStockSharesOutstanding : str
        The number of common stock shares outstanding.
    """

    fiscalDateEnding: str
    reportedCurrency: str
    totalAssets: str
    totalCurrentAssets: str
    cashAndCashEquivalentsAtCarryingValue: str
    cashAndShortTermInvestments: str
    inventory: str
    currentNetReceivables: str
    totalNonCurrentAssets: str
    propertyPlantEquipment: str
    accumulatedDepreciationAmortizationPPE: Optional[str]
    intangibleAssets: str
    intangibleAssetsExcludingGoodwill: str
    goodwill: str
    investments: str
    longTermInvestments: str
    shortTermInvestments: str
    otherCurrentAssets: str
    otherNonCurrentAssets: Optional[str]
    totalLiabilities: str
    totalCurrentLiabilities: str
    currentAccountsPayable: str
    deferredRevenue: str
    currentDebt: str
    shortTermDebt: str
    totalNonCurrentLiabilities: str
    capitalLeaseObligations: str
    longTermDebt: str
    currentLongTermDebt: str
    longTermDebtNoncurrent: str
    shortLongTermDebtTotal: str
    otherCurrentLiabilities: str
    otherNonCurrentLiabilities: str
    totalShareholderEquity: str
    treasuryStock: str
    retainedEarnings: str
    commonStock: str
    commonStockSharesOutstanding: str

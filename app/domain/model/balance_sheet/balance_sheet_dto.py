from dataclasses import dataclass
from typing import Any, Dict, List, Self

from app.domain.model.balance_sheet.annual_report import AnnualReport
from app.domain.utils.entity_dto_interface import EntityDtoInterface


@dataclass
class BalanceSheetDto(EntityDtoInterface):
    """
    A Data Transfer Object (DTO) for balance sheets, facilitating conversion between
    entity objects and dictionaries for easy serialization and deserialization.

    Attributes
    ----------
    symbol : str
        The stock symbol of the company the balance sheet belongs to.
    annualReports : List[AnnualReport]
        A list of annual report objects containing detailed financial data.

    Methods
    -------
    to_dict() -> Dict[str, Any]:
        Converts the BalanceSheetDto instance into a dictionary.
    from_dict(data: Dict[str, Any]) -> Self:
        Creates a BalanceSheetDto instance from a dictionary.
    """

    symbol: str = None
    annualReports: List[AnnualReport] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "symbol": self.symbol,
            "annualReports": [
                {
                    "fiscalDateEnding": report.fiscalDateEnding,
                    "reportedCurrency": report.reportedCurrency,
                    "totalAssets": report.totalAssets,
                    "totalCurrentAssets": report.totalCurrentAssets,
                    "cashAndCashEquivalentsAtCarryingValue": report.cashAndCashEquivalentsAtCarryingValue,
                    "cashAndShortTermInvestments": report.cashAndShortTermInvestments,
                    "inventory": report.inventory,
                    "currentNetReceivables": report.currentNetReceivables,
                    "totalNonCurrentAssets": report.totalNonCurrentAssets,
                    "propertyPlantEquipment": report.propertyPlantEquipment,
                    "accumulatedDepreciationAmortizationPPE": report.accumulatedDepreciationAmortizationPPE,
                    "intangibleAssets": report.intangibleAssets,
                    "intangibleAssetsExcludingGoodwill": report.intangibleAssetsExcludingGoodwill,
                    "goodwill": report.goodwill,
                    "investments": report.investments,
                    "longTermInvestments": report.longTermInvestments,
                    "shortTermInvestments": report.shortTermInvestments,
                    "otherCurrentAssets": report.otherCurrentAssets,
                    "otherNonCurrentAssets": report.otherNonCurrentAssets,
                    "totalLiabilities": report.totalLiabilities,
                    "totalCurrentLiabilities": report.totalCurrentLiabilities,
                    "currentAccountsPayable": report.currentAccountsPayable,
                    "deferredRevenue": report.deferredRevenue,
                    "currentDebt": report.currentDebt,
                    "shortTermDebt": report.shortTermDebt,
                    "totalNonCurrentLiabilities": report.totalNonCurrentLiabilities,
                    "capitalLeaseObligations": report.capitalLeaseObligations,
                    "longTermDebt": report.longTermDebt,
                    "currentLongTermDebt": report.currentLongTermDebt,
                    "longTermDebtNoncurrent": report.longTermDebtNoncurrent,
                    "shortLongTermDebtTotal": report.shortLongTermDebtTotal,
                    "otherCurrentLiabilities": report.otherCurrentLiabilities,
                    "otherNonCurrentLiabilities": report.otherNonCurrentLiabilities,
                    "totalShareholderEquity": report.totalShareholderEquity,
                    "treasuryStock": report.treasuryStock,
                    "retainedEarnings": report.retainedEarnings,
                    "commonStock": report.commonStock,
                    "commonStockSharesOutstanding": report.commonStockSharesOutstanding,
                }
                for report in self.annualReports
            ],
        }

    def from_dict(self, data: Dict[str, Any]) -> Self:
        annual_reports = [
            AnnualReport(**report) for report in data.get("annualReports", [])
        ]
        return BalanceSheetDto(
            symbol=data.get("symbol", ""), annualReports=annual_reports
        )

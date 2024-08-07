from dataclasses import dataclass
from typing import Any, Dict, List, Self

from app.domain.model.income_statement.annual_report import AnnualReport
from app.domain.utils.entity_dto_interface import EntityDtoInterface


@dataclass
class IncomeStatementDto(EntityDtoInterface):
    """
    Represents the income statement data transfer object for a company.

    Attributes:
        symbol (str): The stock symbol of the company (e.g., "IBM").
        annualReports (List[AnnualReport]): A list of annual financial reports for the company.
    """

    symbol: str = None
    annualReports: List[AnnualReport] = None

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts an IncomeStatementDto instance into a dictionary.

        Args:
            dto (IncomeStatementDto): The IncomeStatementDto instance to convert.

        Returns:
            Dict[str, Any]: A dictionary representation of the IncomeStatementDto instance.
        """

        return {
            "symbol": self.symbol,
            "annualReports": [
                {
                    "fiscalDateEnding": report.fiscalDateEnding,
                    "reportedCurrency": report.reportedCurrency,
                    "grossProfit": report.grossProfit,
                    "totalRevenue": report.totalRevenue,
                    "costOfRevenue": report.costOfRevenue,
                    "costofGoodsAndServicesSold": report.costofGoodsAndServicesSold,
                    "operatingIncome": report.operatingIncome,
                    "sellingGeneralAndAdministrative": report.sellingGeneralAndAdministrative,
                    "researchAndDevelopment": report.researchAndDevelopment,
                    "operatingExpenses": report.operatingExpenses,
                    "investmentIncomeNet": report.investmentIncomeNet,
                    "netInterestIncome": report.netInterestIncome,
                    "interestIncome": report.interestIncome,
                    "interestExpense": report.interestExpense,
                    "nonInterestIncome": report.nonInterestIncome,
                    "otherNonOperatingIncome": report.otherNonOperatingIncome,
                    "depreciation": report.depreciation,
                    "depreciationAndAmortization": report.depreciationAndAmortization,
                    "incomeBeforeTax": report.incomeBeforeTax,
                    "incomeTaxExpense": report.incomeTaxExpense,
                    "interestAndDebtExpense": report.interestAndDebtExpense,
                    "netIncomeFromContinuingOperations": report.netIncomeFromContinuingOperations,
                    "comprehensiveIncomeNetOfTax": report.comprehensiveIncomeNetOfTax,
                    "ebit": report.ebit,
                    "ebitda": report.ebitda,
                    "netIncome": report.netIncome,
                }
                for report in self.annualReports
            ],
        }

    def from_dict(self, data: Dict[str, Any]) -> Self:
        annual_reports = [
            AnnualReport(**report) for report in data.get("annualReports", [])
        ]
        return IncomeStatementDto(
            symbol=data.get("symbol", ""), annualReports=annual_reports
        )

import math
from injector import inject
from app.application.services.alpha_vantage.functions import Functions
from app.application.services.alpha_vantage.query import Query
from app.domain.model.balance_sheet.balance_sheet_dto import BalanceSheetDto


class DebtToEquity:
    """
    A service to calculate the Debt-to-Equity ratio for a given stock symbol and year.

    This class implements the ApplicationServiceInterface and provides functionality
    to retrieve financial data from a balance sheet and compute the Debt-to-Equity ratio.
    The ratio is calculated by dividing total liabilities by total shareholder equity.
    The result is truncated to two decimal places.
    """

    @inject
    def __init__(self, query: Query) -> None:
        self.query = query

    def execute(self, symbol: str, year: str = None):
        balance_sheet = self.query.execute(symbol, Functions.BALANCE_SHEET)
        dto: BalanceSheetDto = BalanceSheetDto().from_dict(data=balance_sheet)
        report = next(
            (
                report
                for report in dto.annualReports
                if report.fiscalDateEnding.startswith(year)
            ),
            None,
        )

        if report is None:
            report = dto.annualReports[0]

        de = int(report.totalLiabilities) / int(report.totalShareholderEquity)
        de = math.floor(de * 100) / 100
        return {"value": de, "in": "ratio"}

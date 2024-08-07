from injector import inject

from app.application.services.metrics.balance_sheet import BalanceSheet
from app.application.services.metrics.income_statement import IncomeStatement


class Roe:
    """
    ROE = net_income / shareholders_equity
    """

    @inject
    def __init__(
        self, income_statement: IncomeStatement, balance_sheet: BalanceSheet
    ) -> None:
        self.income_statement = income_statement
        self.balance_sheet = balance_sheet

    def execute(self, symbol: str) -> float | None:
        income_statement = self.income_statement.execute(symbol)
        balance_sheet = self.balance_sheet.execute(symbol)

        if (
            len(income_statement.annualReports) < 1
            or len(balance_sheet.annualReports) < 1
        ):
            return None

        last_net_income = income_statement.annualReports[0].netIncome
        last_shareholder_equity = balance_sheet.annualReports[0].totalShareholderEquity

        return int(last_net_income) / int(last_shareholder_equity)

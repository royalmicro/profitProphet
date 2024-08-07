from injector import inject
from app.application.services.alpha_vantage.functions import Functions
from app.application.services.alpha_vantage.query import Query
from app.domain.model.balance_sheet.balance_sheet_dto import BalanceSheetDto


class BalanceSheet:
    """
    A class to handle the retrieval and processing of balance sheet data.

    Attributes
    ----------
    query : Query
        The query service used to fetch data from an external API.

    Methods
    -------
    execute(symbol: str) -> BalanceSheetDto:
        Executes a query to retrieve balance sheet data for a given stock symbol
        and returns it as a BalanceSheetDto.
    """

    @inject
    def __init__(self, query: Query) -> None:
        self.query = query

    def execute(self, symbol) -> BalanceSheetDto:
        data = self.query.execute(symbol, function=Functions.BALANCE_SHEET)
        dto = BalanceSheetDto()
        return dto.from_dict(data)

from injector import inject

from app.application.services.alpha_vantage.functions import Functions
from app.application.services.alpha_vantage.query import Query
from app.domain.model.income_statement.income_statement_dto import IncomeStatementDto


class IncomeStatement:
    """
    A class to handle the retrieval and processing of income statement data.

    Attributes
    ----------
    query : Query
        The query service used to fetch data from an external API.

    Methods
    -------
    execute(symbol: str) -> IncomeStatementDto:
        Executes a query to retrieve income statement data for a given stock symbol
        and returns it as an IncomeStatementDto.
    """

    @inject
    def __init__(self, query: Query) -> None:
        self.query = query

    def execute(self, symbol) -> IncomeStatementDto:
        data = self.query.execute(symbol, function=Functions.INCOME_STATEMENT)
        dto = IncomeStatementDto()
        return dto.from_dict(data=data)

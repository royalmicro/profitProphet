from injector import inject
from app.application.services.alpha_vantage.functions import Functions
from app.application.services.alpha_vantage.query import Query
from app.application.services.metrics.application_service_interface import (
    ApplicationServiceInterface,
)
from app.domain.model.overview.overview_dto import OverviewDto


class DividendYield(ApplicationServiceInterface):
    """
    Service class responsible for calculating the dividend yield of a company.

    The `DividendYield` class implements the `ApplicationServiceInterface` and is designed
    to query financial data for a given company symbol using the Alpha Vantage API,
    then extract and compute the dividend yield.

    Dependencies:
    -------------
    - Query: A service that handles querying the Alpha Vantage API for financial data.

    Methods:
    --------
    execute(symbol: str) -> int:
        Executes the process of retrieving and calculating the dividend yield for the provided symbol.
    """

    @inject
    def __init__(self, query: Query) -> None:
        self.query = query

    def execute(self, symbol: str) -> int:
        overview = self.query.execute(symbol, Functions.OVERVIEW)
        overview_dto = OverviewDto.from_dict(overview)
        dividend_yield = float(overview_dto.DividendYield) * 100
        return dividend_yield

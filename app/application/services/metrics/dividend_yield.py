from injector import inject
from app.application.services.alpha_vantage.functions import Functions
from app.application.services.alpha_vantage.query import Query
from app.application.services.metrics.application_service_interface import (
    ApplicationServiceInterface,
)
from app.domain.model.company.company_dto import CompanyDto
from app.infrastructure.persistence.company_repository import CompanyRepository


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
    def __init__(self, query: Query, company_repository: CompanyRepository) -> None:
        self.query = query
        self.company_repository = company_repository

    def execute(self, symbol: str) -> int:
        existent_company = self.company_repository.get_by_symbol(symbol)

        if existent_company is not None:
            company = existent_company.to_dict()
        else:
            company_overview = self.query.execute(symbol, Functions.OVERVIEW)
            company = self.company_repository.add(**company_overview).to_dict()

        dto = CompanyDto.from_dict(company)
        dividend_yield = float(dto.DividendYield) * 100
        return dividend_yield

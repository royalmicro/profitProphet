from injector import inject
from app.application.services.alpha_vantage.functions import Functions
from app.application.services.alpha_vantage.query import Query
from app.application.services.metrics.application_service_interface import (
    ApplicationServiceInterface,
)
from app.domain.model.company.company_dto import CompanyDto
from app.infrastructure.persistence.company_repository import CompanyRepository


class EarningPerShare(ApplicationServiceInterface):
    """
    A service class that provides the Earnings Per Share (EPS) for a given company's symbol.
    It interacts with the company repository and external API queries to fetch or compute the EPS value.

    Attributes:
        query (Query): An instance of the Query service used to execute API calls to fetch company data.
        company_repository (CompanyRepository): Repository instance for accessing and persisting company data.

    Methods:
          execute(symbol: str) -> dict:
            Executes the process of fetching the Earnings Per Share (EPS) for a given company symbol.
            If the company exists in the repository, it retrieves the data from there. Otherwise,
            it fetches the company's data using an external API and saves it in the repository.

            Args:
                symbol (str): The stock symbol of the company to fetch EPS for.

            Returns:
                dict: A dictionary containing the EPS value and the currency in which it's denominated.
                Example: {"value": 2.50, "in": "USD"}
    """

    @inject
    def __init__(self, company_repository: CompanyRepository, query: Query) -> None:
        self.query = query
        self.company_repository = company_repository

    def execute(self, symbol: str):
        existent_company = self.company_repository.get_by_symbol(symbol)

        if existent_company is not None:
            company = existent_company.to_dict()
        else:
            company_overview = self.query.execute(symbol, Functions.OVERVIEW)
            company = self.company_repository.add(**company_overview).to_dict()

        dto = CompanyDto.from_dict(company)

        return {"value": dto.EPS, "in": dto.Currency}

from app.configuration.extensions.db_extension import db
from app.domain.model.company.company_dto import CompanyDto
from app.domain.model.company.company_repository_interface import (
    CompanyRepositoryInterface,
)
from app.infrastructure.persistence.sql_alchemy.company.company_mapped import (
    CompanyMapped,
)


class CompanyRepository(CompanyRepositoryInterface):
    """
    A repository class responsible for managing company data persistence using SQLAlchemy.
    This class provides methods to add a new company to the database and retrieve a company by its symbol.

    Attributes:
        db (SQLAlchemy): The SQLAlchemy database instance used for database operations.

    Methods:
        add(**kwargs) -> CompanyMapped:
            Adds a new company to the database. The company data is first converted from a dictionary to a DTO,
            and then mapped to a SQLAlchemy model before being persisted.

            Args:
                **kwargs: Arbitrary keyword arguments containing the company's data.

            Returns:
                CompanyMapped: The most recently added company record, retrieved from the database.

        get_by_symbol(symbol: str) -> CompanyMapped:
            Retrieves a company record from the database based on the provided stock symbol.

            Args:
                symbol (str): The stock symbol of the company to be retrieved.

            Returns:
                CompanyMapped: The company record corresponding to the provided symbol, or None if not found.
    """

    def __init__(self) -> None:
        self.db = db
        super().__init__(self)

    def add(self, **kwargs) -> CompanyMapped:
        dto = CompanyDto.from_dict(kwargs)
        mapped_stock = CompanyMapped(**dto.to_dict())
        self.db.session.add(mapped_stock)
        self.db.session.commit()

        return (
            self.db.session.query(CompanyMapped)
            .order_by(CompanyMapped.id.desc())
            .first()
        )

    def get_by_symbol(self, symbol) -> CompanyMapped:
        company: CompanyMapped = CompanyMapped.query.filter(
            (CompanyMapped.Symbol == symbol)
        ).first()
        return company

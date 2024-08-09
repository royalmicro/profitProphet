from dataclasses import dataclass, asdict


@dataclass
class CompanyDto:
    """
    Data Transfer Object (DTO) representing an overview of financial and company metrics.

    This class encapsulates various financial and descriptive attributes of a company.
    It provides utility methods to convert the object to and from a dictionary,
    facilitating easy serialization and deserialization of the data.

    Methods:
    --------
    to_dict() -> dict:
        Converts the OverviewDto instance into a dictionary.

    from_dict(cls, data: dict) -> OverviewDto:
        Creates an OverviewDto instance from a dictionary, handling key name transformations
        for specific attributes.
    """

    id: int | None
    Symbol: str
    AssetType: str
    Name: str
    Description: str
    CIK: str
    Exchange: str
    Currency: str
    Country: str
    Sector: str
    Industry: str
    Address: str
    OfficialSite: str
    FiscalYearEnd: str
    LatestQuarter: str
    MarketCapitalization: int
    EBITDA: int
    PERatio: float
    PEGRatio: float
    BookValue: float
    DividendPerShare: float
    DividendYield: float
    EPS: float
    RevenuePerShareTTM: float
    ProfitMargin: float
    OperatingMarginTTM: float
    ReturnOnAssetsTTM: float
    ReturnOnEquityTTM: float
    RevenueTTM: int
    GrossProfitTTM: int
    DilutedEPSTTM: float
    QuarterlyEarningsGrowthYOY: float
    QuarterlyRevenueGrowthYOY: float
    AnalystTargetPrice: float
    AnalystRatingStrongBuy: int
    AnalystRatingBuy: int
    AnalystRatingHold: int
    AnalystRatingSell: int
    AnalystRatingStrongSell: int
    TrailingPE: float
    ForwardPE: float
    PriceToSalesRatioTTM: float
    PriceToBookRatio: float
    EVToRevenue: float
    EVToEBITDA: float
    Beta: float
    _52WeekHigh: float
    _52WeekLow: float
    _50DayMovingAverage: float
    _200DayMovingAverage: float
    SharesOutstanding: int
    DividendDate: str
    ExDividendDate: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        data["_52WeekHigh"] = data.pop("52WeekHigh", None)
        data["_52WeekLow"] = data.pop("52WeekLow", None)
        data["_50DayMovingAverage"] = data.pop("50DayMovingAverage", None)
        data["_200DayMovingAverage"] = data.pop("200DayMovingAverage", None)

        if data["id"] is None:
            data["id"] = None

        return cls(**data)

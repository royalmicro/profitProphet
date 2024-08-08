from dataclasses import dataclass, asdict


@dataclass
class OverviewDto:
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
    FiscalYearEnd: str
    LatestQuarter: str
    MarketCapitalization: str
    EBITDA: str
    PERatio: str
    PEGRatio: str
    BookValue: str
    DividendPerShare: str
    DividendYield: str
    EPS: str
    RevenuePerShareTTM: str
    ProfitMargin: str
    OperatingMarginTTM: str
    ReturnOnAssetsTTM: str
    ReturnOnEquityTTM: str
    RevenueTTM: str
    GrossProfitTTM: str
    DilutedEPSTTM: str
    QuarterlyEarningsGrowthYOY: str
    QuarterlyRevenueGrowthYOY: str
    AnalystTargetPrice: str
    AnalystRatingStrongBuy: str
    AnalystRatingBuy: str
    AnalystRatingHold: str
    AnalystRatingSell: str
    AnalystRatingStrongSell: str
    TrailingPE: str
    ForwardPE: str
    PriceToSalesRatioTTM: str
    PriceToBookRatio: str
    EVToRevenue: str
    EVToEBITDA: str
    Beta: str
    Week52High: str
    Week52Low: str
    Day50MovingAverage: str
    Day200MovingAverage: str
    SharesOutstanding: str
    DividendDate: str
    ExDividendDate: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        data["Week52High"] = data["52WeekHigh"]
        data["Week52Low"] = data["52WeekLow"]
        del data["52WeekHigh"]
        del data["52WeekLow"]

        data["Day50MovingAverage"] = data["50DayMovingAverage"]
        data["Day200MovingAverage"] = data["200DayMovingAverage"]
        del data["50DayMovingAverage"]
        del data["200DayMovingAverage"]

        return cls(**data)

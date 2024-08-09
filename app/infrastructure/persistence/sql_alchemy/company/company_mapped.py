from dataclasses import dataclass
from typing import Dict, Optional, Any
from sqlalchemy import String, Text, Integer, Float, BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from app.configuration.extensions.db_extension import db


@dataclass
class CompanyMapped(db.Model):
    """
    Represents a company entity in the application's database.
    """

    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    Symbol: Mapped[str] = mapped_column(String(8), unique=True, nullable=False)
    AssetType: Mapped[str] = mapped_column(String(50), nullable=False)
    Name: Mapped[str] = mapped_column(String(255), nullable=False)
    Description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    CIK: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    Exchange: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    Currency: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    Country: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    Sector: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    Industry: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    Address: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    OfficialSite: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    FiscalYearEnd: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    LatestQuarter: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    MarketCapitalization: Mapped[Optional[int]] = mapped_column(
        BigInteger, nullable=True
    )
    EBITDA: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    PERatio: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    PEGRatio: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    BookValue: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    DividendPerShare: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    DividendYield: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    EPS: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    RevenuePerShareTTM: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    ProfitMargin: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    OperatingMarginTTM: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    ReturnOnAssetsTTM: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    ReturnOnEquityTTM: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    RevenueTTM: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    GrossProfitTTM: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    DilutedEPSTTM: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    QuarterlyEarningsGrowthYOY: Mapped[Optional[float]] = mapped_column(
        Float, nullable=True
    )
    QuarterlyRevenueGrowthYOY: Mapped[Optional[float]] = mapped_column(
        Float, nullable=True
    )
    AnalystTargetPrice: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    AnalystRatingStrongBuy: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True
    )
    AnalystRatingBuy: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    AnalystRatingHold: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    AnalystRatingSell: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    AnalystRatingStrongSell: Mapped[Optional[int]] = mapped_column(
        Integer, nullable=True
    )
    TrailingPE: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    ForwardPE: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    PriceToSalesRatioTTM: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    PriceToBookRatio: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    EVToRevenue: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    EVToEBITDA: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    Beta: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    _52WeekHigh: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    _52WeekLow: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    _50DayMovingAverage: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    _200DayMovingAverage: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    SharesOutstanding: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    DividendDate: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    ExDividendDate: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)

    def to_dict(self) -> Dict[str, Any]:

        response = {
            "Symbol": self.Symbol,
            "AssetType": self.AssetType,
            "Name": self.Name,
            "Description": self.Description,
            "CIK": self.CIK,
            "Exchange": self.Exchange,
            "Currency": self.Currency,
            "Country": self.Country,
            "Sector": self.Sector,
            "Industry": self.Industry,
            "Address": self.Address,
            "OfficialSite": self.OfficialSite,
            "FiscalYearEnd": self.FiscalYearEnd,
            "LatestQuarter": self.LatestQuarter,
            "MarketCapitalization": self.MarketCapitalization,
            "EBITDA": self.EBITDA,
            "PERatio": self.PERatio,
            "PEGRatio": self.PEGRatio,
            "BookValue": self.BookValue,
            "DividendPerShare": self.DividendPerShare,
            "DividendYield": self.DividendYield,
            "EPS": self.EPS,
            "RevenuePerShareTTM": self.RevenuePerShareTTM,
            "ProfitMargin": self.ProfitMargin,
            "OperatingMarginTTM": self.OperatingMarginTTM,
            "ReturnOnAssetsTTM": self.ReturnOnAssetsTTM,
            "ReturnOnEquityTTM": self.ReturnOnEquityTTM,
            "RevenueTTM": self.RevenueTTM,
            "GrossProfitTTM": self.GrossProfitTTM,
            "DilutedEPSTTM": self.DilutedEPSTTM,
            "QuarterlyEarningsGrowthYOY": self.QuarterlyEarningsGrowthYOY,
            "QuarterlyRevenueGrowthYOY": self.QuarterlyRevenueGrowthYOY,
            "AnalystTargetPrice": self.AnalystTargetPrice,
            "AnalystRatingStrongBuy": self.AnalystRatingStrongBuy,
            "AnalystRatingBuy": self.AnalystRatingBuy,
            "AnalystRatingHold": self.AnalystRatingHold,
            "AnalystRatingSell": self.AnalystRatingSell,
            "AnalystRatingStrongSell": self.AnalystRatingStrongSell,
            "TrailingPE": self.TrailingPE,
            "ForwardPE": self.ForwardPE,
            "PriceToSalesRatioTTM": self.PriceToSalesRatioTTM,
            "PriceToBookRatio": self.PriceToBookRatio,
            "EVToRevenue": self.EVToRevenue,
            "EVToEBITDA": self.EVToEBITDA,
            "Beta": self.Beta,
            "_52WeekHigh": self._52WeekHigh,
            "_52WeekLow": self._52WeekLow,
            "_50DayMovingAverage": self._50DayMovingAverage,
            "_200DayMovingAverage": self._200DayMovingAverage,
            "SharesOutstanding": self.SharesOutstanding,
            "DividendDate": self.DividendDate,
            "ExDividendDate": self.ExDividendDate,
        }

        if self.id is not None:
            response["id"] = self.id

        return response

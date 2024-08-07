from injector import inject

from app.application.services.metrics.dividend_yield import DividendYield
from app.application.services.metrics.earning_per_share import EarningPerShare
from app.application.services.metrics.metrics import Metrics
from app.application.services.metrics.roe import Roe


class GetMetrics:
    """
    A class to handle the retrieval and processing of various financial metrics for a list of stock tickers.

    Attributes
    ----------
    roe : Roe
        The service used to calculate the Return on Equity (ROE) metric.

    Methods
    -------
    execute(tickers: list[str], metrics: list[str]) -> list[dict[str, any]]:
        Retrieves the specified metrics for the given list of stock tickers and returns
        the results as a list of dictionaries.
    """

    @inject
    def __init__(
        self, roe: Roe, dividend_yield: DividendYield, eps: EarningPerShare
    ) -> None:
        self.roe = roe
        self.dividend_yield = dividend_yield
        self.eps = eps

    def execute(self, tickers: list[str], metrics: list[str]):
        result: list[dict[str, any]] = []
        for ticker in tickers:
            metrics_result: dict[str, any] = {}
            ticker = ticker.upper()
            for metric in metrics:
                metric = metric.upper()

                if metric == Metrics.ROE:
                    metrics_result[Metrics.ROE] = {
                        "value": self.__get_roe(ticker),
                        "in": "%",
                    }

                if metric == Metrics.DIVIDEND_YIELD:
                    metrics_result[Metrics.DIVIDEND_YIELD] = {
                        "value": self.__get_dividend_yield(ticker),
                        "in": "%",
                    }
                if metric == Metrics.EPS:
                    eps = self.__get_eps(ticker)
                    metrics_result[Metrics.EPS] = {
                        "value": eps["value"],
                        "in": eps["in"],
                    }

            if len(metrics_result) > 0:
                result.append({"symbol": ticker, "metrics": metrics_result})

        return result

    def __get_roe(self, ticker: str):
        return self.roe.execute(ticker)

    def __get_dividend_yield(self, ticker: str):
        return self.dividend_yield.execute(ticker)

    def __get_eps(self, ticker: str) -> dict:
        return self.eps.execute(ticker)

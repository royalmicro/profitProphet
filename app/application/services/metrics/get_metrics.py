from injector import inject

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
    def __init__(self, roe: Roe) -> None:
        self.roe = roe

    def execute(self, tickers: list[str], metrics: list[str]):
        result: list[dict[str, any]] = []
        for ticker in tickers:
            metrics_result: list[dict[str, any]] = []
            ticker = ticker.upper()
            for metric in metrics:
                metric = metric.upper()

                if metric == "ROE":
                    metrics_result.append({"ROE": self.__get_roe(ticker)})
                    continue

            if len(metrics_result) > 0:
                result.append({"symbol": ticker, "metrics": metrics_result})

        return result

    def __get_roe(self, ticker: str):
        return self.roe.execute(ticker)

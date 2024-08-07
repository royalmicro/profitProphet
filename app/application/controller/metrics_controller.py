from flask_restx import Resource
from injector import inject
from flask import request
from app.application.services.metrics.get_metrics import GetMetrics
from app.configuration.api.namespaces import profitProphet_ns


@profitProphet_ns.doc(security="Bearer")
@profitProphet_ns.route("/metrics")
class MetricsController(Resource):
    """
    A Flask-RESTx resource class to handle HTTP requests for retrieving financial metrics for given stock tickers.

    Attributes
    ----------
    get_metrics : GetMetrics
        The service used to retrieve the specified financial metrics.

    Methods
    -------
    get()
        Handles GET requests to retrieve financial metrics for specified stock tickers.
    """

    @inject
    def __init__(self, get_metrics: GetMetrics, *args, **kwargs):
        self.get_metrics = get_metrics
        super().__init__(*args, **kwargs)

    @profitProphet_ns.doc(
        params={
            "tickers": "Symbol for the query",
            "start_date": "Start date for the query (format: YYYY-MM-DD)",
            "end_date": "End date for the query (format: YYYY-MM-DD)",
            "metrics": "Limit of results (1 to 100)",
        }
    )
    def get(self):
        # Parse query parameters
        query_params = request.args.to_dict()
        tickers = query_params.get("tickers").split(",")
        metrics = query_params.get("metrics").split(".")

        result = self.get_metrics.execute(tickers, metrics)

        return (result, 200)

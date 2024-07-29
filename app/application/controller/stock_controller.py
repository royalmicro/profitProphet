from typing import List
from flask_restx import Resource, fields
from injector import inject
from app.configuration.extensions.api_extension import ProfitProphetApi
from app.domain.model.entity_interface import EntityInterface
from app.infrastructure.persistence.stock_repository import StockRepository

restx_api = ProfitProphetApi().get_api_instance()
ns = restx_api.namespace("stocks", description="Stocks operations")

stock = restx_api.model(
    "Stock",
    {
        "id": fields.Integer(readonly=True, description="Stock unique id"),
        "symbol": fields.String(required=True, description="Stock symbol"),
        "name": fields.String(required=True, description="Stock name"),
    },
)


@ns.route("/")
class StockController(Resource):
    """Shows a list of all stocks, and lets you POST to add new stocks"""

    @inject
    def __init__(self, stock_repo: StockRepository, *args, **kwargs):
        self.stock_repository = stock_repo
        super().__init__(*args, **kwargs)

    @ns.doc("list_stocks")
    @ns.marshal_list_with(stock)
    def get(self):
        """List all tasks"""
        stocks: List[EntityInterface] = self.stock_repository.get_all()
        return stocks

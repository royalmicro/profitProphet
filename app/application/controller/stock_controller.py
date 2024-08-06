from flask_jwt_extended import jwt_required
from flask_restx import Resource, abort, reqparse
from injector import inject

from app.application.services.alpha_vantage.query import Query
from app.domain.model.stock.stock import Stock
from app.infrastructure.persistence.stock_repository import StockRepository
from app.configuration.api.namespaces import profitProphet_ns
from app.configuration.api.models import stock_model


parser = reqparse.RequestParser()
parser.add_argument("symbol", type=str)
parser.add_argument("name", type=str)


@profitProphet_ns.doc(security="Bearer")
@profitProphet_ns.param("symbol", "The symbol identifier")
@profitProphet_ns.route("/stocks/<string:symbol>/overview")
class StockItemOverview(Resource):
    """Shows a stock overview"""

    @inject
    def __init__(self, stock_repo: StockRepository, query: Query, *args, **kwargs):
        self.stock_repository = stock_repo
        self.query = query
        super().__init__(*args, **kwargs)

    def get(self, symbol: str):
        res = self.query.execute(symbol=symbol, function="OVERVIEW")
        return res


@profitProphet_ns.doc(security="Bearer")
@profitProphet_ns.route("/stocks/<string:symbol>")
@profitProphet_ns.response(404, "Stock not found")
@profitProphet_ns.param("symbol", "The symbol identifier")
class StockItemsController(Resource):
    """Shows a list of all stocks, and lets you POST to add new stocks"""

    method_decorators = [jwt_required()]

    @inject
    def __init__(self, stock_repo: StockRepository, query: Query, *args, **kwargs):
        self.stock_repository = stock_repo
        self.query = query
        super().__init__(*args, **kwargs)

    @profitProphet_ns.marshal_with(stock_model)
    def get(self, symbol):
        """Stock element"""
        mapped_stock = self.stock_repository.get_by_symbol(symbol)

        if mapped_stock is None:
            return abort(404, message="Stock not found")

        attr_values = {
            column.name: getattr(mapped_stock, column.name)
            for column in mapped_stock.__table__.columns
        }
        return Stock(**attr_values)

    @profitProphet_ns.expect(stock_model)
    def put(self, **kwargs):
        """Update a stock"""
        args = parser.parse_args()

        self.stock_repository.update(Stock(**kwargs, **args))

    @profitProphet_ns.response(204, "Stock deleted")
    def delete(self, **kwargs):
        """Update a stock"""
        self.stock_repository.delete_by_symbol(kwargs.get("symbol"))
        return "", 204


@profitProphet_ns.doc(security="Bearer")
@profitProphet_ns.route("/stocks")
class StockCollectionController(Resource):
    """Shows a list of all stocks, and lets you POST to add new stocks"""

    method_decorators = [jwt_required()]

    @inject
    def __init__(self, stock_repo: StockRepository, *args, **kwargs):
        self.stock_repository = stock_repo
        super().__init__(*args, **kwargs)

    @profitProphet_ns.doc("list_stocks")
    @profitProphet_ns.marshal_list_with(stock_model)
    def get(self):
        """List all stocks"""
        return self.stock_repository.get_all()

    @profitProphet_ns.doc("create_stock")
    @profitProphet_ns.expect(stock_model)
    @profitProphet_ns.marshal_with(stock_model, code=201)
    def post(self):
        """Create a new stock"""
        stock_data = profitProphet_ns.payload
        return (self.stock_repository.add(**stock_data), 201)

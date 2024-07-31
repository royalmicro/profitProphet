from flask_restx import Resource, abort, fields, reqparse
from injector import inject

from app.configuration.extensions.api_extension import ProfitProphetApi
from app.domain.model.stock.stock import Stock
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

parser = reqparse.RequestParser()
parser.add_argument("symbol", type=str)
parser.add_argument("name", type=str)


@ns.route("/<string:symbol>")
@ns.response(404, "Stock not found")
@ns.param("symbol", "The symbol identifier")
class StockItemsController(Resource):
    """Shows a list of all stocks, and lets you POST to add new stocks"""

    @inject
    def __init__(self, stock_repo: StockRepository, *args, **kwargs):
        self.stock_repository = stock_repo
        super().__init__(*args, **kwargs)

    @ns.doc("get_stock")
    @ns.marshal_with(stock)
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

    @ns.expect(stock)
    def put(self, **kwargs):
        """Update a stock"""
        args = parser.parse_args()

        self.stock_repository.update(Stock(**kwargs, **args))

    @ns.response(204, "Stock deleted")
    def delete(self, **kwargs):
        """Update a stock"""
        self.stock_repository.delete(kwargs.get("symbol"))
        return "", 204


@ns.route("/")
class StockCollectionController(Resource):
    """Shows a list of all stocks, and lets you POST to add new stocks"""

    @inject
    def __init__(self, stock_repo: StockRepository, *args, **kwargs):
        self.stock_repository = stock_repo
        super().__init__(*args, **kwargs)

    @ns.doc("list_stocks")
    @ns.marshal_list_with(stock)
    def get(self):
        """List all stocks"""
        return self.stock_repository.get_all()

    @ns.doc("create_stock")
    @ns.expect(stock)
    @ns.marshal_with(stock, code=201)
    def post(self):
        """Create a new stock"""
        stock_data = restx_api.payload
        return (self.stock_repository.add(**stock_data), 201)

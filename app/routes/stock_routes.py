from typing import List
from flask import Blueprint, request
from injector import inject

from app.domain.utils.entity_interface import EntityInterface
from app.domain.model.stock.stock import Stock

from app.infrastructure.persistence.stock_repository import StockRepository
from app.infrastructure.services.http.http_response import HttpResponse

stock_bp = Blueprint("stock", __name__)


@inject
@stock_bp.route("/stocks", methods=["GET"])
def get_stock(stock_repo: StockRepository, http_response: HttpResponse):
    stocks: List[EntityInterface] = stock_repo.get_all()
    return http_response.to_flask_response(stocks, 200)


@inject
@stock_bp.route("/stocks", methods=["POST"])
def add_stock(stock_repo: StockRepository, http_response: HttpResponse):
    data = request.get_json()
    new_stock = Stock(
        stockId=None,
        symbol=data["symbol"],
        name=data["name"],
        historical_data=data["historical_data"],
    )
    stock_repo.add(new_stock)
    return http_response.to_flask_response({"message": "New Stock Created"}, 201)


# @stock_bp.route("/stocks/<int:id>", methods=["DELETE"])
# def delete_stock(stockId):
#     stock = StockEntity().query.get(stockId)
#     db.session.delete(stock)
#     db.session.commit()
#     return HttpResponse(None, 200).to_flask_response()

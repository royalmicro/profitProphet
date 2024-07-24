from typing import List
from flask import Blueprint, request

from app.domain.model.entity.entity_interface import EntityInterface
from app.domain.model.entity.stock.stock_entity import StockEntity
from app.infrastructure.services.http.http_response import HttpResponse
from app.configuration.extensions import db

stock_bp = Blueprint("stock", __name__)


@stock_bp.route("/stocks", methods=["GET"])
def get_stock():
    stocks: List[EntityInterface] = StockEntity.query.all()
    return HttpResponse(stocks, 200).to_flask_response()


@stock_bp.route("/stocks", methods=["POST"])
def add_stock():
    data = request.get_json()
    new_stock = StockEntity(symbol=data["symbol"], name=data["name"])  # type: ignore
    db.session.add(new_stock)
    db.session.commit()
    return HttpResponse(new_stock, 201).to_flask_response()


@stock_bp.route("/stocks/<int:id>", methods=["DELETE"])
def delete_stock(stockId):
    stock = StockEntity().query.get(stockId)  # type: ignore
    db.session.delete(stock)
    db.session.commit()
    return HttpResponse(None, 200).to_flask_response()

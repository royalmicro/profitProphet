from typing import List
from flask import Blueprint, request

from app.domain.model.entity.entity_interface import EntityInterface
from app.domain.model.entity.price_data.data_price_entity import DataPriceEntity
from app.infrastructure.services.http.http_response import HttpResponse
from app.configuration.extensions import db

data_price_bp = Blueprint("price_data", __name__)


@data_price_bp.route("/data_prices", methods=["GET"])
def get_data_price():
    data_prices: List[EntityInterface] = DataPriceEntity.query.all()
    return HttpResponse(data_prices, 200).to_flask_response()


@data_price_bp.route("/data_prices/<int:id>", methods=["GET"])
def get_data_price_item(dataPriceId: int):
    entity = DataPriceEntity().query.get(dataPriceId)
    return HttpResponse(entity, 200).to_flask_response()


@data_price_bp.route("/data_prices", methods=["POST"])
def post_data_price():
    data = request.get_json()
    entity = DataPriceEntity(**data)
    db.session.add(entity)
    db.session.commit()
    return HttpResponse(entity, 201).to_flask_response()


# @price_data_bp.route("/data_prices", methods=["PUT"])
# def put_data_price(): ...


@data_price_bp.route("/data_prices/<int:id>", methods=["DELETE"])
def delete_data_price(entityId):
    entity = DataPriceEntity().query.get(entityId)
    db.session.delete(entity)
    db.session.commit()
    return HttpResponse(None, 200).to_flask_response()

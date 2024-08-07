from flask_restx import fields
from app.configuration.extensions.api_extension import api

metrics_request_model = api.model(
    "Metrics",
    {
        "tickers": fields.List(fields.String),
        "metrics": fields.List(fields.String),
    },
)

stock_model = api.model(
    "Stock",
    {
        "id": fields.Integer(readonly=True, description="Stock unique id"),
        "symbol": fields.String(required=True, description="Stock symbol"),
        "name": fields.String(required=True, description="Stock name"),
    },
)

auth_model = api.model(
    "Auth",
    {
        "username": fields.String(required=True, description="Stock symbol"),
        "password": fields.String(required=True, description="Stock name"),
    },
)

user_model = api.model(
    "User",
    {
        "id": fields.Integer,
        "username": fields.String,
    },
)

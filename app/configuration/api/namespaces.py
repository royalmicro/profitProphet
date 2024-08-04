from app.configuration.extensions.api_extension import api, authorizations

auth_ns = api.namespace("auth", description="Stocks operations")
profitProphet_ns = api.namespace(
    "profitprophet",
    description="Profit Prophet operations",
    authorizations=authorizations,
)

from flask_jwt_extended import create_access_token
from flask_restx import Resource
from injector import inject
from werkzeug.security import check_password_hash
from app.configuration.api.namespaces import auth_ns
from app.configuration.api.models import user_model, auth_model
from app.domain.model.user.user import User
from app.infrastructure.persistence.user_repository import UserRepository


@auth_ns.route("/register")
class RgisterController(Resource):
    """
    Controller for handling user registration.

    This class defines the endpoint for user registration, allowing
    new users to create an account.
    """

    @inject
    def __init__(self, user_repository: UserRepository, *args, **kwargs):
        self.user_repository = user_repository
        super().__init__(*args, **kwargs)

    @auth_ns.expect(auth_model)
    @auth_ns.marshal_with(user_model, code=201)
    def post(self):
        user_data = auth_ns.payload
        user = User(**user_data)
        return (self.user_repository.add_entity(user), 201)


@auth_ns.route("/login")
class LoginController(Resource):
    """
    Controller for handling user login.

    This class defines the endpoint for user login, allowing existing
    users to authenticate and receive an access token.
    """

    @inject
    def __init__(self, user_repository: UserRepository, *args, **kwargs):
        self.user_repository = user_repository
        super().__init__(*args, **kwargs)

    @auth_ns.expect(auth_model)
    def post(self):
        user = self.user_repository.get_by_username(auth_ns.payload.get("username"))
        password = auth_ns.payload["password"]

        if not user:
            return {"error": "User does not exist"}, 401
        if not check_password_hash(user.get_password_hash(), password):
            return {"error": "Incorrect password"}, 401

        return {"access_token": create_access_token(user.get_username())}

import json
from typing import Dict, List

from flask import Response

from app.domain.model.entity_interface import EntityInterface


HEADERS = {"Content-Type": "application/json"}


class HttpResponse:
    """
    Represents an HTTP response with JSON serialization capabilities.

    This class is designed to create an HTTP response that can handle
    different types of data, including lists of entities, single entities,
    or None. It provides methods to serialize the data to JSON and to
    convert it to a Flask Response object.

    Attributes:
        data (List[EntityInterface] | EntityInterface | None): Data to be included in the response.
        status (int): The HTTP status code for the response.
        headers (Dict[str, str]): The headers to be included in the response.

    Methods:
        serialize() -> str: Serializes the data to a JSON string.
        __str__() -> str: Returns the serialized JSON string.
        __repr__() -> str: Returns the serialized JSON string.
        to_flask_response() -> Response: Converts the HttpResponse to a Flask Response object.
    """

    def serialize(self, data_to_serialize) -> str:
        try:
            data = data_to_serialize
            if isinstance(data, list):
                data = [entity.entity_to_dto().to_string() for entity in data]
            else:
                data = data.entity_to_dto().to_string()  # type: ignore

            return json.dumps(data)
        except TypeError as e:
            raise ValueError(f"Data provided cannot be serialized to JSON: {e}") from e

    def to_flask_response(
        self,
        data: List[EntityInterface] | EntityInterface | None,
        status: int,
        headers: Dict[str, str] | None = None,
    ) -> Response:
        response_body = (
            data if isinstance(data, dict) else json.loads(self.serialize(data))
        )
        return Response(
            response=json.dumps(response_body),
            status=status,
            headers=headers,
            mimetype="application/json",
        )

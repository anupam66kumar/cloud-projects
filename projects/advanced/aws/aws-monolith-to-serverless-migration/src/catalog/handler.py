"""bookstore-catalog Lambda — the catalog slice of the strangled monolith.

Handles the read-only catalog routes the monolith used to serve:
    GET /books          -> list
    GET /books/{id}     -> one book

Backed by the DynamoDB 'Books' table. Payload v2.0 (HTTP API) event shape.
No comments on the obvious; only the routing note matters.
"""

import json
import os
from decimal import Decimal

import boto3

TABLE = os.environ.get("BOOKS_TABLE", "Books")
APP_VERSION = os.environ.get("APP_VERSION", "catalog-1.0")

_books = boto3.resource("dynamodb").Table(TABLE)


def _json_default(value):
    if isinstance(value, Decimal):
        return int(value) if value % 1 == 0 else float(value)
    return str(value)


def _resp(status, body):
    return {"statusCode": status, "headers": {"content-type": "application/json"},
            "body": json.dumps(body, default=_json_default)}


def handler(event, context):
    method = event["requestContext"]["http"]["method"]
    path = event["requestContext"]["http"]["path"]
    book_id = (event.get("pathParameters") or {}).get("id")

    if method == "GET" and book_id:
        item = _books.get_item(Key={"id": book_id}).get("Item")
        return _resp(200, item) if item else _resp(404, {"error": "not found"})

    if method == "GET":
        items = _books.scan().get("Items", [])
        return _resp(200, {"version": APP_VERSION, "books": items})

    return _resp(405, {"error": f"{method} {path} not supported"})

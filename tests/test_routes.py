import pytest
from app import app
from models import db
from models.item import Item


@pytest.fixture
def client():

    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.test_client() as client:

        with app.app_context():
            db.drop_all()
            db.create_all()

        yield client


def test_home(client):

    response = client.get("/")

    assert response.status_code == 200


def test_create_item(client):

    response = client.post(
        "/items",
        json={
            "name": "Milk",
            "barcode": "12345",
            "quantity": 5,
            "price": 3.99
        }
    )

    assert response.status_code == 201


def test_get_items(client):

    client.post(
        "/items",
        json={
            "name": "Bread",
            "barcode": "111",
            "quantity": 2,
            "price": 2.50
        }
    )

    response = client.get("/items")

    assert response.status_code == 200
    assert len(response.json) == 1


def test_update_item(client):

    client.post(
        "/items",
        json={
            "name": "Eggs",
            "barcode": "222",
            "quantity": 6,
            "price": 5.99
        }
    )

    response = client.put(
        "/items/1",
        json={
            "quantity": 12
        }
    )

    assert response.status_code == 200
    assert response.json["quantity"] == 12


def test_delete_item(client):

    client.post(
        "/items",
        json={
            "name": "Apple",
            "barcode": "333",
            "quantity": 5,
            "price": 1.99
        }
    )

    response = client.delete("/items/1")

    assert response.status_code == 200


def test_search(client):

    client.post(
        "/items",
        json={
            "name": "Orange Juice",
            "barcode": "444",
            "quantity": 3,
            "price": 4.99
        }
    )

    response = client.get("/search?name=orange")

    assert response.status_code == 200
    assert len(response.json) == 1


def test_low_stock(client):

    client.post(
        "/items",
        json={
            "name": "Cheese",
            "barcode": "555",
            "quantity": 2,
            "price": 6.99
        }
    )

    response = client.get("/low-stock")

    assert response.status_code == 200
    assert len(response.json) == 1
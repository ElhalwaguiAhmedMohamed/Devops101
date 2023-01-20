from fastapi import status
import json


def test_create_order(client):
    data = {
        "name": "item 1",
        "cost": 100,
        "available_quantity": 2000
    }
    response = client.post('/items/', json.dumps(data))
    data = {
        "shopping_cart_id": 1,
        "requested_quantity": 10,
        "total_cost": 100,
        "item_id": 1
    }
    response = client.post('/orders/', json.dumps(data))
    assert response.status_code == 200
    assert response.json()['requested_quantity'] == '10'


def test_read_all_orders(client):
    data = {
        "name": "item 1",
        "cost": 100,
        "available_quantity": 2000
    }
    response = client.post('/items/', json.dumps(data))
    data = {
        "shopping_cart_id": 1,
        "requested_quantity": 10,
        "total_cost": 100,
        "item_id": 1
    }
    client.post('/orders/', json.dumps(data))
    data = {
        "shopping_cart_id": 1,
        "requested_quantity": 10,
        "total_cost": 100,
        "item_id": 1
    }
    client.post('/orders/', json.dumps(data))
    response = client.get("/orders/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_read_order(client):
    data = {
        "name": "item 1",
        "cost": 100,
        "available_quantity": 2000
    }
    response = client.post('/items/', json.dumps(data))
    data = {
        "shopping_cart_id": 1,
        "requested_quantity": 10,
        "total_cost": 100,
        "item_id": 1
    }
    response = client.post("/orders/", json.dumps(data))
    response = client.get("/orders/1/")
    assert response.status_code == 200
    assert response.json()['requested_quantity'] == '10'


def test_update_order(client):
    data = {
        "name": "item 1",
        "cost": 100,
        "available_quantity": 2000
    }
    response = client.post('/items/', json.dumps(data))
    data = {
        "shopping_cart_id": 1,
        "requested_quantity": 10,
        "total_cost": 100,
        "item_id": 1
    }
    client.post("/orders/", json.dumps(data))
    data["requested_quantity"] = 15
    response = client.put("/orders/1", json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_order(client):
    data = {
        "name": "item 1",
        "cost": 100,
        "available_quantity": 2000
    }
    response = client.post('/items/', json.dumps(data))
    data = {
        "shopping_cart_id": 1,
        "requested_quantity": 10,
        "total_cost": 100,
        "item_id": 1
    }
    client.post("/orders/", json.dumps(data))
    msg = client.delete("/orders/1")
    response = client.get("/orders/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND

from fastapi import status
import json


def test_create_item(self, client):
    data = {
        "name": "item 1",
        "cost": 100,
        "available_quantity": 2000
    }
    response = client.post('/items/', json.dumps(data))
    assert response.status_code == 200
    assert response.json()['name'] == 'item 1'


def test_read_all_items(client):
    data = {
        "name": "item 2",
        "cost": 150,
        "available_quantity": 5000
    }
    client.post('/items/', json.dumps(data))
    data = {
        "name": "item 3",
        "cost": 170,
        "available_quantity": 4000
    }
    client.post('/items/', json.dumps(data))
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_read_item(client):
    data = {
        "name": "item 6",
        "cost": 170,
        "available_quantity": 4000
    }
    response = client.post("/items/", json.dumps(data))

    response = client.get("/items/1/")
    assert response.status_code == 200
    assert response.json()['name'] == "item 6"


def test_update_item(client):
    data = {
        "name": "item 4",
        "cost": 170,
        "available_quantity": 4000
    }
    client.post("/items/", json.dumps(data))
    data["name"] = "updated item 4"
    response = client.put("/items/1", json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."


def test_delete_item(client):
    data = {
        "name": "item 5",
        "cost": 170,
        "available_quantity": 4000
    }
    client.post("/items/", json.dumps(data))
    msg = client.delete("/items/1")
    response = client.get("/items/1/")
    assert response.status_code == status.HTTP_404_NOT_FOUND

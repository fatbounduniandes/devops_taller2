import application as app


def get_client():
    app.application.testing = True
    return app.application.test_client()


def test_index_returns_all_heroes():
    client = get_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, dict)
    assert "0" in data
    assert data["0"]["name"] == "A-Bomb"


def test_heroe_by_id_ok():
    client = get_client()
    response = client.get("/0")
    assert response.status_code == 200
    hero = response.get_json()
    assert hero["name"] == "A-Bomb"
    assert hero["publisher"] == "Marvel Comics"


def test_heroe_not_found():
    client = get_client()
    response = client.get("/999")
    assert response.status_code == 404
    body = response.get_json()
    assert "error" in body

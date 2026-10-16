import funtions as f


def test_load_file_returns_dict():
    data = f.load_file('./heroes.csv')
    assert isinstance(data, dict)
    assert len(data) == 6


def test_load_file_keys_and_fields():
    data = f.load_file('./heroes.csv')
    assert "0" in data
    assert "5" in data

    hero = data["0"]
    assert hero["name"] == "A-Bomb"
    assert hero["publisher"] == "Marvel Comics"
    assert hero["alignment"] == "good"

    # Todos los heroes deben tener los campos esperados
    expected_fields = {
        "name", "gender", "eye_color", "race", "hair_color",
        "height", "publisher", "skin_color", "alignment", "weight",
    }
    for hero_id, record in data.items():
        assert expected_fields.issubset(record.keys()), f"Faltan campos en heroe {hero_id}"

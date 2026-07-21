from api.spam_api import send_spam

def test_send_spam():
    data = {
        "person": "Иванов Иван Иванович",
        "communication": "2",
        "callStart": "2026-07-10T13:58:34.598Z",
        "authAs": "9371234567",
        "categories": ["s02"],
        "channel": 0,
        "class": 1,
        "comment": "Реклама",
        "ctnA": "+79377654321",
        "ctnB": "9371234567",
        "services": []
    }
    response = send_spam(data)
    assert response.status_code == 200
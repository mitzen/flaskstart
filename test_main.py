from main import app

target = app.test_client()

def test_app():
 result = target.get("/todo1")
 print(result.data)
 assert result.json["task"] == "Hello world"

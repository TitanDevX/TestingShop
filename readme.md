# 🧪 Running Tests

## ▶️ Run all tests (unit + integration)
⚠️ Make sure the server is running first:
```
python app.py
```
Also make sure to install playwright:
```
playwright install
```
To run tests:
```bash
python -m pytest
```
🚀 Performance Testing (Locust)
Start Locust:
```
locust -f performance/locustfile.py
```
Then open:
http://localhost:8089


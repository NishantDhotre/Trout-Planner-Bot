import requests

def test_agent_response():
    response = requests.post('http://localhost:8000/agent', json={'message': 'Test message'})
    assert response.status_code == 200
    assert 'response' in response.json()

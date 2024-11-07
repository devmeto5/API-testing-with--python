import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def base_url():
    return BASE_URL

def test_get_posts(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert isinstance(response.json(), list), "Response should be a list"

def test_create_post(base_url):
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201, f"Expected 201, but got {response.status_code}"
    response_data = response.json()
    assert response_data["title"] == payload["title"], "Title does not match"
    assert response_data["body"] == payload["body"], "Body does not match"
    assert response_data["userId"] == payload["userId"], "UserId does not match"

def test_update_post(base_url):
    post_id = 1
    updated_data = {
        "title": "updated title",
        "body": "updated body"
    }
    response = requests.put(f"{base_url}/posts/{post_id}", json=updated_data)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    response_data = response.json()
    assert response_data["title"] == updated_data["title"], "Title was not updated correctly"
    assert response_data["body"] == updated_data["body"], "Body was not updated correctly"

def test_delete_post(base_url):
    post_id = 1
    response = requests.delete(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"

if __name__ == "__main__":
    pytest.main()
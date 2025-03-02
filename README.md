# API Testing with Python

This guide will help you create and run automated tests for an API using Python

## Step 1: Install Required Tools
First, you will need Python and the `pip` package manager. Make sure the following tools are installed:

- **Python 3.x**: Download and install from the official site: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **`pip`**: The package manager for installing libraries, usually included with Python.

## Step 2: Install Libraries
Install the necessary libraries for testing:

```bash
pip install requests pytest
```
- **`requests`**: Used for making HTTP requests.
- **`pytest`**: A library for writing and running tests.

## Step 3: Create a Test File
Create a new file, for example, `test_api.py`, and add the following code:

```python
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
```

## Step 4: Code Explanation
- **BASE_URL**: The base URL for the API we are testing.
- **`@pytest.fixture`**: Fixture that provides the base URL for tests.
- **`test_get_posts()`**: Test to verify fetching a list of posts.
- **`test_create_post()`**: Test to verify creating a new post.
- **`test_update_post()`**: Test to verify updating an existing post.
- **`test_delete_post()`**: Test to verify deleting a post.

Each test sends an HTTP request to the API and verifies that the response status code and data are correct.

## Step 5: Run the Tests
To run the tests, execute the following command in the terminal where `test_api.py` is located:

```bash
pytest test_api.py
```
- **`pytest`** will automatically find and execute all functions that start with `test_`.
- After running the tests, you will see a report with the test results.

## Step 6: Analyze Results
- If the tests pass, you will see a `PASSED` message.
- If a test fails, an error message will be displayed explaining why it failed. Analyze the issue and modify either the code or the test to fix it..

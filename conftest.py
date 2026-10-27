import pytest
from api.client import PostsApiClient

@pytest.fixture(scope="session")
def posts_client_get_all_posts():
    """фикстура только для чтения ответа и не должна его мутировать"""
    return PostsApiClient().get_all_posts()

@pytest.fixture(scope="session")
def posts_client_get_one_post():
    """фикстура только для чтения ответа и не должна его мутировать"""
    return PostsApiClient().get_post(1)

@pytest.fixture(scope="session")
def posts_client_get_one_nonexist_post():
    """фикстура только для чтения ответа и не должна его мутировать"""
    return PostsApiClient().get_post(9999)

@pytest.fixture(scope="session")
def posts_client_create_post():
    """фикстура только для чтения ответа и не должна его мутировать"""
    payload = {
        "userID": 133,
        "title": "my first post",
        "body": "nice body, beautiful body, greate body"
    }

    return PostsApiClient().create_post(payload)

@pytest.fixture(scope="session")
def posts_client_create_post_invalid_json():
    """фикстура только для чтения ответа и не должна его мутировать"""
    payload = "message"

    return PostsApiClient().create_post(payload)

@pytest.fixture
def mandatory_keys_and_data_types():
    mandatory_keys_and_data_types = {
        "userId": int,
        "id": int,
        "title": str,
        "body": str
    }

    return mandatory_keys_and_data_types
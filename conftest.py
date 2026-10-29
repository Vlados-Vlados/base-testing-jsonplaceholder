import pytest
from api.client import PostsApiClient, CommentsApiClient


# Posts
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


# Comments
@pytest.fixture(scope="session")
def comments_client_get_all_comments():
    return CommentsApiClient().get_all_comments()


@pytest.fixture(scope="session")
def comments_client_get_comment_of_post():
    return CommentsApiClient().get_comments_of_post(1)

@pytest.fixture(scope="session")
def comments_client_get_comment_of_nonexist_post():
    return CommentsApiClient().get_comments_of_post(9999)


@pytest.fixture(scope="session")
def comments_client_create_comment():
    payload = {
        "postId": 2,
        "name": "Best Friend",
        "email": "bestTest@email.com",
        "body": "if you want be nice, let's use old spice!"
    }
    return CommentsApiClient().create_comment(payload)

@pytest.fixture(scope="session")
def comments_client_create_comment_without_mandatory_key():
    payload = {
        "name": "Best Friend",
        "email": "bestTest@email.com",
        "body": "if you want be nice, let's use old spice!"
    }
    return CommentsApiClient().create_comment(payload)


# Data
@pytest.fixture
def posts_mandatory_keys_and_data_types():
    mandatory_keys_and_data_types = {
        "userId": int,
        "id": int,
        "title": str,
        "body": str
    }

    return mandatory_keys_and_data_types
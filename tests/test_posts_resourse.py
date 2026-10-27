import pytest

class TestsGetPostsList:
    @pytest.mark.positive
    def test_status_200(self, posts_client_get_all_posts):
        r = posts_client_get_all_posts

        assert  r.status_code == 200

    @pytest.mark.positive
    def test_body_is_filled(self, posts_client_get_all_posts):
        r = posts_client_get_all_posts

        assert any(r.json())

    @pytest.mark.positive
    def test_all_posts_have_mandatory_keys(self, posts_client_get_all_posts, mandatory_keys_and_data_types):
        mandatory_keys = set(mandatory_keys_and_data_types.keys())

        r = posts_client_get_all_posts

        for post in r.json():
            post_keys = set(post.keys())
            assert mandatory_keys.issubset(post_keys), (
                f"\nMissing mandatory keys: {mandatory_keys - post_keys} in post with id:{post["id"]}"
                )

    @pytest.mark.positive
    def test_all_posts_mandatory_keys_data_type(self, posts_client_get_all_posts, mandatory_keys_and_data_types):
        r = posts_client_get_all_posts

        for post in r.json():
            for key in post:
                try:
                    assert type(post[key]) == mandatory_keys_and_data_types[key]
                except KeyError:
                    continue

class TestGetOnePost:
    @pytest.mark.positive
    def test_status_200(self, posts_client_get_one_post):
        r = posts_client_get_one_post

        assert r.status_code == 200

    @pytest.mark.positive
    def test_body_have_id_of_post(self, posts_client_get_one_post):
        r = posts_client_get_one_post

        assert r.json()["id"] == 1

    @pytest.mark.negative
    def test_nonexistent_post(self, posts_client_get_one_nonexist_post):
        r = posts_client_get_one_nonexist_post

        assert r.status_code == 404

class TestCreatePost:
    @pytest.mark.positive
    def test_status_201(self, posts_client_create_post):
        r = posts_client_create_post

        assert r.status_code == 201

    @pytest.mark.positive
    def test_id_of_created_post(self, posts_client_create_post):
        r = posts_client_create_post

        assert r.json()["id"] == 101

    @pytest.mark.negative
    def test_status_code_invalid_json(self, posts_client_create_post_invalid_json):
        r = posts_client_create_post_invalid_json

        assert r.status_code == 500
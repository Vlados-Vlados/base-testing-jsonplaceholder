import pytest


class TestGetCommentsList:
    pass


class TestGetCommentsOfPost:
    @pytest.mark.positive
    def test_status_200(self, comments_client_get_comment_of_post):
        r = comments_client_get_comment_of_post

        assert r.status_code == 200

    @pytest.mark.positive
    def test_body_is_filled(self, comments_client_get_comment_of_post):
        r = comments_client_get_comment_of_post

        assert r.json()

    @pytest.mark.positive
    def test_all_comments_belong_to_post(self, comments_client_get_comment_of_post):
        r = comments_client_get_comment_of_post

        assert bool(r.json()) and all(comment["postId"] == 1 for comment in r.json())

    @pytest.mark.negative
    def test_comments_of_nonexist_post(self, comments_client_get_comment_of_nonexist_post):
        r = comments_client_get_comment_of_nonexist_post

        assert r.status_code == 200 # особенность поведения сервиса фальш апи. Данные коммента не возвращаются, он как бы не создан, но ответ успешный(статус код)
        assert not r.json()


class TestCreateComment:
    @pytest.mark.positive
    def test_status_201(self, comments_client_create_comment):
        r = comments_client_create_comment

        assert r.status_code == 201

    @pytest.mark.positive
    def test_id_of_created_comment(self, comments_client_create_comment):
        r = comments_client_create_comment

        assert r.json()["id"] == 501

    @pytest.mark.negative
    def test_without_mandatory_key(self, comments_client_create_comment_without_mandatory_key):
        r = comments_client_create_comment_without_mandatory_key

        assert r.status_code == 201 #тест с целю покрыть сервис негативными проверками. Но фактически, несмотря на отсутствие важного поля в запросе, сервис возвращает успешный ответ, тк это фальш Rest api

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
URL_POSTS = BASE_URL + "/posts"
URL_COMMENTS = BASE_URL + "/comments"


class PostsApiClient:
    def __init__(self):
        pass

    def url_post_id(self, id):
        return URL_POSTS + f"/{id}"

    def get_all_posts(self):
        r = requests.get(url=URL_POSTS, timeout=5)

        return r

    def get_post(self, id):
        r = requests.get(url=self.url_post_id(id), timeout=5)

        return r

    def create_post(self, payload: dict):
        r = requests.post(url=URL_POSTS, json=payload, timeout=5)

        return r

    def update_post(self, id):
        r = requests.put(url=self.url_post_id(id), timeout=5)

        return r

    def delete_post(self, id):
        r = requests.delete(url=self.url_post_id(id), timeout=5)

        return r


class CommentsApiClient:
    def __init__(self):
        pass

    def get_all_comments(self):
        r = requests.get(url=URL_COMMENTS, timeout=5)

        return r

    def get_comments_of_post(self, post_id):
        params = {"postId": post_id}
        r = requests.get(url=URL_COMMENTS, params=params, timeout=5)

        return r

    def create_comment(self, payload):
        r = requests.post(url=URL_COMMENTS, json=payload, timeout=5)

        return r

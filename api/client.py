import requests
BASE_URL = "https://jsonplaceholder.typicode.com"
URL_POSTS = BASE_URL + "/posts"

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

    def create_post(self, payload:dict):
        r = requests.post(url=URL_POSTS, json=payload, timeout=5)

        return r

    def update_post(self, id):
        r = requests.put(url=self.url_post_id(id), timeout=5)

        return r

    def delete_post(self, id):
        r = requests.delete(url=self.url_post_id(id), timeout=5)

        return r
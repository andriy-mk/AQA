# import requests module
import requests


class GitHub:

    def get_user(self, username):
        # making a get request (В тілі методу відправляється HTTP запит з методом GET на URL)
        request = requests.get(f"https://api.github.com/users/{username}")
        body = request.json()  # json content

        # return json content (Метод повертає тіло відповіді від сервера у форматі json)
        return body

    def search_repo(self, name):
        request = requests.get(
            "https://api.github.com/search/repositories", params={"q": name}
        )
        body = request.json()

        return body

import requests
import json
from json import JSONDecodeError
from VmLogin.error import ClientError, ServerError


class API(object):
    def __init__(self, token=None, base_url=None):
        self.token = token
        self.base_url = base_url
        self.session = requests.Session()

    def query(self, url_path, payload=None):
        return self.send_request("GET", url_path, payload=payload)

    def _dispatch_request(self, http_method):
        return {
            "GET": self.session.get,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "POST": self.session.post,
        }.get(http_method, "GET")

    def _handle_exception(self, response):
        status_code = response.status_code
        if status_code < 400:
            return
        if 400 <= status_code < 500:
            try:
                err = json.loads(response.text)
            except JSONDecodeError:
                raise ClientError(
                    status_code, None, response.text, None, response.headers
                )
            error_data = None
            if "data" in err:
                error_data = err["data"]
            raise ClientError(
                status_code, err["code"], err["msg"], response.headers, error_data
            )
        raise ServerError(status_code, response.text)

    def send_request(self, http_method, url_path, payload=None):
        if payload is None:
            payload = {}
        url = self.base_url + url_path
        payload["token"] = self.token
        if http_method == "GET":
            params = {
                "url": url,
                "params": payload,
            }
        else:
            params = {
                "url": url,
                "data": json.dumps(payload),
            }
        response = self._dispatch_request(http_method)(**params)
        self._handle_exception(response)
        try:
            data = response.json()
        except ValueError:
            data = response.text
        result = {}

        if len(result) != 0:
            result["data"] = data
            return result

        return data

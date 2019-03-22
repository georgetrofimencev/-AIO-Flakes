from aiohttp.web import Response
from ujson import encode


from server.apps.main.abstract.result import FlakesHTTPResponse
from config.config import load_config


conf = load_config()


class SessionManager:
    session_name = 'sessionid'

    def set(self,
            user_id: int,
            http_response: FlakesHTTPResponse or Response) -> None:
        session = self._gen_secret_session(user_id)
        http_response.set_cookie(
            SessionManager.session_name,
            value=session
        )

    def get(self):
        pass

    def reset(self, http_request):
        pass

    @staticmethod
    def _gen_secret_session(user_id: int, secret_key=conf['SECRET_FLAKES_KEY']):
        return encode({user_id, secret_key})


session_manager = SessionManager()

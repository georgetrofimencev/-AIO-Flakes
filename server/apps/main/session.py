from aiohttp.web import Response
from ujson import encode

from config.config import load_config


conf = load_config()


class SessionManager:
    session_name = 'sessionid'

    def set(self, http_response: Response, user_id) -> None:
        session = self._gen_secret_session(user_id)
        http_response.set_cookie(
            SessionManager.session_name,
            value=session
        )
        return http_response

    def get(self):
        pass

    def reset(self, http_request):
        pass

    @staticmethod
    def _gen_secret_session(user_id, secret_key=conf['SECRET_FLAKES_KEY']):
        return encode({user_id, secret_key})


session_manager = SessionManager()

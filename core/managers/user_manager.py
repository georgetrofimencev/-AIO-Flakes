from hashlib import sha256
from sqlalchemy.sql import select, insert, or_
from core.db.models import users

from config.settings import PASSWORD_SALT
from server.apps.main.abstract.result import FlakesErrorException


class UserManager:
    """Manager responsible for working with the "users" table entries"""
    def __init__(self, connection):
        self.connection = connection

    async def register_user(self, nickname: str, password: str, telegram_account=None,
                            tags: list = None, sources: list = None):
        """
        Create user row in "users" table with params.

        :param nickname: user nickname as string
        :param password:  password as string(will be hashed)
        :param telegram_account: telegram_account as string(not-required)
        :param tags: tags list as list(not-required)
        :param sources: sources list as list(not-required)
        :return: {
                UserId: record id of "users" table as string,
                UserInfo: data which contains user info as object
                }
        """
        await self._check_register_data_validity(nickname, telegram_account)
        password_hash = UserManager.\
            _generate_password_hash(password)
        query = insert(users).values(
            nickname=nickname,
            password_hash=password_hash,
            telegram_account=telegram_account,
            tags=tags,
            sources=sources
        )
        row = await self.connection.fetchrow(query)
        result = {
            "UserId": str(row),
            "UserInfo": {
                "nickname": nickname,
                "telegram_account": telegram_account
            }
        }
        return result

    async def login_user(self, nickname: str, password: str, *args, **kwargs):
        """
        :param nickname: nickname as a string
        :param password: password as a string

        :return:
            dict with "message" field which contains
            "User is auth" if user login data correctly
        """
        user_id = await self._check_user_validity(nickname, password)
        result = {
                "message": "User is auth",
                "user_id": user_id
            }
        return result

    async def _check_register_data_validity(self, nickname: str, telegram_account: str):
        query = select([users]).\
            where(or_(
                users.c.nickname == nickname,
                users.c.telegram_account == telegram_account)
        )
        if await self.connection.fetch(query):
            raise FlakesErrorException(
                -1,
                error_message=f'User with '
                f'nickname({nickname}) or '
                f'telegram account({telegram_account}) '
                f'already registered')
        return True

    async def _check_user_validity(self, nickname: str, password: str):
        query = select([users]).\
            where(users.c.nickname == nickname)
        record = await self.connection.fetchrow(query)
        if record:
            password_hash = record.get('password_hash')
            if self._check_password_hash(password, password_hash):
                return record.get('id')
            else:
                raise FlakesErrorException(
                    -1,
                    error_message=f'Incorrect password'
                )

        else:
            raise FlakesErrorException(
                -1,
                error_message=f'User with nickname'
                f'({nickname}) does not exist',
            )

    @staticmethod
    def _generate_password_hash(password):
        """
        Generate SHA256 hash for password.

        :param password: password as a string.
        """
        return sha256((password + PASSWORD_SALT).encode("utf-8")).hexdigest()

    def _check_password_hash(self, password, password_hash):
        return True if self._generate_password_hash(password) == password_hash else False

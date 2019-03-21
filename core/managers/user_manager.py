from hashlib import sha256
from sqlalchemy.sql import select, insert, or_
from core.db.models import users

from config.settings import PASSWORD_SALT
from server.apps.main.abstract.result import FlakesErrorException


class UserManager:
    """Manager responsible for working with the "users" table entries"""
    def __init__(self, connection):
        self.connection = connection

    @staticmethod
    def generate_password_hash(password):
        """
        Generate SHA256 hash for password.

        :param password: password as a string.
        """
        return sha256((password + PASSWORD_SALT).encode("utf-8")).hexdigest()

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
        await self._check_data_validity(nickname, telegram_account)
        password_hash = UserManager.\
            generate_password_hash(password)
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

    async def _check_data_validity(self, nickname: str, telegram_account: str):
        query = select([users]).where(or_(users.c.nickname == nickname,
                                          users.c.telegram_account == telegram_account))
        if await self.connection.fetchrow(query):
            raise FlakesErrorException(
                -1,
                error_message=f'User with nickname: {nickname} or '
                f'telegram_account: {telegram_account} already registered')
        return True

from sqlalchemy import Table, Column, Integer, String, JSON, Boolean
import sqlalchemy as sa


metadata = sa.MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, autoincrement=True, primary_key=True),
    Column("nickname", String(128), unique=True, index=True),
    Column("password_hash", String(256)),
    Column("telegram_account", String(128), unique=True, nullable=True),
    Column("telegram_notification", Boolean, default=False),
    Column("sources", JSON()),
    Column("tags", JSON()),
)



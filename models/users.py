import sqlalchemy
from sqlalchemy.dialects.sqlite import UUID

metadata = sqlalchemy.MetaData()
users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key = True),
    sqlalchemy.Column("email", sqlalchemy.String(50), unique=True, index=True)
)


import sqlalchemy
from sqlalchemy.dialects.sqlite import UUID

metadata = sqlalchemy.MetaData()
users_table = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key = True),
    sqlalchemy.Column("email", sqlalchemy.String(50), unique=True, index=True)
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("hashed_password", sqlalchemy.String()),
)

tokens_table = sqlalchemy.Table(
    "tokens",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("token", UUID(as_uuid=False), 
                    server_default=sqlalchemy.text("uuid_generate_v4()")
                    unique=True,
                    nullable=False,
                    index=True),
    sqlalchemy.Column("extpires", sqlalchemy.DateTime(),
    sqlalchemy.Column("user_id", sqlalchemy.ForeginKey("users.id")),
)
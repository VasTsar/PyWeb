import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Objects(SqlAlchemyBase):
    __tablename__ = 'objects'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    information = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    similar = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relationship('User')

import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



from .db_session import SqlAlchemyBase
from constants import DEFAULT_PROFILE_PHOTO

class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    src_avatar = sqlalchemy.Column(sqlalchemy.String, nullable=False, default=DEFAULT_PROFILE_PHOTO)
    warning_message_when_connecting_to_esp = sqlalchemy.Column(sqlalchemy.String, nullable=False, default="true")
    saved_algorithms = orm.relationship("Saved_algorithm", back_populates='user')
    devices = orm.relationship("Devices", back_populates='user')
    questions = orm.relationship("Question", back_populates='user')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
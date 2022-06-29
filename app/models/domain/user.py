from sqlalchemy import(
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.types import(
    Date,
    Boolean,
    Time,
    DateTime
)
from sqlalchemy.orm import(
    relationship,
    backref
)
from app.models.base import ModelBase
from app.core.database import Base
from datetime import datetime
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE



class User(ModelBase, Base):
    __tablename__ = "user"
    id = Column(GUID, primary_key=True, index=True, default=GUID_DEFAULT_SQLITE)
    user = Column(String(255))
    password = Column(String(255))
    active = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())


    @classmethod
    def add(cls, session, data):
        user = User()
        user.user = data.user
        user.password = data.password
        user.active = data.active
        session.add(user)
        session.commit()
        session.refresh(user)
        return User.find_by_id(session=session, id=user.id)


    @classmethod
    def check_login(cls, session, user, password):
        return session.query(
            cls.id,
            cls.user,
            cls.password,
            cls.active,
            cls.date_created
        ).filter(User.user == user, User.password == password).all()



    @classmethod
    def get_user(cls, session, user_id):
        return session.query(
            cls.id,
            cls.user,
            cls.password,
            cls.active,
            cls.date_created
        ).filter(User.id == user_id).all()


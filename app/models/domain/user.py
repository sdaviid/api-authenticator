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


import bcrypt



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
        hashed_password = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())
        user.user = data.user
        user.password = hashed_password
        user.active = data.active
        session.add(user)
        session.commit()
        session.refresh(user)
        return User.find_by_id(session=session, id=user.id)


    @classmethod
    def check_login(cls, session, user, password):
        try:
            temp_user_data = session.query(
                cls.id,
                cls.user,
                cls.password,
                cls.active,
                cls.date_created
            ).filter(User.user == user).one()
            if temp_user_data:
                hashed_password = bcrypt.checkpw(password.encode('utf-8'), temp_user_data.password.decode().encode('utf-8'))
                if hashed_password:
                    return temp_user_data
        except Exception as err:
            print(f'exception check login - {err}')
        return []




    @classmethod
    def get_user(cls, session, user_id):
        return session.query(
            cls.id,
            cls.user,
            cls.password,
            cls.active,
            cls.date_created
        ).filter(User.id == user_id).all()


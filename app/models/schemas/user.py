from datetime import date
from pydantic import Field
from datetime import datetime
from app.models.schemas.base import baseSchema
from uuid import UUID



class UserAdd(baseSchema):
    user: str
    password: str
    active: bool


class UserDetailData(baseSchema):
    id: UUID
    user: str
    password: str
    active: bool
    date_created: datetime


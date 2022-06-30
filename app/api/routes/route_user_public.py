from sqlalchemy.orm import Session
from fastapi import(
    Depends,
    Response,
    status,
    APIRouter
)


from app.models.domain.user import(
    User
)

from app.models.schemas.user import(
    UserDetailData,
    UserAdd
)

from app.core.database import get_db



router = APIRouter()


@router.post(
    '/add',
    status_code=status.HTTP_200_OK,
    response_model=UserDetailData
)
def add_user(data: UserAdd, response: Response, db: Session = Depends(get_db)):
    return User.add(session=db, data=data)

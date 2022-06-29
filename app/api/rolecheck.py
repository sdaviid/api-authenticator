from fastapi import(
    HTTPException,
    Depends
)
from typing import List
from app.models.domain.user import(
    User
)

from app.models.domain.roles import(
    Roles
)

from app.api.deps import(
    get_current_active_user
)
from app.core.database import(
    SessionLocal
)


class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles
        self.client_id = 'cli-web-general'

    def __call__(self, user: User = Depends(get_current_active_user)):
        if user:
            roles = Roles.check_roles_client_id(session=SessionLocal(), id_user=user.id, client_id=self.client_id)
            has_break = False
            for role in roles:
                if role.value in self.allowed_roles:
                    continue
                else:
                    has_break = True
            if has_break == True:
                raise HTTPException(status_code=403, detail="Operation not permitted")

from fastapi import Form
from typing import Optional

class EmailPasswordRequestForm:
    def __init__(
        self,
        email: str = Form(...),
        password: str = Form(...),
        client_id: Optional[str] = Form(None),
        client_secret: Optional[str] = Form(None),
    ):
        self.username = email # alias for compatibility
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret

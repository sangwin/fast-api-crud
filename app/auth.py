from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.database import users_db

# ======================
# CONFIG
# ======================
SECRET_KEY = "CHANGE_THIS_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Use Argon2 only
pwd_context = CryptContext(
    schemes=["argon2"],
    deprecated="auto"
)

# ======================
# PASSWORD HELPERS
# ======================
def hash_password(password: str) -> str:
    """
    Hash password using Argon2.
    - No length limit
    - Memory-hard
    - OWASP recommended
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password using Argon2.
    """
    return pwd_context.verify(plain_password, hashed_password)

# ======================
# AUTH HELPERS
# ======================
def authenticate_user(email: str, password: str):
    for user in users_db:
        if user["email"] == email:
            # ✅ MUST use verify_password (NOT pwd_context.verify directly)
            if verify_password(password, user["password"]):
                return user
    return None

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    for user in users_db:
        if user["email"] == email:
            return user

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

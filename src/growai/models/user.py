from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from growai.db.session import Base


class User(Base):
    __tablename__ = "users"          # name of the "tab"

    id: Mapped[int] = mapped_column(primary_key=True)   # unique number per user
    email: Mapped[str] = mapped_column(String(255), unique=True)
    display_name: Mapped[str] = mapped_column(String(100))
    timezone: Mapped[str] = mapped_column(String(50), default="Europe/Berlin")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
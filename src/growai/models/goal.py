from datetime import date, datetime

from sqlalchemy import ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from growai.db.session import Base


class Goal(Base):
	__tablename__ = "goals"

	id: Mapped[int] = mapped_column(primary_key=True)
	user_id: Mapped[int] = mapped_column(ForeignKey("users.id")) # whose goal
	title: Mapped[str] = mapped_column(String(200))
	focus_area: Mapped[str] = mapped_column(String(50)) # Health, Career, Mind, Money
	description: Mapped[str | None] = mapped_column(Text) # optional
	target_date: Mapped[date | None] # optional deadline
	status: Mapped[str] = mapped_column(String(20), default="active")
	created_at: Mapped[datetime] = mapped_column(server_default=func.now())
import datetime

from typing import Optional, Annotated

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column, declared_attr
from database import Base, str_256
import enum


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[
    datetime.datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.datetime.utcnow)
]





class WorkersOrm(Base):
    __tablename__ = "workers"

    # id: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[intpk]
    username: Mapped[str] # = mapped_column()


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesOrm(Base):
    __tablename__ = "resumes"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str_256]
    compensation: Mapped[int | None] # = mapped_column(nullable=True)
    workload = Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    # created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())")) # из сервера
    # # created_at: Mapped[datetime.datetime] = mapped_column(defoult=text("TIMEZONE('utc', now())")) # из python
    # updated_at: Mapped[datetime.datetime] = mapped_column(
    #     server_default=text("TIMEZONE('utc', now())"),
    #     onupdate=datetime.datetime.utcnow
    # )
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


metadata_obj = MetaData()


#
# worekers_table = Table(
#     "workers",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("username", String),
# )


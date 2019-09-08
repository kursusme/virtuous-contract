from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.models.user import UserType


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String)
    nickname = Column(String, index=True)
    full_name = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    birthdate = Column(Date)
    address = Column(String, index=True)
    postal_code = Column(Integer, index=True)
    phone_number = Column(Integer, index=True)
    user_type = Column(Enum(UserType))
    date_created = Column(DateTime(timezone=True))
    date_updated = Column(DateTime(timezone=True))

    country_id = Column(Integer, ForeignKey("country.id"))
    province_id = Column(Integer, ForeignKey("province.id"))
    city_id = Column(Integer, ForeignKey("city.id"))
    district_id = Column(Integer, ForeignKey("district.id"))
    subdistrict_id = Column(Integer, ForeignKey("subdistrict.id"))

    country = relationship("City", back_populates="users")
    province = relationship("Province", back_populates="users")
    city = relationship("City", back_populates="users")
    district = relationship("District", back_populates="users")
    subdistrict = relationship("Subdistrict", back_populates="users")
    staff = relationship("Employee", uselist=False, back_populates="user")
    student = relationship("Student", uselist=False, back_populates="user")
    tutor = relationship("Tutor", uselist=False, back_populates="user")

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(String, index=True)

    provinces = relationship("Province", back_populates="countries")


class Province(Base):
    __tablename__ = "province"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    country_id = Column(Integer, ForeignKey("country.id"))

    country = relationship("Country", back_populates="provinces")
    cities = relationship("City", back_populates="province")


class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    province_id = Column(Integer, ForeignKey("province.id"))

    province = relationship("Province", back_populates="cities")
    districts = relationship("District", back_populates="city")


class District(Base):
    __tablename__ = "district"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    city_id = Column(Integer, ForeignKey("city.id"))

    city = relationship("City", back_populates="districts")
    subdistrict = relationship("Subdistrict", back_populates="district")


class Subdistrict(Base):
    __tablename__ = "subdistrict"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    district_id = Column(Integer, ForeignKey("district.id"))

    district = relationship("District", back_populates="subdistricts")

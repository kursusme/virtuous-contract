from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    domain = Column(String, index=True)
    date_created = Column(DateTime(timezone=True))
    date_updated = Column(DateTime(timezone=True))

    branches = relationship("Branch", back_populates="company")


class CompanyBranch(Base):
    __tablename__ = "company_branch"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    postal_code = Column(Integer, index=True)
    phone_number = Column(Integer, index=True)

    country_id = Column(Integer, ForeignKey("country.id"))
    province_id = Column(Integer, ForeignKey("province.id"))
    city_id = Column(Integer, ForeignKey("city.id"))
    district_id = Column(Integer, ForeignKey("district.id"))
    subdistrict_id = Column(Integer, ForeignKey("subdistrict.id"))
    company_id = Column(Integer, ForeignKey("company.id"))

    country = relationship("City", back_populates="companies")
    province = relationship("Province", back_populates="companies")
    city = relationship("City", back_populates="companies")
    district = relationship("District", back_populates="companies")
    subdistrict = relationship("Subdistrict", back_populates="companies")
    company = relationship("Company", back_populates="branches")


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    company_branch_id = Column(Integer, ForeignKey("company_branch.id"))

    company_branch = relationship("CompanyBranch", back_populates="departments")
    staff = relationship("Employee", back_populates="department")


class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, index=True)

    department_id = Column(Integer, ForeignKey("department.id"))

    department = relationship("Department", back_populates="staff")

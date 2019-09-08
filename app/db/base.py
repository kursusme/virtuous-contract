# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.db_models.company import Company, CompanyBranch, Department, Employee  # noqa
from app.db_models.location import (  # noqa
    City,
    Country,
    District,
    Province,
    Subdistrict,
)
from app.db_models.user import User  # noqa

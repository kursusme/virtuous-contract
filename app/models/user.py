from enum import Enum


class UserType(int, Enum):
    staff = 1
    tutor = 2
    student = 3

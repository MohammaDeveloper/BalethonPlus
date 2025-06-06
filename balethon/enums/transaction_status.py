from enum import auto

from .name_enum import NameEnum


class TransactionStatus(NameEnum):
    PENDING = auto()
    SUCCEED = auto()
    FAILED = auto()
    REJECTED = auto()
    TIMEOUTE = auto()
    
from enum import auto

from .name_enum import NameEnum


class TransactionStatus(NameEnum):
    FAILED = auto()
    PENDING = auto()
    PAID = auto()
    REJECTED = auto()
    SUCCEED = auto()
    TIMEOUT = auto()
    
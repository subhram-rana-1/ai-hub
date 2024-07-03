from ai_hub.enums import DjangoEnum


class ActionEnum(str, DjangoEnum):
    CLOSE_SLOT = 'CLOSE_SLOT'
    REVIEW = 'REVIEW'
    UNKNOWN = 'UNKNOWN'

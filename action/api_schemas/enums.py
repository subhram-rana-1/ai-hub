from ai_hub.enums import DjangoEnum


class ActionType(str, DjangoEnum):
    CLOSE_SLOT = 'CLOSE_SLOT'
    REVIEW = 'REVIEW'
    UNKNOWN = 'UNKNOWN'

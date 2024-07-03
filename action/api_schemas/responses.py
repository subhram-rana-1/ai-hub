from typing import List

from action.api_schemas.enums import ActionType


class NextAction:
    def __init__(
            self,
            field_asked: str,
            msg: str,
    ):
        self.field_asked = field_asked
        self.msg = msg


class ActionExecutionResponse:
    def __init__(
            self,
            action: ActionType,
            fields: dict,
            next_action: NextAction,
    ):
        self.action = action
        self.fields = fields
        self.next_action = next_action

    def to_dict(self) -> dict:
        return {
            'action': self.action,
            'fields': self.fields,
            'next_action': self.next_action,
        }


class UserInputRefinementResponse(ActionExecutionResponse):
    pass

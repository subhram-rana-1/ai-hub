from action.api_schemas.enums import ActionEnum


class ActionExecutionRequest:
    def __init__(
            self,
            action: ActionEnum,
    ):
        self.action = action

    def to_dict(self) -> dict:
        return {
            'action': self.action,
        }
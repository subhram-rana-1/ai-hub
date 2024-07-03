from action.api_schemas.enums import ActionType
from action.api_schemas.responses import NextAction
from ai_hub.gpt.client import gpt_client


class UserInputValidator:
    def __init__(self):
        self.gpt_client = gpt_client

    def validate(
            self,
            action: ActionType,
            fields: dict,  # user provided input fields
    ) -> NextAction:
        ...

from action.action_to_fields_mappings import ACTION_TO_FIELD_MAPPING
from action.user_input_validator import UserInputValidator
from ai_hub.gpt.client import gpt_client


class UserPromptProcessor:
    def __init__(self):
        self.gpt_client = gpt_client
        self.action = None
        self.fields = None
        self.next_action = None
        self.action_field_mappings = ACTION_TO_FIELD_MAPPING
        self.validator = UserInputValidator()

    def process_prompt(self, prompt: str):
        """After processing prompt set action, fields, next_action fields
        and return the object"""
        # todo:
        #  1. call gpt api and define the action (which is the HUB api)
        #  2. use action->fields mappings to find fields and call gpt api to fill those fields from user given prompt
        #  3. Use validator to decide what to instruct user to do next
        #  4. Fill action, fields, next_action fields and return the object
        return self


def new_user_prompt_processor() -> UserPromptProcessor:
    return UserPromptProcessor()

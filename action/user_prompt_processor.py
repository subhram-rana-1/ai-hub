from ai_hub.gpt.client import gpt_client


class UserPromptProcessor:
    def __init__(self):
        self.gpt_client = gpt_client
        self.action = None
        self.fields = None
        self.next_action = None

    def process_prompt(self):
        """After processing prompt set action, fields, next_action fields
        and return the object"""

        return self


user_prompt_processor = UserPromptProcessor()

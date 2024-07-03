from marshmallow import Schema, fields


class ActionExecutionRequestSchema(Schema):
    user_prompt = fields.String(load_from="user_prompt", required=True)


class ActionExecutionRequest:
    def __init__(self, data):
        self.user_prompt = data["user_prompt"]

    @classmethod
    def deserialize_from_json(cls, json):
        data = ActionExecutionRequestSchema(strict=True).load(json).data
        return ActionExecutionRequest(data)

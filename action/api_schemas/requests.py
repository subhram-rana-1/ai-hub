from marshmallow import Schema, fields


class ActionExecutionRequest(Schema):
    input = fields.Integer(load_from="user_prompt", required=True)


class ActionExecutionRequest:
    def __init__(self, data):
        self.input = data["user_prompt"]

    @classmethod
    def deserialize_from_json(cls, json):
        data = ActionExecutionRequest(strict=True).load(json).data
        return ActionExecutionRequest(data)

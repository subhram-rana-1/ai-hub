from marshmallow import Schema, fields

from action.api_schemas.enums import ActionType


class ActionExecutionRequestSchema(Schema):
    user_prompt = fields.String(load_from="user_prompt", required=True)


class ActionExecutionRequest:
    def __init__(self, data: dict):
        self.user_prompt = data["user_prompt"]

    @classmethod
    def deserialize_from_json(cls, json):
        data = ActionExecutionRequestSchema(strict=True).load(json).data
        return ActionExecutionRequest(data)


class UserInputPayloadSchema(Schema):
    action = fields.String(load_from="action", required=True)
    fields = fields.Dict(load_from="fields", required=True)


class ActionRefinementRequestSchema(Schema):
    payload = fields.Nested(UserInputPayloadSchema, many=False, required=True)


class UserInputPayload:
    def __init__(self, data: dict):
        self.action = data['action']
        self.fields = data['fields']


class ActionRefinementRequest:
    def __init__(self, data: dict):
        self.payload = UserInputPayload(data)

    @classmethod
    def deserialize_from_json(cls, json):
        data = ActionRefinementRequestSchema(strict=True).load(json).data
        return ActionRefinementRequest(data)

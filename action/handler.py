import json

from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from action.api_schemas.requests import ActionExecutionRequest
from action.api_schemas.responses import ActionExecutionResponse
from action.user_prompt_processor import UserPromptProcessor
from action.user_prompt_processor import user_prompt_processor


class ActionHandler:
    def __init__(self):
        prompt_processor = UserPromptProcessor()

    @staticmethod
    @require_POST
    @csrf_exempt
    def execute(
            request: HttpRequest,
            *args,
            **kwargs
    ) -> JsonResponse:
        json_body = json.loads(request.body)
        action_request: ActionExecutionRequest =\
            ActionExecutionRequest.deserialize_from_json(json_body)

        # call gpt api
        prompt_processor: UserPromptProcessor =\
            user_prompt_processor.process_prompt(action_request.user_prompt)

        return JsonResponse(ActionExecutionResponse(
            action=prompt_processor.action,
            fields=prompt_processor.fields,
            next_action=prompt_processor.next_action,
        ).to_dict())

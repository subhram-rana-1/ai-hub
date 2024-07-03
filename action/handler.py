import json

from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from action.api_schemas.requests import ActionExecutionRequest


class ActionHandler:
    @staticmethod
    @require_POST
    @csrf_exempt
    def execute(
            request: HttpRequest,
            *args,
            **kwargs
    ) -> JsonResponse:
        json_body = json.loads(request.body)
        action_request: ActionExecutionRequest.deserialize_from_json(json_body)
        # todo: add logic
        return JsonResponse('anything', safe=False)

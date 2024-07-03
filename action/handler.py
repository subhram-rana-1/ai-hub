import json

from django.views.decorators.http import require_POST
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt


class ActionHandler:
    @staticmethod
    @require_POST
    @csrf_exempt
    def execute(
            request: HttpRequest,
            *args,
            **kwargs
    ) -> JsonResponse:
        json_body: dict = json.loads(request.body)
        # todo: add logic
        return JsonResponse(json_body)

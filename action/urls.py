from django.urls import path

from action.handler import ActionHandler

urlpatterns = [
    path(
        'actions',
        ActionHandler.execute,
        name='execute-action'),
    ]

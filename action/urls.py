from django.urls import path

from action.handler import ActionHandler

urlpatterns = [
    path(
        'actions/execute',
        ActionHandler.execute,
        name='execute-action',
    ),

    path(
        'actions/refine',
        ActionHandler.refine,
        name='execute-action'
    ),

    ]

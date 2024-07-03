from action.api_schemas.requests import ActionRefinementRequest
from action.api_schemas.responses import UserInputRefinementResponse


class UserInputRefiner:
    def refine(
            self,
            user_input_request: ActionRefinementRequest,
    ) -> UserInputRefinementResponse:
        """read the fields and their values, whatever is not present currate those
        and then as per field-prioritisation construct the next_action and return it"""
        pass

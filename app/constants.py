from app.response_objects import ResponseSuccess, ResponseFailure

STATUS_CODES = {
    ResponseSuccess.SUCCESS: 200,
    ResponseFailure.RESOURCE_ERROR: 404,
    ResponseFailure.PARAMETERS_ERROR: 400,
    ResponseFailure.SYSTEM_ERROR: 500
}

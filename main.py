def function_cicd(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object.
    """

    request_json = request.get_json(silent=True)

    if request.args and 'message' in request.args:
        return request.args.get('message')

    elif request_json and 'message' in request_json:
        return request_json['message']

    else:
        return 'Function - 1 with V1.0 with CI/CD Pipeline'

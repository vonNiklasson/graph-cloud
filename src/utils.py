from flask import escape


def get_parameter(request, name: str, default=None):
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and name in request_json:
        val = request_json[name]
    elif request_args and name in request_args:
        val = request_args[name]
    else:
        return default

    return format(escape(val))

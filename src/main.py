from flask import escape
from utils import get_parameter
from Worker import Worker

from extended_networkx_tools import Analytics


def hello_world(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))


def generate_graph(request):
    node_count = int(get_parameter(request, 'node_count', 10))
    optimizer = get_parameter(request, 'optimizer')

    worker = Worker(node_count=node_count, optimizer=optimizer)
    graph = worker.solve()

    return 'Convergence rate: {}'.format(str(Analytics.convergence_rate(graph)))

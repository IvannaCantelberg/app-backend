from flask import Blueprint

bp = Blueprint('smoke', __name__, url_prefix='/smoke')


@bp.route('/', methods=['GET'])
def smoke():
    return {'message': 'Ok'}

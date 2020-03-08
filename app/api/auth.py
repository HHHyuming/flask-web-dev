from flask import request
from functools import wraps

from werkzeug.exceptions import HTTPException


def auth_decorate(func):
    """
    鉴权：user
    :param func:
    :return:
    """
    print(func.__name__)
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(request.args)
        username = request.args.get('username')
        if not username:
            # error_data = {'code': 10011, 'msg': 'validation failed', 'data':[]}
            raise HTTPException('validation failed')
            # return error_data
        return func(*args, **kwargs)
        # acct = basic_authentication()  # custom account lookup function

        # if acct:
        #     return func(*args, **kwargs)
        # flask_restful.abort(401)
    return wrapper
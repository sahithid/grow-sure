from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify

#from the jwt documentation 
# https://flask-jwt-extended.readthedocs.io/en/stable/custom_decorators.html

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_admin"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admin only!"), 403

        return decorator

    return wrapper

def manager_required(): 
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_manager"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Store Manager only!"), 403

        return decorator

    return wrapper
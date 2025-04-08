from functools import wraps
from flask import render_template
from sqlalchemy.exc import IntegrityError


def htmx_error_handler(status_code=400):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            try:
                return view_func(*args, **kwargs)
            except Exception as e:
                msg = str(e.args[0]) if e.args else str(e)
                if isinstance(e, IntegrityError):
                    msg = "Entry already exists"

                return render_template(
                    "partials/message.html", message=msg
                ), status_code

        return wrapper

    return decorator

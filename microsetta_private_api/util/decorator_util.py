import inspect


def has_non_keyword_arguments(func):
    sig = inspect.signature(func)
    params = sig.parameters
    for p in params:
        if params[p].kind != inspect.Parameter.KEYWORD_ONLY:
            return True

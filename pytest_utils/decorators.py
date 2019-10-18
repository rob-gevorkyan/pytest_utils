from functools import wraps

#Decorator for setting the max score of a test
def max_score(max_score):
    def wrapper(f):
        f.max_score = max_score
        return f
    return wrapper

class partial_credit(object):
    """Decorator that indicates that a test allows partial credit
    Usage: @partial_credit(test_weight)
    Then, within the test, set the value by calling
    kwargs['set_score'] with a value. You can make this convenient by
    explicitly declaring a set_score keyword argument, eg.
    ```
    @partial_credit(10)
    def test_partial(set_score=None):
        set_score(4.2)
    ```
    """

    def __init__(self):
        pass
        #self.weight = weight

    def __call__(self, func):
        #func.__weight__ = self.weight

        def set_score(x):
            wrapper.score = x

        @wraps(func)
        def wrapper(*args, **kwargs):
            kwargs['set_score'] = set_score
            return func(*args, **kwargs)

        return wrapper

#Optional decorator for setting the visibility of a test
#Options: 'visible', 'hidden', 'after_due_date', 'after_published'
def visibility(visibility):
    def wrapper(f):
        f.visibility = visibility
        return f
    return wrapper

#Optional decorator for adding extra tags to a test
#Should be an array of strings
def tags(tags):
    def wrapper(f):
        f.tags = tags
        return f
    return wrapper

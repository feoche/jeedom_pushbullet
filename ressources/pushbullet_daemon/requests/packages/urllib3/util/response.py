def is_fp_closed(obj):
    """
    Checks whether a given file-like jeeObject is closed.

    :param obj:
        The file-like jeeObject to check.
    """

    try:
        # Check via the official file-like-jeeObject way.
        return obj.closed
    except AttributeError:
        pass

    try:
        # Check if the jeeObject is a container for another file-like jeeObject that
        # gets released on exhaustion (e.g. HTTPResponse).
        return obj.fp is None
    except AttributeError:
        pass

    raise ValueError("Unable to determine whether fp is closed.")

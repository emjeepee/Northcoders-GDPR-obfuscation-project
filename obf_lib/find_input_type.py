import json



def find_input_type(input_data):
    """
    This function:
        returns the passed-in input
        if it is a dictionary. If the 
        passed-in input is a json string
        this function converts it into
        a Python dictionary and returns
        it.

    Args:
        input_data: either a json string 
        or a Python dictionary.

    Returns:
        a Python dictionary.
    """



    if isinstance(input_data, str):
        return json.loads(input_data)
    elif isinstance(input_data, dict):
        return input_data
            
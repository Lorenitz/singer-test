import os


def get_env(env_var):
    """
    If key is missing, the program will raise the EnvironmentError with a traceback
    showing where the error occured. 
    """
    value = os.getenv(env_var)
    if not value:
        # Raise an EnvironmentError if Key is missing
        raise EnvironmentError(f"{env_var} is not set. Please set it on the environment.")
    return value


def get_config(name, dictionary):
    """
    If key is missing in the dictionary, the program will raise KeyError the with a traceback
    showing where the error occured. 
    """
    try:
        value = dictionary[name]
        return value
    except KeyError:
        # Raise an KeyError if Key is missing
        raise KeyError(f"{name} was not found in config. Only the following keys were found: {str(dictionary.keys())}")
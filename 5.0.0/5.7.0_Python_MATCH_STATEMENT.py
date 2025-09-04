""" 5.7.0_Python_MATCH_STATEMENT """

# ---------

# The match statement provides a way to perform pattern matching
#  It allows for pattern matching against the structure of the data.
#   Takes an expression and compares its value 
#    To successive patterns given as one or more case blocks

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
print(http_error(404))  # Not found
print(http_error(418))  # I'm a teapot
print(http_error(500))  # Something's wrong with the internet

# ----------
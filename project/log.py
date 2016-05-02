DEBUG = False

def error(tag, message):
    """
    Displays an error message beginning with "ERROR ..."

    Arguments:
    tag -- A unique tag that shows where the error occured (like e.g. 'PlayerPosCalc')
    message -- The error message to show.
    """
    print("ERROR [  " + tag + "  ]  --  " + message)

def info(tag, message):
    """
    Shows some information beginning with "INFO ..."

    Arguments:
    tag -- A unique tag that shows where the output came from (like e.g. 'PlayerPosCalc')
    message -- The information that should be displayed.
    """
    print("INFO  [  " + tag + "  ]  --  " + message)

def debug(tag, message):
    """
    This shows the given message but only when the DEBUG flag is set.

    Arguments:
    tag -- A unique tag that shows where the debug output came from (like e.g. 'PlayerPosCalc')
    message -- The information that should be displayed.
    """
    if DEBUG:
        print("DEBUG [  " + tag + "  ]  --  " + message)

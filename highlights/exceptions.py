"""Custom human-readable exceptions
"""


class ImproperConfiguration(Exception):
    """Missing or invalid config variable
    """


class InvalidLink(Exception):
    """invalid link for download
    """


class Abort(Exception):
    """Raise this error to stop further execution of program
    """


class NotAutomated(Exception):
    """Raise error if oauth 2.0 browser login required"""

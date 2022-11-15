"""Basic Flow class
"""


class BasicFlow:
    """Manages overall program flow

    Simple synchronous implementation, no saving result of work into DB
    Static usage of components (highlighter, merger, uploader)"""

    def __init__(self, logger, config):
        self.logger = logger
        self.config = config

    def run(self, **kwargs):
        """Main entry point into flow
        """
        # initialization of components

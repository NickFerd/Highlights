"""Basic Flow class
"""


class BasicFlow:
    """Manages overall program flow

    Simple synchronous implementation"""

    def __init__(self, workflow_config, engine):
        self.config = workflow_config
        self.engine = engine

    def execute(self, **kwargs):
        """Main entry point into flow
        """


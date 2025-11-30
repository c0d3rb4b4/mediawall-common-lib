"""Dispatcher logic for the mediawall-vss-dispatcher service."""


class Dispatcher:
    """Dispatcher class that handles message dispatching."""
    
    def __init__(self, rabbitmq_config: dict, vss_config: dict, global_config: dict):
        """Initialize the Dispatcher.
        
        Args:
            rabbitmq_config: Configuration for RabbitMQ broker.
            vss_config: Configuration for VSS (Video Streaming Service).
            global_config: Global service configuration.
        """
        self.rabbitmq_config = rabbitmq_config
        self.vss_config = vss_config
        self.global_config = global_config
    
    def run(self):
        """Run the dispatcher service."""
        # TODO: Implement dispatcher logic
        print("Dispatcher service started")

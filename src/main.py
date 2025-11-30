"""Main entry point for the mediawall-vss-dispatcher service."""

import yaml
from pathlib import Path

from dispatcher.logic import Dispatcher


def load_config(config_path: str) -> dict:
    """Load configuration from a YAML file.
    
    Args:
        config_path: Path to the YAML configuration file.
        
    Returns:
        Dictionary containing the configuration.
    """
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def main():
    """Main function to initialize and run the dispatcher service."""
    # Load configuration files
    rabbitmq_config = load_config('/config/broker/rabbitmq.yaml')
    vss_config = load_config('/config/vss/vss.yaml')
    global_config = load_config('/config/services/global.yaml')
    
    # Initialize and run the dispatcher
    dispatcher = Dispatcher(
        rabbitmq_config=rabbitmq_config,
        vss_config=vss_config,
        global_config=global_config
    )
    dispatcher.run()


if __name__ == '__main__':
    main()

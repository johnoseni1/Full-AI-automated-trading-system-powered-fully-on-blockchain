from typing import Any, Dict

from aitrade.enums import RunMode


def start_webserver(args: Dict[str, Any]) -> None:
    """
    Main entry point for webserver mode
    """
    from aitrade.configuration import Configuration
    from aitrade.rpc.api_server import ApiServer

    # Initialize configuration
    config = Configuration(args, RunMode.WEBSERVER).get_config()
    ApiServer(config, standalone=True)

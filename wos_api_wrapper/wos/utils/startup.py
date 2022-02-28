from wos_api_wrapper.wos.utils.config_manager import ConfigManager


config_manager = ConfigManager()
try:
    config = config_manager.get_or_create_config()
    API_KEY = config.get('Authentication', 'APIKey')
except EOFError:
    pass

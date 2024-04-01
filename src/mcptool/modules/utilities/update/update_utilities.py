import requests

from loguru import logger

from ..constants import VERSION


class UpdateUtilities:
    @staticmethod
    @logger.catch
    def update_available():
        """
        Method to check if an update is available

        Returns:
            bool: True if an update is available, False otherwise
        """

        try:
            response = requests.get(f'https://raw.githubusercontent.com/wrrulos/MCPTool/development/settings.json')
            
            if response.status_code != 200:
                return False
            
            settings = response.json()
            return settings['version'] != VERSION
        
        except Exception as e:
            logger.warning(f'Error checking for updates: {e}')
            return False

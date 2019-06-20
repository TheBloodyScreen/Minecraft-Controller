import yaml
import yaml.scanner
from bloodyterminal import btext

config = dict()

try:
    with open("config/config.yml", "r") as f:
        try:
            btext.info('Loading config.yml')
            config = yaml.safe_load(f) or {}
            btext.success('config.yml loaded successfully!')

        except yaml.scanner.ScannerError as e:
            raise Exception("Configuration file at 'config/config.yml' contains invalid YAML...")

        except Exception as e:
            print(type(e))

except FileNotFoundError as e:
    raise Exception("Configuration file not found at: 'config/config.yml'...")

import os
import yaml
from dotenv import load_dotenv


def load_config():
    load_dotenv()

    with open("configs/config.yaml") as f:
        content = f.read()

    for key, value in os.environ.items():
        content = content.replace(f'${{{key}}}', value)

    config = yaml.safe_load(content)
    
    return config

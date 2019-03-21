import yaml
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
DEFAULT_MODE = BASE_DIR / 'modes' / 'development.yaml'


def load_config(mode: str = None):
    with open(DEFAULT_MODE.parent / f'{mode}.yaml' if mode else DEFAULT_MODE) as conf:
        config = yaml.load(conf)
    return config

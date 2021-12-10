from typing import Optional
import yaml


def get_path(yml_file: str) -> Optional[str]:
    """
    reads the yaml fil and  extracts the db path
    """
    try:
        with open(yml_file, 'r') as f_stream:
            return yaml.safe_load(f_stream).get('DB_PATH')
    except yaml.YAMLError:
        return



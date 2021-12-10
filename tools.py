from typing import Optional
import yaml


def rvg_timer(fnc):
    import time

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        output = fnc(*args, **kwargs)
        end_time = time.perf_counter()
        total_perf_time = round(end_time-start_time,5)
        print(f'Function {fnc.__name__} took {total_perf_time} seconds to perform.')
        return output
    return wrapper


def log_params(fnc):
    def wrapper(*args, **kwargs):
        list_args = []
        try:
            args_filtered = [arg for arg in args if not str(arg).startswith('<')]
            list_args.extend(args_filtered)
            list_args.extend(kwargs)
        except ValueError:
            pass
        print(f'Function {fnc.__name__} was provided the args - {list_args}')
        return fnc(*args, **kwargs)
    return wrapper


@log_params
@rvg_timer
def get_path(yml_file: str) -> Optional[str]:
    """
    reads the yaml fil and  extracts the db path
    """
    try:
        with open(yml_file, 'r') as f_stream:
            return yaml.safe_load(f_stream).get('DB_PATH')
    except yaml.YAMLError:
        return




import os
from platform import platform

def parse_home_dir(dirname, filename):
    platform_os = platform()
    if platform_os.startswith('Linux'):
        return '{}/{}/{}'.format(os.path.expanduser("~"), dirname, filename)
    elif platform_os.startswith('Windows'):
        return '{0}\{1}\{2}'.format(os.path.expanduser("~"), dirname, filename)

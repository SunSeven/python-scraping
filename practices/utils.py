import os
from platform import platform

def parse_home_dir(logname):
    platform_os = platform()
    if platform_os.startswith('Linux'):
        return '{}/log/{}'.format(os.path.expanduser("~"), logname)
    elif platform_os.startswith('Windows'):
        return '{0}\log\\{1}'.format(os.path.expanduser("~"), logname)

if __name__ == '__main__':
    parse_home_dir('error.log')
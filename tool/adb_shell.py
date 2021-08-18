#!/usr/bin/python
from core.read_config import config
import os


def clear_app():
    os.system('adb shell pm clear com.sgkt.phone')


def install_app():
    app_path = os.path.join(config.BASE_DIR, 'app', 'tzkt.apk')
    print(app_path)
    os.system('adb install -r {}'.format(app_path))


# if __name__ == '__main__':
    # install_app()
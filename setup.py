# -*- coding: utf-8 -*-
import os
import sys
import subprocess


# config
ENV_NAME = '.venv'
REQUIREMENTS_NAME = 'requirements.txt'


def create_virtual_environment():
    version_info = sys.version_info
    python_version = 'python{}.{}'.format(version_info.major, version_info.minor)
    interpreter = sys.executable if sys.executable else python_version

    # venv exist
    env_path = os.path.join(ENV_NAME)
    if os.path.exists(env_path):
        print(f"virtual environment '{ENV_NAME}(base: {python_version})' has been created.")
        return
    subprocess.check_call([interpreter, '-m', 'venv', ENV_NAME])
    print(f"virtual environment '{ENV_NAME}(base: {python_version})' created.")


def install_dependencies():
    bin_path = os.path.join(ENV_NAME, 'bin')
    if not os.path.exists(bin_path): bin_path = os.path.join(ENV_NAME, 'Scripts')
    interpreter_path = os.path.join(bin_path, 'python')
    pip_path = os.path.join(bin_path, 'pip')

    # upgrade pip version
    subprocess.check_call([interpreter_path, '-m', 'pip', 'install', '--upgrade', 'pip'])

    # install requirements packages
    if os.path.isfile(REQUIREMENTS_NAME):
        subprocess.check_call([pip_path, 'install', '-r', REQUIREMENTS_NAME])
        pip_list = subprocess.check_output([interpreter_path, '-m', 'pip', 'list', '--format=freeze'], text=True)

        with open(REQUIREMENTS_NAME, 'w') as f:
            f.write(pip_list)
    else:
        print(f"{REQUIREMENTS_NAME} file not found. skipping dependencies installation.")


if __name__ == '__main__':
    create_virtual_environment()
    install_dependencies()
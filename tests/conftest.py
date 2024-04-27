import subprocess
import os
import pytest
import logging

@pytest.fixture(scope='session', autouse=True)
def configure_logging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.fixture(scope="session", autouse=True)
def set_env():
    # Replace 'your-command' with the actual command to produce the environment variables
    # For example: 'printenv' or a script that prints 'key=value' lines
    command = ["nuv", "-config", "-dump"]
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout

    # Parse the output and set environment variables
    for line in output.splitlines():
        try:
            key, value = line.split('=', 1)
            os.environ[key] = value
            #print("OK:", key)
        except:
            print("ERR:", line)

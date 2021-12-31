import os
import subprocess
import re

base_dir = __file__
for x in range(3):
    base_dir = os.path.dirname(base_dir)
docker_dir = os.path.join(base_dir, 'docker')

container_name = "vault_vault_1"


def run_dev_vault():
    command = ["docker-compose", "-f", "docker-compose-dev.yml", "up", "-d"]
    subprocess.check_call(command, cwd=docker_dir)


def stop_dev_vault():
    command = ["docker-compose", "-f", "docker-compose-dev.yml", "down"]
    subprocess.check_call(command, cwd=docker_dir)


def get_dev_logs():

    command = ["docker-compose", "-f", "docker-compose-dev.yml", "logs", "--no-color"]
    return subprocess.check_output(command, cwd=docker_dir).decode("utf8")


def get_prod_logs():

    command = ["docker-compose", "-f", "docker-compose-prod.yml", "logs", "--no-color"]
    return subprocess.check_output(command, cwd=docker_dir).decode("utf8")

def get_credentials(logs):
    
    unseal_key = re.search("Unseal Key: (\S+)", logs, re.MULTILINE).groups()[0]
    root_token = re.search("Root Token: (\S+)", logs, re.MULTILINE).groups()[0]
    
    return {"unseal_key": unseal_key, "root_token": root_token}

if __name__ == "__main__":
    from pprint import pprint

    # run_dev_vault()
    # stop_dev_vault()
    logs = get_dev_logs()
    pprint(get_credentials(logs))

from ruamel.yaml import YAML

yaml = YAML()


def get_yaml(yaml_path):
    with open(yaml_path, "r") as f_yaml:
        yaml_data = yaml.load(f_yaml)
    return yaml_data


def get_default_config():
    default_config_path = "./default.yaml"
    default_config = get_yaml(default_config_path)
    return default_config[default_config["env"]]

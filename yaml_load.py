import yaml

def load_config(path: str):
    with open(path, "r", encoding="utf-8") as f:
        # ❌ Unsafe loader on old PyYAML
        return yaml.load(f)  # no Loader specified

if __name__ == "__main__":
    # Example config
    print(load_config("config.yaml"))
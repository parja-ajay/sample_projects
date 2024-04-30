class ConfigReader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_params = self.read_config()

    def read_config(self):
        with open(self.config_file, 'r') as f:
            config_params = {}
            for line in f:
                key, value = line.strip().split('=')
                config_params[key.strip()] = value.strip()
        return config_params

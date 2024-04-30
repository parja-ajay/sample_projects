import pandas as pd

class DataProcessing:
    def __init__(self, config_params):
        self.config_params = config_params

    def calculate_temperature(self, job_length, complexity):
        temperature_log = []
        initial_temp = float(self.config_params['initial_temp'])
        initial_time = float(self.config_params['initial_time'])

        if complexity == 'simple':
            temp = float(self.config_params['simple_temp'])
            time = float(self.config_params['simple_time'])
        elif complexity == 'average':
            temp = float(self.config_params['average_temp'])
            time = float(self.config_params['average_time'])
        elif complexity == 'hard':
            temp = float(self.config_params['hard_temp'])
            time = float(self.config_params['hard_time'])

        for _ in range(abs(int(job_length // time))):
            temperature_log.append({'time': initial_time, 'temperature': initial_temp})
            initial_temp += temp
            initial_time += time

        return pd.DataFrame(temperature_log)

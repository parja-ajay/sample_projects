from config_reader import ConfigReader
from file_handler import FileHandler
from data_processing import DataProcessing
import pandas as pd

def main():
    # Read config
    config_reader = ConfigReader('config.txt')
    config_params = config_reader.config_params

    # Read input file
    file_handler = FileHandler(config_params['input_file_location'], config_params['output_file_location'])
    df = file_handler.read_csv()

    # Calculate temperature
    temp_calculator = DataProcessing(config_params)
    temp_log = []
    for index, row in df.iterrows():
        temp_log.append(temp_calculator.calculate_temperature(row['Job Length (mins)'], row['Job Complexity']))
    temp_df = pd.concat(temp_log)

    # Write to output file
    file_handler.write_csv(temp_df)

if __name__ == "__main__":
    main()

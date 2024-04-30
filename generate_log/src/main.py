# main.py
import pandas as pd
import datetime
from data_processing import process_job

# Function to read properties from the config file
def read_config(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key.strip()] = value.strip()
    return config

# Function to main process
def main():
    # Read config file
    config = read_config('config.txt')
    
    # Read input CSV file
    input_file = config['input_file_location']
    df = pd.read_csv(input_file)
    
    # Initialize temperature log dataframe
    temp_log = pd.DataFrame(columns=['time', 'temperature'])
    
    # Process each row in the dataframe
    for index, row in df.iterrows():
        temp, time = process_job(row, config)
        if temp and time:
            temp_log = pd.concat([temp_log, pd.DataFrame({'time': time, 'temperature': temp})])
    
    # Get current timestamp
    curr_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    # Write temperature log to CSV file
    output_file = f"{config['output_file_location']}/temperature_{curr_timestamp}.log"
    temp_log.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()

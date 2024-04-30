import pandas as pd

class FileHandler:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_csv(self):
        return pd.read_csv(self.input_file)

    def write_csv(self, df):
        df.to_csv(self.output_file, index=False)

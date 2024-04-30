# data_processing.py

# Function to process job complexity
def process_job(row, config):
    job_length = row['Job Length (mins)']
    job_complexity = row['Job Complexity']
    
    # Determine temperature and time parameters based on job complexity
    if job_complexity == 'simple':
        temp_param = float(config['simple_temp'])
        time_param = float(config['simple_time'])
    elif job_complexity == 'average':
        temp_param = float(config['average_temp'])
        time_param = float(config['average_time'])
    elif job_complexity == 'hard':
        temp_param = float(config['hard_temp'])
        time_param = float(config['hard_time'])
    else:
        return None
    
    # Calculate temperature and time logs
    quotient = abs(job_length / time_param)
    temp_log = []
    time_log = []
    initial_temp = float(config['initial_temp'])
    initial_time = float(config['initial_time'])
    
    for _ in range(int(quotient)):
        out_temp = initial_temp + temp_param
        temp_log.append(out_temp)
        initial_temp = out_temp
        
        out_time = initial_time + time_param
        time_log.append(out_time)
        initial_time = out_time
        
    return temp_log, time_log

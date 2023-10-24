from datetime import datetime

today = datetime.now()

data_time = today.strftime('%Y-%m-%d-%H-%M-%S')

print(data_time)
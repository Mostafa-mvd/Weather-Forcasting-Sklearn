import os
import platform


all_column_names = ['T', 'TM', 'Tm', 'SLP', 'H', 
                    'PP', 'VV', 'V', 'VM', 'VG', 
                    'RA', 'SN', 'TS', 'FG']

feature_columns = ['TM', 'Tm', 'SLP', 'H', 'PP',
                    'VV', 'V', 'VM', 'VG', 'RA', 
                    'SN', 'TS', 'FG']

os_type = platform.system()

if os_type == 'Windows':
    separator = "\\"
else:
    separator = "/"

csv_main_file_path = f"{os.path.dirname(__file__)}{separator}weather_parameters_data.csv"
csv_predicted_file_path = f"{os.path.dirname(__file__)}{separator}predicted_weather_parameters.csv"

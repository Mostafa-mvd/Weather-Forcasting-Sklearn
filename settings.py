import os
import platform


# weather_parameters --------------------------------------------

# all_column_names = ['T', 'TM', 'Tm', 'H', 'PP', 'VV', 'V', 'VM']

# feature_columns = ['TM', 'Tm', 'H', 'PP', 'VV', 'V', 'VM']


# weather_aqi_parameters ---------------------------------------------------------------------

all_column_names = ['O3', 'CO', 'NO', 'NO2', 'Nox', 'SO2', 'PM10', 'PM2.5']

feature_columns = ['CO', 'NO', 'NO2', 'Nox', 'SO2', 'PM10', 'PM2.5']


os_type = platform.system()

if os_type == 'Windows':
    separator = "\\"
else:
    separator = "/"


#‌ csv_main_file_path = f"{os.path.dirname(__file__)}{separator}weather_parameters.csv"

csv_main_file_path = f"{os.path.dirname(__file__)}{separator}weather_aqi_parameters.csv"

csv_predicted_file_path = f"{os.path.dirname(__file__)}{separator}predicted_parameters.csv"

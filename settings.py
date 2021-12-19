import os
import platform


os_type = platform.system()

if os_type == 'Windows':
    separator = "\\"
else:
    separator = "/"



# required_columns is for getting features and target.
# feature_columns have to be selected from required_columns.

# weather_parameters --------------------------------------------

required_columns = ['T', 'TM', 'Tm', 'SLP', 'H', 'PP', 'VV',
                    'V', 'VM', 'VG', 'RA', 'SN', 'TS', 'FG']


feature_columns = ['TM', 'Tm', 'SLP', 'H', 'PP', 'VV', 'V', 
                   'VM', 'VG', 'RA', 'SN', 'TS', 'FG']


csv_main_file_path = f"{os.path.dirname(__file__)}{separator}weather_parameters.csv"

# weather_aqi_parameters ---------------------------------------------------------------------

# required_columns = ['O3', 'CO', 'NO', 'NO2', 'Nox', 'SO2', 'PM10', 'PM2.5']

# feature_columns = ['CO', 'NO', 'NO2', 'Nox', 'SO2', 'PM10', 'PM2.5']


# csv_main_file_path = f"{os.path.dirname(__file__)}{separator}weather_aqi_parameters.csv"


# predicted_parameters ---------------------------------------------------------------------

csv_predicted_file_path = f"{os.path.dirname(__file__)}{separator}predicted_parameters.csv"


# predicting parameters in weather forcasting


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


import settings
import utils


if __name__ == "__main__":

    # Level 1 --------------------------------------------------------------

    weather_df_with_nan_value = utils.get_dataframe(
        settings.csv_main_file_path, 
        settings.required_columns)
    
    # Level 2 --------------------------------------------------------------

    weather_df_without_nan_value = utils.replace_nan_value_with_mean(
        weather_df_with_nan_value, settings.required_columns)

    # Level 3 --------------------------------------------------------------

    features_df = weather_df_without_nan_value[utils.get_features()][1:]
    target_df = weather_df_without_nan_value[utils.get_target()][1:]

    # Level 4 --------------------------------------------------------------

    features_train, features_test, \
    target_train, target_test = train_test_split(
        features_df, 
        target_df, 
        test_size=10)

    # Level 5 --------------------------------------------------------------

    scaler = StandardScaler()
    scaler.fit(features_train)
    scaled_features_train = scaler.transform(features_train)
    scaled_features_test = scaler.transform(features_test)

    # Level 6 --------------------------------------------------------------

    model = utils.get_mlp_regressor_obj()

    utils.fit(
        scaled_features_train,
        target_train.values.ravel(),
        model)

    # Level 7 --------------------------------------------------------------

    y_predicted = model.predict(scaled_features_test)

    # Level 8 --------------------------------------------------------------

    score = utils.calculating_regr_score(target_test, y_predicted)

    # Level 9 --------------------------------------------------------------
    
    data = utils.join_data(
        features_test.values, 
        y_predicted,
        target_df.name)

    # Level 10 --------------------------------------------------------------

    utils.csv_writer(
        data,
        settings.csv_predicted_file_path,
        score)

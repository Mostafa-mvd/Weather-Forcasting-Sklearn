
# predicting parameters in weather forcasting


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


import settings
import utils


if __name__ == "__main__":

    # Level 1 --------------------------------------------------------------

    laptop_df = utils.get_dataframe(
        settings.csv_main_file_path, 
        settings.all_column_names)

    # Level 2 --------------------------------------------------------------

    features_df = laptop_df[utils.get_features()][1:]
    target_df = laptop_df[utils.get_target()][1:]

    # Level 3 --------------------------------------------------------------

    features_train, features_test, \
    target_train, target_test = train_test_split(
        features_df, 
        target_df, 
        test_size=10)

    # Level 4 --------------------------------------------------------------

    scaler = StandardScaler()
    scaler.fit(features_train)
    scaled_features_train = scaler.transform(features_train)
    scaled_features_test = scaler.transform(features_test)

    # Level 5 --------------------------------------------------------------

    model = utils.get_mlp_regressor_obj()
    # model = utils.get_mlp_classifier_obj()

    utils.fit(
        scaled_features_train,
        target_train.values.ravel(),
        model)

    # Level 6 --------------------------------------------------------------

    y_predicted = model.predict(scaled_features_test)

    # Level 7 --------------------------------------------------------------

    score = utils.calculating_regr_score(target_test, y_predicted)
    # score = utils.calculating_classification_accuracy(target_test, y_predicted)

    # Level 8 --------------------------------------------------------------
    
    data = utils.join_data(
        features_test.values, 
        y_predicted,
        target_df.name)

    # Level 9 --------------------------------------------------------------

    utils.csv_writer(
        data,
        settings.csv_predicted_file_path,
        score)

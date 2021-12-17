
# predicting parameters in weather forcasting


from sklearn.model_selection import train_test_split
from sklearn import metrics

import settings
import utils


if __name__ == "__main__":

    laptop_df = utils.get_dataframe(
        settings.csv_main_file_path, 
        settings.all_column_names)

    features_df = laptop_df[utils.get_features()][1:]
    target_df = laptop_df[utils.get_target()][1:]

    features_train, features_test, \
    target_train, target_test = train_test_split(
        features_df, 
        target_df, 
        test_size=10)

    model = utils.get_linear_regression_obj()
    # model = utils.get_decision_tree_obj()
    # model = utils.get_mlp_classifier_obj()
    # model = utils.get_mlp_regressor_obj()

    utils.fit(
        features_train, 
        target_train, 
        model)

    y_predicted = model.predict(features_test)

    # classification accuracy, best possible 100 %
    # score = utils.calculating_classification_accuracy(target_test, y_predicted)

    #regression score, best possible 100 %
    score = utils.calculating_regr_score(target_test, y_predicted)

    # mlp models score, best possible 100 %
    # score = utils.calculating_mlp_score(features_test, target_test, model)

    data = utils.join_data(
        features_test.values, 
        y_predicted,
        target_df.name)

    utils.csv_writer(
        data,
        settings.csv_predicted_file_path,
        score)

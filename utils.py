import csv
from sklearn import metrics

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

import settings


def get_features():
    return settings.feature_columns


def get_target():
    target = set(settings.all_column_names) - set(settings.feature_columns)

    if len(target) == 1:
        return target.pop()

    raise Exception("size of your target list must be 1")


def join_data(x_test_arr, y_pred, target_name):
    data = list()
    feature_columns = get_features()

    for idx_i, features_arr in enumerate(x_test_arr):
        dict_data = dict()

        for idx_j, feature in enumerate(features_arr):
            dict_data[feature_columns[idx_j]] = feature

        dict_data[target_name] = '{:.2f}'.format(float(y_pred[idx_i]))
        data.append(dict_data)
    
    return data


def get_dataframe(file_path, columns):
    return pd.read_csv(
        filepath_or_buffer=file_path, header=None,
        names=columns, encoding='latin-1')


def get_linear_regression_obj():
    return LinearRegression()


def get_decision_tree_obj():
    return DecisionTreeClassifier()


def get_mlp_classifier_obj():
    return MLPClassifier(hidden_layer_sizes=50, activation='identity', solver='adam',
                         max_iter=500, learning_rate='adaptive', learning_rate_init=0.001,
                         random_state=42)


def get_mlp_regressor_obj():
    return MLPRegressor(hidden_layer_sizes=6, activation='identity', solver='adam',
                        max_iter=100, learning_rate='adaptive', learning_rate_init=0.001,
                        random_state=42)


def fit(x_train, y_train, model_obj):
    model_obj.fit(x_train, y_train)


def calculating_classification_accuracy(y_test, y_pred):
    return "{:.3f}%".format(metrics.accuracy_score(y_test, y_pred)*100)


def calculating_regr_score(y_test, y_pred):
    return "{:.3f}%".format(metrics.r2_score(y_test, y_pred)*100)


def calculating_mlp_score(x_test, y_test, mlp_model):
    return "{:.3f}%".format(mlp_model.score(x_test, y_test)*100)


def accuracy_line(accuracy):
    accuracy_row = ['-' for _ in range(len(settings.all_column_names))]
    accuracy_row.append(accuracy)

    return accuracy_row


def csv_writer(data, path, accuracy=''):
    with open(file=path, mode="w", encoding="latin-1") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')

        head_row = [*settings.all_column_names] + ["Accuracy"]

        writer.writerow(head_row)
        writer.writerow(accuracy_line(accuracy))

        for dict_data in data:
            line = list()
            
            for col_key in settings.all_column_names:
                line.append(dict_data[col_key])

            writer.writerow(line)

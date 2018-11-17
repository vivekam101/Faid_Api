from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier

def build_model(data_frame, feature_columns, target):
    return build_random_forest(data_frame, feature_columns, target)

def build_linear_svc(data_frame, feature_columns, target):
    clf = SVC(kernel="linear", C=0.025)
    clf.fit(data_frame[feature_columns], data_frame[target])
    return clf

def build_knn(data_frame, feature_columns, target):
    clf = KNeighborsClassifier(2)
    clf.fit(data_frame[feature_columns], data_frame[target])
    return clf

def build_decision_tree(data_frame, feature_columns, target):
    clf = DecisionTreeClassifier(max_depth=5)
    clf.fit(data_frame[feature_columns], data_frame[target])
    return clf

def build_random_forest(data_frame, feature_columns, target):
    clf = RandomForestClassifier(n_estimators=10)
    clf.fit(data_frame[feature_columns], data_frame[target])
    return clf
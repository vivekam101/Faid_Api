from sklearn.metrics import accuracy_score

def get_accuracy(model, test_set, feature_columns, target):
    return accuracy_score(test_set[target], model.predict(test_set[feature_columns]))

def get_probablity(model, lead, expected_class):
    print("modelling")
    prob = model.predict_proba(lead)
    # prob = 1.0
    cls_ = model.predict(lead)
    # _cls=1
    # print(prob,cls_)
    classes_ = model.classes_
    index = classes_.tolist().index(expected_class)
    return cls_[0], prob[0, index]
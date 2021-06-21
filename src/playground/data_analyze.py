import pandas as pd

from sklearn.datasets import load_breast_cancer
import numpy as np

import xgboost as xgb
from sklearn.model_selection import cross_validate,cross_val_predict, StratifiedKFold

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target
X_cols = cancer.feature_names
 
splits = 5
skf = StratifiedKFold(n_splits=splits, shuffle=True, random_state=42)
score_funcs = ["accuracy","precision_macro","recall_macro","f1_macro"]
 
clf = xgb.XGBClassifier(objective="binary:logistic")
 
score = cross_validate(clf, X, y, cv=skf, scoring=score_funcs,return_estimator=True)
 
print(score["test_accuracy"].mean())
print(score["test_precision_macro"].mean())
print(score["test_recall_macro"].mean())
print(score["test_f1_macro"].mean())

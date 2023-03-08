import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pickle
import dvc.api
import sys

# input_file = sys.argv[1]
# output_file = sys.argv[2]


# def train_and_evaluate_models(X_train, X_test, y_train, y_test):
# Define the list of classifiers to evaluate
classifiers = [LogisticRegression(), DecisionTreeClassifier(), RandomForestClassifier(), KNeighborsClassifier(),
               GradientBoostingClassifier()]

# Create an empty dictionary to store the scores for each classifier
scores = {}

# Loop through each classifier and train it on the training data, then test it on the testing data and store the score
for clf in classifiers:
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    score = accuracy_score(y_test, y_pred)
    scores[clf.__class__.__name__] = score

# Find the classifier with the highest score
best_clf = max(scores, key=scores.get)

# Print the results
print("Best classifier:", best_clf)
print("Accuracy score:", scores[best_clf])
best_accuracy = scores[best_clf]

# Log the best model and its accuracy
with dvc.api.open('best_model.pkl', 'wb') as file:
    pickle.dump(best_clf, file)

with dvc.api.open('best_accuracy.txt', 'w') as file:
    file.write(str(best_accuracy))

    # return best_clf, best_accuracy

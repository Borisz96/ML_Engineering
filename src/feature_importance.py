import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import pickle
import dvc.api
import sys
import matplotlib.pyplot as plt
import numpy as np
from train import *

# Calculate feature importances
importances = best_clf.feature_importances_

# Sort feature importances in descending order
indices = np.argsort(importances)[::-1]

# Rearrange feature names so they match the sorted feature importances
names = [feature_cols[i] for i in indices]

# Create plot
plt.figure()

# Add title
plt.title("Feature Importance")

# Add bars
plt.bar(range(X_train[feature_cols].shape[1]), importances[indices])

# Add feature names as x-axis labels
plt.xticks(range(X_train[feature_cols].shape[1]), names, rotation=90)

# Show plot
plt.show()
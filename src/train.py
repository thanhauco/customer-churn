from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
def train(X, y):
    model = RandomForestClassifier()
    model.fit(X, y)
    return model
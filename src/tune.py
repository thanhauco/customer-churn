from sklearn.model_selection import GridSearchCV
def tune(model, params, X, y):
    grid = GridSearchCV(model, params)
    grid.fit(X, y)
    return grid.best_estimator_
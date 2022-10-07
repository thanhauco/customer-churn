import shap
def explain(model, data):
    explainer = shap.TreeExplainer(model)
    return explainer.shap_values(data)
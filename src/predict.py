import pickle
def predict(model_path, data):
    with open(model_path, 'rb') as f: model = pickle.load(f)
    return model.predict(data)
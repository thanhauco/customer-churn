from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
def preprocess(df):
    imputer = SimpleImputer()
    scaler = StandardScaler()
    return scaler.fit_transform(imputer.fit_transform(df))
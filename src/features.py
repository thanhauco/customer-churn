def add_features(df):
    df['total_spend'] = df['monthly_spend'] * df['tenure']
    return df
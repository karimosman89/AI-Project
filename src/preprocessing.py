import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)
    
    # Perform preprocessing (e.g., scaling numerical features)
    scaler = StandardScaler()
    df[['feature1', 'feature2']] = scaler.fit_transform(df[['feature1', 'feature2']])
    
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data('data/raw/data.csv', 'data/processed/processed_data.csv')

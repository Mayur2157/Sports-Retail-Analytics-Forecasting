import pandas as pd
from scipy.stats import pearsonr

df = pd.read_csv('correlation_data.csv')
corr, _ = pearsonr(df['revenue'], df['review_count'])
print(f'Correlation: {corr}')

import pandas as pd

city = 'Shanghai'
df = pd.read_csv(f'{city}/{city}_centerline.csv')

print(df)

df = df.drop(columns=[" w_tr_right_m", ' w_tr_left_m'], axis=1)
df['z_m'] = 0

df.to_csv(f'./{city}/center_line.csv', index=False, header=False)
print(df)
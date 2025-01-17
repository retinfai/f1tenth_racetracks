import pandas as pd
import os

# iterate through all the directories and run this function

def create_centerline(city):
    city = city.replace(' ', '_')
    if city.startswith('.'):
        return
    
    if city == 'Mexico_City':
        df = pd.read_csv(f'{city}/MexicoCity_centerline.csv', encoding='latin-1')
    else:
        df = pd.read_csv(f'{city}/{city}_centerline.csv')

    print(df)

    df = df.drop(columns=[" w_tr_right_m", ' w_tr_left_m'], axis=1)
    df['z_m'] = 0
    
    df = df.iloc[::3, :]

    df.to_csv(f'./{city}/center_line_third.csv', index=False, header=False)
    print(df)

def create_goalpositions(city):
    city = city.replace(' ', '_')
    if city.startswith('.'):
        return
    
    if city == 'Mexico_City':
        df = pd.read_csv(f'{city}/MexicoCity_centerline.csv', encoding='latin-1')
    else:
        df = pd.read_csv(f'{city}/{city}_centerline.csv')

    # print(df)

    df = df.drop(columns=[" w_tr_right_m", ' w_tr_left_m'], axis=1)

    df = df.iloc[::3, :]

    df['goal_position'] = df.apply(lambda row: (row['# x_m'], row[' y_m']), axis=1)
    df = df['goal_position']
    # df = pd.DataFrame.from_dict({'goal_positions': df['goal_position'].values})
    print(df)
    df.to_json(f'./{city}/goal_positions.json', orient='records', indent=0)


directories = os.listdir('./')

for directory in directories:
    if os.path.isdir(directory):
        create_goalpositions(directory)

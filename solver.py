import pandas as pd
import numpy as np

df2 = pd.DataFrame(np.array([["", "", 7,5,"",9,"",3,""], 
                             ["", 8, 9,"",2,"","","",6], 
                             ["", 1, "",8,"",6,9,7,""],
                            [7,"",5,"",6,"","",8,""],
                            ["","",8,9,"",5,6,"",""],
                            ["",6,"","",1,8,"","",9],
                            ["",7,"","","","","",1,""],
                            [8,"","","",5,"",2,9,""],
                            ["",5,"",1,"",2,4,"",7]]),
                   columns=[i for i in range(1,10)],
                  index=[i for i in range(1,10)])b

def get_row(df,row):
    list_ = list(set(df.loc[row]))
    return [int(i) for i in list_ if i !=""]

def get_column(df,col):
    list_ = list(df[col])
    return [int(i) for i in list_ if i !=""]

def get_block(df,row,col):
    return 1

def get_options(x,y):
    x.extend(y)
    in_play = list(set(x))
    options = [i for i in range(1,10) if i not in in_play]
    return len(options)

def options_finder(df,row,col):
    if df[col][row] !="":
        return None
    else:
        return get_options(get_row(df,row),get_column(df,col))
    
def get_options_2(x,y):
    x.extend(y)
    in_play = list(set(x))
    options = [i for i in range(1,10) if i not in in_play]
    return options
    
def fetch_value(df,row,col):
    if df[col][row] !="":
        return None
    else:
        return get_options_2(get_row(df,row),get_column(df,col))[0]

def create_options_df(df):
    df_output = pd.DataFrame(index=[i for i in range(1,10)], columns=[i for i in range(1,10)])
    for row in range(1,10):
        for col in range(1,10):
            df_output[col][row]=options_finder(df,row,col)
    return df_output

def location_finder(df,value):
    output = []
    for row in range(1,10):
        for col in range(1,10):
            if df[col][row] ==value:
                output.append([row,col])
    return output


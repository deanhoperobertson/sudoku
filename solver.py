import pandas as pd
import numpy as np
import math

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
                   index=[i for i in range(1,10)])

def roundup(x):
    '''
    Rounds down coordonate the closest block limit

    Args:
        x: (int) input coordinate

    Returns:
        int: rouded down value
    '''
    if x ==1 : return 3
    else:  return int(math.ceil(x / 3.0)) * 3

def rounddown(x):
    '''
    Rounds up coordonate the closest block limit

    Args:
        x: (int) input coordinate

    Returns:
        int: rouded up value
    '''
    if x%3 ==0: return x-2
    else: 
        val = round(x - (x%3.5))
        if val ==0: return 1 
        else: return val

def get_block(df,row,col):
    '''
    Fetches all the numbers in a given 3x3 block

    Args:
        df: (pandas.Dataframe) sudoku dataframe
        row: (int) row number
        col: (int) col number

    Returns:
        list: all the numbers in a block
    '''
    output=[]
    for c in range(rounddown(col),roundup(col)+1):
        for r in range(rounddown(row),roundup(row)+1):
            output.append(df2[c][r])
    return [int(i) for i in output if i !=""]

def options_finder(df,row,col):
    '''
    Find the missing values at a specific coordinate

    Args:
        df: (pandas.Dataframe) sudoku dataframe
        row: (int) row number
        col: (int) col number

    Returns:
        int: number of potential values at gint point

    '''
    if df[col][row] !="":
        return None
    else:
        rows = [int(i) for i in list(set(df.loc[row])) if i !=""]
        cols = [int(i) for i in list(df[col]) if i !=""]
        block = get_block(df,row,col)
        
        rows.extend(cols)
        rows.extend(block)
        options = [i for i in range(1,10) if i not in list(set(rows))]
        return len(options)

    
def fetch_value(df,row,col):
    '''
    Find the value at specific coordinate

    Args:
        df: (pandas.Dataframe) sudoku dataframe
        row: (int) row number
        col: (int) col number

    Returns:
        int: value
    '''
    if df[col][row] !="":
        return None
    else:
        rows = [int(i) for i in list(set(df.loc[row])) if i !=""]
        cols = [int(i) for i in list(df[col]) if i !=""]
        block = get_block(df,row,col)
        
        rows.extend(cols)
        rows.extend(block)
        options = [i for i in range(1,10) if i not in list(set(rows))]
        return options[0]

def create_options_df(df):
    '''
    Create value options matrix

    Args:
        df: (pandas.Dataframe) sudoku dataframe

    Returns:
        dataframe: matrix with options in each cell
    '''

    df_output = pd.DataFrame(index=[i for i in range(1,10)], columns=[i for i in range(1,10)])
    for row in range(1,10):
        for col in range(1,10):
            df_output[col][row]=options_finder(df,row,col)
    return df_output

def location_finder(df):
    '''
    Find the location of cells whihc has only 1 possible option

    Args:
        df: (pandas.Dataframe) sudoku dataframe

    Returns:
        list: coordinates of cells
    '''
    output = []
    for row in range(1,10):
        for col in range(1,10):
            if df[col][row] ==1:
                output.append([row,col])
    return output

def solve(df):
    '''
    Solves the sudoku puzzle

    Args:
        df: (pandas.Dataframe) sudoku dataframe

    Returns:
        df: solved puzzle
    '''
    action = True
    while action == True:
        coords=location_finder(create_options_df(df))
        if coords:
            for i in coords:
                row = i[0]
                col = i[1]
                val = fetch_value(df,row,col)
                df[col][row] = val
        else:
            break
    return df

print(solve(df2))
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
                   columns=[i for i in range(0,9)],
                   index=[i for i in range(0,9)])

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
    
    x_start, y_start = 3*(row//3), 3*(col//3)
    x_end, y_end = x_start + 3, y_start + 3
    
    for c in range(y_start,y_end):
        for r in range(x_start,x_end):
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

    df_output = pd.DataFrame(index=[i for i in range(0,9)], columns=[i for i in range(0,9)])
    for row in range(0,9):
        for col in range(0,9):
            df_output[col][row]=options_finder(df,row,col)
    return df_output

def location_finder(df,value):
    '''
    Find the location of cells whihc has only 1 possible option

    Args:
        df: (pandas.Dataframe) sudoku dataframe

    Returns:
        list: coordinates of cells
    '''
    output = []
    for row in range(0,9):
        for col in range(0,9):
            if df[col][row] ==value:
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
        coords=location_finder(create_options_df(df),1)
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
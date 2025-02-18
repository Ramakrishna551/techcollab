import pandas as pd
#creation of dataframe using dictionary
dic={'fruits':['apples','banana','mangoes'],'count':[12,20,30]}
df= pd.DataFrame(dic,index=['a','b','c'])
print(df)
print(" ")
#creating dataframe using list 
data =[1,2,3,4]
df1=pd.DataFrame(data)
print(df1)
print(" ")
#cha ged index of dataframe  in list 
d=[1,2,3,4]
series =pd.Series(d)
print(series)
print(" ")
series=pd.Series(d,index=['a','b','c','d'])
print(series)

#creationof dataframe  using series 
series = pd.Series([6,12],index=['a','b'])
df = pd.DataFrame(series)
print(df)

import numpy as np
numpyarray=np.array([[50000,60000],['john','james']])
df=pd.DataFrame({'name':numpyarray[1],'salary':numpyarray[0]})
print(df)

#Merge operation 
player=['player1','player2','player3']
point=[8,9,10]
title=['Game1','Game2','Game3']
df1=pd.DataFrame({'Player':player,'Point':point,'Title':title})
print(df1)

import pandas as pd
player=['player1','player2','player3']
point=[8,9,10]
title=['Game1','Game2','Game3']
df1=pd.DataFrame({'Player':player,'Point':point,'Title':title})
print(df1)
print(" ")
player=['Player1','player5','playe6']
power =['punch','kick','Elbow']
title=['Game1','Game5','Game6']
df2=pd.DataFrame({'Player':player,'Power':power,'Title':title})
print(df2)

print(" ")

#inner merge --in common using Title attribute
print(df1.merge(df2,on='Title',how='inner'))
print(" ")
#inner merge using common i.e Player attribute 
#print(df1.merge(df2, on='Player',how='inner'))
h = df1.merge(df2,on='Player',how='inner')
print(h)
print(" ")

print(df1.merge(df2))

print(" ")
#left merge 
print(df1.merge(df2,on='Player',how='left'))

print(" ")
#right merge
print(df1.merge(df2,on='Player',how='right'))

print(" ")
#Outer merge
# whenever the value is not common then print NaN
print(df1.merge(df2,on='Player',how='outer')) 

print(" ")
#how to perform join operation in pandas 
player=['player1','player5','player6']
power=['punch','kick','elbow']
titles=['Game1','Game5','Game6']
df3=pd.DataFrame({'Player':player,'Power':power,'Titles':titles},index=['L1','L2','L3'])
print(df3)
print(" ")
player=['player1','player5','player6']
power=['punch','kick','elbow']
titles=['Game1','Game5','Game6']
df4=pd.DataFrame({'Player':player,'Power':power,'Titles':titles},index=['L2','L3','L4'])
print(df4)

print(" ")
# print(df3.join(df4,how='inner'))#error
# print(df3.join(df4,how='left'))#error
#moudle 5 
#problems
#1. Write a function that takes start and end of a range returns a pandas series
# object containing numbers within that range.
# In case the user does not pass start or end or both they should default to 1
# and 10 respectively. E.g:
# -> range_series() -> Should Return a pandas series from 1 to 10
# range_series(5) -> Should Return a pandas series from 5 to 10
# range_series(5, 10) -> Should Return a pandas series from 5 to 15

#Create a method that takes n NumPy arrays of the same dimensions,
#sums them and returns the answer 
import pandas as pd
import numpy as np

def range_series(start=1, end=10):
    return pd.Series(range(start, end + 1))

def sum_numpy_arrays(*arrays):
    return np.sum(arrays, axis=0)

# Examples
print(range_series())  # Should return a series from 1 to 10
print(range_series(5))  # Should return a series from 5 to 10
print(range_series(5, 15))  # Should return a series from 5 to 15

# Example usage of sum_numpy_arrays
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
arr3 = np.array([[13, 14, 15], [16, 17, 18]])
print(sum_numpy_arrays(arr1, arr2, arr3))

print(" ")
#. Create a function that takes in two lists named keys and values as
# arguments
# Keys would be strings and contain n string values
# Values would be a list containing n lists
# The methods should return a new pandas DataFrame with keys as column
# names and values as their corresponding values, e.g:
# ->create_dataframe(["One", "Two"], [["X", "Y"], ["A", "B"]]) -> should return a
# data frame
# One Two
# 0 X A
# 1 Y B
import pandas as pd

def create_dataframe(keys, values):
    """
    Creates a pandas DataFrame using keys as column names and values as column values.
    
    Parameters:
        keys (list of str): Column names
        values (list of list): Column values
        
    Returns:
        pd.DataFrame: A DataFrame with the given keys and values.
    """
    return pd.DataFrame({k: v for k, v in zip(keys, values)})

# Example usage:
df = create_dataframe(["One", "Two"], [["X", "Y"], ["A", "B"]])
print(df)

print(" ")
#  Create a function that concatenates two DataFrames. Use a previously
# created function to create two DataFrames and pass them as parameters
# Make sure that the indexes are reset before returning.
import pandas as pd

def create_dataframe(keys, values):
    """
    Creates a pandas DataFrame using keys as column names and values as column values.
    
    Parameters:
        keys (list of str): Column names
        values (list of list): Column values
        
    Returns:
        pd.DataFrame: A DataFrame with the given keys and values.
    """
    return pd.DataFrame(dict(zip(keys, values)))

def concatenate_dataframes(df1, df2):
    """
    Concatenates two DataFrames and resets the index.
    
    Parameters:
        df1 (pd.DataFrame): First DataFrame
        df2 (pd.DataFrame): Second DataFrame
        
    Returns:
        pd.DataFrame: Concatenated DataFrame with reset index.
    """
    return pd.concat([df1, df2], ignore_index=True)

# Example usage:
df1 = create_dataframe(["One", "Two"], [["X", "Y"], ["A", "B"]])
df2 = create_dataframe(["One", "Two"], [["M", "N"], ["C", "D"]])
concatenated_df = concatenate_dataframes(df1, df2)
print(concatenated_df)
print(" ")
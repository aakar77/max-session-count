'''
Creater : Aakar Jinwala
'''

import pandas as pd
import numpy as np
import time
from string import ascii_uppercase

def main():

    filename = "test.txt"
    
    # reading data into pandas dataframe
    df = pd.read_csv(filename, sep=",", header=None)
    df.columns = ["user", "unixtimestamp"]
    df.user = df.user.astype(np.int64)

    # making a seperate field of timestamp to faciliate time comparison = 1 hour
    df['timestamp'] = pd.to_datetime(df.unixtimestamp)
    
    # defining numeric series for data
    numArray = [i for i in range(df.size)]
    
    # sort the values as per the user
    df = df.sort_values(by=['user'])
    df = df.groupby('user').apply(lambda x: x.sort_values('timestamp'))

    # defining condtions for filter and apply labels
    diff_time = df.timestamp.diff() > pd.datetools.timedelta(minutes=60)
    diff_user = df.user != df.user.shift()
    session_id = (diff_user | diff_time).cumsum()
    
    # define new label called session_id for stroing the session
    df['session_id'] = session_id.map(pd.Series(numArray))
    print(df.shape)
    print(df)

    # Count as per session IDs
    df2 = df.groupby(['session_id'])['session_id'].count() 
    print(df2)

    maxval = df2
    print(maxval)

    # Find maximum value in each session
    df3 = df.groupby(['session_id'])['unixtimestamp'].max()

    # concatenate the two dataframes based on session_id as index
    result = pd.concat([df2,df3], axis = 1)
    result.columns = ['count','max_timestamp']
    #print(result)
    #print(result.shape)

    result_count = result.loc[result['count'] == result['count'].max()]
    
    # Select row having maximum timestamp
    result_count = result_count.loc[result_count['max_timestamp'] == result_count['max_timestamp'].max()]
    #print(result_count)

    # getting user Id corresponding to the value
    userId = df.loc[df['session_id'] == result_count.index.get_values()[0], 'user'].iloc[0]
    # printing out the final output
    print(userId,result_count['count'].iloc[0],result_count['max_timestamp'].iloc[0],sep=',')

if __name__ == "__main__":
    main()
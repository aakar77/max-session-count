
Problem Statement Breakdown:

1) So, here in this problem task, I have to find first find relation among the sessions 
having two conditions
    a) two consecutive rows having different user ID belongs to two different sessions
    b) two consecutive rows timestamp difference should be < 1 hour, they belong to same session 
2) Now, after grouping values by session, count number of entries for that particular session
3) Lastly, also find maximum timestamp value associated with each session
4) Output the user ID, no of entries and maximum timestamp in that session 


Systems Dependencies and environment setup:

1) I have used Python 3 language having version 3.5.2, 
 a) Although my primary language is Java 7, I believe manipulating data is best with Python. 
 b) With Java it difficult and verbose to manipulate, though possible, I will try doing that too soon
2) Since the problem involves dealing with large amount of data, I thought of using Pandas dataframe 
 and role is for Big Data Engineer Position
3) I have used Anaconda version 4.2.0 (64-bit) which encompases all Dependencies

Files in the folder:

1) prog.py is the version of program, in which I have accomplished the task using Pandas dataframe
2) Just type "python3 prog.py test.txt" to run the program, here test.txt is filename
3) datagen.py is the program which I have used to generate the data for test.txt file
4) data.txt is the sample small subset used for testing the program

Analysis: ( O(N^2) time and O(N) space where N corresponds to number of rows)

1) Using pandas and numpy libraries makes the computation more efficient as they are written in C++
   internally and C++ is fastest language.
2) Sorting takes about O(N log N) time complexity, I am sorting the entire dataset,
   first by user ID and later by TimesStamp
   a) Sorting directly according timestamp is valid as it is just number of seconds.
   b) 1508723553000 < 1508723554000 
3) Computing the session_id takes O(N) time, 
    a) Here shift operation is used which compares values between two consecutive rows entries.
    b) Also, unix timestamp is converted into timestamp format for time difference = 60 minutes
    i.e. 1 hr
    c) For labelling the session_id based on 3 a) and 3 b),
    I have used integer value ranging from 1 to O(N)
4) For Counting no of entries for a particular session, group by session ID and stores resultant 
   data in dataframe. This operation takes O(N * K), where K is no of sessions,
   a) If K == N i.e. each entry corresponds to one session and each and every session has one entry 
   only, time complexity will be O(N * N) = O(N^2)
5) For finding maximum timestamp value group by session ID and store resultant data in dataframe takes      
   O(N * K), where K is no of session formed. If K = N, worst case O(N^2)

6) Total Time Complexity would be O(N log N) + O(N^2) + O(N^2) + O(N) = O(N^2)
7) I have used four dataframes here with one having maximum space complexity = O(N)







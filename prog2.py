from datetime import datetime, time
import sys

def checkTimeDiff(t1,t2):
    t1 = datetime.fromtimestamp(int(t1/1000))
    t2 = datetime.fromtimestamp(int(t2/1000))
    
    if math.abs(t1.hour - t2.hour) >= 1:
        return True
    else:
        return False

def main():

    # initializations
    data_list = []
    value_i = 0
    prev_user = 0

    #filename = "test.txt"
    filename = str(sys.argv[1])

    # reading a data and constructing list of tuples
    with open(filename) as f:
        for line in f:
            # fetching data
            line = line.replace('\n','')
            entry = line.split(',')
            
            #generating list of tuple values
            tups = (entry[0], entry[1])
            data_list.append(tups)

    # sorting the list of tuples based on userId and timestamp value
    data_list = sorted(data_list, key=lambda element: (element[0],element[1]))
    
    dict = {}

    i = 0

    myList = []
    for j, k in data_list:
        
        # starting label so no comparison
        if i == 0:
            i = 1
            myList.append((j, k))
        else:
            try:
                if(prev_user != j or (not checkTimeDiff(k,prev_time))):
                    dict[i] = myList
                    myList = []
                    i+=1
                else:
                    myList.append((j,k))
            except:
                print('Error for',k,' ',prev_time)

        # updating the previous values
        prev_user = j
        prev_time = k
        print(i)
                
    print(data_list)

    
if __name__ == "__main__":
    main()

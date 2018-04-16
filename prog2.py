from datetime import datetime, time

def checkTimeDiff(t1,t2):
    t1 = datetime.fromtimestamp(int(t1))
    t2 = datetime.fromtimestamp(int(t2))
    
    if math.abs(t1.hour - t2.hour) >= 1:
        return True
    else:
        return False


def main():

    # initializations
    data_list = []
    value_i = 0
    prev_user = 0

    # reading a data and constructing list of tuples
    with open('data.txt') as f:
        for line in f:
            # fetching data
            line = line.replace('\n','')
            entry = line.split(',')
            
            #generating list of tuple values
            tups = (entry[0], entry[1])
            data_list.append(tups)

    # sorting the list of tuples based on userId and timestamp value
    data_list = sorted(data_list, key=lambda element: (element[0],element[1]))
    
    i = 0
    for j, k in data_list:
        
        # starting label so no comparison
        if i == 0:
            i = 1
        else:
            try:
                if(prev_user != j or (not checkTimeDiff(k,prev_time))):
                    i+=1
            except:
                print('Error for',k,' ',prev_time)

        # updating the previous values
        prev_user = j
        prev_time = k
        print(i)
                

    print(data_list)


    
if __name__ == "__main__":
    main()

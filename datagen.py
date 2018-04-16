from datetime import datetime, time
import numpy as np

def main():

    user_arr = np
    start_timestamp = 1293840000
    range = 100000000
    
    user_id = np.random.randint(low=100, high=800, size=1000000)
    
    timest_array = np.random.randint(low=1306155333, high=1396255333, size=1000000)
    timest_array = timest_array * 1000

    result_arr = np.array(list(zip(user_id, timest_array)))

    with open("test.txt", "w") as f:
        np.savetxt(f,result_arr.astype(int), fmt='%i', delimiter=",")
    
if __name__ == "__main__":
    main()

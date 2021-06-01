import pickle
import pandas as pd

with open('/mnt/DATA/yg/uniinfo/3DDFA_V2/configs/bfm_noneck_v3.pkl', 'rb') as file:
    data_list = []
    while True:
        try:
            data = pickle.load(file)
        except EOFError:
            break
        data_list.append(data)
        
        #print(data)

    df = pd.DataFrame(data_list)
    print(df)
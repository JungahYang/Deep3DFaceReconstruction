import pickle

fname = "/mnt/DATA/yg/3DDFA_V2/configs/param_mean_std_62d_120x120.pkl"
with open(fname, 'rb') as file:
    data_list = []
    while True:
        try:
            data = pickle.load(file)
            with open("/mnt/DATA/yg/3DDFA_V2/configs/pick.txt", 'a') as f:
                f.writelines(str(data))
        except EOFError:
            break
        print(data.shape)
        data_list.append(data)
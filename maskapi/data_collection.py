from apireader import ds,find_masks_stores
def data_reset():
    ds.ds_data_list=[]
    ds.ds_remain=[]
    ds.ds_lat=[]
    ds.ds_lng=[]
    ds.ds_name=[]
def data_collect(address):
    data_reset()
    find_masks_stores(address, 1)
    for i in range(0,len(ds.ds_data_list)):
        print("위도:",ds.ds_data_list[i]["lat"]," 이름:",ds.ds_data_list[i]["name"],
              " 수량:",ds.ds_data_list[i]["remain_stat"])
        ds.ds_lat.append(ds.ds_data_list[i]["lat"])
        ds.ds_lng.append(ds.ds_data_list[i]["lng"])
        ds.ds_name.append(ds.ds_data_list[i]["name"])
        ds.ds_remain.append(ds.ds_data_list[i]["remain_stat"])
        if ds.ds_remain[i] == "None":
            ds.ds_remain[i]=="Not Sell"
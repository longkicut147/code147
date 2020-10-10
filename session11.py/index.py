
#C.R.U.D: Create, Read, Update, Delete

#Create:
information = {
    #key: value
    "do_kho": ["snack", "thit bo kho"], #trong key k có dấu cách
    "dong_lanh": {
        "do_song":[],
        "do_tai_chin":[],
        "do_chin": "khong co do" },     #còn trong value có thể có
    "is_open": True,
    "gia_dung": "chao chong dinh"     
}
# print(information)


#Read:
# print(information["do_kho"])
#phan information["do_kho"] la thuc hien Read (doc gia tri)


#Update:
information["dong_lanh"]["do_song"].append("ca map") #them "ca map" vao value dang list cua "do_song"
information["dong_lanh"]["do_chin"] = "ca kho"  #them "ca kho" vao value dang string cua "do_chin"

# print(information["dong_lanh"]["do_song"])


#Delete:
del information["is_open"]
print(information)





import csv
path = "https://raw.githubusercontent.com/dulangaweerakoon/images_mturk_pickplace/master/dist"
with open("batch.csv", "w") as csv_file:
    csv_file.write("image_url\n")
    for i in range(1,4):
        for j in range(1,15):
            for k in range(1,3):
                csv_file.write(path+str(i)+"/Configuration_"+str(j)+"_v"+str(k)+".png\n")
        
     

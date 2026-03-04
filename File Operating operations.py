import pickle
import csv
with open("Sample.txt","w") as f:
    f.write("Hello,this is a text file example.")
with open("Sample.txt","r") as f:
    print("Text file content:",f.read())
data={"Name":"alice","Age":22,"Course":"B.Tech"}
with open("data.bin","wb")as f:
    pickle.dump(data,f)
with open("data.bin","rb")as f:
    binary_data=pickle.load(f)
    print("Binary file content:",binary_data)
with open ("Students.csv","w",newline='')as f:
    w=csv.writer(f)
    w.writerow(["Name","Age","Grade"])
    w.writerow(["John",20,"A"])
    w.writerow(["Sara",21,"B"])
with open("Students.csv","r")as f:
    r=csv.reader(f)
    print("CSV File Content:")
    for row in r:
        print(row)
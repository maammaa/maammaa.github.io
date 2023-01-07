import wget
import os 
keyword ='ariana'
path = os.path.join(keyword)
os.mkdir(path)
count =1
list_of_src=[]
with open ('src.txt', 'r')as f:
    for line in f:
        list_of_src.append(line.strip('\n'))
def delList(L):
    for i in L:
        if L.count(i) != 1:
            for x in range((L.count(i) - 1)):
                L.remove(i)
    return L
re=delList(list_of_src)
with open('test.txt' , mode="w") as file: #清空檔案
    file.truncate(0)
with open ('test.txt', 'a')as f:
    for r in re :
        f.write(r+'\n')
for img in re:   
    save_as= os.path.join(path, keyword+'-'+str(count)+'.jpg')
    wget.download(img,save_as)
    count+=1
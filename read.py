data = []
count = 0
sum_length = 0
average_length = 0
try:

    with open('reviews.txt','r') as file:
        for line in file:
            count += 1
            data.append(line)
            if count % 1000 == 0:
                print(len(data))
                # print('----------%d----------'%count)
                # print(data[count - 1])
except Exception as e:
    print(e)
print('檔案讀取完了，總共有',len(data),'筆資料。')

for item in data:
    sum_length += len(item)
average_length = sum_length / len(data)
print('資料的平均長度為',average_length)

new = []
for d in data: #留言篩選印出留言資料小於100個字的
    if len(d) <= 100:
        new.append(d.strip())
print(new)


data = []
count = 0
try:

    with open('reviews.txt','r') as file:
        for line in file:
            count += 1
            data.append(line)
            if count % 1000 == 0:
                print('----------%d----------'%count)
                print(data[count - 1])
except Exception as e:
    print(e)
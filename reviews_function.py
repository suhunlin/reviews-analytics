import os
def read_file(filename):
    datas = []
    try:
        with open(filename,'r',encoding='utf-8-sig') as file:
            for line in file:
                datas.append(line.strip())
    except Exception as error_message:
        print(error_message)
    return datas

def load_count_datas_to_dictionary(datas):
    wc = {}
    count = 0
    if not datas:
        print('沒有的資料載入!!!')
        return wc
    else:
        print('共載入:',len(datas),'筆資料')
        for data in datas:
            count += 1
            split_data_by_space = data.split()
            for word in split_data_by_space:
                if word in wc:
                    wc[word] += 1
                else:
                    wc[word] = 1
            if count % 10000 == 0:
                print('-----載入', count ,'資料，請耐心等待!!!-----')
    print('共載入:',len(wc),'個字進入字典!!!')
    return wc

def print_user_inquire_word(word_dictionary,user_input):
    if user_input in word_dictionary:
        print(word_dictionary[user_input])
    else:
        print('輸入的字不存在字典裡!!!')
def print_word_dictionary_info(word_dictionary):
    for word in word_dictionary:
        print(word ,':' ,word_dictionary[word])

def main():
    filename = 'reviews.txt'
    if os.path.exists(filename):
        datas = read_file(filename)
    else:
        datas = []

    word_dictionary = load_count_datas_to_dictionary(datas)
    # print_word_dictionary_info(word_dictionary)
    while True:
        user_input = input('請輸入要查詢出現次數的字(結束請輸入q):')
        if user_input == 'q':
            print('謝謝查詢，慢走不送!!!!')
            break
        print_user_inquire_word(word_dictionary,user_input)


if __name__ == '__main__':
    main()

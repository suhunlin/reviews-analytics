import os
def read_file(filename):
    messages = []
    try:
        with open(filename,'r',encoding='utf-8-sig') as file:
            for message in file:
                messages.append(message.strip())

    except Exception as error_message:
        print(error_message)
    return messages

def count_every_word(messages):
    wc_dict = {}

    for message in messages:
        split_message_by_space = message.split()
        for word in split_message_by_space:
            if word in wc_dict:
                wc_dict[word] += 1
            else:
                wc_dict[word] = 1
    return wc_dict

def count_word_by_user_input(user_input,wc_dict):
    if user_input in wc_dict:
        print(user_input,'出現了',wc_dict[user_input],'次')
    else:
        print('這個字沒有出現過唷!!!')

def main():
    filename = 'reviews.txt'
    if os.path.exists(filename):
        messages = read_file(filename)
    else:
        messages = []

    wc_dict = count_every_word(messages)
    while True:
        user_input = input('請輸入要查詢次數的單字(q結束):')
        if user_input == 'q':
            break
        count_word_by_user_input(user_input, wc_dict)

if __name__ == '__main__':
    main()



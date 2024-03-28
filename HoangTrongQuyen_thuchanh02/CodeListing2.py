import string 

def word_count(file_path):
    word_counts = {}
    file_path = string('/ThisPC/WINDOW(C:)/Users/DELL//Dowlloads/P1_data.txt')

    try:
   
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().lower()

            # Loại bỏ các ký tự đặc biệt
            for char in string.punctuation:
                content = content.replace(char, ' ')

            # Tách các từ và đếm số lần xuất hiện
            words = content.split()
            for word in words:
                word_counts[word] = word_counts.get(word, 0) + 1

    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}")

    return word_counts

# Ví dụ sử dụng
file_path = "/content/P1_data.txt"
word_counts = word_count(file_path)
print(word_counts)
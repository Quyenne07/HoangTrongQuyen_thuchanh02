def count_chars(string):
    # Tạo một dictionary rỗng
    char_count = {}
    
    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    string = string.strip()
    
    # Duyệt qua từng ký tự trong chuỗi
    for char in string:
        # Chuyển đổi ký tự thành chữ thường
        char = char.lower()
        
        # Nếu ký tự là chữ cái
        if char.isalpha():
            # Nếu ký tự đã có trong dictionary, tăng giá trị lên 1
            if char in char_count:
                char_count[char] += 1
            # Ngược lại, thêm ký tự vào dictionary với giá trị ban đầu là 1
            else:
                char_count[char] = 1
    
    return char_count

string1 = 'Happiness'
print(count_chars(string1))
# Output: {'h': 1, 'a': 1, 'p': 2, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}

string2 = 'smiles'
print(count_chars(string2))
# Output: {'s': 2, 'm': 1, 'i': 1, 'l': 1, 'e': 1}
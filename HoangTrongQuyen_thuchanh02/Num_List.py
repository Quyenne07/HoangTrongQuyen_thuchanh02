from collections import deque

def max_in_sliding_window(num_list, k):
    if not num_list or k == 0:
        return []

    # Tạo một hàng đợi deque để theo dõi các chỉ số của các số lớn nhất
    window = deque()

    # Xử lý cửa sổ đầu tiên
    for i in range(k):
        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()
        window.append(i)

    result = []
    result.append(num_list[window[0]])

    # Xử lý các cửa sổ tiếp theo
    for i in range(k, len(num_list)):
        # Loại bỏ các chỉ số không thuộc cửa sổ hiện tại
        if window[0] <= i - k:
            window.popleft()

        # Loại bỏ các số nhỏ hơn số hiện tại trong cửa sổ hiện tại
        while window and num_list[i] >= num_list[window[-1]]:
            window.pop()

        window.append(i)
        result.append(num_list[window[0]])

    return result

# Ví dụ sử dụng
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
size = 3
print(max_in_sliding_window(num_list, size))
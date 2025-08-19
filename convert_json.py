import json

# Đường dẫn file input và output
input_file = 'global2imgpath.json'  # Thay bằng path thực tế nếu cần
output_file = 'id2index.json'

# Load file input
try:
    with open(input_file, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Error: File {input_file} không tìm thấy. Vui lòng kiểm tra path.")
    exit(1)

# Transform data
id2index = {}
if isinstance(data, dict):
    # Nếu là dictionary, enumerate các item
    for index, (key, value) in enumerate(data.items()):
        # Giả định value là path dài, cần extract group/video/keyframe
        # Điều chỉnh logic này nếu cấu trúc khác
        parts = value.split('/')
        if len(parts) >= 3:
            # Lấy các phần cuối hoặc theo pattern của README.md (1/1/xxx)
            # Ở đây tạm giả định lấy pattern từ ví dụ README
            group = "1"  # Hard-code theo ví dụ, thay đổi nếu cần
            video = "1"  # Hard-code theo ví dụ, thay đổi nếu cần
            keyframe = parts[-1].split('.')[0] if '.' in parts[-1] else parts[-1]
            id2index[str(index)] = f"{group}/{video}/{keyframe}"
        else:
            print(f"Warning: Value '{value}' không đủ phần. Skipping key {key}.")
elif isinstance(data, list):
    # Nếu là list, enumerate các item
    for index, value in enumerate(data):
        parts = value.split('/')
        if len(parts) >= 3:
            group = "1"
            video = "1"
            keyframe = parts[-1].split('.')[0] if '.' in parts[-1] else parts[-1]
            id2index[str(index)] = f"{group}/{video}/{keyframe}"
        else:
            print(f"Warning: Value '{value}' không đủ phần. Skipping index {index}.")

# Save output
with open(output_file, 'w') as f:
    json.dump(id2index, f, indent=4)

print(f"Convert thành công! File output: {output_file}")

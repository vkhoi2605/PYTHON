prompt = "\nNhap noi dung: "
prompt += "\nnhap 'quit' de thoat"
message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)
def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

print("Binary Converter Bot")
print("Enter some text and I'll convert it to 8-bit ASCII binary.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter text: ").strip()
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    if user_input:  
        binary_result = text_to_binary(user_input)
        print(f"Binary: {binary_result}\n")
    else:
        print("Please enter some text!\n")
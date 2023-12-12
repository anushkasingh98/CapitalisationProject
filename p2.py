import p1

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of the file '{file_path}':\n{content}")
            return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "example.txt"  # Update with the actual path to your text file
    content = read_text_file(file_path)
    output = p1.Capitalise_Paragraph(content)
    print(f"Capitalized Content is:\n{output}")

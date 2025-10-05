def WordCounter(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            data = content.split()
            no_of_words = len(data)
            print(f"Total number of words in '{filename}': {no_of_words}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


filename = "test (Task 3).txt"
WordCounter(filename)
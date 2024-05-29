import random
import string
import os

def generate_random_text(length=100):
    """Generate random text of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def main():
    if os.path.exists('output'):
        mode = 'a'  # Append mode if file exists
    else:
        mode = 'w'  # Write mode if file doesn't exist

    # Open 'output' file in append or write mode
    with open('output', mode) as file:
        if mode == 'a':
            file.write('\n')  # Add a new line if appending

        # Generate random text
        random_text = generate_random_text()
        # Write random text to the file
        file.write(random_text)

if __name__ == "__main__":
    main()

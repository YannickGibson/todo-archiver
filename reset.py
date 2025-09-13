""" Replace TODO file with fresh headings only. """

from constants import *

def generate_todo_markdown(headings):
    markdown = "# 📆 TODO's\n\n"
    
    for heading in headings:
        markdown += f"\n## {heading}\n\n"
    
    return markdown

def main():
    # Generate the markdown
    todo_markdown = generate_todo_markdown(HEADINGS)

    def save_to_file(content, filename=TODO_FILE):
        """Save markdown content to a file."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

    save_to_file(todo_markdown)

if __name__ == "__main__":
    main()
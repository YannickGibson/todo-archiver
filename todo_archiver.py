""" Archive completed tasks from todo file. So tasks prefixed with '- [x]'. """
import os
import re
from datetime import datetime
from constants import * 


def make_heading_pattern(text):
    return re.compile(rf'^##\s+{text}', re.IGNORECASE)

def to_snake_case(text):
    return text.lower().replace(' ', '_')

def ensure_archive_dir():
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

def write_lines(path, lines, mode='a'):
    with open(path, mode, encoding='utf-8') as f:
        f.writelines(lines)

def read_archive(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()

def create_heading_dicts(heading_strings):
    heading_dicts = []
    for heading in heading_strings:
        d = {
            'name': heading,
            'pattern': make_heading_pattern(heading),
            'archive_file': os.path.join(ARCHIVE_DIR, f'{to_snake_case(heading)}.md'),
        }
        heading_dicts.append(d)
    return heading_dicts

def main():
    ensure_archive_dir()
    heading_dicts = create_heading_dicts(HEADINGS)

    # Read and filter todoa.md
    current_cat = None
    updated_todo = []
    new_archives = {i: [] for i in range(len(heading_dicts))}

    with open(TODO_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            # Detect category switch
            for index, info in enumerate(heading_dicts):
                if info['pattern'].match(line):
                    current_cat = index
                    break

            if line.strip().startswith('- [x]') and current_cat is not None:
                # Split - [x] and insert a date
                date_str = datetime.now().strftime('%Y-%m-%d')
                line = line.replace('- [x]', f'- [x] `{date_str}`', 1)
                # Check if there is new line at end, if not add one
                if not line.endswith('\n'):
                    line += '\n'
                # New completed task for this category
                new_archives[current_cat].append(line)
            else:
                updated_todo.append(line)

    # Write back cleaned todoa.md
    with open(TODO_FILE, 'w', encoding='utf-8') as f:
        f.writelines(updated_todo)

    # Append new tasks into per-category archives
    for index, info in enumerate(heading_dicts):
        if new_archives[index]:
            write_lines(info['archive_file'], new_archives[index])

    # Build completed.md by reading each full archive file
    completed = ["# ✅ Completed TODO's\n\n\n"]
    for index, info in enumerate(heading_dicts):
        completed.append(f"## {info['name']}\n")
        # Grab everything in that archive file
        lines = read_archive(info['archive_file'])
        completed.extend(lines)
        if index < len(heading_dicts) - 1:
            completed.append('\n\n')  # Separator between categories

    with open(COMPLETED_FILE, 'w', encoding='utf-8') as f:
        f.writelines(completed)

    print("✅ Done: todoa.md updated; per-category archives and completed.md now in sync.")

    # After syncing completed.md, create a timestamped merged archive
    merged_dir = os.path.join(ARCHIVE_DIR, 'merged_archive')
    os.makedirs(merged_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    merged_filename = f"todom_{timestamp}.md"
    merged_path = os.path.join(merged_dir, merged_filename)

    # Read post-processed todoa.md and completed.md
    with open(TODO_FILE, 'r', encoding='utf-8') as f:
        todo_content = f.read()
    with open(COMPLETED_FILE, 'r', encoding='utf-8') as f:
        completed_content = f.read()

    # Write them into the merged file
    merged_content = "# 📆 Merged TODO's\n\n\n" + todo_content + "\n\n\n\n" + completed_content
    with open(merged_path, 'w', encoding='utf-8') as f:
        f.write(merged_content)

    # Overwrite root merged file
    with open(MERGED_FILE, 'w', encoding='utf-8') as f:
        f.write(merged_content)

    print(f"✅ Created merged archive: {merged_path}")  

if __name__ == '__main__':
    main()
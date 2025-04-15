import os

ALLOWED_EXTENSIONS = {
    ".scala", ".sbt", ".js", ".ts", ".jsx", ".tsx", 
    ".json", ".yaml", ".yml", ".conf", ".env", 
    ".md", ".html", ".css", ".scss", ".less", 
    ".helm", ".tpl", ".dockerfile", ".sh",
}

ALLOWED_BASE_FILES = {"readme", "license", "changelog", "dockerfile"}

EXCLUDED_DIRECTORIES = {"node_modules", ".git", "target", "dist", "__pycache__", "venv"}

MAX_FILE_SIZE = 100_000

def should_include_file(file_name):
    lower_file = file_name.lower()
    base, ext = os.path.splitext(lower_file)
    if ext in ALLOWED_EXTENSIONS:
        return True
    if lower_file.startswith("dockerfile"):
        return True
    if base in ALLOWED_BASE_FILES:
        return True
    return False

def write_content_in_parts(content_blocks, base_output_file):
    current_part = []
    current_size = 0
    part_number = 1

    def write_part_file(part_content, part_num):
        part_file = f"{base_output_file.replace('.txt', '')}_part{part_num}.txt"
        try:
            with open(part_file, 'w', encoding='utf-8') as out_file:
                out_file.write("\n".join(part_content))
            print(f"Written part {part_num} to {part_file}")
        except Exception as e:
            print(f"Error writing to part file {part_file}: {e}")

    for block in content_blocks:
        block_size = len(block)
        if current_size + block_size > MAX_FILE_SIZE:
            write_part_file(current_part, part_number)
            part_number += 1
            current_part = []
            current_size = 0
        current_part.append(block)
        current_size += block_size

    if current_part:
        write_part_file(current_part, part_number)

def parse_project(root_dir, output_dir, project_name):
    content_blocks = []
    for current_root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRECTORIES]
        for file in files:
            if should_include_file(file):
                file_path = os.path.join(current_root, file)
                relative_path = os.path.relpath(file_path, root_dir)
                header = f"\n// ---- Start of {relative_path} ----\n"
                footer = f"\n// ---- End of {relative_path} ----\n"
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = [line.strip() for line in f if line.strip()]
                        if lines:
                            content_blocks.append(header + "\n".join(lines) + footer)
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    os.makedirs(output_dir, exist_ok=True)
    base_output_file = os.path.join(output_dir, f"{project_name}_documentation.txt")
    if content_blocks:
        write_content_in_parts(content_blocks, base_output_file)

def process_all_projects(projects_dir, output_dir):
    if not os.path.exists(projects_dir):
        print(f"The directory '{projects_dir}' does not exist.")
        return
    for project_name in os.listdir(projects_dir):
        project_path = os.path.join(projects_dir, project_name)
        if os.path.isdir(project_path):
            print(f"Processing project: {project_name}")
            parse_project(project_path, output_dir, project_name)

if __name__ == "__main__":
    projects_dir = "projects"
    output_dir = "output"
    process_all_projects(projects_dir, output_dir)
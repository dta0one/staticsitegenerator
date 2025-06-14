import re, os, glob

from block_to_html import markdown_to_html_node
from htmlnode import HTMLNode


def extract_title(markdown):
    h1 = re.search(r"^# (.*)", markdown, re.MULTILINE)
    if not h1:
        raise Exception("No h1 header")
    return h1.group(1)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path}, to {dest_path} using {template_path}.")

    with open(from_path) as file:
        content = file.read()

    with open(template_path) as file:
        template = file.read()

    processed_content = markdown_to_html_node(content).to_html()    
    processed_title = extract_title(content)

    new_page = (template
        .replace("{{ Title }}", processed_title)
        .replace("{{ Content }}", processed_content)
    )
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(new_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    markdown_files = glob.glob(f"{dir_path_content}/**/*.md", recursive=True)

    for markdown_file in markdown_files:
        html_file = markdown_file.replace(dir_path_content, dest_dir_path, 1).replace(".md", ".html")
        os.makedirs(os.path.dirname(html_file), exist_ok=True)
        generate_page(markdown_file, template_path, html_file)
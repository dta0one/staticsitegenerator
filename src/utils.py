import re

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



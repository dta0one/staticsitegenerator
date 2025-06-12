from block_to_html import markdown_to_html_node
from htmlnode import HTMLNode


def extract_title(markdown):
    #pull h1 header
    if not h1:
        raise Exception("No h1 header")
    return h1


def generate_page(from_path, template_path, dest_path):
    print("Generating page from {from_path}, to {dest_path} using {template_path}.")
    open_from_path = open(from_path)
    open_template_path = open(template_path)
    html_string = markdown_to_html_node(open_from_path).to_html()
    title = extract_title(open_from_path)
    

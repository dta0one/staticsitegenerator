import os, shutil, glob

from copystatic import copy_files_recursive
from utils import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

#    markdown_files = glob.glob("content/**/*.md", recursive=True)
#
#    for markdown_file in markdown_files:
#        html_file = markdown_file.replace("content", "public", 1).replace(".md", ".html")
#        os.makedirs(os.path.dirname(html_file), exist_ok=True)
#        generate_page(markdown_file, template_path, html_file)
        

main()

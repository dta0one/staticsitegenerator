import re


def extract_markdown_images(text):
    # This regex looks for image pattern: ![alt text](url)
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    # This regex looks for link pattern: [anchor text](url)
    # The (?<!!) ensures we don't match image patterns
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches



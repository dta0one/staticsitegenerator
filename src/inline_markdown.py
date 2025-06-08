import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # If the node is not TextType.TEXT, just add it as-is
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)
            continue

        # If delimiter doesn't exist in the text, add the node unchanged
        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        # Ensure delimiters are paired correctly
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

        # Split the text using the delimiter
        parts = node.text.split(delimiter)
        
        # Debugging Logs (optional for troubleshooting)
        #print(f"Original text: {node.text}")
        #print(f"Parts after splitting: {parts}")
        #print(f"Delimiter: {delimiter}")
        #print(f"TextType: {text_type}")
        
        # Process each part and assign correct TextType
        for index, part in enumerate(parts):
            # Skip empty parts caused by consecutive or trailing delimiters
            if part == "":
                continue
            
            # Assign TextType based on whether part is inside or outside delimiters

            if index % 2 == 0:
                # Text outside delimiters
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Text inside delimiters
                new_nodes.append(TextNode(part, text_type))
    
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    images_found = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            images_found = extract_markdown_images(node.text)
            if not images_found:
                # No images found, just add the original node
                new_nodes.append(node)
            else:
                remaining_text = node.text
                
                for alt_text, url in images_found:
                    # Create the image markdown pattern that appears in the text
                    image_markdown = f"![{alt_text}]({url})"
                    
                    # Split at the first occurrence of this image markdown
                    parts = remaining_text.split(image_markdown, 1)
                    
                    # parts[0] is text before the image
                    if parts[0]:  # Only add if not empty
                        new_nodes.append(TextNode(parts[0], TextType.TEXT))
                    
                    # Add the image node
                    new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                    
                    # Update remaining_text to what's after the image
                    if len(parts) > 1:
                        remaining_text = parts[1]
                    else:
                        remaining_text = ""
                
                # Don't forget to add any remaining text as a node
                if remaining_text:
                    new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        else:
            new_nodes.append(node)

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    links_found = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            links_found = extract_markdown_links(node.text)
            if not links_found:
                # No links found, just add the original node
                new_nodes.append(node)
            else:
                remaining_text = node.text
                
                for text, url in links_found:
                    # Create the link markdown pattern that appears in the text
                    link_markdown = f"[{text}]({url})"
                    
                    # Split at the first occurrence of this link markdown
                    parts = remaining_text.split(link_markdown, 1)
                    
                    # parts[0] is text before the link
                    if parts[0]:  # Only add if not empty
                        new_nodes.append(TextNode(parts[0], TextType.TEXT))
                    
                    # Add the link node
                    new_nodes.append(TextNode(text, TextType.LINK, url))
                    
                    # Update remaining_text to what's after the link
                    if len(parts) > 1:
                        remaining_text = parts[1]
                    else:
                        remaining_text = ""
                
                # Don't forget to add any remaining text as a node
                if remaining_text:
                    new_nodes.append(TextNode(remaining_text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes


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


#creating specific functions from main delimiter function
def split_nodes_bold(old_nodes):
    return split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

def split_nodes_italic(old_nodes):
    return split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)

def split_nodes_code(old_nodes):
    return split_nodes_delimiter(old_nodes, "`", TextType.CODE)


#the actual function using everything to markdown text
def text_to_textnodes(text):
    print (text)
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_bold(nodes)
    nodes = split_nodes_italic(nodes)
    nodes = split_nodes_code(nodes)
    return nodes


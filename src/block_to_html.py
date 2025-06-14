import re
from splitblocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, text_node_to_html_node, TextType
from inline_markdown import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    new_node = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.HEADING:
                matches = re.match(r"^#{1,6}", block)
                count = len(matches.group(0)) if matches else 0
                new_block = ParentNode(f"h{count}", text_to_children(block[count + 1:]), None)
                new_node.append(new_block)
            case BlockType.CODE:
                split_block = block.splitlines()
                sliced_block = [line.lstrip() for line in split_block[1:-1]]
                joined_sliced_block = "\n".join(sliced_block) + "\n"
                inner_block = [text_node_to_html_node(TextNode(joined_sliced_block, TextType.CODE))]
                new_block = ParentNode("pre", inner_block, None)
                new_node.append(new_block)
            case BlockType.QUOTE:
                cleaned_block = []
                for line in block.splitlines():
                    if line.startswith(">"):
                        cleaned_block.append(line[1:].lstrip())
                    else:
                        cleaned_block.append(line)
                joined_block = "\n".join(cleaned_block)
                new_block = ParentNode("blockquote", text_to_children(joined_block), None)
                new_node.append(new_block)
            case BlockType.UNORDERED_LIST:
                new_block = ParentNode("ul", list_to_children(block), None)
                new_node.append(new_block)
            case BlockType.ORDERED_LIST:
                new_block = ParentNode("ol", list_to_children(block), None)
                new_node.append(new_block)
            case BlockType.PARAGRAPH:
                split_block = block.splitlines()
                cleaned_block = [line.strip() for line in split_block]
                joined_block = " ".join(cleaned_block)
                new_block = ParentNode("p", text_to_children(joined_block), None)
                new_node.append(new_block)
    return ParentNode("div", new_node, None)


def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))    
    return children


def list_to_children(text):
    children = []
    for line in text.split("\n"):
        if re.match("^- ", line) or re.match(r"^\* ", line) or re.match(r"^\+ ", line):
            children.append(ParentNode("li",text_to_children(line[2:]), None))
        elif re.match(rf"^\d+. ", line):
            match_ordered = re.match(rf"^\d+. ", line)
            children.append(ParentNode("li", 
                                       text_to_children(line[match_ordered.span()[1]:]), 
                                       None))
    return children


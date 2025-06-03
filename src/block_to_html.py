import re
from splitblocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, text_node_to_html_node

def markdown_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block_type(block)
        match type:
            case BlockType.HEADING:
                pass
            case BlockType.CODE:
                pass
            case BlockType.QUOTE:
                block = ParentNode("blockquote", text_to_children(block), None)
            case BlockType.UNORDERED_LIST:
                block = ParentNode("ul", list_to_children(block), None)
            case BlockType.ORDERED_LIST:
                block = ParentNode("ol", list_to_children(block), None)
            case BlockType.PARAGRAPH:
                block = ParentNode("p", text_to_children(block), None)


def text_to_children(text):
    pass

def list_to_children(text):
    children = []
    for line in text.split("\n"):
        if re.match("^- ", line) or re.match("^* ", line) or re.match("^+ ", line):
            children.append(ParentNode("li",text_to_children(line[2:]), None))
        elif re.match(rf"^\d+. ", line):
            match_ordered = re.match(rf"^\d+. ", line)
            children.append(ParentNode("li", 
                                       text_to_children(line[match_ordered.span()[1]:]), 
                                       None))
    return children


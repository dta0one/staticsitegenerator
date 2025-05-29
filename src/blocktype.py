import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    lines = block.split('\n')
    if re.match(r"^#{1,6} (.*)", block):
        return BlockType.HEADING
    if re.search(r"^`{3}(.*)`{3}$", block, re.DOTALL):
        return BlockType.CODE
    if re.match(r"^>", block):
        if all(re.match(r"^>", line) for line in lines):
            return BlockType.QUOTE
    if re.match(r"^- ", block):
        if all(re.match("^- ", line) for line in lines):
            return BlockType.UNORDERED_LIST
    #if re.match(r"^1. ", block):
    #    for line in lines:
    #        if re.match(r"^{n}. ")
    #    return BlockType.ORDERED_LIST

    else:
        return BlockType.PARAGRAPH

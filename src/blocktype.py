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
    lines = block.strip().split('\n')
    if re.match(r"^#{1,6} (.*)", block) and len(lines) == 1:
        return BlockType.HEADING
    if re.match(r"^`{3}$", lines[0]) and re.match(r"^`{3}$", lines[-1]) and len(lines) > 2:
        return BlockType.CODE
    if all(re.match(r"^>", line) for line in lines):
        return BlockType.QUOTE
    if all(re.match("^- ", line) for line in lines):
        return BlockType.UNORDERED_LIST
    if all(re.match(rf"^{i}\. ", line) for i, line in enumerate(lines, start=1)):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

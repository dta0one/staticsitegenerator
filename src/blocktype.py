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
    print(f"Block being processed: {block}")
    print(f"Lines after splitting: {lines}")
    if re.match(r"^#{1,6} (.*)", block) and len(lines) == 1:
        print("Heading condition is True")
        return BlockType.HEADING
    if re.match(r"^`{3}$", lines[0].strip()) and re.match(r"^`{3}$", lines[-1].strip()) and len(lines) > 2:
        print("Code condition is True")
        return BlockType.CODE
    if all(re.match(r"^>", line) for line in lines):
        print("Quote condition is True")
        return BlockType.QUOTE
    if all(re.match("^- ", line) for line in lines):
        print("Unordered list condition is True")
        return BlockType.UNORDERED_LIST
    if all(re.match(rf"^{i}\. ", line) for i, line in enumerate(lines, start=1)):
        print("Ordered list condition is True")        
        return BlockType.ORDERED_LIST
    else:
        print("Falling through to Paragraph")
        return BlockType.PARAGRAPH

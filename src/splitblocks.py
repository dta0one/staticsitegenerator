
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_block = []
    for block in blocks:
        if block.strip():
            stripped_block.append(block.strip())

    return stripped_block

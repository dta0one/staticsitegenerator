
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_block = []
    for block in blocks:
        stripblock = block.strip()
        if stripblock:
            stripped_block.append(stripblock)

    return stripped_block

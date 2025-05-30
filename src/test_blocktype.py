import unittest

from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):

    def test_space(self):
        md = "This is random text that should be a pragraph"
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_heading(self):
        md = "###### This is a heading"
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_wrong(self):
        md = "#########This looks like a heading but is a paragraph."
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_code(self):
        md = """
```
def test_heading_wrong(self):
    md = "#########This looks like a heading but is a paragraph."
    result = block_to_block_type(md)
    self.assertEqual(result, BlockType.PARAGRAPH)
```
"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.CODE)

    def test_quote(self):
        md = """
> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
> tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
> quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
> Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
> fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
> qui officia deserunt mollit anim id est laborum.
"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list(self):
        md = """
- first item
- second item
- third item
"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        md = """
1. first item
2. second item
3. third item
"""
        result = block_to_block_type(md)
        self.assertEqual(result, BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()
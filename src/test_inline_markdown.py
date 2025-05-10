import unittest
from inline_markdown import (
    extract_markdown_links,
    extract_markdown_images,
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        # Basic test with a single link
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)
        
        # Test with multiple links
        matches = extract_markdown_links(
            "Check out [Boot.dev](https://www.boot.dev) and [YouTube](https://www.youtube.com)"
        )
        self.assertListEqual([
            ("Boot.dev", "https://www.boot.dev"),
            ("YouTube", "https://www.youtube.com")
        ], matches)
        
        # Test with links that have special characters in the URL
        matches = extract_markdown_links(
            "Links with special chars: [GitHub](https://github.com/user/repo?query=value&param=123)"
        )
        self.assertListEqual([
            ("GitHub", "https://github.com/user/repo?query=value&param=123")
        ], matches)
        
        # Test with an image and a link - should only extract the link
        matches = extract_markdown_links(
            "An image ![alt text](image.jpg) and a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)
        
        # Test with empty text
        matches = extract_markdown_links("")
        self.assertListEqual([], matches)
        
        # Test with no links
        matches = extract_markdown_links("Just some plain text without any links")
        self.assertListEqual([], matches)



if __name__ == "__main__":
    unittest.main()

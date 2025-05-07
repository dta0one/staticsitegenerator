import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from textnode import extract_markdown_images, extract_markdown_links
from htmlnode import HTMLNode, ParentNode, LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertIsNone(html_node.props)

    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertIsNone(html_node.props)

    def test_link(self):
        node = TextNode("Click me", TextType.LINK, url="https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click me")
        self.assertEqual(html_node.props["href"], "https://example.com")
        self.assertIsNone(html_node.props.get("alt"))  # Ensure no extra props

    def test_image(self):
        node = TextNode("Description of image", TextType.IMAGE, url="https://image.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")  # IMAGE value should be blank
        self.assertEqual(html_node.props["src"], "https://image.com")
        self.assertEqual(html_node.props["alt"], "Description of image")

    def test_invalid_type(self):
        class RandomNode:
            pass

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

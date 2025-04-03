import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_href(self):
        node = HTMLNode("a", "Click me!", None, {"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
        
    def test_props_to_html_with_google(self):
        node = HTMLNode("b", "Click here!", None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')
        
    def test_props_to_html_with_yahoo(self):
        node = HTMLNode("CCCC", "Four C's", None, {"href": "https://yahoo.com"})
        self.assertEqual(node.props_to_html(), ' href="https://yahoo.com"')
        
if __name__ == "__main__":
    unittest.main()
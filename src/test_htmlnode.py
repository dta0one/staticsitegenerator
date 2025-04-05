import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_empty_value_raises_error(self):
        node = LeafNode("p", "")
        # This should raise ValueError
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_none_value_raises_error(self):
        node = LeafNode("p", None)
        # This should raise ValueError
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_with_multiple_props(self):
        node = LeafNode("img", "An image", {"src": "image.jpg", "alt": "Description", "width": "500"})
        self.assertEqual(node.to_html(), '<img src="image.jpg" alt="Description" width="500">An image</img>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_node_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_parent_node_with_one_child(self):
        child_node = LeafNode("span", "child content")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child content</span></div>")

    def test_parent_node_with_props(self):
        parent_node = ParentNode("div", [], {"class": "center", "id": "main"})
        self.assertEqual(parent_node.to_html(), '<div class="center" id="main"></div>')

    def test_nested_parent_nodes(self):
        child_node = ParentNode("p", [LeafNode(None, "nested child")])
        parent_node = ParentNode("div", [child_node])
        # Testing that it returns some kind of valid HTML string for now
        self.assertTrue(parent_node.to_html().startswith("<div>"))

if __name__ == "__main__":
    unittest.main()
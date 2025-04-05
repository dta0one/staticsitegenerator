class HTMLNode():
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("to_html method not implemented")
	
	def props_to_html(self):
		if not self.props:
			return ""
		result = ""
		for key, value in self.props.items():
			result += f' {key}="{value}"'
		return result
		
	def __repr__(self):
		children_count = 0
		if self.children is not None:
			children_count = len(self.children)
		return f"HTMLNode(tag={self.tag}, value={self.value}, children={children_count}, props={self.props})"
	
class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super(LeafNode, self).__init__(tag, value, None, props)

	def to_html(self):
		if not self.value:
			raise ValueError("All leaf nodes must have a value")
		if self.tag is None:
			return self.value
		return F"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
	
	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"
	
class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super(ParentNode, self).__init__(tag, None, children, props)

	def to_html(self):
		if self.tag is None:
			raise ValueError("ParentNode tag is missing")
		if self.children is None:
			raise ValueError("ParentNode children is missing")
		
		html = f"<{self.tag}"

		if self.props:
			html += self.props_to_html()

		html += ">"

		for child in self.children:
			html += child.to_html()

		html += f"</{self.tag}>"

		return html
	
	def __repr__(self):
		return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
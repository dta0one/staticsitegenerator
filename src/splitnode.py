from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # If the node is not TextType.TEXT, just add it as-is
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)
            continue

        # If delimiter doesn't exist in the text, add the node unchanged
        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        # Ensure delimiters are paired correctly
        if node.text.count(delimiter) % 2 != 0:
            raise Exception(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

        # Split the text using the delimiter
        parts = node.text.split(delimiter)
        
        # Debugging Logs (optional for troubleshooting)
        #print(f"Original text: {node.text}")
        #print(f"Parts after splitting: {parts}")
        #print(f"Delimiter: {delimiter}")
        #print(f"TextType: {text_type}")
        
        # Process each part and assign correct TextType
        for index, part in enumerate(parts):
            # Skip empty parts caused by consecutive or trailing delimiters
            if part == "":
                continue
            
            # Assign TextType based on whether part is inside or outside delimiters

            if index % 2 == 0:
                # Text outside delimiters
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Text inside delimiters
                new_nodes.append(TextNode(part, text_type))
    
    return new_nodes
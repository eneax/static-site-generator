class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # True: if all of the properties of two TextNode objects are equal.
    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    # Returns a string representation of the TextNode object.
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
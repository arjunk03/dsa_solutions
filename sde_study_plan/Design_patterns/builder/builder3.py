
class HtmlElement:
    indent_size = 2
    def __init__(self, name, text):
        self.name = name
        self.text = text
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)
   
    def __str__(self, indent=0):
        lines = []
        i = ' ' * (indent * 2)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * 2)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str__(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)
    
class HtmlBuilder:
    def __init__(self, root_name):
        self.root = HtmlElement(root_name, "")
    
    def add_child(self, child_name, child_text):
        child = HtmlElement(child_name, child_text)
        self.root.add_element(child)
        return self
    
    def build(self):
        return str(self.root)
    
# Example usage
if __name__ == "__main__":  
    builder = HtmlBuilder("html")
    builder.add_child("head", "").add_child("title", "My Title")
    builder.add_child("body", "").add_child("h1", "Hello World").add_child("p", "This is a paragraph.")
    
    print(builder.build())
    
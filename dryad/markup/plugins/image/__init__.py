from dryad.markup.doctree import Block

class ImageBlock(Block):
    def __init__(self, path):
        self.path = path

def parse_image(block_name, inline_text, body_lines):
    path = inline_text.strip()
    return ImageBlock(path)

BLOCK_PARSERS = [(u'^image$', parse_image)]


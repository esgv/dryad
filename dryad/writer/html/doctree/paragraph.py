from dryad.writer import *
import pystache

paragraph_template = """\
<p>{{{child_text}}}</p>

"""

class Paragraph:
    def write(self):
        context = {
            'child_text': str_nodes(*self.child_nodes)
        }
        
        return pystache.render(paragraph_template, context)
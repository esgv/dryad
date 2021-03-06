from pyforge.all import *
from dryad.markup.doctree import Span, Block

supported_languages = [
    u'code',                     # Do not highlight.
    u'auto',                     # Automatically determine language.
    u'c++',    u'cpp',           # C++
    u'python', u'python3',       # Python
    u'yaml',   u'xml',           # markup
]

class CodeBlock(Block):
    def __init__(self, language, body_lines):
        self.language = language
        self.body_lines = list(body_lines)

class CodeSpan(Span):
    def __init__(self, language, body_text):
        self.language = language
        self.body_text = body_text

def parse_code_block(block_name, inline_text, body_lines):
    body_lines = list(body_lines)
    min_indent = get_min_indent(body_lines)
    body_lines = dedented_by(body_lines, min_indent)
    body_lines = blank_lines_stripped(body_lines)

    return CodeBlock(block_name, body_lines)

def parse_code_span(span_name, body_text):
    return CodeSpan(span_name, body_text)

supported_languages_re = u'^' + make_strings_re(supported_languages) + u'$'

BLOCK_PARSERS = [(supported_languages_re, parse_code_block)]
SPAN_PARSERS  = [(supported_languages_re, parse_code_span )]


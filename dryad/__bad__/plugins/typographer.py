# Typographer
# ===========

# Special symbols
    # '<<'
    # '>>'
    # '--'
    # '->'
    # '<-'
    # '<->'
    
# Heuristic replace
    # '-'   to em dash
    # ' - ' to en dash
    # Non-breaking spaces where needed (propositions, articles, dashes).
    # Automatic quotes.
    # Periods and commas should be taken inside strongs and emphs.
    # Automatic links.

# Math typographer
# ================

# \left and \right on all parens. 
    # Excluding \text and non-matching braces
    # Excluding when \left or \right is already present
# Alternatively, \left and \right on specific occasions: 
    # when there is a \frac inside
    # when there is a \left or \right inside
# commas and dots in cases

from pyforge.all import *
from dryad.markup.doctree import find, type_selector
from dryad.markup.doctree.text import Text
from dryad.markup.plugins.elements.math import MathBlock

typographic_escapes = {
    u'->' : u'\u2192',
    u'<-' : u'\u2190',
    u'<->': u'\u2194',
    u'--' : u'\u2014',    # em dash
    u'<<' : u'\u00ab',    # left quote
    u'>>' : u'\u00bb'     # right quote
}

typographic_replaces = {
    (u' - '     , u' \u2014 '),          # em dash (expreimental)
    (ur'"(.*?)"', u'\u00ab\\1\u00bb')
}

math_replaces = [
    (ur'\\left\s*([(\[]|\\lfloor)' , ur'\1'),
    (ur'\\right\s*([)\]]\\rfloor)', ur'\1'),
    (ur'\((.*?)\)', ur'\\left( \1 \\right)'),
    (ur'\[(.*?)\]', ur'\\left[ \1 \\right]'),
    (ur'\\lfloor(.*?)\\rfloor', ur'\\left\lfloor \1 \\right\\rfloor'),
]

def typograph_text(text):
    text = multiple_replace(text, typographic_escapes)
    return multiple_replace_re(text, typographic_replaces)

def typograph_math(body_text):
    #return multiple_replace_re(body_text, math_replaces)
    return body_text

def typograph_all_text(root):
    for node in find(root, type_selector(Text)):
        node.body_text = typograph_text(node.body_text)

def typograph_all_math_blocks(root):
    for node in find(root, type_selector(MathBlock)):
        node.body_lines = list(map(typograph_math, node.body_lines))

after_parse_document = [typograph_all_text, typograph_all_math_blocks]


# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523638460.782017
_enable_loop = True
_template_filename = '/Users/Josh/Downloads/fomo_intex2/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['skip', 'top_center', 'content_right', 'content_center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top_center():
            return render_top_center(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def skip():
            return render_skip(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'skip'):
            context['self'].skip(**pageargs)
        

        __M_writer('\n    <a href="#content" class="skip">Skip to content</a>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_center'):
            context['self'].top_center(**pageargs)
        

        __M_writer('\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_skip(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def skip():
            return render_skip(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_center():
            return render_top_center(context)
        __M_writer = context.writer()
        __M_writer('\n<div class="row">\n        <img class="img-responsive background_img" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Images/record_fit.png" alt="Black Piano"/>\n        <div class="title">\n            <a name="main-content" tabindex="-1"></a>\n            <h1>Family-Oriented Music Organization</h1>\n            <a href="/catalog/" id="shop" class="btn btn-sm btn-success">SHOP NOW</a><br/><br/>\n        </div>\n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer("\n    <img src='")
        __M_writer(str( STATIC_URL ))
        __M_writer("homepage/media/images/music.png' alt='Saxophone Icon'>\n    <br>\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\n<div id="content">\n    <h2 class=\'cen\'>Buy or rent from our collection!</h2>\n    <p><strong>Why is music important?</strong> Music participation provides a unique opportunity for literacy preparation. Whether the children are singing, playing, or listening, teachers direct them to listen and hear in new ways which exercises their aural discrimination. Playing instruments and adding movement to the lessons teaches children about sequential learning which is essential in reading comprehension.</p>\n    <p>Plato once said that music "is a more potent instrument than any other for education". You will find many teachers of young children who would agree with him. Recent research has found that music uses both sides of the brain, a fact that makes it valuable in all areas of development. Music affects the growth of a child\'s brain academically, emotionally, physically and spiritually.</p>\n    <p><strong>Music is academic.</strong> For some people, this is the primary reason for providing music lessons to their children. A recent study from the University of California found that music trains the brain for higher forms of thinking. Second graders who were given music lessons scored 27% higher on proportional math and fractions tests than children who received no special instruction. Research indicates that musical training permanently wires a young mind for enhanced performance.</p>\n    <p><strong>Music is physical.</strong> Music can be described as a sport. Learning to sing and keep rhythm develops coordination. The air and wind power necessary to blow a flute, trumpet or saxophone promotes a healthy body.</p>\n    <p><strong>Music is emotional.</strong> Music is an art form. We are emotional beings and every child requires an artistic outlet. Music may be your child\'s vehicle of expression.</p>\n    <p><strong>Music is for life.</strong> Most people can\'t play soccer, or football at 70 or 80 years of age but they can sing. And they can play piano or some other instrument. Music is a gift you can give your child that will last their entire lives.</p>\n    <p>Did you know that music making is part of what makes humans human? <strong>Every culture makes music</strong>. Not only that, <strong>every past culture has made music too</strong>. Musical instruments are amongst the oldest man-made objects ever found. For example, there are <strong>flutes around 37,000 years old</strong> and perhaps even older!</p>\n    <p>Compare this with reading and writing. The earliest forms of writing are no more than about 3500 years old. <strong>And many cultures of the world still do not read or write</strong>.</p>\n    <p>Or how about this? Scientists have recently discovered that music affects many parts of our brain very deeply (grown-ups can look at the book <em>This is Your Brain On Music</em> by Daniel Levitin to find out more). But you don&#8217;t need to be a scientist to understand that! <strong>Trying singing &#8216;Happy Birthday&#8217; or a Christmas song</strong> and you will understand. What do these tunes make you think of? How do they make you feel? <strong>You&#8217;ll be filled with all sorts of memories and feelings</strong> when you hear these tunes—many more than would if you simply said the words &#8216;birthday&#8217; or &#8216;Christmas&#8217;.</p>\n    <p><strong>Music gets under your skin. It creates strong feelings. And it creates strong memories.</strong></p>\n    <p><strong>Music is a language. It is a language for all humans.</strong> It is a language that is there when normal language is of little use. </p>\n</div>\n\n\n    </br>\n    </br>\n    </br>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Josh/Downloads/fomo_intex2/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 4, "53": 17, "58": 24, "63": 46, "69": 3, "75": 3, "81": 6, "88": 6, "89": 8, "90": 8, "96": 21, "103": 21, "104": 22, "105": 22, "111": 26, "117": 26, "123": 117}}
__M_END_METADATA
"""

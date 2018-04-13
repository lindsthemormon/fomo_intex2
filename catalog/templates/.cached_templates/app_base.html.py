# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523640658.265493
_enable_loop = True
_template_filename = '/Users/Josh/Downloads/fomo_intex2/catalog/templates/app_base.html'
_template_uri = 'app_base.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['menu', 'nav_main', 'content_left', 'content_right']


from catalog import models as cmod 

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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        cat_id = context.get('cat_id', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def nav_main():
            return render_nav_main(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def menu():
            return render_menu(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav_main'):
            context['self'].nav_main(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def nav_main():
            return render_nav_main(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n       <li class = "nav item ')
        __M_writer(str( 'active' if request.dmp.page == 'index' and request.dmp.app == 'homepage' else ''))
        __M_writer('"><a href="/index/">Home</a></li>\n       <li class = "nav item ')
        __M_writer(str( 'active' if request.dmp.page == 'index' and request.dmp.app == 'catalog' else ''))
        __M_writer('"><a href="/catalog/">Catalog</a></li>\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('"><a href="/about">About Us</a></li>\n       <li class=" ')
        __M_writer(str('active' if request.dmp.page == 'faq' else '' ))
        __M_writer('"><a href="/faq">FAQ</a></li>\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('"><a href="/contact">Contact</a></li>\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'terms' else '' ))
        __M_writer('"><a href="/terms">Terms</a></li>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cat_id = context.get('cat_id', UNDEFINED)
        category = context.get('category', UNDEFINED)
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer("\n</br>\n</br>\n<ul id='catlist'>\n    ")

        category_list = cmod.Category.objects.all()
        product_list = cmod.Product.objects.all()
            
        
        __M_writer('\n')
        if cat_id == 0:
            __M_writer("        <li id='all_products'><a class='active' href='/catalog/index/'> All Products </a></li>\n")
        else:
            __M_writer("        <li id='all_products'><a href='/catalog/index/'> All Products </a></li>\n")
        for c in category_list:
            if category == c.name:
                __M_writer("            <li><a class='active' href='/catalog/index/")
                __M_writer(str( c.id ))
                __M_writer("'/> ")
                __M_writer(str( c.name ))
                __M_writer(' </a></li>\n')
            else:
                __M_writer("            <li><a href='/catalog/index/")
                __M_writer(str( c.id ))
                __M_writer("'/> ")
                __M_writer(str( c.name ))
                __M_writer(' </a></li>\n')
        __M_writer('</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n</br>\n    <h3>Recently Viewed</h3>\n        ')

        if request.dmp.page == 'details':
            myList = request.last_five[1:6]
        else:
            myList = request.last_five[0:5]
                
        
        __M_writer("\n        <ol id='thumbnailsRight' class='rv cen'>\n")
        for h in myList:
            __M_writer('                <a href="/catalog/details/')
            __M_writer(str(h.id))
            __M_writer('/"><li class =\'rightimage\' alt=""><img src=\'')
            __M_writer(str(h.image_url()))
            __M_writer("'></li></a>\n                <p>")
            __M_writer(str(h.name))
            __M_writer('</p>\n')
        __M_writer('         </ol>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Josh/Downloads/fomo_intex2/catalog/templates/app_base.html", "uri": "app_base.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "47": 1, "48": 2, "53": 7, "58": 19, "63": 43, "68": 61, "74": 5, "80": 5, "86": 10, "93": 10, "94": 12, "95": 12, "96": 13, "97": 13, "98": 14, "99": 14, "100": 15, "101": 15, "102": 16, "103": 16, "104": 17, "105": 17, "111": 22, "119": 22, "120": 26, "125": 29, "126": 30, "127": 31, "128": 32, "129": 33, "130": 35, "131": 36, "132": 37, "133": 37, "134": 37, "135": 37, "136": 37, "137": 38, "138": 39, "139": 39, "140": 39, "141": 39, "142": 39, "143": 42, "149": 46, "156": 46, "157": 49, "164": 54, "165": 56, "166": 57, "167": 57, "168": 57, "169": 57, "170": 57, "171": 58, "172": 58, "173": 60, "179": 173}}
__M_END_METADATA
"""

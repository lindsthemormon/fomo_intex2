# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523574458.7526429
_enable_loop = True
_template_filename = 'C:/Users/Linds/Desktop/fomo_intex2/catalog/templates/thanks.html'
_template_uri = 'thanks.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['content_center']


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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        your_email = context.get('your_email', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        your_email = context.get('your_email', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content cen">\r\n        <h1>Thank You!</h1>\r\n        <p>Your purchase is on its way.Please check your email, ')
        __M_writer(str(your_email))
        __M_writer(', for a receipt!</p>\r\n        <br /><br />\r\n        <a href = \'/catalog/index/\'>\r\n            <button type="button" class="btn btn-primary">Continue shopping</button>\r\n        </a>\r\n    </div>\r\n    <br /><br /><br />\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Linds/Desktop/fomo_intex2/catalog/templates/thanks.html", "uri": "thanks.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 13, "48": 3, "55": 3, "56": 6, "57": 6, "63": 57}}
__M_END_METADATA
"""

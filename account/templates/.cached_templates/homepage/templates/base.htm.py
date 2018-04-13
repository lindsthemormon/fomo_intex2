# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523641006.875967
_enable_loop = True
_template_filename = '/Users/Josh/Downloads/fomo_intex2/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['header_maintenance', 'skip', 'nav_main', 'top_center', 'content_left', 'content_center', 'content_right', 'bottom', 'footer']


from catalog import models as cmod

from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def nav_main():
            return render_nav_main(context._locals(__M_locals))
        def skip():
            return render_skip(context._locals(__M_locals))
        def bottom():
            return render_bottom(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def top_center():
            return render_top_center(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def header_maintenance():
            return render_header_maintenance(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n<!DOCTYPE html>\n\n\n<html>\n<meta charset="UTF-8">\n<head>\n\n    <title>FOMO</title>\n\n')
        __M_writer('    <!--<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>-->\n    <script src="//ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/js/bootstrap.min.js"></script>\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/css/bootstrap.min.css"/>\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/css/bootstrap-theme.min.css"/>\n    <link href=\'https://fonts.googleapis.com/css?family=Satisfy\' rel=\'stylesheet\'>\n    <link href=\'https://fonts.googleapis.com/css?family=Hammersmith One\' rel=\'stylesheet\'>\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\n\n\n')
        __M_writer('    <script src="/django_mako_plus/dmp-common.min.js"></script>\n    ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n')
        __M_writer('    <link rel="fluid icon" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/favicon.ico">\n\n\n</head>\n<body>\n<a href="#content" class="skip">Skip to content</a>\n\n<header>\n    <!--Maintenance Message-->\n    <div id="maintenance">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_maintenance'):
            context['self'].header_maintenance(**pageargs)
        

        __M_writer('\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'skip'):
            context['self'].skip(**pageargs)
        

        __M_writer('\n    </div>\n\n\n    <!--Make a navbar-->\n    <nav class="navbar navbar-inverse">\n      <div class="container-fluid">\n        <div class="navbar-header">\n          <a class="navbar-brand" href="/index"><i class="fa fa-headphones" style="color:#3D5A67;"></i></a>\n        </div>\n          <ul class="nav navbar-nav">\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav_main'):
            context['self'].nav_main(**pageargs)
        

        __M_writer('\n        </ul>\n               <ul class="nav navbar-nav navbar-right">\n')
        if request.user.is_authenticated:
            __M_writer('                       <li class=" ')
            __M_writer(str( 'active' if request.dmp.page == 'cart' else '' ))
            __M_writer('">\n                            <a href="/catalog/cart">\n\n')
            if cmod.Order.objects.filter(user = request.user,status='cart').first() is not None:
                __M_writer('                                       ')
                __M_writer(str(cmod.Order.objects.filter(user = request.user,status='cart').first().num_items()))
                __M_writer('\n                                       <span class="glyphicon glyphicon-shopping-cart"></span>\n')
            __M_writer('                            </a>\n                       </li>\n                        <li class="dropdown">\n                           <a class="dropdown-toggle" data-toggle="dropdown" href="#">\n                               Welcome ')
            __M_writer(str(request.user.first_name))
            __M_writer(' ')
            __M_writer(str(request.user.last_name))
            __M_writer('\n                           <span class="caret"></span></a>\n                           <ul class="dropdown-menu blue">\n                            <li><a href="#"><i class="fa fa-id-card" style="color:#3D5A67;"></i> My Account</a></li>\n                            <li><a href="/account/logout"><i class="fa fa-user-times" style="color:#3D5A67;"></i> Log Out</a></li>\n                           </ul>\n                         </li>\n')
        else:
            __M_writer('                        <li><a href="/account/signup"><i class="fa fa-user-plus"></i> Sign Up</a></li>\n                        <li><a href="/account/login"><i class="fa fa-sign-in"></i> Login</a></li>\n               </ul>\n')
        __M_writer('\n      </div>\n    </nav>\n\n\n</header>\n\n<main>\n\n    <div id="top">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_center'):
            context['self'].top_center(**pageargs)
        

        __M_writer('\n    </div>\n\n    <div id="middle">\n        <div id="left">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\n        </div>\n\n        <div id="center">\n            <div id="content">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\n            </div>\n        </div>\n\n        <div id="right">\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\n        </div>\n    </div>\n\n    <div id="bottom">\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bottom'):
            context['self'].bottom(**pageargs)
        

        __M_writer('\n    </div>\n\n</main>\n\n<div class="footerstuff cen">\n    <footer>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n</footer>\n</div>\n\n\n</body>\n\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_maintenance(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_maintenance():
            return render_header_maintenance(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_skip(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def skip():
            return render_skip(context)
        __M_writer = context.writer()
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
        __M_writer('\n                   <li class="')
        __M_writer(str( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('"><a href="/">Home</a></li>\n                   <li class = "nav item ')
        __M_writer(str( 'active' if request.dmp.page == 'index' and request.dmp.app == 'catalog' else ''))
        __M_writer('"><a href="/catalog/">Catalog</a></li>\n                   <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('"><a href="/about">About Us</a></li>\n                   <li class=" ')
        __M_writer(str('active' if request.dmp.page == 'faq' else '' ))
        __M_writer('"><a href="/faq">FAQ</a></li>\n                   <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('"><a href="/contact">Contact</a></li>\n                   <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'terms' else '' ))
        __M_writer('"><a href="/terms">Terms</a></li>\n')
        if request.user.is_staff:
            __M_writer('                        <li class=" ')
            __M_writer(str( 'active' if request.dmp.page == 'admin' else '' ))
            __M_writer('"><a href="/admin/">Manage</a></li>\n')
        __M_writer('              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_center():
            return render_top_center(context)
        __M_writer = context.writer()
        __M_writer('\n            <!--Page Title-->\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottom(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bottom():
            return render_bottom(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n        ')
        __M_writer('\n        &copy; Copyright ')
        __M_writer(str( datetime.now().year))
        __M_writer('. All rights reserved.\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Josh/Downloads/fomo_intex2/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 128, "22": 0, "48": 2, "49": 14, "50": 14, "51": 14, "52": 16, "53": 16, "54": 17, "55": 17, "56": 18, "57": 18, "58": 25, "59": 26, "60": 26, "61": 29, "62": 29, "63": 29, "68": 39, "73": 40, "78": 61, "79": 64, "80": 65, "81": 65, "82": 65, "83": 68, "84": 69, "85": 69, "86": 69, "87": 72, "88": 76, "89": 76, "90": 76, "91": 76, "92": 83, "93": 84, "94": 88, "99": 100, "104": 105, "109": 110, "114": 115, "119": 120, "124": 130, "130": 39, "141": 40, "152": 51, "159": 51, "160": 52, "161": 52, "162": 53, "163": 53, "164": 54, "165": 54, "166": 55, "167": 55, "168": 56, "169": 56, "170": 57, "171": 57, "172": 58, "173": 59, "174": 59, "175": 59, "176": 61, "182": 98, "188": 98, "194": 105, "205": 110, "216": 115, "227": 120, "238": 127, "244": 127, "245": 128, "246": 129, "247": 129, "253": 247}}
__M_END_METADATA
"""

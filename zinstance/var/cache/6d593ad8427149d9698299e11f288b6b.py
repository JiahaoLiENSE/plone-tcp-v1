# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/toolbar.pt'

__tokens = {73: (u'view/context_state', 2, 35), 126: (u' python: view.get_personal_bar(', 3, 33), 184: (u'context_state/is_toolbar_visible', 4, 24), 323: (u'${view/get_options}', 6, 75), 325: (u'view/get_options', 6, 77), 477: (u'view/get_toolbar_logo', 9, 53), 569: (u'view/show_switcher', 11, 55), 714: (u'view/base_render', 14, 38), 906: (u'personal_bar/user_actions', 19, 29), 994: (u'personal_bar/homelink_url', 21, 36), 1120: (u'personal_bar/user_name', 23, 33), 1337: (u'personal_bar/user_name', 28, 35), 1472: (u'personal_bar/user_actions', 31, 37), 1543: (u'action', 32, 43), 1599: (u'action/title', 33, 47), 1727: (u"python:action['id'] == 'personaltools-logout'", 36, 43)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235426090896 = {u'class': u'plone-toolbar-switcher', }
_static_140235374589712 = {u'class': u'plone-toolbar-container', }
_static_140235489934800 = {}
_static_140235426089040 = {u'class': u'plone-toolbar-main', }
_static_140235374545680 = {u'role': u'toolbar', u'id': u'edit-bar', }
_static_140235435449424 = __compile_zt_expr
_static_140235426114320 = {u'class': u'plone-toolbar-submenu-header', }
_static_140235385307216 = set([])
_static_140235385301200 = {u'class': u'plone-toolbar-logo', }
_static_140235426054224 = {u'class': u'icon-user', u'aria-hidden': u'true', }
_static_140235374543376 = {u'data-pat-toolbar': u'${view/get_options}', u'role': u'toolbar', u'id': u'edit-zone', u'class': u'pat-toolbar', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235373955536 = {u'class': u'icon-logout', }
_static_140235373981200 = {u'href': u'#', }
_static_140235426115280 = {u'class': u'plone-toolbar-caret', }
_static_140235373979600 = {u'id': u'portal-personaltools', u'class': u'plone-toolbar-separator', }
_static_140235385299792 = {u'src': u'view/get_toolbar_logo', u'alt': u'Plone Toolbar', }
_static_140235451402128 = {u'class': u'user-action', }
_static_140235451404112 = {u'href': u'', }
_static_140235426058448 = {u'id': u'personal-bar-container', }

import re
import functools
from itertools import chain as __chain
from sys import exc_clear as __exc_clear
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(modules, nothing, tales, zope_version_4_8_7_):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is long)):
                target = unicode(target)
            else:
                if (__tt is str):
                    target = decode(target)
                else:
                    if (__tt is not unicode):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (unicode(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is long)):
                target = unicode(target)
            else:
                if (__tt is str):
                    target = decode(target)
                else:
                    if (__tt is not unicode):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (unicode(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        decode = econtext['__decode']
        convert = econtext['__convert']
        translate = econtext['__translate']
        on_error_handler = econtext['__on_error_handler']
        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8b17af4b10> name=None at 7f8b17af4910> -> __attrs_140235374542992
            __attrs_140235374542992 = _static_140235374545680
            __backup_context_state_140235432665744 = get('context_state', __marker)

            # <Value u'view/context_state' (2:35)> -> __value
            __token = 73
            try:
                __zt_tmp = __attrs_140235374542992
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/context_state', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_personal_bar_140235426057104 = get('personal_bar', __marker)

            # <Value u'python: view.get_personal_bar()' (3:33)> -> __value
            __token = 126
            try:
                __zt_tmp = __attrs_140235374542992
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u' view.get_personal_bar()', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['personal_bar'] = __value

            # <Value u'context_state/is_toolbar_visible' (4:24)> -> __condition
            __token = 184
            try:
                __zt_tmp = __attrs_140235374542992
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'context_state/is_toolbar_visible', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140235374543312 = __i18n_domain
                __i18n_domain = u'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="edit-bar" role="toolbar">\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b17af4210> name=None at 7f8b17af4610> -> __attrs_140235374590480
                __attrs_140235374590480 = _static_140235374543376

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="edit-zone" role="toolbar" class="pat-toolbar"')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374591056
                __default_140235374591056 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution u'${view/get_options}' (6:75)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8b17aff050> -> __attr_data_pat_toolbar
                __token = 323
                __token = 325
                try:
                    __zt_tmp = __attrs_140235374590480
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_pat_toolbar = _static_140235435449424('path', u'view/get_options', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_data_pat_toolbar = __quote(__attr_data_pat_toolbar, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_data_pat_toolbar = __attr_data_pat_toolbar
                if (__attr_data_pat_toolbar is None):
                    pass
                else:
                    if (__attr_data_pat_toolbar is _DEFAULT_MARKER):
                        __attr_data_pat_toolbar = None
                    else:
                        __tt = type(__attr_data_pat_toolbar)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __attr_data_pat_toolbar = unicode(__attr_data_pat_toolbar)
                        else:
                            if (__tt is str):
                                __attr_data_pat_toolbar = decode(__attr_data_pat_toolbar)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __attr_data_pat_toolbar = __attr_data_pat_toolbar.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_data_pat_toolbar)
                                        __attr_data_pat_toolbar = (unicode(__attr_data_pat_toolbar) if (__attr_data_pat_toolbar is __converted) else __converted)
                                    else:
                                        __attr_data_pat_toolbar = __attr_data_pat_toolbar()
                if (__attr_data_pat_toolbar is not None):
                    __append((u' data-pat-toolbar="%s"' % __attr_data_pat_toolbar))
                __append(u'>\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b17aff710> name=None at 7f8b17aff2d0> -> __attrs_140235374589520
                __attrs_140235374589520 = _static_140235374589712

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="plone-toolbar-container">\n      ')

                # <Static value=<_ast.Dict object at 0x7f8b185368d0> name=None at 7f8b18536950> -> __attrs_140235385299088
                __attrs_140235385299088 = _static_140235385301200

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a class="plone-toolbar-logo">\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b18536350> name=None at 7f8b18536b10> -> __attrs_140235426087184
                __attrs_140235426087184 = _static_140235385299792

                # <img ... (0:0)
                # --------------------------------------------------------
                __append(u'<img alt="Plone Toolbar"')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385299856
                __default_140235385299856 = _DEFAULT_MARKER

                # <Substitution u'view/get_toolbar_logo' (9:53)> -> __attr_src
                __token = 477
                try:
                    __zt_tmp = __attrs_140235426087184
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_140235435449424('path', u'view/get_toolbar_logo', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((u' src="%s"' % __attr_src))
                __append(u' />\n      </a>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8b1ac1cf90> name=None at 7f8b18536590> -> __attrs_140235426089680
                __attrs_140235426089680 = _static_140235426090896

                # <Value u'view/show_switcher' (11:55)> -> __condition
                __token = 569
                try:
                    __zt_tmp = __attrs_140235426089680
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/show_switcher', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a class="plone-toolbar-switcher">')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426088464
                    __attrs_140235426088464 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>Left-Top switcher</span></a>')
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426090640
                __attrs_140235426090640 = _static_140235489934800

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append(u'<nav>\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1ac1c850> name=None at 7f8b1ac1c1d0> -> __attrs_140235426060240
                __attrs_140235426060240 = _static_140235426089040

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="plone-toolbar-main">\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426060624
                __attrs_140235426060624 = _static_140235489934800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426061456
                __default_140235426061456 = _DEFAULT_MARKER

                # <Value u'view/base_render' (14:38)> -> __cache_140235426061584
                __token = 714
                try:
                    __zt_tmp = __attrs_140235426060624
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235426061584 = _static_140235435449424('path', u'view/base_render', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/base_render' (14:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ac15790> -> __condition
                __expression = __cache_140235426061584

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div>\n          </div>')
                else:
                    __content = __cache_140235426061584
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </ul>\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1ac150d0> name=None at 7f8b1ac15850> -> __attrs_140235426059728
                __attrs_140235426059728 = _static_140235426058448

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul id="personal-bar-container">\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b17a6a7d0> name=None at 7f8b1ac15250> -> __attrs_140235373978704
                __attrs_140235373978704 = _static_140235373979600

                # <Value u'personal_bar/user_actions' (19:29)> -> __condition
                __token = 906
                try:
                    __zt_tmp = __attrs_140235373978704
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'personal_bar/user_actions', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li id="portal-personaltools" class="plone-toolbar-separator">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b17a6ae10> name=None at 7f8b17a6a190> -> __attrs_140235426054928
                    __attrs_140235426054928 = _static_140235373981200

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373979472
                    __default_140235373979472 = _DEFAULT_MARKER

                    # <Substitution u'personal_bar/homelink_url' (21:36)> -> __attr_href
                    __token = 994
                    try:
                        __zt_tmp = __attrs_140235426054928
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140235435449424('path', u'personal_bar/homelink_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8b1ac14050> name=None at 7f8b1ac14c10> -> __attrs_140235426056464
                    __attrs_140235426056464 = _static_140235426054224

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="icon-user" aria-hidden="true"></span>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426114640
                    __attrs_140235426114640 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426113168
                    __default_140235426113168 = _DEFAULT_MARKER

                    # <Value u'personal_bar/user_name' (23:33)> -> __cache_140235426112464
                    __token = 1120
                    try:
                        __zt_tmp = __attrs_140235426114640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235426112464 = _static_140235435449424('path', u'personal_bar/user_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'personal_bar/user_name' (23:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ac22bd0> -> __condition
                    __expression = __cache_140235426112464

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'User')
                    else:
                        __content = __cache_140235426112464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8b1ac22ed0> name=None at 7f8b1ac227d0> -> __attrs_140235426112208
                    __attrs_140235426112208 = _static_140235426115280

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="plone-toolbar-caret"></span>\n            </a>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426115088
                    __attrs_140235426115088 = _static_140235489934800

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8b1ac22b10> name=None at 7f8b1ac22b50> -> __attrs_140235427768144
                    __attrs_140235427768144 = _static_140235426114320

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li class="plone-toolbar-submenu-header">\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427767504
                    __attrs_140235427767504 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427770064
                    __default_140235427770064 = _DEFAULT_MARKER

                    # <Value u'personal_bar/user_name' (28:35)> -> __cache_140235427766416
                    __token = 1337
                    try:
                        __zt_tmp = __attrs_140235427767504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235427766416 = _static_140235435449424('path', u'personal_bar/user_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'personal_bar/user_name' (28:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1adb6510> -> __condition
                    __expression = __cache_140235427766416

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'Username')
                    else:
                        __content = __cache_140235427766416
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n              </li>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8b1c440790> name=None at 7f8b1adb6e10> -> __attrs_140235451401104
                    __attrs_140235451401104 = _static_140235451402128
                    __backup_action_140235373980112 = get('action', __marker)

                    # <Value u'personal_bar/user_actions' (31:37)> -> __iterator
                    __token = 1472
                    try:
                        __zt_tmp = __attrs_140235451401104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140235435449424('path', u'personal_bar/user_actions', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    (__iterator, ____index_140235451402768, ) = getitem('repeat')(u'action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="user-action">\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8b1c440f50> name=None at 7f8b1c440950> -> __attrs_140235451401232
                        __attrs_140235451401232 = _static_140235451404112

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Value u'action' (32:43)> -> __cache_140235451400784
                        __token = 1543
                        try:
                            __zt_tmp = __attrs_140235451401232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235451400784 = _static_140235435449424('path', u'action', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        if (u'href' not in __chain(__cache_140235451400784)):
                            __append(u' href=""')
                        __attr_140235451400272 = __cache_140235451400784
                        for (name, value, ) in __attr_140235451400272.items():
                            if ((name not in _static_140235385307216) and (value is not None)):
                                __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                        __append(u'>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373956432
                        __attrs_140235373956432 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451404240
                        __default_140235451404240 = _DEFAULT_MARKER

                        # <Value u'action/title' (33:47)> -> __cache_140235451401552
                        __token = 1599
                        try:
                            __zt_tmp = __attrs_140235373956432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235451401552 = _static_140235435449424('path', u'action/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'action/title' (33:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1c440450> -> __condition
                        __expression = __cache_140235451401552

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                     action title\n                  ')
                        else:
                            __content = __cache_140235451401552
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373955216
                        __attrs_140235373955216 = _static_140235489934800

                        # <Value u"python:action['id'] == 'personaltools-logout'" (36:43)> -> __condition
                        __token = 1727
                        try:
                            __zt_tmp = __attrs_140235373955216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140235435449424('python', u"action['id'] == 'personaltools-logout'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        if __condition:
                            __append(u'\n                    ')

                            # <Static value=<_ast.Dict object at 0x7f8b17a649d0> name=None at 7f8b17a64c50> -> __attrs_140235373954768
                            __attrs_140235373954768 = _static_140235373955536

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="icon-logout"></span>\n                  ')
                        __append(u'\n                </a>\n              </li>')
                        ____index_140235451402768 -= 1
                        if (____index_140235451402768 > 0):
                            __append('\n              ')
                    if (__backup_action_140235373980112 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_140235373980112
                    __append(u'\n            </ul>\n          </li>')
                __append(u'\n        </ul>\n      </nav>\n    </div>\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_140235374543312
            if (__backup_personal_bar_140235426057104 is __marker):
                del econtext['personal_bar']
            else:
                econtext['personal_bar'] = __backup_personal_bar_140235426057104
            if (__backup_context_state_140235432665744 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_140235432665744
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
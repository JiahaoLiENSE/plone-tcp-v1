# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.contentmenu-2.3.4-py2.7.egg/plone/app/contentmenu/contentmenu.pt'

__tokens = {72: (u'view/menu', 3, 17), 39: (u'view/available', 2, 15), 139: (u'menu', 5, 30), 228: (u'menuItem/submenu', 8, 28), 276: (u' menuItem/extra/i', 9, 30), 181: (u'menuItem/extra/id', 7, 27), 707: (u'menuItem/extra/class | nothing', 17, 34), 772: (u" python:state_class and state_class or '", 18, 33), 391: (u"python:menuItem['action'] or 'javascript:void(0)'", 13, 31), 473: (u" python:not menuItem['action'] and 'cursor: default;; pointer-events: none' or No", 14, 31), 587: (u'le menuItem/descript', 15, 29), 640: (u'ass string:label-${state_cl', 16, 28), 1023: (u'menuItem/extra/stateTitle | nothing', 24, 27), 927: (u'string:icon-${identifier} ${menuItem/extra/class} toolbar-menu-icon', 23, 34), 1240: (u'not: menuItem/extra/stateTitle | nothing', 29, 27), 1168: (u'string:icon-${identifier} toolbar-menu-icon', 28, 34), 1318: (u'not: menuItem/extra/stateTitle | nothing', 30, 28), 1478: (u'menuItem/title', 34, 27), 1655: (u'menuItem/extra/shortTitle | menuItem/title', 40, 25), 1867: (u'menuItem/extra/stateTitle | nothing', 46, 29), 1931: (u'menuItem/extra/stateTitle', 47, 27), 2104: (u'not:menuItem/extra/hideChildren | not:submenu | nothing', 53, 27), 2244: (u'not:menuItem/extra/hideChildren | not:submenu | nothing', 57, 25), 2382: (u'not:menuItem/extra/stateTitle | nothing', 59, 30), 2455: (u'menuItem/title', 60, 31), 2642: (u'menuItem/extra/stateTitle | nothing', 64, 31), 2579: (u'string:${menuItem/extra/class}', 63, 38), 2708: (u'menuItem/extra/stateTitle', 65, 29), 2974: (u'submenu', 72, 36), 2862: (u'string:${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator}', 71, 34), 3426: (u'subMenuItem/action', 81, 29), 3093: (u'subMenuItem/action', 76, 35), 3148: (u' subMenuItem/descriptio', 77, 35), 3205: (u'd subMenuItem/extra/id | nothi', 78, 31), 3272: (u'ss subMenuItem/extra/class | noth', 79, 33), 3357: (u'dal subMenuItem/extra/modal | not', 80, 47), 3505: (u'subMenuItem/title', 83, 35), 3806: (u'not:subMenuItem/action', 91, 29), 3674: (u'subMenuItem/extra/id | nothing', 89, 33), 3741: (u' subMenuItem/extra/class | nothin', 90, 35), 3922: (u'subMenuItem/title', 94, 39)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386071147472 = {u'class': u'plone-toolbar-short-title', }
_static_140386069892944 = {u'class': u'subMenuItem/extra/class | nothing', u'href': u'#', u'id': u'subMenuItem/extra/id | nothing', u'data-pat-plone-modal': u'subMenuItem/extra/modal | nothing', u'title': u'subMenuItem/description', }
_static_140386071809552 = {u'class': u'', u'aria-hidden': u'true', }
_static_140386071311184 = {u'class': u'plone-toolbar-caret', }
_static_140386079220240 = {u'style': u"python:not menuItem['action'] and 'cursor: default; pointer-events: none' or None", u'href': u'#', u'class': u'string:label-${state_class}', u'title': u'menuItem/description', }
_static_140386071147216 = {u'class': u'plone-toolbar-title', }
_static_140386069982672 = {u'class': u'string:${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator}', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386071190224 = {u'id': u'menuItem/extra/id', }
_static_140386186296528 = __compile_zt_expr
_static_140386072585232 = {u'class': u'string:${menuItem/extra/class}', }
_static_140386078077904 = {u'id': u'subMenuItem/extra/id | nothing', u'class': u'subMenuItem/extra/class | nothing', }
_static_140386069981200 = {u'class': u'plone-toolbar-submenu-header', }
_static_140386071806480 = {u'class': u'', u'aria-hidden': u'true', }
_static_140386069979728 = {u'aria-hidden': u'true', }
_static_140386071147984 = {u'class': u'plone-toolbar-state-title', }
_static_140386247937936 = {}

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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071926032
            __attrs_140386071926032 = _static_140386247937936
            __backup_menu_140386069890448 = get('menu', __marker)

            # <Value u'view/menu' (3:17)> -> __value
            __token = 72
            try:
                __zt_tmp = __attrs_140386071926032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/menu', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['menu'] = __value

            # <Value u'view/available' (2:15)> -> __condition
            __token = 39
            try:
                __zt_tmp = __attrs_140386071926032
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'view/available', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140386071926160 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071187536
                __attrs_140386071187536 = _static_140386247937936
                __backup_menuItem_140386078063568 = get('menuItem', __marker)

                # <Value u'menu' (5:30)> -> __iterator
                __token = 139
                try:
                    __zt_tmp = __attrs_140386071187536
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'menu', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386071190736, ) = getitem('repeat')(u'menuItem', __iterator)
                econtext['menuItem'] = None
                for __item in __iterator:
                    econtext['menuItem'] = __item
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae2de79ad0> name=None at 7fae2de79850> -> __attrs_140386073253008
                    __attrs_140386073253008 = _static_140386071190224
                    __backup_submenu_140386070084176 = get('submenu', __marker)

                    # <Value u'menuItem/submenu' (8:28)> -> __value
                    __token = 228
                    try:
                        __zt_tmp = __attrs_140386073253008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'menuItem/submenu', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['submenu'] = __value
                    __backup_identifier_140386071806928 = get('identifier', __marker)

                    # <Value u'menuItem/extra/id' (9:30)> -> __value
                    __token = 276
                    try:
                        __zt_tmp = __attrs_140386073253008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'menuItem/extra/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['identifier'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071188944
                    __default_140386071188944 = _DEFAULT_MARKER

                    # <Substitution u'menuItem/extra/id' (7:27)> -> __attr_id
                    __token = 181
                    try:
                        __zt_tmp = __attrs_140386073253008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140386186296528('path', u'menuItem/extra/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae2e622210> name=None at 7fae2e6222d0> -> __attrs_140386071806608
                    __attrs_140386071806608 = _static_140386079220240
                    __backup_state_class_140386070082960 = get('state_class', __marker)

                    # <Value u'menuItem/extra/class | nothing' (17:34)> -> __value
                    __token = 707
                    try:
                        __zt_tmp = __attrs_140386071806608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'menuItem/extra/class | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['state_class'] = __value
                    __backup_state_class_140386070082448 = get('state_class', __marker)

                    # <Value u"python:state_class and state_class or ''" (18:33)> -> __value
                    __token = 772
                    try:
                        __zt_tmp = __attrs_140386071806608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u"state_class and state_class or ''", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['state_class'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079221648
                    __default_140386079221648 = _DEFAULT_MARKER

                    # <Substitution u"python:menuItem['action'] or 'javascript:void(0)'" (13:31)> -> __attr_href
                    __token = 391
                    try:
                        __zt_tmp = __attrs_140386071806608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('python', u"menuItem['action'] or 'javascript:void(0)'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079223504
                    __default_140386079223504 = _DEFAULT_MARKER

                    # <Substitution u"python:not menuItem['action'] and 'cursor: default; pointer-events: none' or None" (14:31)> -> __attr_style
                    __token = 473
                    try:
                        __zt_tmp = __attrs_140386071806608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_140386186296528('python', u"not menuItem['action'] and 'cursor: default; pointer-events: none' or None", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((u' style="%s"' % __attr_style))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071808016
                    __default_140386071808016 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<Substitution u'menuItem/description' (15:29)> at 7fae2e622d90> -> __attr_title

                    # <Substitution u'menuItem/description' (15:29)> -> __attr_title
                    __token = 587
                    try:
                        __zt_tmp = __attrs_140386071806608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140386186296528('path', u'menuItem/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071806096
                    __default_140386071806096 = _DEFAULT_MARKER

                    # <Substitution u'string:label-${state_class}' (16:28)> -> __attr_class
                    __token = 640
                    try:
                        __zt_tmp = __attrs_140386071806608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140386186296528('string', u'label-${state_class}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u' >\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2df10210> name=None at 7fae2df10050> -> __attrs_140386071808720
                    __attrs_140386071808720 = _static_140386071806480

                    # <Value u'menuItem/extra/stateTitle | nothing' (24:27)> -> __condition
                    __token = 1023
                    try:
                        __zt_tmp = __attrs_140386071808720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span aria-hidden="true"')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071807952
                        __default_140386071807952 = _DEFAULT_MARKER

                        # <Substitution u'string:icon-${identifier} ${menuItem/extra/class} toolbar-menu-icon' (23:34)> -> __attr_class
                        __token = 927
                        try:
                            __zt_tmp = __attrs_140386071808720
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140386186296528('string', u'icon-${identifier} ${menuItem/extra/class} toolbar-menu-icon', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'></span>')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2df10e10> name=None at 7fae2df10cd0> -> __attrs_140386070895824
                    __attrs_140386070895824 = _static_140386071809552

                    # <Value u'not: menuItem/extra/stateTitle | nothing' (29:27)> -> __condition
                    __token = 1240
                    try:
                        __zt_tmp = __attrs_140386070895824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('not', u' menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span aria-hidden="true"')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070895568
                        __default_140386070895568 = _DEFAULT_MARKER

                        # <Substitution u'string:icon-${identifier} toolbar-menu-icon' (28:34)> -> __attr_class
                        __token = 1168
                        try:
                            __zt_tmp = __attrs_140386070895824
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140386186296528('string', u'icon-${identifier} toolbar-menu-icon', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'></span>')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070895376
                    __attrs_140386070895376 = _static_140386247937936

                    # <Negate value=<Value u'not: menuItem/extra/stateTitle | nothing' (30:28)> at 7fae2de31890> -> __cache_140386070894736

                    # <Value u'not: menuItem/extra/stateTitle | nothing' (30:28)> -> __cache_140386070894736
                    __token = 1318
                    try:
                        __zt_tmp = __attrs_140386070895376
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386070894736 = _static_140386186296528('not', u' menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __cache_140386070894736 = not __cache_140386070894736
                    __condition = __cache_140386070894736
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7fae2de6f2d0> name=None at 7fae2de6f850> -> __attrs_140386071147664
                    __attrs_140386071147664 = _static_140386071147216

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="plone-toolbar-title">')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071148240
                    __default_140386071148240 = _DEFAULT_MARKER

                    # <Value u'menuItem/title' (34:27)> -> __cache_140386070895696
                    __token = 1478
                    try:
                        __zt_tmp = __attrs_140386071147664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386070895696 = _static_140386186296528('path', u'menuItem/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'menuItem/title' (34:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de31f50> -> __condition
                    __expression = __cache_140386070895696

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n              Menu Title\n            ')
                    else:
                        __content = __cache_140386070895696
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2de6f3d0> name=None at 7fae2de6f9d0> -> __attrs_140386071146768
                    __attrs_140386071146768 = _static_140386071147472

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="plone-toolbar-short-title">')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071147024
                    __default_140386071147024 = _DEFAULT_MARKER

                    # <Value u'menuItem/extra/shortTitle | menuItem/title' (40:25)> -> __cache_140386071149904
                    __token = 1655
                    try:
                        __zt_tmp = __attrs_140386071146768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386071149904 = _static_140386186296528('path', u'menuItem/extra/shortTitle | menuItem/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'menuItem/extra/shortTitle | menuItem/title' (40:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de6fa10> -> __condition
                    __expression = __cache_140386071149904

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n            Short Title\n          ')
                    else:
                        __content = __cache_140386071149904
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fae2de6f5d0> name=None at 7fae2de6ff50> -> __attrs_140386071312848
                    __attrs_140386071312848 = _static_140386071147984

                    # <Value u'menuItem/extra/stateTitle | nothing' (46:29)> -> __condition
                    __token = 1867
                    try:
                        __zt_tmp = __attrs_140386071312848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="plone-toolbar-state-title">')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071150480
                        __default_140386071150480 = _DEFAULT_MARKER

                        # <Value u'menuItem/extra/stateTitle' (47:27)> -> __cache_140386071147728
                        __token = 1931
                        try:
                            __zt_tmp = __attrs_140386071312848
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386071147728 = _static_140386186296528('path', u'menuItem/extra/stateTitle', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'menuItem/extra/stateTitle' (47:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de6f190> -> __condition
                        __expression = __cache_140386071147728

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                State title\n            ')
                        else:
                            __content = __cache_140386071147728
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>')
                    __append(u'\n        ')
                    __condition = __cache_140386070894736
                    if __condition:
                        __append(u'</span>')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2de97350> name=None at 7fae2de31b90> -> __attrs_140386071312528
                    __attrs_140386071312528 = _static_140386071311184

                    # <Value u'not:menuItem/extra/hideChildren | not:submenu | nothing' (53:27)> -> __condition
                    __token = 2104
                    try:
                        __zt_tmp = __attrs_140386071312528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('not', u'menuItem/extra/hideChildren | not:submenu | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="plone-toolbar-caret"></span>')
                    __append(u'\n      </a>')
                    if (__backup_state_class_140386070082448 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_140386070082448
                    if (__backup_state_class_140386070082960 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_140386070082960
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae2dd52250> name=None at 7fae2de97b90> -> __attrs_140386069981456
                    __attrs_140386069981456 = _static_140386069979728

                    # <Value u'not:menuItem/extra/hideChildren | not:submenu | nothing' (57:25)> -> __condition
                    __token = 2244
                    try:
                        __zt_tmp = __attrs_140386069981456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('not', u'menuItem/extra/hideChildren | not:submenu | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<ul aria-hidden="true">\n        ')

                        # <Static value=<_ast.Dict object at 0x7fae2dd52810> name=None at 7fae2dd52190> -> __attrs_140386069980368
                        __attrs_140386069980368 = _static_140386069981200

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="plone-toolbar-submenu-header">\n          ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069982096
                        __attrs_140386069982096 = _static_140386247937936

                        # <Negate value=<Value u'not:menuItem/extra/stateTitle | nothing' (59:30)> at 7fae2dd52ad0> -> __cache_140386069981904

                        # <Value u'not:menuItem/extra/stateTitle | nothing' (59:30)> -> __cache_140386069981904
                        __token = 2382
                        try:
                            __zt_tmp = __attrs_140386069982096
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386069981904 = _static_140386186296528('not', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __cache_140386069981904 = not __cache_140386069981904
                        __condition = __cache_140386069981904
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072584976
                        __attrs_140386072584976 = _static_140386247937936

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072588112
                        __default_140386072588112 = _DEFAULT_MARKER

                        # <Value u'menuItem/title' (60:31)> -> __cache_140386072584272
                        __token = 2455
                        try:
                            __zt_tmp = __attrs_140386072584976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386072584272 = _static_140386186296528('path', u'menuItem/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'menuItem/title' (60:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dfce790> -> __condition
                        __expression = __cache_140386072584272

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Menu Title')
                        else:
                            __content = __cache_140386072584272
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fae2dfce410> name=None at 7fae2dfceb90> -> __attrs_140386072584592
                        __attrs_140386072584592 = _static_140386072585232

                        # <Value u'menuItem/extra/stateTitle | nothing' (64:31)> -> __condition
                        __token = 2642
                        try:
                            __zt_tmp = __attrs_140386072584592
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('path', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072584336
                            __default_140386072584336 = _DEFAULT_MARKER

                            # <Substitution u'string:${menuItem/extra/class}' (63:38)> -> __attr_class
                            __token = 2579
                            try:
                                __zt_tmp = __attrs_140386072584592
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140386186296528('string', u'${menuItem/extra/class}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072585616
                            __default_140386072585616 = _DEFAULT_MARKER

                            # <Value u'menuItem/extra/stateTitle' (65:29)> -> __cache_140386072585296
                            __token = 2708
                            try:
                                __zt_tmp = __attrs_140386072584592
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140386072585296 = _static_140386186296528('path', u'menuItem/extra/stateTitle', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                            # <BinOp left=<Value u'menuItem/extra/stateTitle' (65:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dfced50> -> __condition
                            __expression = __cache_140386072585296

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n                State title\n            ')
                            else:
                                __content = __cache_140386072585296
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>')
                        __append(u'\n          ')
                        __condition = __cache_140386069981904
                        if __condition:
                            __append(u'</span>')
                        __append(u'\n        </li>\n        ')

                        # <Static value=<_ast.Dict object at 0x7fae2dd52dd0> name=None at 7fae2dd52d90> -> __attrs_140386069892176
                        __attrs_140386069892176 = _static_140386069982672
                        __backup_subMenuItem_140386070486864 = get('subMenuItem', __marker)

                        # <Value u'submenu' (72:36)> -> __iterator
                        __token = 2974
                        try:
                            __zt_tmp = __attrs_140386069892176
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140386186296528('path', u'submenu', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        (__iterator, ____index_140386069889616, ) = getitem('repeat')(u'subMenuItem', __iterator)
                        econtext['subMenuItem'] = None
                        for __item in __iterator:
                            econtext['subMenuItem'] = __item

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<li')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069890064
                            __default_140386069890064 = _DEFAULT_MARKER

                            # <Substitution u'string:${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator}' (71:34)> -> __attr_class
                            __token = 2862
                            try:
                                __zt_tmp = __attrs_140386069892176
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140386186296528('string', u'${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>\n          ')

                            # <Static value=<_ast.Dict object at 0x7fae2dd3cf50> name=None at 7fae2dd3cb10> -> __attrs_140386078077840
                            __attrs_140386078077840 = _static_140386069892944

                            # <Value u'subMenuItem/action' (81:29)> -> __condition
                            __token = 3426
                            try:
                                __zt_tmp = __attrs_140386078077840
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('path', u'subMenuItem/action', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<a')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069891984
                                __default_140386069891984 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/action' (76:35)> -> __attr_href
                                __token = 3093
                                try:
                                    __zt_tmp = __attrs_140386078077840
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140386186296528('path', u'subMenuItem/action', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((u' href="%s"' % __attr_href))

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069890576
                                __default_140386069890576 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<Substitution u'subMenuItem/description' (77:35)> at 7fae2dd3cd90> -> __attr_title

                                # <Substitution u'subMenuItem/description' (77:35)> -> __attr_title
                                __token = 3148
                                try:
                                    __zt_tmp = __attrs_140386078077840
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_title = _static_140386186296528('path', u'subMenuItem/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                if (__attr_title is not None):
                                    __append((u' title="%s"' % __attr_title))

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069890512
                                __default_140386069890512 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/id | nothing' (78:31)> -> __attr_id
                                __token = 3205
                                try:
                                    __zt_tmp = __attrs_140386078077840
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140386186296528('path', u'subMenuItem/extra/id | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069891664
                                __default_140386069891664 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/class | nothing' (79:33)> -> __attr_class
                                __token = 3272
                                try:
                                    __zt_tmp = __attrs_140386078077840
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140386186296528('path', u'subMenuItem/extra/class | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((u' class="%s"' % __attr_class))

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069889680
                                __default_140386069889680 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/modal | nothing' (80:47)> -> __attr_data_pat_plone_modal
                                __token = 3357
                                try:
                                    __zt_tmp = __attrs_140386078077840
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_data_pat_plone_modal = _static_140386186296528('path', u'subMenuItem/extra/modal | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_data_pat_plone_modal is not None):
                                    __append((u' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                                __append(u'>\n            ')

                                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078077520
                                __attrs_140386078077520 = _static_140386247937936

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078080720
                                __default_140386078080720 = _DEFAULT_MARKER

                                # <Value u'subMenuItem/title' (83:35)> -> __cache_140386078077968
                                __token = 3505
                                try:
                                    __zt_tmp = __attrs_140386078077520
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140386078077968 = _static_140386186296528('path', u'subMenuItem/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                                # <BinOp left=<Value u'subMenuItem/title' (83:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e50ba90> -> __condition
                                __expression = __cache_140386078077968

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                  Title\n              ')
                                else:
                                    __content = __cache_140386078077968
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'\n          </a>')
                            __append(u'\n          ')

                            # <Static value=<_ast.Dict object at 0x7fae2e50b3d0> name=None at 7fae2e50b910> -> __attrs_140386078080080
                            __attrs_140386078080080 = _static_140386078077904

                            # <Value u'not:subMenuItem/action' (91:29)> -> __condition
                            __token = 3806
                            try:
                                __zt_tmp = __attrs_140386078080080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('not', u'subMenuItem/action', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078078224
                                __default_140386078078224 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/id | nothing' (89:33)> -> __attr_id
                                __token = 3674
                                try:
                                    __zt_tmp = __attrs_140386078080080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140386186296528('path', u'subMenuItem/extra/id | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078078928
                                __default_140386078078928 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/class | nothing' (90:35)> -> __attr_class
                                __token = 3741
                                try:
                                    __zt_tmp = __attrs_140386078080080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140386186296528('path', u'subMenuItem/extra/class | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((u' class="%s"' % __attr_class))
                                __append(u'>\n            ')

                                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071111184
                                __attrs_140386071111184 = _static_140386247937936

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071113616
                                __default_140386071113616 = _DEFAULT_MARKER

                                # <Value u'subMenuItem/title' (94:39)> -> __cache_140386071109712
                                __token = 3922
                                try:
                                    __zt_tmp = __attrs_140386071111184
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140386071109712 = _static_140386186296528('path', u'subMenuItem/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                                # <BinOp left=<Value u'subMenuItem/title' (94:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de665d0> -> __condition
                                __expression = __cache_140386071109712

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                  Title\n              ')
                                else:
                                    __content = __cache_140386071109712
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n          </span>')
                            __append(u'\n        </li>')
                            ____index_140386069889616 -= 1
                            if (____index_140386069889616 > 0):
                                __append('\n        ')
                        if (__backup_subMenuItem_140386070486864 is __marker):
                            del econtext['subMenuItem']
                        else:
                            econtext['subMenuItem'] = __backup_subMenuItem_140386070486864
                        __append(u'\n      </ul>')
                    __append(u'\n    </li>')
                    if (__backup_identifier_140386071806928 is __marker):
                        del econtext['identifier']
                    else:
                        econtext['identifier'] = __backup_identifier_140386071806928
                    if (__backup_submenu_140386070084176 is __marker):
                        del econtext['submenu']
                    else:
                        econtext['submenu'] = __backup_submenu_140386070084176
                    __append(u'\n  ')
                    ____index_140386071190736 -= 1
                    if (____index_140386071190736 > 0):
                        __append('')
                if (__backup_menuItem_140386078063568 is __marker):
                    del econtext['menuItem']
                else:
                    econtext['menuItem'] = __backup_menuItem_140386078063568
                __append(u'\n')
                __i18n_domain = __previous_i18n_domain_140386071926160
            if (__backup_menu_140386069890448 is __marker):
                del econtext['menu']
            else:
                econtext['menu'] = __backup_menu_140386069890448
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.contentmenu-2.3.4-py2.7.egg/plone/app/contentmenu/contentmenu.pt'

__tokens = {72: (u'view/menu', 3, 17), 39: (u'view/available', 2, 15), 139: (u'menu', 5, 30), 228: (u'menuItem/submenu', 8, 28), 276: (u' menuItem/extra/i', 9, 30), 181: (u'menuItem/extra/id', 7, 27), 707: (u'menuItem/extra/class | nothing', 17, 34), 772: (u" python:state_class and state_class or '", 18, 33), 391: (u"python:menuItem['action'] or 'javascript:void(0)'", 13, 31), 473: (u" python:not menuItem['action'] and 'cursor: default;; pointer-events: none' or No", 14, 31), 587: (u'le menuItem/descript', 15, 29), 640: (u'ass string:label-${state_cl', 16, 28), 1023: (u'menuItem/extra/stateTitle | nothing', 24, 27), 927: (u'string:icon-${identifier} ${menuItem/extra/class} toolbar-menu-icon', 23, 34), 1240: (u'not: menuItem/extra/stateTitle | nothing', 29, 27), 1168: (u'string:icon-${identifier} toolbar-menu-icon', 28, 34), 1318: (u'not: menuItem/extra/stateTitle | nothing', 30, 28), 1478: (u'menuItem/title', 34, 27), 1655: (u'menuItem/extra/shortTitle | menuItem/title', 40, 25), 1867: (u'menuItem/extra/stateTitle | nothing', 46, 29), 1931: (u'menuItem/extra/stateTitle', 47, 27), 2104: (u'not:menuItem/extra/hideChildren | not:submenu | nothing', 53, 27), 2244: (u'not:menuItem/extra/hideChildren | not:submenu | nothing', 57, 25), 2382: (u'not:menuItem/extra/stateTitle | nothing', 59, 30), 2455: (u'menuItem/title', 60, 31), 2642: (u'menuItem/extra/stateTitle | nothing', 64, 31), 2579: (u'string:${menuItem/extra/class}', 63, 38), 2708: (u'menuItem/extra/stateTitle', 65, 29), 2974: (u'submenu', 72, 36), 2862: (u'string:${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator}', 71, 34), 3426: (u'subMenuItem/action', 81, 29), 3093: (u'subMenuItem/action', 76, 35), 3148: (u' subMenuItem/descriptio', 77, 35), 3205: (u'd subMenuItem/extra/id | nothi', 78, 31), 3272: (u'ss subMenuItem/extra/class | noth', 79, 33), 3357: (u'dal subMenuItem/extra/modal | not', 80, 47), 3505: (u'subMenuItem/title', 83, 35), 3806: (u'not:subMenuItem/action', 91, 29), 3674: (u'subMenuItem/extra/id | nothing', 89, 33), 3741: (u' subMenuItem/extra/class | nothin', 90, 35), 3922: (u'subMenuItem/title', 94, 39)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235451418960 = {u'aria-hidden': u'true', }
_static_140235451419408 = {u'class': u'plone-toolbar-submenu-header', }
_static_140235451403792 = {u'class': u'plone-toolbar-state-title', }
_static_140235385297744 = {u'class': u'', u'aria-hidden': u'true', }
_static_140235385322256 = {u'class': u'subMenuItem/extra/class | nothing', u'href': u'#', u'id': u'subMenuItem/extra/id | nothing', u'data-pat-plone-modal': u'subMenuItem/extra/modal | nothing', u'title': u'subMenuItem/description', }
_static_140235489934800 = {}
_static_140235451403664 = {u'class': u'plone-toolbar-caret', }
_static_140235435449424 = __compile_zt_expr
_static_140235451403472 = {u'class': u'plone-toolbar-short-title', }
_static_140235373954896 = {u'style': u"python:not menuItem['action'] and 'cursor: default; pointer-events: none' or None", u'href': u'#', u'class': u'string:label-${state_class}', u'title': u'menuItem/description', }
_static_140235385319504 = {u'class': u'string:${menuItem/extra/class}', }
_static_140235385294992 = {u'class': u'', u'aria-hidden': u'true', }
_static_140235432291984 = {u'id': u'menuItem/extra/id', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235426058896 = {u'class': u'string:${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator}', }
_static_140235374542992 = {u'class': u'plone-toolbar-title', }
_static_140235426107472 = {u'id': u'subMenuItem/extra/id | nothing', u'class': u'subMenuItem/extra/class | nothing', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432288912
            __attrs_140235432288912 = _static_140235489934800
            __backup_menu_140235377128016 = get('menu', __marker)

            # <Value u'view/menu' (3:17)> -> __value
            __token = 72
            try:
                __zt_tmp = __attrs_140235432288912
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/menu', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['menu'] = __value

            # <Value u'view/available' (2:15)> -> __condition
            __token = 39
            try:
                __zt_tmp = __attrs_140235432288912
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'view/available', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140235432289104 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432289424
                __attrs_140235432289424 = _static_140235489934800
                __backup_menuItem_140235374585040 = get('menuItem', __marker)

                # <Value u'menu' (5:30)> -> __iterator
                __token = 139
                try:
                    __zt_tmp = __attrs_140235432289424
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140235435449424('path', u'menu', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                (__iterator, ____index_140235432289232, ) = getitem('repeat')(u'menuItem', __iterator)
                econtext['menuItem'] = None
                for __item in __iterator:
                    econtext['menuItem'] = __item
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7f8b1b206e90> name=None at 7f8b1b206ad0> -> __attrs_140235373955088
                    __attrs_140235373955088 = _static_140235432291984
                    __backup_submenu_140235426058832 = get('submenu', __marker)

                    # <Value u'menuItem/submenu' (8:28)> -> __value
                    __token = 228
                    try:
                        __zt_tmp = __attrs_140235373955088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'menuItem/submenu', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['submenu'] = __value
                    __backup_identifier_140235428387728 = get('identifier', __marker)

                    # <Value u'menuItem/extra/id' (9:30)> -> __value
                    __token = 276
                    try:
                        __zt_tmp = __attrs_140235373955088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'menuItem/extra/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['identifier'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373954256
                    __default_140235373954256 = _DEFAULT_MARKER

                    # <Substitution u'menuItem/extra/id' (7:27)> -> __attr_id
                    __token = 181
                    try:
                        __zt_tmp = __attrs_140235373955088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140235435449424('path', u'menuItem/extra/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))
                    __append(u'>\n      ')

                    # <Static value=<_ast.Dict object at 0x7f8b17a64750> name=None at 7f8b17a64490> -> __attrs_140235385297488
                    __attrs_140235385297488 = _static_140235373954896
                    __backup_state_class_140235426107600 = get('state_class', __marker)

                    # <Value u'menuItem/extra/class | nothing' (17:34)> -> __value
                    __token = 707
                    try:
                        __zt_tmp = __attrs_140235385297488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'menuItem/extra/class | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['state_class'] = __value
                    __backup_state_class_140235432668816 = get('state_class', __marker)

                    # <Value u"python:state_class and state_class or ''" (18:33)> -> __value
                    __token = 772
                    try:
                        __zt_tmp = __attrs_140235385297488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"state_class and state_class or ''", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['state_class'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373956176
                    __default_140235373956176 = _DEFAULT_MARKER

                    # <Substitution u"python:menuItem['action'] or 'javascript:void(0)'" (13:31)> -> __attr_href
                    __token = 391
                    try:
                        __zt_tmp = __attrs_140235385297488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140235435449424('python', u"menuItem['action'] or 'javascript:void(0)'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373953680
                    __default_140235373953680 = _DEFAULT_MARKER

                    # <Substitution u"python:not menuItem['action'] and 'cursor: default; pointer-events: none' or None" (14:31)> -> __attr_style
                    __token = 473
                    try:
                        __zt_tmp = __attrs_140235385297488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_140235435449424('python', u"not menuItem['action'] and 'cursor: default; pointer-events: none' or None", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((u' style="%s"' % __attr_style))

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385296848
                    __default_140235385296848 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<Substitution u'menuItem/description' (15:29)> at 7f8b17a64790> -> __attr_title

                    # <Substitution u'menuItem/description' (15:29)> -> __attr_title
                    __token = 587
                    try:
                        __zt_tmp = __attrs_140235385297488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140235435449424('path', u'menuItem/description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385298384
                    __default_140235385298384 = _DEFAULT_MARKER

                    # <Substitution u'string:label-${state_class}' (16:28)> -> __attr_class
                    __token = 640
                    try:
                        __zt_tmp = __attrs_140235385297488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140235435449424('string', u'label-${state_class}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u' >\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b18535b50> name=None at 7f8b18535e90> -> __attrs_140235385296272
                    __attrs_140235385296272 = _static_140235385297744

                    # <Value u'menuItem/extra/stateTitle | nothing' (24:27)> -> __condition
                    __token = 1023
                    try:
                        __zt_tmp = __attrs_140235385296272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span aria-hidden="true"')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385295568
                        __default_140235385295568 = _DEFAULT_MARKER

                        # <Substitution u'string:icon-${identifier} ${menuItem/extra/class} toolbar-menu-icon' (23:34)> -> __attr_class
                        __token = 927
                        try:
                            __zt_tmp = __attrs_140235385296272
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140235435449424('string', u'icon-${identifier} ${menuItem/extra/class} toolbar-menu-icon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'></span>')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b18535090> name=None at 7f8b18535f10> -> __attrs_140235374545616
                    __attrs_140235374545616 = _static_140235385294992

                    # <Value u'not: menuItem/extra/stateTitle | nothing' (29:27)> -> __condition
                    __token = 1240
                    try:
                        __zt_tmp = __attrs_140235374545616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('not', u' menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span aria-hidden="true"')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374546064
                        __default_140235374546064 = _DEFAULT_MARKER

                        # <Substitution u'string:icon-${identifier} toolbar-menu-icon' (28:34)> -> __attr_class
                        __token = 1168
                        try:
                            __zt_tmp = __attrs_140235374545616
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140235435449424('string', u'icon-${identifier} toolbar-menu-icon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'></span>')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374546512
                    __attrs_140235374546512 = _static_140235489934800

                    # <Negate value=<Value u'not: menuItem/extra/stateTitle | nothing' (30:28)> at 7f8b17af41d0> -> __cache_140235374543312

                    # <Value u'not: menuItem/extra/stateTitle | nothing' (30:28)> -> __cache_140235374543312
                    __token = 1318
                    try:
                        __zt_tmp = __attrs_140235374546512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235374543312 = _static_140235435449424('not', u' menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __cache_140235374543312 = not __cache_140235374543312
                    __condition = __cache_140235374543312
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8b17af4090> name=None at 7f8b17af48d0> -> __attrs_140235451402128
                    __attrs_140235451402128 = _static_140235374542992

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="plone-toolbar-title">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374543504
                    __default_140235374543504 = _DEFAULT_MARKER

                    # <Value u'menuItem/title' (34:27)> -> __cache_140235374545872
                    __token = 1478
                    try:
                        __zt_tmp = __attrs_140235451402128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235374545872 = _static_140235435449424('path', u'menuItem/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'menuItem/title' (34:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17af4d90> -> __condition
                    __expression = __cache_140235374545872

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n              Menu Title\n            ')
                    else:
                        __content = __cache_140235374545872
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1c440cd0> name=None at 7f8b1c440f50> -> __attrs_140235451404048
                    __attrs_140235451404048 = _static_140235451403472

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="plone-toolbar-short-title">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451404240
                    __default_140235451404240 = _DEFAULT_MARKER

                    # <Value u'menuItem/extra/shortTitle | menuItem/title' (40:25)> -> __cache_140235451400976
                    __token = 1655
                    try:
                        __zt_tmp = __attrs_140235451404048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235451400976 = _static_140235435449424('path', u'menuItem/extra/shortTitle | menuItem/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'menuItem/extra/shortTitle | menuItem/title' (40:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1c440610> -> __condition
                    __expression = __cache_140235451400976

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n            Short Title\n          ')
                    else:
                        __content = __cache_140235451400976
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8b1c440e10> name=None at 7f8b1c440d50> -> __attrs_140235451402512
                    __attrs_140235451402512 = _static_140235451403792

                    # <Value u'menuItem/extra/stateTitle | nothing' (46:29)> -> __condition
                    __token = 1867
                    try:
                        __zt_tmp = __attrs_140235451402512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="plone-toolbar-state-title">')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451402000
                        __default_140235451402000 = _DEFAULT_MARKER

                        # <Value u'menuItem/extra/stateTitle' (47:27)> -> __cache_140235451403024
                        __token = 1931
                        try:
                            __zt_tmp = __attrs_140235451402512
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235451403024 = _static_140235435449424('path', u'menuItem/extra/stateTitle', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'menuItem/extra/stateTitle' (47:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1c440690> -> __condition
                        __expression = __cache_140235451403024

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                State title\n            ')
                        else:
                            __content = __cache_140235451403024
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>')
                    __append(u'\n        ')
                    __condition = __cache_140235374543312
                    if __condition:
                        __append(u'</span>')
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1c440d90> name=None at 7f8b1c440650> -> __attrs_140235451419216
                    __attrs_140235451419216 = _static_140235451403664

                    # <Value u'not:menuItem/extra/hideChildren | not:submenu | nothing' (53:27)> -> __condition
                    __token = 2104
                    try:
                        __zt_tmp = __attrs_140235451419216
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('not', u'menuItem/extra/hideChildren | not:submenu | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="plone-toolbar-caret"></span>')
                    __append(u'\n      </a>')
                    if (__backup_state_class_140235432668816 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_140235432668816
                    if (__backup_state_class_140235426107600 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_140235426107600
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7f8b1c444950> name=None at 7f8b17af4310> -> __attrs_140235451417488
                    __attrs_140235451417488 = _static_140235451418960

                    # <Value u'not:menuItem/extra/hideChildren | not:submenu | nothing' (57:25)> -> __condition
                    __token = 2244
                    try:
                        __zt_tmp = __attrs_140235451417488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('not', u'menuItem/extra/hideChildren | not:submenu | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<ul aria-hidden="true">\n        ')

                        # <Static value=<_ast.Dict object at 0x7f8b1c444b10> name=None at 7f8b1c444450> -> __attrs_140235451417744
                        __attrs_140235451417744 = _static_140235451419408

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="plone-toolbar-submenu-header">\n          ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426058512
                        __attrs_140235426058512 = _static_140235489934800

                        # <Negate value=<Value u'not:menuItem/extra/stateTitle | nothing' (59:30)> at 7f8b1c444d10> -> __cache_140235451419920

                        # <Value u'not:menuItem/extra/stateTitle | nothing' (59:30)> -> __cache_140235451419920
                        __token = 2382
                        try:
                            __zt_tmp = __attrs_140235426058512
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235451419920 = _static_140235435449424('not', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __cache_140235451419920 = not __cache_140235451419920
                        __condition = __cache_140235451419920
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                        __append(u'\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235385322128
                        __attrs_140235385322128 = _static_140235489934800

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426061648
                        __default_140235426061648 = _DEFAULT_MARKER

                        # <Value u'menuItem/title' (60:31)> -> __cache_140235426060112
                        __token = 2455
                        try:
                            __zt_tmp = __attrs_140235385322128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235426060112 = _static_140235435449424('path', u'menuItem/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'menuItem/title' (60:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ac15a90> -> __condition
                        __expression = __cache_140235426060112

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Menu Title')
                        else:
                            __content = __cache_140235426060112
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8b1853b050> name=None at 7f8b1853be10> -> __attrs_140235385321808
                        __attrs_140235385321808 = _static_140235385319504

                        # <Value u'menuItem/extra/stateTitle | nothing' (64:31)> -> __condition
                        __token = 2642
                        try:
                            __zt_tmp = __attrs_140235385321808
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140235435449424('path', u'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span')

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385319952
                            __default_140235385319952 = _DEFAULT_MARKER

                            # <Substitution u'string:${menuItem/extra/class}' (63:38)> -> __attr_class
                            __token = 2579
                            try:
                                __zt_tmp = __attrs_140235385321808
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140235435449424('string', u'${menuItem/extra/class}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>')

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385319632
                            __default_140235385319632 = _DEFAULT_MARKER

                            # <Value u'menuItem/extra/stateTitle' (65:29)> -> __cache_140235385320592
                            __token = 2708
                            try:
                                __zt_tmp = __attrs_140235385321808
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140235385320592 = _static_140235435449424('path', u'menuItem/extra/stateTitle', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                            # <BinOp left=<Value u'menuItem/extra/stateTitle' (65:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1853b590> -> __condition
                            __expression = __cache_140235385320592

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n                State title\n            ')
                            else:
                                __content = __cache_140235385320592
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>')
                        __append(u'\n          ')
                        __condition = __cache_140235451419920
                        if __condition:
                            __append(u'</span>')
                        __append(u'\n        </li>\n        ')

                        # <Static value=<_ast.Dict object at 0x7f8b1ac15290> name=None at 7f8b1c4440d0> -> __attrs_140235385321744
                        __attrs_140235385321744 = _static_140235426058896
                        __backup_subMenuItem_140235368735568 = get('subMenuItem', __marker)

                        # <Value u'submenu' (72:36)> -> __iterator
                        __token = 2974
                        try:
                            __zt_tmp = __attrs_140235385321744
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140235435449424('path', u'submenu', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        (__iterator, ____index_140235385322704, ) = getitem('repeat')(u'subMenuItem', __iterator)
                        econtext['subMenuItem'] = None
                        for __item in __iterator:
                            econtext['subMenuItem'] = __item

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<li')

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385323216
                            __default_140235385323216 = _DEFAULT_MARKER

                            # <Substitution u'string:${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator}' (71:34)> -> __attr_class
                            __token = 2862
                            try:
                                __zt_tmp = __attrs_140235385321744
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140235435449424('string', u'${menuItem/extra/li_class | nothing} ${subMenuItem/extra/separator}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_class is not None):
                                __append((u' class="%s"' % __attr_class))
                            __append(u'>\n          ')

                            # <Static value=<_ast.Dict object at 0x7f8b1853bb10> name=None at 7f8b1853b110> -> __attrs_140235426111248
                            __attrs_140235426111248 = _static_140235385322256

                            # <Value u'subMenuItem/action' (81:29)> -> __condition
                            __token = 3426
                            try:
                                __zt_tmp = __attrs_140235426111248
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('path', u'subMenuItem/action', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<a')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427769744
                                __default_140235427769744 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/action' (76:35)> -> __attr_href
                                __token = 3093
                                try:
                                    __zt_tmp = __attrs_140235426111248
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140235435449424('path', u'subMenuItem/action', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((u' href="%s"' % __attr_href))

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427769872
                                __default_140235427769872 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<Substitution u'subMenuItem/description' (77:35)> at 7f8b1adb6750> -> __attr_title

                                # <Substitution u'subMenuItem/description' (77:35)> -> __attr_title
                                __token = 3148
                                try:
                                    __zt_tmp = __attrs_140235426111248
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_title = _static_140235435449424('path', u'subMenuItem/description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                if (__attr_title is not None):
                                    __append((u' title="%s"' % __attr_title))

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427769168
                                __default_140235427769168 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/id | nothing' (78:31)> -> __attr_id
                                __token = 3205
                                try:
                                    __zt_tmp = __attrs_140235426111248
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140235435449424('path', u'subMenuItem/extra/id | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427766928
                                __default_140235427766928 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/class | nothing' (79:33)> -> __attr_class
                                __token = 3272
                                try:
                                    __zt_tmp = __attrs_140235426111248
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140235435449424('path', u'subMenuItem/extra/class | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((u' class="%s"' % __attr_class))

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426107664
                                __default_140235426107664 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/modal | nothing' (80:47)> -> __attr_data_pat_plone_modal
                                __token = 3357
                                try:
                                    __zt_tmp = __attrs_140235426111248
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_data_pat_plone_modal = _static_140235435449424('path', u'subMenuItem/extra/modal | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_data_pat_plone_modal is not None):
                                    __append((u' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                                __append(u'>\n            ')

                                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426108880
                                __attrs_140235426108880 = _static_140235489934800

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426110160
                                __default_140235426110160 = _DEFAULT_MARKER

                                # <Value u'subMenuItem/title' (83:35)> -> __cache_140235426108560
                                __token = 3505
                                try:
                                    __zt_tmp = __attrs_140235426108880
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140235426108560 = _static_140235435449424('path', u'subMenuItem/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                                # <BinOp left=<Value u'subMenuItem/title' (83:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ac21c90> -> __condition
                                __expression = __cache_140235426108560

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                  Title\n              ')
                                else:
                                    __content = __cache_140235426108560
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'\n          </a>')
                            __append(u'\n          ')

                            # <Static value=<_ast.Dict object at 0x7f8b1ac21050> name=None at 7f8b1ac21f50> -> __attrs_140235427785168
                            __attrs_140235427785168 = _static_140235426107472

                            # <Value u'not:subMenuItem/action' (91:29)> -> __condition
                            __token = 3806
                            try:
                                __zt_tmp = __attrs_140235427785168
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('not', u'subMenuItem/action', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426108240
                                __default_140235426108240 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/id | nothing' (89:33)> -> __attr_id
                                __token = 3674
                                try:
                                    __zt_tmp = __attrs_140235427785168
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140235435449424('path', u'subMenuItem/extra/id | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((u' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427783952
                                __default_140235427783952 = _DEFAULT_MARKER

                                # <Substitution u'subMenuItem/extra/class | nothing' (90:35)> -> __attr_class
                                __token = 3741
                                try:
                                    __zt_tmp = __attrs_140235427785168
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140235435449424('path', u'subMenuItem/extra/class | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_class is not None):
                                    __append((u' class="%s"' % __attr_class))
                                __append(u'>\n            ')

                                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427785872
                                __attrs_140235427785872 = _static_140235489934800

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<span>')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427784016
                                __default_140235427784016 = _DEFAULT_MARKER

                                # <Value u'subMenuItem/title' (94:39)> -> __cache_140235427784272
                                __token = 3922
                                try:
                                    __zt_tmp = __attrs_140235427785872
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140235427784272 = _static_140235435449424('path', u'subMenuItem/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                                # <BinOp left=<Value u'subMenuItem/title' (94:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1adba050> -> __condition
                                __expression = __cache_140235427784272

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append(u'\n                  Title\n              ')
                                else:
                                    __content = __cache_140235427784272
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</span>\n          </span>')
                            __append(u'\n        </li>')
                            ____index_140235385322704 -= 1
                            if (____index_140235385322704 > 0):
                                __append('\n        ')
                        if (__backup_subMenuItem_140235368735568 is __marker):
                            del econtext['subMenuItem']
                        else:
                            econtext['subMenuItem'] = __backup_subMenuItem_140235368735568
                        __append(u'\n      </ul>')
                    __append(u'\n    </li>')
                    if (__backup_identifier_140235428387728 is __marker):
                        del econtext['identifier']
                    else:
                        econtext['identifier'] = __backup_identifier_140235428387728
                    if (__backup_submenu_140235426058832 is __marker):
                        del econtext['submenu']
                    else:
                        econtext['submenu'] = __backup_submenu_140235426058832
                    __append(u'\n  ')
                    ____index_140235432289232 -= 1
                    if (____index_140235432289232 > 0):
                        __append('')
                if (__backup_menuItem_140235374585040 is __marker):
                    del econtext['menuItem']
                else:
                    econtext['menuItem'] = __backup_menuItem_140235374585040
                __append(u'\n')
                __i18n_domain = __previous_i18n_domain_140235432289104
            if (__backup_menu_140235377128016 is __marker):
                del econtext['menu']
            else:
                econtext['menu'] = __backup_menu_140235377128016
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
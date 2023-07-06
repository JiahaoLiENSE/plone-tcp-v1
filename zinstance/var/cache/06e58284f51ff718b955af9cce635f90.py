# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/toolbar.pt'

__tokens = {73: (u'view/context_state', 2, 35), 126: (u' python: view.get_personal_bar(', 3, 33), 184: (u'context_state/is_toolbar_visible', 4, 24), 323: (u'${view/get_options}', 6, 75), 325: (u'view/get_options', 6, 77), 477: (u'view/get_toolbar_logo', 9, 53), 569: (u'view/show_switcher', 11, 55), 714: (u'view/base_render', 14, 38), 906: (u'personal_bar/user_actions', 19, 29), 994: (u'personal_bar/homelink_url', 21, 36), 1120: (u'personal_bar/user_name', 23, 33), 1337: (u'personal_bar/user_name', 28, 35), 1472: (u'personal_bar/user_actions', 31, 37), 1543: (u'action', 32, 43), 1599: (u'action/title', 33, 47), 1727: (u"python:action['id'] == 'personaltools-logout'", 36, 43)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386078086928 = {u'class': u'user-action', }
_static_140386071497552 = {u'class': u'plone-toolbar-switcher', }
_static_140386078095760 = {u'id': u'portal-personaltools', u'class': u'plone-toolbar-separator', }
_static_140386071779408 = {u'class': u'icon-user', u'aria-hidden': u'true', }
_static_140386078152016 = {u'class': u'plone-toolbar-submenu-header', }
_static_140386071496912 = {u'src': u'view/get_toolbar_logo', u'alt': u'Plone Toolbar', }
_static_140386070740688 = {u'role': u'toolbar', u'id': u'edit-bar', }
_static_140386079111952 = {u'class': u'plone-toolbar-container', }
_static_140386078071312 = {u'class': u'plone-toolbar-main', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386071495504 = {u'class': u'plone-toolbar-logo', }
_static_140386072524880 = {u'class': u'icon-logout', }
_static_140386186296528 = __compile_zt_expr
_static_140386069891280 = set([])
_static_140386077787728 = {u'href': u'', }
_static_140386078042960 = {u'href': u'#', }
_static_140386071209488 = {u'data-pat-toolbar': u'${view/get_options}', u'role': u'toolbar', u'id': u'edit-zone', u'class': u'pat-toolbar', }
_static_140386179408208 = {u'id': u'personal-bar-container', }
_static_140386078154512 = {u'class': u'plone-toolbar-caret', }
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

            # <Static value=<_ast.Dict object at 0x7fae2de0bed0> name=None at 7fae2de0bb10> -> __attrs_140386073253136
            __attrs_140386073253136 = _static_140386070740688
            __backup_context_state_140386071779472 = get('context_state', __marker)

            # <Value u'view/context_state' (2:35)> -> __value
            __token = 73
            try:
                __zt_tmp = __attrs_140386073253136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/context_state', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_personal_bar_140386078099152 = get('personal_bar', __marker)

            # <Value u'python: view.get_personal_bar()' (3:33)> -> __value
            __token = 126
            try:
                __zt_tmp = __attrs_140386073253136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u' view.get_personal_bar()', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['personal_bar'] = __value

            # <Value u'context_state/is_toolbar_visible' (4:24)> -> __condition
            __token = 184
            try:
                __zt_tmp = __attrs_140386073253136
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'context_state/is_toolbar_visible', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140386073253776 = __i18n_domain
                __i18n_domain = u'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="edit-bar" role="toolbar">\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2de7e610> name=None at 7fae2e611350> -> __attrs_140386071624592
                __attrs_140386071624592 = _static_140386071209488

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="edit-zone" role="toolbar" class="pat-toolbar"')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071624976
                __default_140386071624976 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution u'${view/get_options}' (6:75)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fae2dee3750> -> __attr_data_pat_toolbar
                __token = 323
                __token = 325
                try:
                    __zt_tmp = __attrs_140386071624592
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_pat_toolbar = _static_140386186296528('path', u'view/get_options', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
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

                # <Static value=<_ast.Dict object at 0x7fae2e607b10> name=None at 7fae2de7e2d0> -> __attrs_140386195031888
                __attrs_140386195031888 = _static_140386079111952

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="plone-toolbar-container">\n      ')

                # <Static value=<_ast.Dict object at 0x7fae2dec4350> name=None at 7fae2dec4950> -> __attrs_140386071498512
                __attrs_140386071498512 = _static_140386071495504

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a class="plone-toolbar-logo">\n        ')

                # <Static value=<_ast.Dict object at 0x7fae2dec48d0> name=None at 7fae2dec4210> -> __attrs_140386071495312
                __attrs_140386071495312 = _static_140386071496912

                # <img ... (0:0)
                # --------------------------------------------------------
                __append(u'<img alt="Plone Toolbar"')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071496144
                __default_140386071496144 = _DEFAULT_MARKER

                # <Substitution u'view/get_toolbar_logo' (9:53)> -> __attr_src
                __token = 477
                try:
                    __zt_tmp = __attrs_140386071495312
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_140386186296528('path', u'view/get_toolbar_logo', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((u' src="%s"' % __attr_src))
                __append(u' />\n      </a>\n      ')

                # <Static value=<_ast.Dict object at 0x7fae2dec4b50> name=None at 7fae2dec4a10> -> __attrs_140386071496528
                __attrs_140386071496528 = _static_140386071497552

                # <Value u'view/show_switcher' (11:55)> -> __condition
                __token = 569
                try:
                    __zt_tmp = __attrs_140386071496528
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/show_switcher', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a class="plone-toolbar-switcher">')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078070928
                    __attrs_140386078070928 = _static_140386247937936

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>Left-Top switcher</span></a>')
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078069840
                __attrs_140386078069840 = _static_140386247937936

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append(u'<nav>\n        ')

                # <Static value=<_ast.Dict object at 0x7fae2e509a10> name=None at 7fae2e509b90> -> __attrs_140386078068944
                __attrs_140386078068944 = _static_140386078071312

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="plone-toolbar-main">\n          ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386179408592
                __attrs_140386179408592 = _static_140386247937936

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078118160
                __default_140386078118160 = _DEFAULT_MARKER

                # <Value u'view/base_render' (14:38)> -> __cache_140386078118480
                __token = 714
                try:
                    __zt_tmp = __attrs_140386179408592
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140386078118480 = _static_140386186296528('path', u'view/base_render', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/base_render' (14:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e5155d0> -> __condition
                __expression = __cache_140386078118480

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div>\n          </div>')
                else:
                    __content = __cache_140386078118480
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </ul>\n        ')

                # <Static value=<_ast.Dict object at 0x7fae345ae150> name=None at 7fae2e509f90> -> __attrs_140386179411664
                __attrs_140386179411664 = _static_140386179408208

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul id="personal-bar-container">\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2e50f990> name=None at 7fae2e50fc90> -> __attrs_140386078097168
                __attrs_140386078097168 = _static_140386078095760

                # <Value u'personal_bar/user_actions' (19:29)> -> __condition
                __token = 906
                try:
                    __zt_tmp = __attrs_140386078097168
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'personal_bar/user_actions', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li id="portal-personaltools" class="plone-toolbar-separator">\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae2e502b50> name=None at 7fae2e502610> -> __attrs_140386128026512
                    __attrs_140386128026512 = _static_140386078042960

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386128023760
                    __default_140386128023760 = _DEFAULT_MARKER

                    # <Substitution u'personal_bar/homelink_url' (21:36)> -> __attr_href
                    __token = 994
                    try:
                        __zt_tmp = __attrs_140386128026512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('path', u'personal_bar/homelink_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae2df09850> name=None at 7fae2df09390> -> __attrs_140386071780368
                    __attrs_140386071780368 = _static_140386071779408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="icon-user" aria-hidden="true"></span>\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071779536
                    __attrs_140386071779536 = _static_140386247937936

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071779728
                    __default_140386071779728 = _DEFAULT_MARKER

                    # <Value u'personal_bar/user_name' (23:33)> -> __cache_140386071780432
                    __token = 1120
                    try:
                        __zt_tmp = __attrs_140386071779536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386071780432 = _static_140386186296528('path', u'personal_bar/user_name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'personal_bar/user_name' (23:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2df09f50> -> __condition
                    __expression = __cache_140386071780432

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'User')
                    else:
                        __content = __cache_140386071780432
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae2e51df10> name=None at 7fae2df09750> -> __attrs_140386078151120
                    __attrs_140386078151120 = _static_140386078154512

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="plone-toolbar-caret"></span>\n            </a>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078153872
                    __attrs_140386078153872 = _static_140386247937936

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul>\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae2e51d550> name=None at 7fae2e51de50> -> __attrs_140386078151056
                    __attrs_140386078151056 = _static_140386078152016

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li class="plone-toolbar-submenu-header">\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078088528
                    __attrs_140386078088528 = _static_140386247937936

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078087376
                    __default_140386078087376 = _DEFAULT_MARKER

                    # <Value u'personal_bar/user_name' (28:35)> -> __cache_140386078154448
                    __token = 1337
                    try:
                        __zt_tmp = __attrs_140386078088528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386078154448 = _static_140386186296528('path', u'personal_bar/user_name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'personal_bar/user_name' (28:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e50d550> -> __condition
                    __expression = __cache_140386078154448

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'Username')
                    else:
                        __content = __cache_140386078154448
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n              </li>\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae2e50d710> name=None at 7fae2e51d790> -> __attrs_140386078061392
                    __attrs_140386078061392 = _static_140386078086928
                    __backup_action_140386072951312 = get('action', __marker)

                    # <Value u'personal_bar/user_actions' (31:37)> -> __iterator
                    __token = 1472
                    try:
                        __zt_tmp = __attrs_140386078061392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140386186296528('path', u'personal_bar/user_actions', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    (__iterator, ____index_140386078062800, ) = getitem('repeat')(u'action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="user-action">\n                ')

                        # <Static value=<_ast.Dict object at 0x7fae2e4c4650> name=None at 7fae2e4c4810> -> __attrs_140386077786576
                        __attrs_140386077786576 = _static_140386077787728

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Value u'action' (32:43)> -> __cache_140386077788368
                        __token = 1543
                        try:
                            __zt_tmp = __attrs_140386077786576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386077788368 = _static_140386186296528('path', u'action', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if (u'href' not in __chain(__cache_140386077788368)):
                            __append(u' href=""')
                        __attr_140386077789392 = __cache_140386077788368
                        for (name, value, ) in __attr_140386077789392.items():
                            if ((name not in _static_140386069891280) and (value is not None)):
                                __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                        __append(u'>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077788432
                        __attrs_140386077788432 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077787408
                        __default_140386077787408 = _DEFAULT_MARKER

                        # <Value u'action/title' (33:47)> -> __cache_140386077787536
                        __token = 1599
                        try:
                            __zt_tmp = __attrs_140386077788432
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386077787536 = _static_140386186296528('path', u'action/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'action/title' (33:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e4c46d0> -> __condition
                        __expression = __cache_140386077787536

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                     action title\n                  ')
                        else:
                            __content = __cache_140386077787536
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077789136
                        __attrs_140386077789136 = _static_140386247937936

                        # <Value u"python:action['id'] == 'personaltools-logout'" (36:43)> -> __condition
                        __token = 1727
                        try:
                            __zt_tmp = __attrs_140386077789136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('python', u"action['id'] == 'personaltools-logout'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:
                            __append(u'\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fae2dfbf850> name=None at 7fae2dfbff10> -> __attrs_140386072525456
                            __attrs_140386072525456 = _static_140386072524880

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span class="icon-logout"></span>\n                  ')
                        __append(u'\n                </a>\n              </li>')
                        ____index_140386078062800 -= 1
                        if (____index_140386078062800 > 0):
                            __append('\n              ')
                    if (__backup_action_140386072951312 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_140386072951312
                    __append(u'\n            </ul>\n          </li>')
                __append(u'\n        </ul>\n      </nav>\n    </div>\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_140386073253776
            if (__backup_personal_bar_140386078099152 is __marker):
                del econtext['personal_bar']
            else:
                econtext['personal_bar'] = __backup_personal_bar_140386078099152
            if (__backup_context_state_140386071779472 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_140386071779472
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
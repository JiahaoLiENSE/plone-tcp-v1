# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.locking-2.3.0-py2.7.egg/plone/locking/browser/info.pt'

__tokens = {77: (u'view/info/is_locked_for_current_user', 3, 24), 141: (u' view/lock_is_stealabl', 4, 26), 194: (u's view/lock_in', 5, 28), 238: (u'locked', 6, 24), 398: (u'lock_details/author_page', 11, 27), 647: (u'lock_details/author_page', 16, 34), 590: (u'lock_details/fullname', 15, 26), 738: (u'lock_details/time_difference', 18, 29), 858: (u'not:lock_details/author_page', 21, 27), 1060: (u'lock_details/fullname', 25, 29), 1148: (u'lock_details/time_difference', 27, 29), 1245: (u'stealable', 29, 29), 1293: (u'string:${context/absolute_url}/@@plone_lock_operations/force_unlock', 30, 37)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140235423489680 = {u'href': u'lock_details/author_page', }
_static_140235489934800 = {}
_static_140235426071184 = {u'id': u'plone-lock-status', }
_static_140235385267216 = {u'action': u'string:${context/absolute_url}/@@plone_lock_operations/force_unlock', u'method': u'POST', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235435449424 = __compile_zt_expr
_static_140235431317264 = {u'type': u'submit', u'value': u'Unlock', }
_static_140235385325968 = {u'class': u'portalMessage info', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1ac18290> name=None at 7f8b1ac185d0> -> __attrs_140235385326224
            __attrs_140235385326224 = _static_140235426071184
            __backup_locked_140235374309136 = get('locked', __marker)

            # <Value u'view/info/is_locked_for_current_user' (3:24)> -> __value
            __token = 77
            try:
                __zt_tmp = __attrs_140235385326224
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/info/is_locked_for_current_user', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['locked'] = __value
            __backup_stealable_140235373353808 = get('stealable', __marker)

            # <Value u'view/lock_is_stealable' (4:26)> -> __value
            __token = 141
            try:
                __zt_tmp = __attrs_140235385326224
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/lock_is_stealable', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['stealable'] = __value
            __backup_lock_details_140235374305616 = get('lock_details', __marker)

            # <Value u'view/lock_info' (5:28)> -> __value
            __token = 194
            try:
                __zt_tmp = __attrs_140235385326224
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/lock_info', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['lock_details'] = __value
            __previous_i18n_domain_140235385324048 = __i18n_domain
            __i18n_domain = u'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="plone-lock-status">\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235385324240
            __attrs_140235385324240 = _static_140235489934800

            # <Value u'locked' (6:24)> -> __condition
            __token = 238
            try:
                __zt_tmp = __attrs_140235385324240
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'locked', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1853c990> name=None at 7f8b1853ced0> -> __attrs_140235423489360
                __attrs_140235423489360 = _static_140235385325968

                # <dl ... (0:0)
                # --------------------------------------------------------
                __append(u'<dl class="portalMessage info">\n      ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235428385552
                __attrs_140235428385552 = _static_140235489934800

                # <dt ... (0:0)
                # --------------------------------------------------------
                __append(u'<dt>')
                __stream_140235428385296 = []
                __append_140235428385296 = __stream_140235428385296.append
                __append_140235428385296(u'Locked')
                __msgid_140235428385296 = __re_whitespace(''.join(__stream_140235428385296)).strip()
                if u'label_locked':
                    __append(translate(u'label_locked', mapping=None, default=__msgid_140235428385296, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</dt>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373759504
                __attrs_140235373759504 = _static_140235489934800

                # <dd ... (0:0)
                # --------------------------------------------------------
                __append(u'<dd>\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235385309648
                __attrs_140235385309648 = _static_140235489934800

                # <Value u'lock_details/author_page' (11:27)> -> __condition
                __token = 398
                try:
                    __zt_tmp = __attrs_140235385309648
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'lock_details/author_page', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:
                    __stream_140235428633488_author = ''
                    __stream_140235428633488_time = ''
                    __stream_140235373758352 = []
                    __append_140235373758352 = __stream_140235373758352.append
                    __append_140235373758352(u'\n          This item was locked by\n          ')
                    __stream_140235428633488_author = []
                    __append_140235428633488_author = __stream_140235428633488_author.append

                    # <Static value=<_ast.Dict object at 0x7f8b1a9a1e90> name=None at 7f8b1a9a1c10> -> __attrs_140235423486800
                    __attrs_140235423486800 = _static_140235423489680

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140235428633488_author(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423486160
                    __default_140235423486160 = _DEFAULT_MARKER

                    # <Substitution u'lock_details/author_page' (16:34)> -> __attr_href
                    __token = 647
                    try:
                        __zt_tmp = __attrs_140235423486800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140235435449424('path', u'lock_details/author_page', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140235428633488_author((u' href="%s"' % __attr_href))
                    __append_140235428633488_author(u'>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385309520
                    __default_140235385309520 = _DEFAULT_MARKER

                    # <Value u'lock_details/fullname' (15:26)> -> __cache_140235385308944
                    __token = 590
                    try:
                        __zt_tmp = __attrs_140235423486800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235385308944 = _static_140235435449424('path', u'lock_details/fullname', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'lock_details/fullname' (15:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b18538590> -> __condition
                    __expression = __cache_140235385308944

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235385308944
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140235428633488_author(__content)
                    __append_140235428633488_author(u'</a>')
                    __append_140235373758352(u'${author}')
                    __stream_140235428633488_author = ''.join(__stream_140235428633488_author)
                    __append_140235373758352(u'\n          ')
                    __stream_140235428633488_time = []
                    __append_140235428633488_time = __stream_140235428633488_time.append

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235385308176
                    __attrs_140235385308176 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140235428633488_time(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235428385104
                    __default_140235428385104 = _DEFAULT_MARKER

                    # <Value u'lock_details/time_difference' (18:29)> -> __cache_140235428385808
                    __token = 738
                    try:
                        __zt_tmp = __attrs_140235385308176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235428385808 = _static_140235435449424('path', u'lock_details/time_difference', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'lock_details/time_difference' (18:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ae4d250> -> __condition
                    __expression = __cache_140235428385808

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235428385808
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140235428633488_time(__content)
                    __append_140235428633488_time(u'</span>')
                    __append_140235373758352(u'${time}')
                    __stream_140235428633488_time = ''.join(__stream_140235428633488_time)
                    __append_140235373758352(u' ago.\n        ')
                    __msgid_140235373758352 = __re_whitespace(''.join(__stream_140235373758352)).strip()
                    if u'description_webdav_locked_by_author_on_time':
                        __append(translate(u'description_webdav_locked_by_author_on_time', mapping={u'time': __stream_140235428633488_time, u'author': __stream_140235428633488_author, }, default=__msgid_140235373758352, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235385310032
                __attrs_140235385310032 = _static_140235489934800

                # <Value u'not:lock_details/author_page' (21:27)> -> __condition
                __token = 858
                try:
                    __zt_tmp = __attrs_140235385310032
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('not', u'lock_details/author_page', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:
                    __stream_140235428633488_author = ''
                    __stream_140235428633488_time = ''
                    __stream_140235423489104 = []
                    __append_140235423489104 = __stream_140235423489104.append
                    __append_140235423489104(u'\n          This item was locked by\n          ')
                    __stream_140235428633488_author = []
                    __append_140235428633488_author = __stream_140235428633488_author.append

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235385266256
                    __attrs_140235385266256 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140235428633488_author(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385269648
                    __default_140235385269648 = _DEFAULT_MARKER

                    # <Value u'lock_details/fullname' (25:29)> -> __cache_140235385269456
                    __token = 1060
                    try:
                        __zt_tmp = __attrs_140235385266256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235385269456 = _static_140235435449424('path', u'lock_details/fullname', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'lock_details/fullname' (25:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1852e9d0> -> __condition
                    __expression = __cache_140235385269456

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235385269456
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140235428633488_author(__content)
                    __append_140235428633488_author(u'</span>')
                    __append_140235423489104(u'${author}')
                    __stream_140235428633488_author = ''.join(__stream_140235428633488_author)
                    __append_140235423489104(u'\n          ')
                    __stream_140235428633488_time = []
                    __append_140235428633488_time = __stream_140235428633488_time.append

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235385270096
                    __attrs_140235385270096 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140235428633488_time(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385267152
                    __default_140235385267152 = _DEFAULT_MARKER

                    # <Value u'lock_details/time_difference' (27:29)> -> __cache_140235385267984
                    __token = 1148
                    try:
                        __zt_tmp = __attrs_140235385270096
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235385267984 = _static_140235435449424('path', u'lock_details/time_difference', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'lock_details/time_difference' (27:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1852e150> -> __condition
                    __expression = __cache_140235385267984

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235385267984
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140235428633488_time(__content)
                    __append_140235428633488_time(u'</span>')
                    __append_140235423489104(u'${time}')
                    __stream_140235428633488_time = ''.join(__stream_140235428633488_time)
                    __append_140235423489104(u' ago.\n        ')
                    __msgid_140235423489104 = __re_whitespace(''.join(__stream_140235423489104)).strip()
                    if u'description_webdav_locked_by_author_on_time':
                        __append(translate(u'description_webdav_locked_by_author_on_time', mapping={u'time': __stream_140235428633488_time, u'author': __stream_140235428633488_author, }, default=__msgid_140235423489104, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1852e410> name=None at 7f8b1852e690> -> __attrs_140235431314192
                __attrs_140235431314192 = _static_140235385267216

                # <Value u'stealable' (29:29)> -> __condition
                __token = 1245
                try:
                    __zt_tmp = __attrs_140235431314192
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'stealable', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form method="POST"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431316176
                    __default_140235431316176 = _DEFAULT_MARKER

                    # <Substitution u'string:${context/absolute_url}/@@plone_lock_operations/force_unlock' (30:37)> -> __attr_action
                    __token = 1293
                    try:
                        __zt_tmp = __attrs_140235431314192
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140235435449424('string', u'${context/absolute_url}/@@plone_lock_operations/force_unlock', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((u' action="%s"' % __attr_action))
                    __append(u'>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431315792
                    __attrs_140235431315792 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140235431267936_unlock_button = ''
                    __stream_140235431314000 = []
                    __append_140235431314000 = __stream_140235431314000.append
                    __append_140235431314000(u'\n            If you are certain this user has abandoned the object,\n            you may\n            ')
                    __stream_140235431267936_unlock_button = []
                    __append_140235431267936_unlock_button = __stream_140235431267936_unlock_button.append

                    # <Static value=<_ast.Dict object at 0x7f8b1b118f10> name=None at 7f8b1b118650> -> __attrs_140235431314064
                    __attrs_140235431314064 = _static_140235431317264

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append_140235431267936_unlock_button(u'<input type="submit"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431315920
                    __default_140235431315920 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7f8b1b1181d0> at 7f8b1b118550> -> __attr_value
                    __attr_value = u'Unlock'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append_140235431267936_unlock_button((u' value="%s"' % __attr_value))
                    __append_140235431267936_unlock_button(u' />')
                    __append_140235431314000(u'${unlock_button}')
                    __stream_140235431267936_unlock_button = ''.join(__stream_140235431267936_unlock_button)
                    __append_140235431314000(u'\n            the object. You will then be able to edit it.\n          ')
                    __msgid_140235431314000 = __re_whitespace(''.join(__stream_140235431314000)).strip()
                    if u'description_webdav_locked_steal':
                        __append(translate(u'description_webdav_locked_steal', mapping={u'unlock_button': __stream_140235431267936_unlock_button, }, default=__msgid_140235431314000, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n        </form>')
                __append(u'\n      </dd>\n    </dl>\n  ')
            __append(u'\n</div>')
            __i18n_domain = __previous_i18n_domain_140235385324048
            if (__backup_lock_details_140235374305616 is __marker):
                del econtext['lock_details']
            else:
                econtext['lock_details'] = __backup_lock_details_140235374305616
            if (__backup_stealable_140235373353808 is __marker):
                del econtext['stealable']
            else:
                econtext['stealable'] = __backup_stealable_140235373353808
            if (__backup_locked_140235374309136 is __marker):
                del econtext['locked']
            else:
                econtext['locked'] = __backup_locked_140235374309136
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
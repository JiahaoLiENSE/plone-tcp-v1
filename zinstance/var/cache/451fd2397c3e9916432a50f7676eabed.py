# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/nextprevious/links.pt'

__tokens = {173: (u'view/enabled|nothing', 4, 25), 226: (u' view/isViewTemplate|nothin', 5, 31), 276: (u'python:enabled and isViewTemplate', 6, 20), 446: (u'view/previous', 12, 31), 486: (u'previous', 13, 25), 581: (u'previous/url', 15, 31), 699: (u'view/next', 20, 27), 735: (u'next', 21, 25), 822: (u'next/url', 23, 31)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140386186296528 = __compile_zt_expr
_static_140386078120656 = {u'href': u'', u'rel': u'previous', u'title': u'Go to previous item', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386079109456 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140386071190736 = {u'href': u'', u'rel': u'next', u'title': u'Go to next item', }

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

            # <Static value=<_ast.Dict object at 0x7fae2e607150> name=None at 7fae2e607a10> -> __attrs_140386079185296
            __attrs_140386079185296 = _static_140386079109456
            __backup_enabled_140386071503504 = get('enabled', __marker)

            # <Value u'view/enabled|nothing' (4:25)> -> __value
            __token = 173
            try:
                __zt_tmp = __attrs_140386079185296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/enabled|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_140386070893648 = get('isViewTemplate', __marker)

            # <Value u'view/isViewTemplate|nothing' (5:31)> -> __value
            __token = 226
            try:
                __zt_tmp = __attrs_140386079185296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/isViewTemplate|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value u'python:enabled and isViewTemplate' (6:20)> -> __condition
            __token = 276
            try:
                __zt_tmp = __attrs_140386079185296
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('python', u'enabled and isViewTemplate', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e515ad0> name=None at 7fae2e063a10> -> __attrs_140386071190480
                __attrs_140386071190480 = _static_140386078120656
                __backup_previous_140386070894416 = get('previous', __marker)

                # <Value u'view/previous' (12:31)> -> __value
                __token = 446
                try:
                    __zt_tmp = __attrs_140386071190480
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/previous', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value u'previous' (13:25)> -> __condition
                __token = 486
                try:
                    __zt_tmp = __attrs_140386071190480
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'previous', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<link rel="previous"')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071190160
                    __default_140386071190160 = _DEFAULT_MARKER

                    # <Substitution u'previous/url' (15:31)> -> __attr_href
                    __token = 581
                    try:
                        __zt_tmp = __attrs_140386071190480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('path', u'previous/url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071190096
                    __default_140386071190096 = _DEFAULT_MARKER

                    # <Translate msgid=u'title_previous_item' node=<_ast.Str object at 0x7fae2de799d0> at 7fae2de79150> -> __attr_title
                    __attr_title = u'Go to previous item'
                    __attr_title = translate(u'title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u' />')
                if (__backup_previous_140386070894416 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_140386070894416
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2de79cd0> name=None at 7fae2de79e10> -> __attrs_140386071208080
                __attrs_140386071208080 = _static_140386071190736
                __backup_next_140386077802448 = get('next', __marker)

                # <Value u'view/next' (20:27)> -> __value
                __token = 699
                try:
                    __zt_tmp = __attrs_140386071208080
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/next', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['next'] = __value

                # <Value u'next' (21:25)> -> __condition
                __token = 735
                try:
                    __zt_tmp = __attrs_140386071208080
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'next', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<link rel="next"')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078061392
                    __default_140386078061392 = _DEFAULT_MARKER

                    # <Substitution u'next/url' (23:31)> -> __attr_href
                    __token = 822
                    try:
                        __zt_tmp = __attrs_140386071208080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('path', u'next/url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071209360
                    __default_140386071209360 = _DEFAULT_MARKER

                    # <Translate msgid=u'title_next_item' node=<_ast.Str object at 0x7fae2de7e650> at 7fae2de7e890> -> __attr_title
                    __attr_title = u'Go to next item'
                    __attr_title = translate(u'title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u' />')
                if (__backup_next_140386077802448 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_140386077802448
                __append(u'\n\n')
            if (__backup_isViewTemplate_140386070893648 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_140386070893648
            if (__backup_enabled_140386071503504 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_140386071503504
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
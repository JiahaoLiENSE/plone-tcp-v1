# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/nextprevious/links.pt'

__tokens = {173: (u'view/enabled|nothing', 4, 25), 226: (u' view/isViewTemplate|nothin', 5, 31), 276: (u'python:enabled and isViewTemplate', 6, 20), 446: (u'view/previous', 12, 31), 486: (u'previous', 13, 25), 581: (u'previous/url', 15, 31), 699: (u'view/next', 20, 27), 735: (u'next', 21, 25), 822: (u'next/url', 23, 31)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235427768976 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140235373904528 = {u'href': u'', u'rel': u'previous', u'title': u'Go to previous item', }
_static_140235385292240 = {u'href': u'', u'rel': u'next', u'title': u'Go to next item', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1adb6a90> name=None at 7f8b1adb60d0> -> __attrs_140235373905872
            __attrs_140235373905872 = _static_140235427768976
            __backup_enabled_140235426055312 = get('enabled', __marker)

            # <Value u'view/enabled|nothing' (4:25)> -> __value
            __token = 173
            try:
                __zt_tmp = __attrs_140235373905872
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/enabled|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_140235385310736 = get('isViewTemplate', __marker)

            # <Value u'view/isViewTemplate|nothing' (5:31)> -> __value
            __token = 226
            try:
                __zt_tmp = __attrs_140235373905872
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/isViewTemplate|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value u'python:enabled and isViewTemplate' (6:20)> -> __condition
            __token = 276
            try:
                __zt_tmp = __attrs_140235373905872
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('python', u'enabled and isViewTemplate', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b17a58290> name=None at 7f8b17a585d0> -> __attrs_140235385294800
                __attrs_140235385294800 = _static_140235373904528
                __backup_previous_140235423364752 = get('previous', __marker)

                # <Value u'view/previous' (12:31)> -> __value
                __token = 446
                try:
                    __zt_tmp = __attrs_140235385294800
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/previous', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value u'previous' (13:25)> -> __condition
                __token = 486
                try:
                    __zt_tmp = __attrs_140235385294800
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'previous', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<link rel="previous"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385294160
                    __default_140235385294160 = _DEFAULT_MARKER

                    # <Substitution u'previous/url' (15:31)> -> __attr_href
                    __token = 581
                    try:
                        __zt_tmp = __attrs_140235385294800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140235435449424('path', u'previous/url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385294288
                    __default_140235385294288 = _DEFAULT_MARKER

                    # <Translate msgid=u'title_previous_item' node=<_ast.Str object at 0x7f8b18534410> at 7f8b18534e90> -> __attr_title
                    __attr_title = u'Go to previous item'
                    __attr_title = translate(u'title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u' />')
                if (__backup_previous_140235423364752 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_140235423364752
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b185345d0> name=None at 7f8b18534a90> -> __attrs_140235432577040
                __attrs_140235432577040 = _static_140235385292240
                __backup_next_140235374338192 = get('next', __marker)

                # <Value u'view/next' (20:27)> -> __value
                __token = 699
                try:
                    __zt_tmp = __attrs_140235432577040
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/next', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['next'] = __value

                # <Value u'next' (21:25)> -> __condition
                __token = 735
                try:
                    __zt_tmp = __attrs_140235432577040
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'next', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <link ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<link rel="next"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235432578448
                    __default_140235432578448 = _DEFAULT_MARKER

                    # <Substitution u'next/url' (23:31)> -> __attr_href
                    __token = 822
                    try:
                        __zt_tmp = __attrs_140235432577040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140235435449424('path', u'next/url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235432577808
                    __default_140235432577808 = _DEFAULT_MARKER

                    # <Translate msgid=u'title_next_item' node=<_ast.Str object at 0x7f8b1b24c0d0> at 7f8b1b24ca10> -> __attr_title
                    __attr_title = u'Go to next item'
                    __attr_title = translate(u'title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u' />')
                if (__backup_next_140235374338192 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_140235374338192
                __append(u'\n\n')
            if (__backup_isViewTemplate_140235385310736 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_140235385310736
            if (__backup_enabled_140235426055312 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_140235426055312
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
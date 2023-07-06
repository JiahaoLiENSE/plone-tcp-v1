# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/anontools.pt'

__tokens = {42: (u'python:view.user_actions and view.anonymous', 1, 42), 138: (u'view/user_actions', 4, 34), 208: (u'action', 6, 29), 242: (u'action/title', 7, 26)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235385295568 = {u'id': u'portal-anontools', }
_static_140235489934800 = {}
_static_140235438232272 = set([])
_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235373798352 = {u'href': u'', }

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

            # <Static value=<_ast.Dict object at 0x7f8b185352d0> name=None at 7f8b18535b90> -> __attrs_140235374543376
            __attrs_140235374543376 = _static_140235385295568

            # <Value u'python:view.user_actions and view.anonymous' (1:42)> -> __condition
            __token = 42
            try:
                __zt_tmp = __attrs_140235374543376
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('python', u'view.user_actions and view.anonymous', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="portal-anontools">\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373798992
                __attrs_140235373798992 = _static_140235489934800

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul>\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373798608
                __attrs_140235373798608 = _static_140235489934800

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373800720
                __attrs_140235373800720 = _static_140235489934800
                __backup_action_140235451442832 = get('action', __marker)

                # <Value u'view/user_actions' (4:34)> -> __iterator
                __token = 138
                try:
                    __zt_tmp = __attrs_140235373800720
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140235435449424('path', u'view/user_actions', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                (__iterator, ____index_140235373798224, ) = getitem('repeat')(u'action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append(u'\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8b17a3e3d0> name=None at 7f8b17a3e9d0> -> __attrs_140235385307856
                    __attrs_140235385307856 = _static_140235373798352

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Value u'action' (6:29)> -> __cache_140235385307728
                    __token = 208
                    try:
                        __zt_tmp = __attrs_140235385307856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235385307728 = _static_140235435449424('path', u'action', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if (u'href' not in __chain(__cache_140235385307728)):
                        __append(u' href=""')
                    __attr_140235385310032 = __cache_140235385307728
                    for (name, value, ) in __attr_140235385310032.items():
                        if ((name not in _static_140235438232272) and (value is not None)):
                            __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373799248
                    __default_140235373799248 = _DEFAULT_MARKER

                    # <Value u'action/title' (7:26)> -> __cache_140235373798800
                    __token = 242
                    try:
                        __zt_tmp = __attrs_140235385307856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235373798800 = _static_140235435449424('path', u'action/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'action/title' (7:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a3e250> -> __condition
                    __expression = __cache_140235373798800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n              action title\n          ')
                    else:
                        __content = __cache_140235373798800
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</a>\n      ')
                    ____index_140235373798224 -= 1
                    if (____index_140235373798224 > 0):
                        __append('')
                if (__backup_action_140235451442832 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140235451442832
                __append(u'\n    </li>\n  </ul>\n</div>')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
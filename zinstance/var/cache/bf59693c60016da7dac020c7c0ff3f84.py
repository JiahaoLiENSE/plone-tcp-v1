# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.portlets-4.4.8-py2.7.egg/plone/app/portlets/portlets/classic.pt'

__tokens = {33: (u'view/use_macro', 1, 33), 87: (u' view/path_expressio', 2, 38), 136: (u'use_macro', 4, 24), 182: (u'python:path(path_expression)', 5, 34), 182: (u'python:path(path_expression)', 5, 34), 255: (u'not:use_macro', 8, 24), 303: (u'python:path(path_expression)', 9, 32)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235489934800 = {}
_static_140235377128656 = u'python:path(path_expression)'

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374115856
            __attrs_140235374115856 = _static_140235489934800
            __backup_use_macro_140235385274832 = get('use_macro', __marker)

            # <Value u'view/use_macro' (1:33)> -> __value
            __token = 33
            try:
                __zt_tmp = __attrs_140235374115856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/use_macro', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['use_macro'] = __value
            __backup_path_expression_140235374586128 = get('path_expression', __marker)

            # <Value u'view/path_expression' (2:38)> -> __value
            __token = 87
            try:
                __zt_tmp = __attrs_140235374115856
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/path_expression', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['path_expression'] = __value
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235377127952
            __attrs_140235377127952 = _static_140235489934800

            # <Value u'use_macro' (4:24)> -> __condition
            __token = 136
            try:
                __zt_tmp = __attrs_140235377127952
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'use_macro', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235377129104
                __attrs_140235377129104 = _static_140235489934800
                __backup_macroname_140235424304256 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f8b17d6b4d0> name=None at 7f8b17d6bfd0> -> __value
                __value = _static_140235377128656
                econtext['macroname'] = __value

                # <Value u'python:path(path_expression)' (5:34)> -> __macro
                __token = 182
                try:
                    __zt_tmp = __attrs_140235377129104
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140235435449424('python', u'path(path_expression)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __token = 182
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140235424304256 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140235424304256
                __append(u'\n  ')
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235377131152
            __attrs_140235377131152 = _static_140235489934800

            # <Value u'not:use_macro' (8:24)> -> __condition
            __token = 255
            try:
                __zt_tmp = __attrs_140235377131152
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('not', u'use_macro', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235385248912
                __attrs_140235385248912 = _static_140235489934800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385245904
                __default_140235385245904 = _DEFAULT_MARKER

                # <Value u'python:path(path_expression)' (9:32)> -> __cache_140235377127568
                __token = 303
                try:
                    __zt_tmp = __attrs_140235385248912
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235377127568 = _static_140235435449424('python', u'path(path_expression)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:path(path_expression)' (9:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b18529d50> -> __condition
                __expression = __cache_140235377127568

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140235377127568
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  ')
            __append(u'\n\n')
            if (__backup_path_expression_140235374586128 is __marker):
                del econtext['path_expression']
            else:
                econtext['path_expression'] = __backup_path_expression_140235374586128
            if (__backup_use_macro_140235385274832 is __marker):
                del econtext['use_macro']
            else:
                econtext['use_macro'] = __backup_use_macro_140235385274832
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
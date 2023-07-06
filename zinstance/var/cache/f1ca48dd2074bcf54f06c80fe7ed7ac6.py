# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.portlets-4.4.8-py2.7.egg/plone/app/portlets/portlets/classic.pt'

__tokens = {33: (u'view/use_macro', 1, 33), 87: (u' view/path_expressio', 2, 38), 136: (u'use_macro', 4, 24), 182: (u'python:path(path_expression)', 5, 34), 182: (u'python:path(path_expression)', 5, 34), 255: (u'not:use_macro', 8, 24), 303: (u'python:path(path_expression)', 9, 32)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386186297040 = __C2ZContextWrapper
_static_140386186296528 = __compile_zt_expr
_static_140386078146960 = u'python:path(path_expression)'
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069451088
            __attrs_140386069451088 = _static_140386247937936
            __backup_use_macro_140386080023312 = get('use_macro', __marker)

            # <Value u'view/use_macro' (1:33)> -> __value
            __token = 33
            try:
                __zt_tmp = __attrs_140386069451088
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/use_macro', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['use_macro'] = __value
            __backup_path_expression_140386069982224 = get('path_expression', __marker)

            # <Value u'view/path_expression' (2:38)> -> __value
            __token = 87
            try:
                __zt_tmp = __attrs_140386069451088
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/path_expression', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['path_expression'] = __value
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078148816
            __attrs_140386078148816 = _static_140386247937936

            # <Value u'use_macro' (4:24)> -> __condition
            __token = 136
            try:
                __zt_tmp = __attrs_140386078148816
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'use_macro', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078146768
                __attrs_140386078146768 = _static_140386247937936
                __backup_macroname_140386115853680 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7fae2e51c190> name=None at 7fae2e51c950> -> __value
                __value = _static_140386078146960
                econtext['macroname'] = __value

                # <Value u'python:path(path_expression)' (5:34)> -> __macro
                __token = 182
                try:
                    __zt_tmp = __attrs_140386078146768
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140386186296528('python', u'path(path_expression)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __token = 182
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140386115853680 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140386115853680
                __append(u'\n  ')
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078148560
            __attrs_140386078148560 = _static_140386247937936

            # <Value u'not:use_macro' (8:24)> -> __condition
            __token = 255
            try:
                __zt_tmp = __attrs_140386078148560
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('not', u'use_macro', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070520208
                __attrs_140386070520208 = _static_140386247937936

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070522192
                __default_140386070522192 = _DEFAULT_MARKER

                # <Value u'python:path(path_expression)' (9:32)> -> __cache_140386070740624
                __token = 303
                try:
                    __zt_tmp = __attrs_140386070520208
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140386070740624 = _static_140386186296528('python', u'path(path_expression)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:path(path_expression)' (9:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de0bf10> -> __condition
                __expression = __cache_140386070740624

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140386070740624
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n  ')
            __append(u'\n\n')
            if (__backup_path_expression_140386069982224 is __marker):
                del econtext['path_expression']
            else:
                econtext['path_expression'] = __backup_path_expression_140386069982224
            if (__backup_use_macro_140386080023312 is __marker):
                del econtext['use_macro']
            else:
                econtext['use_macro'] = __backup_use_macro_140386080023312
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
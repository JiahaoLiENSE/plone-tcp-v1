# -*- coding: utf-8 -*-
__filename = 'index_html'

__tokens = {56: (u'template/title', 4, 24), 170: (u'context/title_or_id', 9, 27), 247: (u'template/title', 10, 29), 290: (u'template/title', 11, 27), 386: (u'template/id', 13, 43)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386113767248 = {u'charset': u'utf-8', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386186296528 = __compile_zt_expr
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
            __append(u'<!DOCTYPE html>\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386125437904
            __attrs_140386125437904 = _static_140386247937936

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386120856528
            __attrs_140386120856528 = _static_140386247937936

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386121272080
            __attrs_140386121272080 = _static_140386247937936

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title>')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386124525712
            __default_140386124525712 = _DEFAULT_MARKER

            # <Value u'template/title' (4:24)> -> __cache_140386119525776
            __token = 56
            try:
                __zt_tmp = __attrs_140386121272080
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386119525776 = _static_140386186296528('path', u'template/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'template/title' (4:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae30d95e10> -> __condition
            __expression = __cache_140386119525776

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'The title')
            else:
                __content = __cache_140386119525776
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</title>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae30714750> name=None at 7fae3070ff50> -> __attrs_140386113767120
            __attrs_140386113767120 = _static_140386113767248

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta charset="utf-8" />\n  </head>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386113768144
            __attrs_140386113768144 = _static_140386247937936

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n    \n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386113768976
            __attrs_140386113768976 = _static_140386247937936

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h2>')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386187334352
            __attrs_140386187334352 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386187334224
            __default_140386187334224 = _DEFAULT_MARKER

            # <Value u'context/title_or_id' (9:27)> -> __cache_140386187333904
            __token = 170
            try:
                __zt_tmp = __attrs_140386187334352
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386187333904 = _static_140386186296528('path', u'context/title_or_id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'context/title_or_id' (9:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae34d3d190> -> __condition
            __expression = __cache_140386187333904

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>content title or id</span>')
            else:
                __content = __cache_140386187333904
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n        ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386187335568
            __attrs_140386187335568 = _static_140386247937936

            # <Value u'template/title' (10:29)> -> __condition
            __token = 247
            try:
                __zt_tmp = __attrs_140386187335568
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'template/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386187335440
                __default_140386187335440 = _DEFAULT_MARKER

                # <Value u'template/title' (11:27)> -> __cache_140386187335056
                __token = 290
                try:
                    __zt_tmp = __attrs_140386187335568
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140386187335056 = _static_140386186296528('path', u'template/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                # <BinOp left=<Value u'template/title' (11:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae34d3d650> -> __condition
                __expression = __cache_140386187335056

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>optional template title</span>')
                else:
                    __content = __cache_140386187335056
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append(u'</h2>\n\n    This is Page Template ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386187336528
            __attrs_140386187336528 = _static_140386247937936

            # <em ... (0:0)
            # --------------------------------------------------------
            __append(u'<em>')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386187336144
            __default_140386187336144 = _DEFAULT_MARKER

            # <Value u'template/id' (13:43)> -> __cache_140386187334416
            __token = 386
            try:
                __zt_tmp = __attrs_140386187336528
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386187334416 = _static_140386186296528('path', u'template/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'template/id' (13:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae34d3d910> -> __condition
            __expression = __cache_140386187334416

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'template id')
            else:
                __content = __cache_140386187334416
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</em>.\n  </body>\n</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
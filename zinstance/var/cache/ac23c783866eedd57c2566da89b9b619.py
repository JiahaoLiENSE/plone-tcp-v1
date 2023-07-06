# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/footer.pt'

__tokens = {96: (u'view/render_footer_portlets', 3, 53), 64: (u'nothing', 3, 21)}

from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from chameleon.tal import ErrorInfo as _ErrorInfo

_static_140235435449424 = __compile_zt_expr
_static_140235426070096 = {u'class': u'row', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235489934800 = {}
_static_140235428419600 = {u'class': u'col-xs-12', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1ac17e50> name=None at 7f8b1ac17a10> -> __attrs_140235428419664
            __attrs_140235428419664 = _static_140235426070096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="row">\n\t')

            # <Static value=<_ast.Dict object at 0x7f8b1ae55810> name=None at 7f8b1ae55a10> -> __attrs_140235428418448
            __attrs_140235428418448 = _static_140235428419600

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="col-xs-12">\n\t\t')
            ____fallback_140235489734160 = len(__stream)
            try:

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235428419792
                __attrs_140235428419792 = _static_140235489934800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235428421072
                __default_140235428421072 = _DEFAULT_MARKER

                # <Value u'view/render_footer_portlets' (3:53)> -> __cache_140235428419856
                __token = 96
                try:
                    __zt_tmp = __attrs_140235428419792
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235428419856 = _static_140235435449424('path', u'view/render_footer_portlets', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'view/render_footer_portlets' (3:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ae55890> -> __condition
                __expression = __cache_140235428419856

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div />')
                else:
                    __content = __cache_140235428419856
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            except (Exception, ) as __exc:
                econtext['error'] = _ErrorInfo(__exc, __tokens[__token][1:3])
                if (on_error_handler is not None):
                    on_error_handler(__exc)
                del __stream[____fallback_140235489734160:]

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>')

                # <Value u'nothing' (3:21)> -> __content
                __token = 64
                try:
                    __zt_tmp = __attrs_140235428418448
                except get('NameError', NameError):
                    __zt_tmp = None

                __content = _static_140235435449424('path', u'nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
                __append(u'</div>')

            __append(u'\n\t</div>\n</div>\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
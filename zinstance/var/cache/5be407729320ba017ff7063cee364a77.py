# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/resources/browser/styles.pt'

__tokens = {26: (u'view/styles', 1, 26), 73: (u'style/conditionalcomment', 2, 34), 137: (u'condcomment', 3, 38), 194: (u'string:&lt;!--[if ${condcomment', 4, 43), 353: (u' style/re', 8, 29), 313: (u'style/src', 7, 31), 401: (u'e style/bund', 9, 36), 453: (u'condcomment', 9, 88), 511: (u'string:&lt;![endif]', 10, 44)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386186297040 = __C2ZContextWrapper
_static_140386186296528 = __compile_zt_expr
_static_140386071625168 = {u'href': u'style/src', u'data-bundle': u'style/bundle', u'rel': u'style', }
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071624976
            __attrs_140386071624976 = _static_140386247937936
            __backup_style_140386071623952 = get('style', __marker)

            # <Value u'view/styles' (1:26)> -> __iterator
            __token = 26
            try:
                __zt_tmp = __attrs_140386071624976
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140386186296528('path', u'view/styles', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            (__iterator, ____index_140386071623504, ) = getitem('repeat')(u'style', __iterator)
            econtext['style'] = None
            for __item in __iterator:
                econtext['style'] = __item

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071624464
                __attrs_140386071624464 = _static_140386247937936
                __backup_condcomment_140386078100560 = get('condcomment', __marker)

                # <Value u'style/conditionalcomment' (2:34)> -> __value
                __token = 73
                try:
                    __zt_tmp = __attrs_140386071624464
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'style/conditionalcomment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['condcomment'] = __value

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071622416
                __attrs_140386071622416 = _static_140386247937936

                # <Value u'condcomment' (3:38)> -> __condition
                __token = 137
                try:
                    __zt_tmp = __attrs_140386071622416
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'condcomment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071247120
                    __attrs_140386071247120 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071248464
                    __default_140386071248464 = _DEFAULT_MARKER

                    # <Value u'string:<!--[if ${condcomment}]>' (4:43)> -> __cache_140386071247952
                    __token = 194
                    try:
                        __zt_tmp = __attrs_140386071247120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386071247952 = _static_140386186296528('string', u'<!--[if ${condcomment}]>', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'string:<!--[if ${condcomment}]>' (4:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de878d0> -> __condition
                    __expression = __cache_140386071247952

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386071247952
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2dee3dd0> name=None at 7fae2dee3950> -> __attrs_140386127851024
                __attrs_140386127851024 = _static_140386071625168

                # <link ... (0:0)
                # --------------------------------------------------------
                __append(u'<link')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127847696
                __default_140386127847696 = _DEFAULT_MARKER

                # <Substitution u'style/rel' (8:29)> -> __attr_rel
                __token = 353
                try:
                    __zt_tmp = __attrs_140386127851024
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_rel = _static_140386186296528('path', u'style/rel', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_rel = __quote(__attr_rel, '"', '&quot;', u'style', _DEFAULT_MARKER)
                if (__attr_rel is not None):
                    __append((u' rel="%s"' % __attr_rel))

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127848336
                __default_140386127848336 = _DEFAULT_MARKER

                # <Substitution u'style/src' (7:31)> -> __attr_href
                __token = 313
                try:
                    __zt_tmp = __attrs_140386127851024
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140386186296528('path', u'style/src', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127850704
                __default_140386127850704 = _DEFAULT_MARKER

                # <Substitution u'style/bundle' (9:36)> -> __attr_data_bundle
                __token = 401
                try:
                    __zt_tmp = __attrs_140386127851024
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_bundle = _static_140386186296528('path', u'style/bundle', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_data_bundle = __quote(__attr_data_bundle, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_bundle is not None):
                    __append((u' data-bundle="%s"' % __attr_data_bundle))
                __append(u' />')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078119696
                __attrs_140386078119696 = _static_140386247937936

                # <Value u'condcomment' (9:88)> -> __condition
                __token = 453
                try:
                    __zt_tmp = __attrs_140386078119696
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'condcomment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078085904
                    __attrs_140386078085904 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078088592
                    __default_140386078088592 = _DEFAULT_MARKER

                    # <Value u'string:<![endif]-->' (10:44)> -> __cache_140386078120208
                    __token = 511
                    try:
                        __zt_tmp = __attrs_140386078085904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386078120208 = _static_140386186296528('string', u'<![endif]-->', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'string:<![endif]-->' (10:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e515250> -> __condition
                    __expression = __cache_140386078120208

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386078120208
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n    ')
                if (__backup_condcomment_140386078100560 is __marker):
                    del econtext['condcomment']
                else:
                    econtext['condcomment'] = __backup_condcomment_140386078100560
                ____index_140386071623504 -= 1
                if (____index_140386071623504 > 0):
                    __append('')
            if (__backup_style_140386071623952 is __marker):
                del econtext['style']
            else:
                econtext['style'] = __backup_style_140386071623952
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
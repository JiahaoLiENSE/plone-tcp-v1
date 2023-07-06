# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/resources/browser/styles.pt'

__tokens = {26: (u'view/styles', 1, 26), 73: (u'style/conditionalcomment', 2, 34), 137: (u'condcomment', 3, 38), 194: (u'string:&lt;!--[if ${condcomment', 4, 43), 353: (u' style/re', 8, 29), 313: (u'style/src', 7, 31), 401: (u'e style/bund', 9, 36), 453: (u'condcomment', 9, 88), 511: (u'string:&lt;![endif]', 10, 44)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235489934800 = {}
_static_140235427783696 = {u'href': u'style/src', u'data-bundle': u'style/bundle', u'rel': u'style', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427785488
            __attrs_140235427785488 = _static_140235489934800
            __backup_style_140235373978192 = get('style', __marker)

            # <Value u'view/styles' (1:26)> -> __iterator
            __token = 26
            try:
                __zt_tmp = __attrs_140235427785488
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140235435449424('path', u'view/styles', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            (__iterator, ____index_140235451454480, ) = getitem('repeat')(u'style', __iterator)
            econtext['style'] = None
            for __item in __iterator:
                econtext['style'] = __item

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427349840
                __attrs_140235427349840 = _static_140235489934800
                __backup_condcomment_140235373980624 = get('condcomment', __marker)

                # <Value u'style/conditionalcomment' (2:34)> -> __value
                __token = 73
                try:
                    __zt_tmp = __attrs_140235427349840
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'style/conditionalcomment', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['condcomment'] = __value

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427785424
                __attrs_140235427785424 = _static_140235489934800

                # <Value u'condcomment' (3:38)> -> __condition
                __token = 137
                try:
                    __zt_tmp = __attrs_140235427785424
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'condcomment', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427784464
                    __attrs_140235427784464 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427785616
                    __default_140235427785616 = _DEFAULT_MARKER

                    # <Value u'string:<!--[if ${condcomment}]>' (4:43)> -> __cache_140235427784592
                    __token = 194
                    try:
                        __zt_tmp = __attrs_140235427784464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235427784592 = _static_140235435449424('string', u'<!--[if ${condcomment}]>', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'string:<!--[if ${condcomment}]>' (4:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1adba610> -> __condition
                    __expression = __cache_140235427784592

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235427784592
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1adba410> name=None at 7f8b1adbafd0> -> __attrs_140235432668752
                __attrs_140235432668752 = _static_140235427783696

                # <link ... (0:0)
                # --------------------------------------------------------
                __append(u'<link')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235432668304
                __default_140235432668304 = _DEFAULT_MARKER

                # <Substitution u'style/rel' (8:29)> -> __attr_rel
                __token = 353
                try:
                    __zt_tmp = __attrs_140235432668752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_rel = _static_140235435449424('path', u'style/rel', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_rel = __quote(__attr_rel, '"', '&quot;', u'style', _DEFAULT_MARKER)
                if (__attr_rel is not None):
                    __append((u' rel="%s"' % __attr_rel))

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235432665552
                __default_140235432665552 = _DEFAULT_MARKER

                # <Substitution u'style/src' (7:31)> -> __attr_href
                __token = 313
                try:
                    __zt_tmp = __attrs_140235432668752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140235435449424('path', u'style/src', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235432667408
                __default_140235432667408 = _DEFAULT_MARKER

                # <Substitution u'style/bundle' (9:36)> -> __attr_data_bundle
                __token = 401
                try:
                    __zt_tmp = __attrs_140235432668752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_bundle = _static_140235435449424('path', u'style/bundle', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_data_bundle = __quote(__attr_data_bundle, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_bundle is not None):
                    __append((u' data-bundle="%s"' % __attr_data_bundle))
                __append(u' />')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432665168
                __attrs_140235432665168 = _static_140235489934800

                # <Value u'condcomment' (9:88)> -> __condition
                __token = 453
                try:
                    __zt_tmp = __attrs_140235432665168
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'condcomment', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432668432
                    __attrs_140235432668432 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235432666768
                    __default_140235432666768 = _DEFAULT_MARKER

                    # <Value u'string:<![endif]-->' (10:44)> -> __cache_140235432668368
                    __token = 511
                    try:
                        __zt_tmp = __attrs_140235432668432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235432668368 = _static_140235435449424('string', u'<![endif]-->', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'string:<![endif]-->' (10:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b262ad0> -> __condition
                    __expression = __cache_140235432668368

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235432668368
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n    ')
                if (__backup_condcomment_140235373980624 is __marker):
                    del econtext['condcomment']
                else:
                    econtext['condcomment'] = __backup_condcomment_140235373980624
                ____index_140235451454480 -= 1
                if (____index_140235451454480 > 0):
                    __append('')
            if (__backup_style_140235373978192 is __marker):
                del econtext['style']
            else:
                econtext['style'] = __backup_style_140235373978192
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
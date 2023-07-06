# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/toc.pt'

__tokens = {104: (u'view/enabled', 2, 19)}

from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386069150224 = {u'class': u'portletItem', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386070661968 = {u'class': u'portletContent', }
_static_140386186296528 = __compile_zt_expr
_static_140386070661840 = {u'class': u'portletHeader', }
_static_140386069241616 = {u'style': u'display: none', u'role': u'section', u'id': u'document-toc', u'class': u'portlet toc', }

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

            # <Static value=<_ast.Dict object at 0x7fae2dc9df10> name=None at 7fae2dc9d9d0> -> __attrs_140386070660560
            __attrs_140386070660560 = _static_140386069241616

            # <Value u'view/enabled' (2:19)> -> __condition
            __token = 104
            try:
                __zt_tmp = __attrs_140386070660560
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'view/enabled', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140386070661136 = __i18n_domain
                __i18n_domain = u'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="document-toc" class="portlet toc"  role="section" style="display: none">\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2ddf8ad0> name=None at 7fae2ddf8c10> -> __attrs_140386070659984
                __attrs_140386070659984 = _static_140386070661840

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header class="portletHeader">')
                __stream_140386070661392 = []
                __append_140386070661392 = __stream_140386070661392.append
                __append_140386070661392(u'Contents')
                __msgid_140386070661392 = __re_whitespace(''.join(__stream_140386070661392)).strip()
                if u'label_tableofcontents':
                    __append(translate(u'label_tableofcontents', mapping=None, default=__msgid_140386070661392, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2ddf8b50> name=None at 7fae2ddf8650> -> __attrs_140386071858448
                __attrs_140386071858448 = _static_140386070661968

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section class="portletContent">\n\t  ')

                # <Static value=<_ast.Dict object at 0x7fae2dc87a10> name=None at 7fae2dc87150> -> __attrs_140386069149840
                __attrs_140386069149840 = _static_140386069150224

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portletItem">\n\t  </div>\n  </section>\n</section>')
                __i18n_domain = __previous_i18n_domain_140386070661136
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/toc.pt'

__tokens = {104: (u'view/enabled', 2, 19)}

from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235435449424 = __compile_zt_expr
_static_140235427304656 = {u'style': u'display: none', u'role': u'section', u'id': u'document-toc', u'class': u'portlet toc', }
_static_140235373904784 = {u'class': u'portletContent', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235432265936 = {u'class': u'portletItem', }
_static_140235374583696 = {u'class': u'portletHeader', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1ad454d0> name=None at 7f8b1ad45ad0> -> __attrs_140235374583120
            __attrs_140235374583120 = _static_140235427304656

            # <Value u'view/enabled' (2:19)> -> __condition
            __token = 104
            try:
                __zt_tmp = __attrs_140235374583120
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'view/enabled', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140235374583184 = __i18n_domain
                __i18n_domain = u'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="document-toc" class="portlet toc"  role="section" style="display: none">\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b17afdf90> name=None at 7f8b17afde90> -> __attrs_140235426108048
                __attrs_140235426108048 = _static_140235374583696

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header class="portletHeader">')
                __stream_140235374581648 = []
                __append_140235374581648 = __stream_140235374581648.append
                __append_140235374581648(u'Contents')
                __msgid_140235374581648 = __re_whitespace(''.join(__stream_140235374581648)).strip()
                if u'label_tableofcontents':
                    __append(translate(u'label_tableofcontents', mapping=None, default=__msgid_140235374581648, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b17a58390> name=None at 7f8b17a58d50> -> __attrs_140235428385552
                __attrs_140235428385552 = _static_140235373904784

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section class="portletContent">\n\t  ')

                # <Static value=<_ast.Dict object at 0x7f8b1b2008d0> name=None at 7f8b1b200090> -> __attrs_140235373757456
                __attrs_140235373757456 = _static_140235432265936

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portletItem">\n\t  </div>\n  </section>\n</section>')
                __i18n_domain = __previous_i18n_domain_140235374583184
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
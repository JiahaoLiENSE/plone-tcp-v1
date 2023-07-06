# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/logo.pt'

__tokens = {110: (u' view/navigation_root_titl', 4, 24), 60: (u'view/navigation_root_url', 3, 24), 342: (u'c view/img_s', 10, 27), 250: (u'view/logo_title', 8, 29), 297: (u' view/logo_titl', 9, 30)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235435449424 = __compile_zt_expr
_static_140235385298384 = {u'href': u'view/navigation_root_url', u'id': u'portal-logo', u'title': u'Home', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235385296336 = {u'src': u'logo.png', u'alt': u'', u'title': u'view/logo_title', }

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

            # <Static value=<_ast.Dict object at 0x7f8b18535dd0> name=None at 7f8b18535250> -> __attrs_140235385295760
            __attrs_140235385295760 = _static_140235385298384
            __previous_i18n_domain_140235385297744 = __i18n_domain
            __i18n_domain = u'plone'

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a id="portal-logo"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385297872
            __default_140235385297872 = _DEFAULT_MARKER

            # <Translate msgid=None node=<Substitution u'view/navigation_root_title' (4:24)> at 7f8b18535d50> -> __attr_title

            # <Substitution u'view/navigation_root_title' (4:24)> -> __attr_title
            __token = 110
            try:
                __zt_tmp = __attrs_140235385295760
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140235435449424('path', u'view/navigation_root_title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', u'Home', _DEFAULT_MARKER)
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385296976
            __default_140235385296976 = _DEFAULT_MARKER

            # <Substitution u'view/navigation_root_url' (3:24)> -> __attr_href
            __token = 60
            try:
                __zt_tmp = __attrs_140235385295760
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140235435449424('path', u'view/navigation_root_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b185355d0> name=None at 7f8b185357d0> -> __attrs_140235385308880
            __attrs_140235385308880 = _static_140235385296336

            # <img ... (0:0)
            # --------------------------------------------------------
            __append(u'<img')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385309968
            __default_140235385309968 = _DEFAULT_MARKER

            # <Substitution u'view/img_src' (10:27)> -> __attr_src
            __token = 342
            try:
                __zt_tmp = __attrs_140235385308880
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140235435449424('path', u'view/img_src', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', u'logo.png', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385307472
            __default_140235385307472 = _DEFAULT_MARKER

            # <Substitution u'view/logo_title' (8:29)> -> __attr_alt
            __token = 250
            try:
                __zt_tmp = __attrs_140235385308880
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_alt = _static_140235435449424('path', u'view/logo_title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_alt is not None):
                __append((u' alt="%s"' % __attr_alt))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385310096
            __default_140235385310096 = _DEFAULT_MARKER

            # <Substitution u'view/logo_title' (9:30)> -> __attr_title
            __token = 297
            try:
                __zt_tmp = __attrs_140235385308880
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140235435449424('path', u'view/logo_title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u' /></a>')
            __i18n_domain = __previous_i18n_domain_140235385297744
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
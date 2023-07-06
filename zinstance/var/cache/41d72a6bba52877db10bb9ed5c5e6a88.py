# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/links/rsslink.pt'

__tokens = {28: (u'view/rsslinks', 1, 28), 162: (u'link/url', 4, 31), 203: (u' link/titl', 5, 31)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235373905104 = {u'href': u'', u'type': u'application/rss+xml', u'rel': u'alternate', u'title': u'RSS 1.0', }
_static_140235489934800 = {}

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432577808
            __attrs_140235432577808 = _static_140235489934800
            __backup_link_140235427351568 = get('link', __marker)

            # <Value u'view/rsslinks' (1:28)> -> __iterator
            __token = 28
            try:
                __zt_tmp = __attrs_140235432577808
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140235435449424('path', u'view/rsslinks', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            (__iterator, ____index_140235432576144, ) = getitem('repeat')(u'link', __iterator)
            econtext['link'] = None
            for __item in __iterator:
                econtext['link'] = __item
                __append(u'\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b17a584d0> name=None at 7f8b17a58fd0> -> __attrs_140235373906000
                __attrs_140235373906000 = _static_140235373905104

                # <link ... (0:0)
                # --------------------------------------------------------
                __append(u'<link rel="alternate"')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373904656
                __default_140235373904656 = _DEFAULT_MARKER

                # <Substitution u'link/url' (4:31)> -> __attr_href
                __token = 162
                try:
                    __zt_tmp = __attrs_140235373906000
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140235435449424('path', u'link/url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373907152
                __default_140235373907152 = _DEFAULT_MARKER

                # <Substitution u'link/title' (5:31)> -> __attr_title
                __token = 203
                try:
                    __zt_tmp = __attrs_140235373906000
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140235435449424('path', u'link/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', u'RSS 1.0', _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u' type="application/rss+xml" />\n')
                ____index_140235432576144 -= 1
                if (____index_140235432576144 > 0):
                    __append('')
            if (__backup_link_140235427351568 is __marker):
                del econtext['link']
            else:
                econtext['link'] = __backup_link_140235427351568
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
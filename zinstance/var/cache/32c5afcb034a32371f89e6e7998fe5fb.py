# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/links/search.pt'

__tokens = {40: (u'view/navigation_root_url', 1, 40), 263: (u'string:${navigation_root_url}/@@search', 7, 31)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235489934800 = {}
_static_140235374339792 = {u'href': u'', u'rel': u'search', u'title': u'Search this site', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374341456
            __attrs_140235374341456 = _static_140235489934800
            __backup_navigation_root_url_140235423363984 = get('navigation_root_url', __marker)

            # <Value u'view/navigation_root_url' (1:40)> -> __value
            __token = 40
            try:
                __zt_tmp = __attrs_140235374341456
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/navigation_root_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['navigation_root_url'] = __value
            __previous_i18n_domain_140235374341712 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b17ac26d0> name=None at 7f8b17ac2bd0> -> __attrs_140235374560272
            __attrs_140235374560272 = _static_140235374339792

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link rel="search"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374559952
            __default_140235374559952 = _DEFAULT_MARKER

            # <Substitution u'string:${navigation_root_url}/@@search' (7:31)> -> __attr_href
            __token = 263
            try:
                __zt_tmp = __attrs_140235374560272
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140235435449424('string', u'${navigation_root_url}/@@search', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374562384
            __default_140235374562384 = _DEFAULT_MARKER

            # <Translate msgid=u'title_search_this_site' node=<_ast.Str object at 0x7f8b17af8590> at 7f8b17af8090> -> __attr_title
            __attr_title = u'Search this site'
            __attr_title = translate(u'title_search_this_site', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u' />\n')
            __i18n_domain = __previous_i18n_domain_140235374341712
            if (__backup_navigation_root_url_140235423363984 is __marker):
                del econtext['navigation_root_url']
            else:
                econtext['navigation_root_url'] = __backup_navigation_root_url_140235423363984
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
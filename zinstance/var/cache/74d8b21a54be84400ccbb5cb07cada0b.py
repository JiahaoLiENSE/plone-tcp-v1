# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/links/author.pt'

__tokens = {185: (u'view/navigation_root_url', 4, 37), 419: (u'string:${navigation_root_url}/author/${context/Creator|nothing}', 11, 31)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386186297040 = __C2ZContextWrapper
_static_140386186296528 = __compile_zt_expr
_static_140386078151696 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140386078152144 = {u'href': u'', u'rel': u'author', u'title': u'Author information', }

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

            # <Static value=<_ast.Dict object at 0x7fae2e51d410> name=None at 7fae2e4c7f10> -> __attrs_140386078154512
            __attrs_140386078154512 = _static_140386078151696
            __backup_navigation_root_url_140386073196368 = get('navigation_root_url', __marker)

            # <Value u'view/navigation_root_url' (4:37)> -> __value
            __token = 185
            try:
                __zt_tmp = __attrs_140386078154512
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/navigation_root_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['navigation_root_url'] = __value
            __previous_i18n_domain_140386078153552 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2e51d5d0> name=None at 7fae2e51d650> -> __attrs_140386072992336
            __attrs_140386072992336 = _static_140386078152144

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link rel="author"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078151504
            __default_140386078151504 = _DEFAULT_MARKER

            # <Substitution u'string:${navigation_root_url}/author/${context/Creator|nothing}' (11:31)> -> __attr_href
            __token = 419
            try:
                __zt_tmp = __attrs_140386072992336
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140386186296528('string', u'${navigation_root_url}/author/${context/Creator|nothing}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078151568
            __default_140386078151568 = _DEFAULT_MARKER

            # <Translate msgid=u'title_author_info' node=<_ast.Str object at 0x7fae2e51d750> at 7fae2e51d790> -> __attr_title
            __attr_title = u'Author information'
            __attr_title = translate(u'title_author_info', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u' />\n')
            __i18n_domain = __previous_i18n_domain_140386078153552
            if (__backup_navigation_root_url_140386073196368 is __marker):
                del econtext['navigation_root_url']
            else:
                econtext['navigation_root_url'] = __backup_navigation_root_url_140386073196368
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
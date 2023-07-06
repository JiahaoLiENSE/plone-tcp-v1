# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/browser/templates/colophon.pt'

__tokens = {}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info

_static_140235373355536 = {u'href': u'http://plone.com', u'target': u'_blank', u'title': u'This site was built using the Plone Open Source CMS/WCM.', }
_static_140235373358096 = {u'class': u'portletContent', }
_static_140235428379600 = {u'class': u'portlet portletClassic', u'id': u'portal-colophon', }
_static_140235374092432 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }

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

    def render_portlet(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8b1ae4bbd0> name=None at 7f8b1ae4b850> -> __attrs_140235428378640
            __attrs_140235428378640 = _static_140235428379600

            # <aside ... (0:0)
            # --------------------------------------------------------
            __append(u'<aside class="portlet portletClassic" id="portal-colophon">\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b179d2c10> name=None at 7f8b179d2610> -> __attrs_140235373357136
            __attrs_140235373357136 = _static_140235373358096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="portletContent">\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b179d2210> name=None at 7f8b179d2750> -> __attrs_140235423522128
            __attrs_140235423522128 = _static_140235373355536

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a href="http://plone.com" target="_blank"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423520272
            __default_140235423520272 = _DEFAULT_MARKER

            # <Translate msgid=u'title_built_with_plone' node=<_ast.Str object at 0x7f8b179d2550> at 7f8b179d28d0> -> __attr_title
            __attr_title = u'This site was built using the Plone Open Source CMS/WCM.'
            __attr_title = translate(u'title_built_with_plone', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u'>')
            __stream_140235373358160 = []
            __append_140235373358160 = __stream_140235373358160.append
            __append_140235373358160(u'\n        Powered by Plone &amp; Python')
            __msgid_140235373358160 = __re_whitespace(''.join(__stream_140235373358160)).strip()
            if u'label_powered_by_plone':
                __append(translate(u'label_powered_by_plone', mapping=None, default=__msgid_140235373358160, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n    </div>\n  </aside>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<_ast.Dict object at 0x7f8b17a86090> name=None at 7f8b17a864d0> -> __attrs_140235374095376
            __attrs_140235374095376 = _static_140235374092432
            __previous_i18n_domain_140235374094288 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n\n  ')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140235374094288
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_portlet': render_portlet, 'render': render, }
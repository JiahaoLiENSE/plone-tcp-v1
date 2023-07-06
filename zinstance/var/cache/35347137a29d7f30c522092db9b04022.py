# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.standardtiles-2.5.0-py2.7.egg/plone/app/standardtiles/templates/description.pt'

__tokens = {392: (u'view/value', 10, 22)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235322724112 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }
_static_140235435449424 = __compile_zt_expr
_static_140235435450064 = __C2ZContextWrapper
_static_140235489934800 = {}
_static_140235323222160 = {u'class': u'documentDescription', }

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
            __append(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n')

            # <Static value=<_ast.Dict object at 0x7f8b14988f10> name=None at 7f8b14988310> -> __attrs_140235322564432
            __attrs_140235322564432 = _static_140235322724112
            __previous_i18n_domain_140235322562768 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322561616
            __attrs_140235322561616 = _static_140235489934800

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b14a02890> name=None at 7f8b14a02cd0> -> __attrs_140235323223568
            __attrs_140235323223568 = _static_140235323222160

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="documentDescription">')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235323223184
            __default_140235323223184 = _DEFAULT_MARKER

            # <Value u'view/value' (10:22)> -> __cache_140235323221520
            __token = 392
            try:
                __zt_tmp = __attrs_140235323223568
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235323221520 = _static_140235435449424('path', u'view/value', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'view/value' (10:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b14a02850> -> __condition
            __expression = __cache_140235323221520

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n      Description here\n    ')
            else:
                __content = __cache_140235323221520
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n  </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140235322562768
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
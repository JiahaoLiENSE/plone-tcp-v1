# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/analytics/view.pt'

__tokens = {55: (u'view/webstats_js', 2, 29), 93: (u'webstats_js', 3, 20), 134: (u'webstats_js', 4, 28)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386186297040 = __C2ZContextWrapper
_static_140386186296528 = __compile_zt_expr
_static_140386078079696 = {u'id': u'plone-analytics', }

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

            # <Static value=<_ast.Dict object at 0x7fae2e50bad0> name=None at 7fae2e027710> -> __attrs_140386070043984
            __attrs_140386070043984 = _static_140386078079696
            __backup_webstats_js_140386080001168 = get('webstats_js', __marker)

            # <Value u'view/webstats_js' (2:29)> -> __value
            __token = 55
            try:
                __zt_tmp = __attrs_140386070043984
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/webstats_js', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['webstats_js'] = __value

            # <Value u'webstats_js' (3:20)> -> __condition
            __token = 93
            try:
                __zt_tmp = __attrs_140386070043984
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'webstats_js', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="plone-analytics" >')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072951248
                __default_140386072951248 = _DEFAULT_MARKER

                # <Value u'webstats_js' (4:28)> -> __cache_140386069211216
                __token = 134
                try:
                    __zt_tmp = __attrs_140386070043984
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140386069211216 = _static_140386186296528('path', u'webstats_js', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                # <BinOp left=<Value u'webstats_js' (4:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dc96a50> -> __condition
                __expression = __cache_140386069211216

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'\n  Here goes the webstats_js\n')
                else:
                    __content = __cache_140386069211216
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>')
            if (__backup_webstats_js_140386080001168 is __marker):
                del econtext['webstats_js']
            else:
                econtext['webstats_js'] = __backup_webstats_js_140386080001168
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
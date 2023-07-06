# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/dublin_core.pt'

__tokens = {25: (u'view/metatags', 1, 25), 67: (u'python:keyval[0]', 2, 27), 92: (u' python:keyval[1', 2, 52)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386186297040 = __C2ZContextWrapper
_static_140386078061392 = {u'content': u'python:keyval[1]', u'name': u'python:keyval[0]', }
_static_140386186296528 = __compile_zt_expr

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

            # <Static value=<_ast.Dict object at 0x7fae2e507350> name=None at 7fae2e507910> -> __attrs_140386078064336
            __attrs_140386078064336 = _static_140386078061392
            __backup_keyval_140386071905168 = get('keyval', __marker)

            # <Value u'view/metatags' (1:25)> -> __iterator
            __token = 25
            try:
                __zt_tmp = __attrs_140386078064336
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140386186296528('path', u'view/metatags', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            (__iterator, ____index_140386078062928, ) = getitem('repeat')(u'keyval', __iterator)
            econtext['keyval'] = None
            for __item in __iterator:
                econtext['keyval'] = __item

                # <meta ... (0:0)
                # --------------------------------------------------------
                __append(u'<meta')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078063632
                __default_140386078063632 = _DEFAULT_MARKER

                # <Substitution u'python:keyval[0]' (2:27)> -> __attr_name
                __token = 67
                try:
                    __zt_tmp = __attrs_140386078064336
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140386186296528('python', u'keyval[0]', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((u' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078064528
                __default_140386078064528 = _DEFAULT_MARKER

                # <Substitution u'python:keyval[1]' (2:52)> -> __attr_content
                __token = 92
                try:
                    __zt_tmp = __attrs_140386078064336
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_content = _static_140386186296528('python', u'keyval[1]', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_content = __quote(__attr_content, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_content is not None):
                    __append((u' content="%s"' % __attr_content))
                __append(u' />')
                ____index_140386078062928 -= 1
                if (____index_140386078062928 > 0):
                    __append('\n')
            if (__backup_keyval_140386071905168 is __marker):
                del econtext['keyval']
            else:
                econtext['keyval'] = __backup_keyval_140386071905168
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
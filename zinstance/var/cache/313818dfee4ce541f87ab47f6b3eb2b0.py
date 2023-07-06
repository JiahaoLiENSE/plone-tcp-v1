# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.portlets-4.4.8-py2.7.egg/plone/app/portlets/browser/templates/column.pt'

__tokens = {27: (u'options/portlets', 1, 27), 97: (u'string:portletwrapper-${portlet/hash}', 3, 23), 173: (u' portlet/has', 4, 37), 216: (u"python:view.safe_render(portlet['renderer'])", 5, 28)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386186297040 = __C2ZContextWrapper
_static_140386071779344 = {u'data-portlethash': u'portlet/hash', u'class': u'portletWrapper', u'id': u'string:portletwrapper-${portlet/hash}', }
_static_140386186296528 = __compile_zt_expr
_static_140386247937936 = {}

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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070777552
            __attrs_140386070777552 = _static_140386247937936
            __backup_portlet_140386069972624 = get('portlet', __marker)

            # <Value u'options/portlets' (1:27)> -> __iterator
            __token = 27
            try:
                __zt_tmp = __attrs_140386070777552
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140386186296528('path', u'options/portlets', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            (__iterator, ____index_140386070777744, ) = getitem('repeat')(u'portlet', __iterator)
            econtext['portlet'] = None
            for __item in __iterator:
                econtext['portlet'] = __item
                __append(u'\n')

                # <Static value=<_ast.Dict object at 0x7fae2df09810> name=None at 7fae2df09290> -> __attrs_140386069149840
                __attrs_140386069149840 = _static_140386071779344

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portletWrapper"')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069147984
                __default_140386069147984 = _DEFAULT_MARKER

                # <Substitution u'string:portletwrapper-${portlet/hash}' (3:23)> -> __attr_id
                __token = 97
                try:
                    __zt_tmp = __attrs_140386069149840
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140386186296528('string', u'portletwrapper-${portlet/hash}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069148496
                __default_140386069148496 = _DEFAULT_MARKER

                # <Substitution u'portlet/hash' (4:37)> -> __attr_data_portlethash
                __token = 173
                try:
                    __zt_tmp = __attrs_140386069149840
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_portlethash = _static_140386186296528('path', u'portlet/hash', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_data_portlethash = __quote(__attr_data_portlethash, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_portlethash is not None):
                    __append((u' data-portlethash="%s"' % __attr_data_portlethash))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071778256
                __default_140386071778256 = _DEFAULT_MARKER

                # <Value u"python:view.safe_render(portlet['renderer'])" (5:28)> -> __cache_140386071781136
                __token = 216
                try:
                    __zt_tmp = __attrs_140386069149840
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140386071781136 = _static_140386186296528('python', u"view.safe_render(portlet['renderer'])", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                # <BinOp left=<Value u"python:view.safe_render(portlet['renderer'])" (5:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2df09dd0> -> __condition
                __expression = __cache_140386071781136

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140386071781136
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>\n')
                ____index_140386070777744 -= 1
                if (____index_140386070777744 > 0):
                    __append('')
            if (__backup_portlet_140386069972624 is __marker):
                del econtext['portlet']
            else:
                econtext['portlet'] = __backup_portlet_140386069972624
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
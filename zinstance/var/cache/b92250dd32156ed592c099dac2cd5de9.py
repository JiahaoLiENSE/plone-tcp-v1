# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/sections.pt'

__tokens = {196: (u'python:view.navtree', 5, 20), 962: (u'python:view.render_globalnav()', 21, 42)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386069900944 = {u'class': u'icon-bar', }
_static_140386070483856 = {u'class': u'icon-bar', }
_static_140386069900304 = {u'class': u'plone-collapse plone-navbar-collapse', u'id': u'portal-globalnav-collapse', }
_static_140386069198480 = {u'data-toggle': u'collapse', u'type': u'button', u'class': u'plone-navbar-toggle', u'data-target': u'#portal-globalnav-collapse', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386069197392 = {u'class': u'plone-navbar-header', }
_static_140386070083344 = {u'class': u'plone-navbar pat-navigationmarker', u'id': u'portal-globalnav-wrapper', }
_static_140386069899920 = {u'class': u'icon-bar', }
_static_140386186296528 = __compile_zt_expr
_static_140386071550352 = {u'class': u'container', }
_static_140386069900880 = {u'class': u'sr-only', }
_static_140386070486736 = {u'class': u'plone-nav plone-navbar-nav', u'id': u'portal-globalnav', }
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070082128
            __attrs_140386070082128 = _static_140386247937936

            # <Value u'python:view.navtree' (5:20)> -> __condition
            __token = 196
            try:
                __zt_tmp = __attrs_140386070082128
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('python', u'view.navtree', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140386070081936 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2dd6b710> name=None at 7fae2dd6bb50> -> __attrs_140386070083280
                __attrs_140386070083280 = _static_140386070083344

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append(u'<nav class="plone-navbar pat-navigationmarker" id="portal-globalnav-wrapper">\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2ded1990> name=None at 7fae2ded1410> -> __attrs_140386069200080
                __attrs_140386069200080 = _static_140386071550352

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="container">\n      ')

                # <Static value=<_ast.Dict object at 0x7fae2dc93250> name=None at 7fae2dc93390> -> __attrs_140386069197840
                __attrs_140386069197840 = _static_140386069197392

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="plone-navbar-header">\n        ')

                # <Static value=<_ast.Dict object at 0x7fae2dc93690> name=None at 7fae2dc93990> -> __attrs_140386069897616
                __attrs_140386069897616 = _static_140386069198480

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="button" class="plone-navbar-toggle" data-toggle="collapse" data-target="#portal-globalnav-collapse">\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2dd3ee50> name=None at 7fae2de36d50> -> __attrs_140386069897296
                __attrs_140386069897296 = _static_140386069900880

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="sr-only">')
                __stream_140386070084304 = []
                __append_140386070084304 = __stream_140386070084304.append
                __append_140386070084304(u'Toggle navigation')
                __msgid_140386070084304 = __re_whitespace(''.join(__stream_140386070084304)).strip()
                if u'toggle_navigation':
                    __append(translate(u'toggle_navigation', mapping=None, default=__msgid_140386070084304, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2dd3ea90> name=None at 7fae2dd3e290> -> __attrs_140386069897680
                __attrs_140386069897680 = _static_140386069899920

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="icon-bar"></span>\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2dd3ee90> name=None at 7fae2dd3e550> -> __attrs_140386069899984
                __attrs_140386069899984 = _static_140386069900944

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="icon-bar"></span>\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2ddcd390> name=None at 7fae2ddcde50> -> __attrs_140386070484112
                __attrs_140386070484112 = _static_140386070483856

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="icon-bar"></span>\n        </button>\n      </div>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7fae2dd3ec10> name=None at 7fae2dd3e750> -> __attrs_140386070485968
                __attrs_140386070485968 = _static_140386069900304

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="plone-collapse plone-navbar-collapse" id="portal-globalnav-collapse">\n        ')

                # <Static value=<_ast.Dict object at 0x7fae2ddcded0> name=None at 7fae2ddcd750> -> __attrs_140386070522512
                __attrs_140386070522512 = _static_140386070486736

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="plone-nav plone-navbar-nav" id="portal-globalnav">\n          ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070523856
                __attrs_140386070523856 = _static_140386247937936

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070520720
                __default_140386070520720 = _DEFAULT_MARKER

                # <Value u'python:view.render_globalnav()' (21:42)> -> __cache_140386070523664
                __token = 962
                try:
                    __zt_tmp = __attrs_140386070523856
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140386070523664 = _static_140386186296528('python', u'view.render_globalnav()', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:view.render_globalnav()' (21:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2ddd6210> -> __condition
                __expression = __cache_140386070523664

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <navtree ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<navtree />')
                else:
                    __content = __cache_140386070523664
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </ul>\n      </div>\n    </div>\n  </nav>\n\n')
                __i18n_domain = __previous_i18n_domain_140386070081936
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
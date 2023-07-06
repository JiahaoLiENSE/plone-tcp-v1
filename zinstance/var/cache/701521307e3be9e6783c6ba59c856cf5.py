# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/sections.pt'

__tokens = {196: (u'python:view.navtree', 5, 20), 962: (u'python:view.render_globalnav()', 21, 42)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235373759248 = {u'class': u'icon-bar', }
_static_140235442515792 = {u'class': u'plone-navbar-header', }
_static_140235374138640 = {u'data-toggle': u'collapse', u'type': u'button', u'class': u'plone-navbar-toggle', u'data-target': u'#portal-globalnav-collapse', }
_static_140235489934800 = {}
_static_140235374547280 = {u'class': u'plone-nav plone-navbar-nav', u'id': u'portal-globalnav', }
_static_140235373800400 = {u'class': u'icon-bar', }
_static_140235435449424 = __compile_zt_expr
_static_140235373757200 = {u'class': u'icon-bar', }
_static_140235442512208 = {u'class': u'container', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235442515344 = {u'class': u'plone-navbar pat-navigationmarker', u'id': u'portal-globalnav-wrapper', }
_static_140235374141264 = {u'class': u'sr-only', }
_static_140235374138832 = {u'class': u'plone-collapse plone-navbar-collapse', u'id': u'portal-globalnav-collapse', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235385249744
            __attrs_140235385249744 = _static_140235489934800

            # <Value u'python:view.navtree' (5:20)> -> __condition
            __token = 196
            try:
                __zt_tmp = __attrs_140235385249744
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('python', u'view.navtree', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140235385249360 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1bbc6d90> name=None at 7f8b1bbc6d50> -> __attrs_140235442514192
                __attrs_140235442514192 = _static_140235442515344

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append(u'<nav class="plone-navbar pat-navigationmarker" id="portal-globalnav-wrapper">\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1bbc6150> name=None at 7f8b1bbc6f90> -> __attrs_140235442513168
                __attrs_140235442513168 = _static_140235442512208

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="container">\n      ')

                # <Static value=<_ast.Dict object at 0x7f8b1bbc6f50> name=None at 7f8b1bbc6350> -> __attrs_140235374137424
                __attrs_140235374137424 = _static_140235442515792

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="plone-navbar-header">\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b17a91510> name=None at 7f8b17a911d0> -> __attrs_140235374138448
                __attrs_140235374138448 = _static_140235374138640

                # <button ... (0:0)
                # --------------------------------------------------------
                __append(u'<button type="button" class="plone-navbar-toggle" data-toggle="collapse" data-target="#portal-globalnav-collapse">\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b17a91f50> name=None at 7f8b17a91f90> -> __attrs_140235373757136
                __attrs_140235373757136 = _static_140235374141264

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="sr-only">')
                __stream_140235374138064 = []
                __append_140235374138064 = __stream_140235374138064.append
                __append_140235374138064(u'Toggle navigation')
                __msgid_140235374138064 = __re_whitespace(''.join(__stream_140235374138064)).strip()
                if u'toggle_navigation':
                    __append(translate(u'toggle_navigation', mapping=None, default=__msgid_140235374138064, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b17a34310> name=None at 7f8b17a34b50> -> __attrs_140235373756688
                __attrs_140235373756688 = _static_140235373757200

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="icon-bar"></span>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b17a34b10> name=None at 7f8b17a34150> -> __attrs_140235373759504
                __attrs_140235373759504 = _static_140235373759248

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="icon-bar"></span>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b17a3ebd0> name=None at 7f8b17a34590> -> __attrs_140235373800208
                __attrs_140235373800208 = _static_140235373800400

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span class="icon-bar"></span>\n        </button>\n      </div>\n\n      ')

                # <Static value=<_ast.Dict object at 0x7f8b17a915d0> name=None at 7f8b17a91750> -> __attrs_140235374548368
                __attrs_140235374548368 = _static_140235374138832

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="plone-collapse plone-navbar-collapse" id="portal-globalnav-collapse">\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b17af5150> name=None at 7f8b17af5950> -> __attrs_140235374547920
                __attrs_140235374547920 = _static_140235374547280

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="plone-nav plone-navbar-nav" id="portal-globalnav">\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426046480
                __attrs_140235426046480 = _static_140235489934800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426049424
                __default_140235426049424 = _DEFAULT_MARKER

                # <Value u'python:view.render_globalnav()' (21:42)> -> __cache_140235374550800
                __token = 962
                try:
                    __zt_tmp = __attrs_140235426046480
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235374550800 = _static_140235435449424('python', u'view.render_globalnav()', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:view.render_globalnav()' (21:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17af5310> -> __condition
                __expression = __cache_140235374550800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <navtree ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<navtree />')
                else:
                    __content = __cache_140235374550800
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n        </ul>\n      </div>\n    </div>\n  </nav>\n\n')
                __i18n_domain = __previous_i18n_domain_140235385249360
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
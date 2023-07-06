# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/browser/templates/main_template.pt'

__tokens = {3333: (u'provider:plone.abovecontenttitle', 83, 73), 3465: (u'context/@@title', 85, 41), 3585: (u'provider:plone.belowcontenttitle', 87, 73), 3729: (u'context/@@description', 90, 40), 3879: (u'provider:plone.abovecontentbody', 94, 70), 4013: (u'nothing', 96, 64), 4165: (u'provider:plone.belowcontentbody', 100, 70), 71: (u'string:&lt;!DOCTYPE ht', 2, 36), 344: (u"python:context.restrictedTraverse('@@plone_portal_state')", 8, 31), 426: (u" python:context.restrictedTraverse('@@plone_context_state'", 9, 23), 506: (u"w python:context.restrictedTraverse('@@plone", 10, 19), 574: (u"ut python:context.restrictedTraverse('@@plone_layou", 11, 20), 641: (u'ang python:portal_state.langua', 12, 11), 687: (u'view nocall:view | nocall: plone', 13, 10), 736: (u'dummy python: plone_layout.mark_view', 14, 10), 794: (u'al_url python:portal_state.porta', 15, 14), 853: (u"mission python:context.restrictedTraverse('portal_membership').checkPe", 16, 18), 950: (u"operties python:context.restrictedTraverse('portal_properties').site_p", 17, 17), 1049: (u"lude_head python:request.get('ajax_include_hea", 18, 18), 1116: (u' ajax_load p', 19, 9), 1195: (u'lang', 21, 27), 1244: (u'provider:plone.httpheaders', 23, 40), 1312: (u'provider:plone.htmlhead', 25, 36), 1367: (u'nothing', 27, 26), 1653: (u'provider:plone.scripts', 34, 32), 1778: (u'provider:plone.htmlhead.links', 37, 33), 1915: (u'portal_state/is_rtl', 42, 26), 1958: (u" python:plone_layout.have_portlets('plone.leftcolumn', view", 43, 22), 2041: (u"r python:plone_layout.have_portlets('plone.rightcolumn', vie", 44, 21), 2133: (u'ss python:plone_layout.bodyClass(template, vi', 45, 28), 2309: (u'  python:plone_view.patterns_settings', 48, 22), 2214: (u'body_class', 46, 30), 2253: (u" python:isRTL and 'rtl' or 'ltr", 47, 27), 2419: (u'provider:plone.toolbar', 51, 32), 2530: (u'provider:plone.portaltop', 54, 34), 2633: (u'provider:plone.mainnavigation', 57, 59), 2783: (u'provider:plone.globalstatusmessage', 62, 42), 2960: (u'provider:plone.abovecontent', 67, 59), 4621: (u'provider:plone.belowcontent', 115, 63), 4794: (u'sl', 123, 26), 4892: (u'provider:plone.leftcolumn', 125, 38), 5067: (u'sr', 131, 26), 5165: (u'provider:plone.rightcolumn', 133, 38), 5328: (u'provider:plone.portalfooter', 138, 34)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386127894992 = {u'id': u'portal-column-two', }
_static_140386184355600 = set([])
_static_140386204893584 = {u'id': u'viewlet-above-content-body', }
_static_140386178004496 = {u'lang': u'lang', u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140386204876624 = {u'id': u'viewlet-below-content-body', }
_static_140386247937936 = {}
_static_140386204895824 = {u'id': u'content-core', }
_static_140386127695952 = {u'id': u'global_statusmessage', }
_static_140386177587152 = {u'id': u'portal-column-content', }
_static_140386135567312 = {u'id': u'visual-portal-wrapper', u'dir': u"python:isRTL and 'rtl' or 'ltr'", u'class': u'body_class', }
_static_140386135566480 = {u'content': u'Plone - http://plone.com', u'name': u'generator', }
_static_140386204875984 = {u'id': u'viewlet-below-content', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386177933520 = {u'id': u'portal-mainnavigation', }
_static_140386128635024 = {u'id': u'viewlet-above-content-title', }
_static_140386127896080 = {u'id': u'portal-footer-wrapper', }
_static_140386127697680 = {u'id': u'viewlet-above-content', }
_static_140386204879056 = {u'id': u'viewlet-below-content-title', }
_static_140386175263888 = {u'id': u'portal-column-one', }
_static_140386177934800 = {u'id': u'portal-top', }
_static_140386186296528 = __compile_zt_expr
_static_140386195055184 = {u'id': u'content', }

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

    def render_content(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_content_description = econtext[u'__slot_content_description'].pop()
        except:
            __slot_content_description = None

        try:
            __slot_main = econtext[u'__slot_main'].pop()
        except:
            __slot_main = None

        try:
            __slot_body = econtext[u'__slot_body'].pop()
        except:
            __slot_body = None

        try:
            __slot_content_core = econtext[u'__slot_content_core'].pop()
        except:
            __slot_content_core = None

        try:
            __slot_content_title = econtext[u'__slot_content_title'].pop()
        except:
            __slot_content_title = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175266640
            __attrs_140386175266640 = _static_140386247937936

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n\n\n        ')
            if (__slot_body is None):

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386195055248
                __attrs_140386195055248 = _static_140386247937936
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7fae3549a250> name=None at 7fae3549a910> -> __attrs_140386195056208
                __attrs_140386195056208 = _static_140386195055184

                # <article ... (0:0)
                # --------------------------------------------------------
                __append(u'<article id="content">\n\n          ')
                if (__slot_main is None):

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386128634256
                    __attrs_140386128634256 = _static_140386247937936
                    __append(u'\n\n          ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386128637712
                    __attrs_140386128637712 = _static_140386247937936

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<header>\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae31542490> name=None at 7fae315422d0> -> __attrs_140386204878800
                    __attrs_140386204878800 = _static_140386128635024

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-above-content-title">')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386128634832
                    __default_140386128634832 = _DEFAULT_MARKER

                    # <Value u'provider:plone.abovecontenttitle' (83:73)> -> __cache_140386128635408
                    __token = 3333
                    try:
                        __zt_tmp = __attrs_140386204878800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386128635408 = _static_140386186296528('provider', u'plone.abovecontenttitle', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.abovecontenttitle' (83:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae31542910> -> __condition
                    __expression = __cache_140386128635408

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386128635408
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n            ')
                    if (__slot_content_title is None):

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204880400
                        __attrs_140386204880400 = _static_140386247937936
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204878096
                        __attrs_140386204878096 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204880080
                        __default_140386204880080 = _DEFAULT_MARKER

                        # <Value u'context/@@title' (85:41)> -> __cache_140386204879568
                        __token = 3465
                        try:
                            __zt_tmp = __attrs_140386204878096
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386204879568 = _static_140386186296528('path', u'context/@@title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'context/@@title' (85:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae35df8f50> -> __condition
                        __expression = __cache_140386204879568

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <h1 ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<h1 />')
                        else:
                            __content = __cache_140386204879568
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n            ')
                    else:
                        __slot_content_title(__stream, econtext.copy(), rcontext)
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae35df88d0> name=None at 7fae35df8950> -> __attrs_140386204880016
                    __attrs_140386204880016 = _static_140386204879056

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-below-content-title">')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204878928
                    __default_140386204878928 = _DEFAULT_MARKER

                    # <Value u'provider:plone.belowcontenttitle' (87:73)> -> __cache_140386204880336
                    __token = 3585
                    try:
                        __zt_tmp = __attrs_140386204880016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386204880336 = _static_140386186296528('provider', u'plone.belowcontenttitle', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.belowcontenttitle' (87:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae35df8890> -> __condition
                    __expression = __cache_140386204880336

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386204880336
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n\n            ')
                    if (__slot_content_description is None):

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204895632
                        __attrs_140386204895632 = _static_140386247937936
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204893648
                        __attrs_140386204893648 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204894608
                        __default_140386204894608 = _DEFAULT_MARKER

                        # <Value u'context/@@description' (90:40)> -> __cache_140386204894096
                        __token = 3729
                        try:
                            __zt_tmp = __attrs_140386204893648
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386204894096 = _static_140386186296528('path', u'context/@@description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'context/@@description' (90:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae35dfc0d0> -> __condition
                        __expression = __cache_140386204894096

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<p />')
                        else:
                            __content = __cache_140386204894096
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n            ')
                    else:
                        __slot_content_description(__stream, econtext.copy(), rcontext)
                    __append(u'\n          </header>\n\n          ')

                    # <Static value=<_ast.Dict object at 0x7fae35dfc190> name=None at 7fae35dfc290> -> __attrs_140386204896976
                    __attrs_140386204896976 = _static_140386204893584

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-above-content-body">')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204895504
                    __default_140386204895504 = _DEFAULT_MARKER

                    # <Value u'provider:plone.abovecontentbody' (94:70)> -> __cache_140386204879824
                    __token = 3879
                    try:
                        __zt_tmp = __attrs_140386204896976
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386204879824 = _static_140386186296528('provider', u'plone.abovecontentbody', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.abovecontentbody' (94:70)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae35df8790> -> __condition
                    __expression = __cache_140386204879824

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386204879824
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fae35dfca50> name=None at 7fae35dfcf50> -> __attrs_140386204896656
                    __attrs_140386204896656 = _static_140386204895824

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="content-core">\n            ')
                    if (__slot_content_core is None):

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204876560
                        __attrs_140386204876560 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204873744
                        __default_140386204873744 = _DEFAULT_MARKER

                        # <Value u'nothing' (96:64)> -> __cache_140386204874384
                        __token = 4013
                        try:
                            __zt_tmp = __attrs_140386204876560
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386204874384 = _static_140386186296528('path', u'nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'nothing' (96:64)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae35df76d0> -> __condition
                        __expression = __cache_140386204874384

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n              Page body text\n            ')
                        else:
                            __content = __cache_140386204874384
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    else:
                        __slot_content_core(__stream, econtext.copy(), rcontext)
                    __append(u'\n          </div>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fae35df7f50> name=None at 7fae35df7e10> -> __attrs_140386204873360
                    __attrs_140386204873360 = _static_140386204876624

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-below-content-body">')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204875920
                    __default_140386204875920 = _DEFAULT_MARKER

                    # <Value u'provider:plone.belowcontentbody' (100:70)> -> __cache_140386204873872
                    __token = 4165
                    try:
                        __zt_tmp = __attrs_140386204873360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386204873872 = _static_140386186296528('provider', u'plone.belowcontentbody', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.belowcontentbody' (100:70)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae35df72d0> -> __condition
                    __expression = __cache_140386204873872

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386204873872
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n\n          ')
                else:
                    __slot_main(__stream, econtext.copy(), rcontext)
                __append(u'\n        </article>\n\n        ')
            else:
                __slot_body(__stream, econtext.copy(), rcontext)
            __append(u'\n\n<!--                 <metal:sub define-slot="sub" tal:content="nothing">\n                   This slot is here for backwards compatibility only.\n                   Don\'t use it in your custom templates.\n                </metal:sub> -->\n      </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_column_one_slot = econtext[u'__slot_column_one_slot'].pop()
        except:
            __slot_column_one_slot = None

        try:
            __slot_head_slot = econtext[u'__slot_head_slot'].pop()
        except:
            __slot_head_slot = None

        try:
            __slot_column_two_slot = econtext[u'__slot_column_two_slot'].pop()
        except:
            __slot_column_two_slot = None

        try:
            __slot_style_slot = econtext[u'__slot_style_slot'].pop()
        except:
            __slot_style_slot = None

        try:
            __slot_javascript_head_slot = econtext[u'__slot_javascript_head_slot'].pop()
        except:
            __slot_javascript_head_slot = None

        try:
            __slot_global_statusmessage = econtext[u'__slot_global_statusmessage'].pop()
        except:
            __slot_global_statusmessage = None

        try:
            __slot_top_slot = econtext[u'__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_portlets_one_slot = econtext[u'__slot_portlets_one_slot'].pop()
        except:
            __slot_portlets_one_slot = None

        try:
            __slot_portlets_two_slot = econtext[u'__slot_portlets_two_slot'].pop()
        except:
            __slot_portlets_two_slot = None

        try:
            __slot_content = econtext[u'__slot_content'].pop()
        except:
            __slot_content = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386178006160
            __attrs_140386178006160 = _static_140386247937936
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386178006992
            __attrs_140386178006992 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386178005520
            __default_140386178005520 = _DEFAULT_MARKER

            # <Value u'string:<!DOCTYPE html>' (2:36)> -> __cache_140386178003536
            __token = 71
            try:
                __zt_tmp = __attrs_140386178006992
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386178003536 = _static_140386186296528('string', u'<!DOCTYPE html>', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'string:<!DOCTYPE html>' (2:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae344574d0> -> __condition
            __expression = __cache_140386178003536

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140386178003536
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n')

            # <Static value=<_ast.Dict object at 0x7fae34457610> name=None at 7fae34457390> -> __attrs_140386178003280
            __attrs_140386178003280 = _static_140386178004496
            __backup_portal_state_140386179279184 = get('portal_state', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone_portal_state')" (8:31)> -> __value
            __token = 344
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"context.restrictedTraverse('@@plone_portal_state')", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_context_state_140386177668112 = get('context_state', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone_context_state')" (9:23)> -> __value
            __token = 426
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"context.restrictedTraverse('@@plone_context_state')", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_plone_view_140386133913488 = get('plone_view', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone')" (10:19)> -> __value
            __token = 506
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"context.restrictedTraverse('@@plone')", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_plone_layout_140386134468944 = get('plone_layout', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone_layout')" (11:20)> -> __value
            __token = 574
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"context.restrictedTraverse('@@plone_layout')", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_lang_140386134468432 = get('lang', __marker)

            # <Value u'python:portal_state.language()' (12:11)> -> __value
            __token = 641
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u'portal_state.language()', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['lang'] = __value
            __backup_view_140386133931728 = get('view', __marker)

            # <Value u'nocall:view | nocall: plone_view' (13:10)> -> __value
            __token = 687
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('nocall', u'view | nocall: plone_view', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_dummy_140386130227472 = get('dummy', __marker)

            # <Value u'python: plone_layout.mark_view(view)' (14:10)> -> __value
            __token = 736
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u' plone_layout.mark_view(view)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['dummy'] = __value
            __backup_portal_url_140386134093328 = get('portal_url', __marker)

            # <Value u'python:portal_state.portal_url()' (15:14)> -> __value
            __token = 794
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u'portal_state.portal_url()', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_checkPermission_140386133913424 = get('checkPermission', __marker)

            # <Value u"python:context.restrictedTraverse('portal_membership').checkPermission" (16:18)> -> __value
            __token = 853
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"context.restrictedTraverse('portal_membership').checkPermission", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['checkPermission'] = __value
            __backup_site_properties_140386134561552 = get('site_properties', __marker)

            # <Value u"python:context.restrictedTraverse('portal_properties').site_properties" (17:17)> -> __value
            __token = 950
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"context.restrictedTraverse('portal_properties').site_properties", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['site_properties'] = __value
            __backup_ajax_include_head_140386130230480 = get('ajax_include_head', __marker)

            # <Value u"python:request.get('ajax_include_head', False)" (18:18)> -> __value
            __token = 1049
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"request.get('ajax_include_head', False)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['ajax_include_head'] = __value
            __backup_ajax_load_140386134562064 = get('ajax_load', __marker)

            # <Value u'python:False' (19:9)> -> __value
            __token = 1116
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u'False', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['ajax_load'] = __value
            __previous_i18n_domain_140386178040912 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386178003920
            __default_140386178003920 = _DEFAULT_MARKER

            # <Substitution u'lang' (21:27)> -> __attr_lang
            __token = 1195
            try:
                __zt_tmp = __attrs_140386178003280
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140386186296528('path', u'lang', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((u' lang="%s"' % __attr_lang))
            __append(u'>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386178041424
            __attrs_140386178041424 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386178041616
            __default_140386178041616 = _DEFAULT_MARKER

            # <Value u'provider:plone.httpheaders' (23:40)> -> __cache_140386178042192
            __token = 1244
            try:
                __zt_tmp = __attrs_140386178041424
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386178042192 = _static_140386186296528('provider', u'plone.httpheaders', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.httpheaders' (23:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae34460810> -> __condition
            __expression = __cache_140386178042192

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140386178042192
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386178043408
            __attrs_140386178043408 = _static_140386247937936

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386178040464
            __attrs_140386178040464 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386178043664
            __default_140386178043664 = _DEFAULT_MARKER

            # <Value u'provider:plone.htmlhead' (25:36)> -> __cache_140386178040400
            __token = 1312
            try:
                __zt_tmp = __attrs_140386178040464
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386178040400 = _static_140386186296528('provider', u'plone.htmlhead', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.htmlhead' (25:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae34460690> -> __condition
            __expression = __cache_140386178040400

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140386178040400
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194999632
            __attrs_140386194999632 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386194997904
            __default_140386194997904 = _DEFAULT_MARKER

            # <Value u'nothing' (27:26)> -> __cache_140386194999760
            __token = 1367
            try:
                __zt_tmp = __attrs_140386194999632
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386194999760 = _static_140386186296528('path', u'nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'nothing' (27:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae3548cc10> -> __condition
            __expression = __cache_140386194999760

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n        Various slots where you can insert elements in the header from a template.\n    ')
            else:
                __content = __cache_140386194999760
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    ')
            if (__slot_top_slot is None):

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386195000912
                __attrs_140386195000912 = _static_140386247937936
            else:
                __slot_top_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n    ')
            if (__slot_head_slot is None):

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194998672
                __attrs_140386194998672 = _static_140386247937936
            else:
                __slot_head_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n    ')
            if (__slot_style_slot is None):

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194999312
                __attrs_140386194999312 = _static_140386247937936
            else:
                __slot_style_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194999376
            __attrs_140386194999376 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386194999184
            __default_140386194999184 = _DEFAULT_MARKER

            # <Value u'provider:plone.scripts' (34:32)> -> __cache_140386194999696
            __token = 1653
            try:
                __zt_tmp = __attrs_140386194999376
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386194999696 = _static_140386186296528('provider', u'plone.scripts', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.scripts' (34:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae3548c7d0> -> __condition
            __expression = __cache_140386194999696

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140386194999696
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    ')
            if (__slot_javascript_head_slot is None):

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194997520
                __attrs_140386194997520 = _static_140386247937936
            else:
                __slot_javascript_head_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386194998864
            __attrs_140386194998864 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386194999824
            __default_140386194999824 = _DEFAULT_MARKER

            # <Value u'provider:plone.htmlhead.links' (37:33)> -> __cache_140386194997584
            __token = 1778
            try:
                __zt_tmp = __attrs_140386194998864
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386194997584 = _static_140386186296528('provider', u'plone.htmlhead.links', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.htmlhead.links' (37:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae3548c210> -> __condition
            __expression = __cache_140386194997584

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <link ... (0:0)
                # --------------------------------------------------------
                __append(u'<link />')
            else:
                __content = __cache_140386194997584
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7fae31bde890> name=None at 7fae31bde9d0> -> __attrs_140386135567824
            __attrs_140386135567824 = _static_140386135566480

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta name="generator" content="Plone - http://plone.com" />\n\n  </head>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae31bdebd0> name=None at 7fae3548c5d0> -> __attrs_140386135565008
            __attrs_140386135565008 = _static_140386135567312
            __backup_isRTL_140386130455888 = get('isRTL', __marker)

            # <Value u'portal_state/is_rtl' (42:26)> -> __value
            __token = 1915
            try:
                __zt_tmp = __attrs_140386135565008
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'portal_state/is_rtl', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['isRTL'] = __value
            __backup_sl_140386130995024 = get('sl', __marker)

            # <Value u"python:plone_layout.have_portlets('plone.leftcolumn', view)" (43:22)> -> __value
            __token = 1958
            try:
                __zt_tmp = __attrs_140386135565008
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"plone_layout.have_portlets('plone.leftcolumn', view)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['sl'] = __value
            __backup_sr_140386130994256 = get('sr', __marker)

            # <Value u"python:plone_layout.have_portlets('plone.rightcolumn', view)" (44:21)> -> __value
            __token = 2041
            try:
                __zt_tmp = __attrs_140386135565008
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"plone_layout.have_portlets('plone.rightcolumn', view)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['sr'] = __value
            __backup_body_class_140386130455504 = get('body_class', __marker)

            # <Value u'python:plone_layout.bodyClass(template, view)' (45:28)> -> __value
            __token = 2133
            try:
                __zt_tmp = __attrs_140386135565008
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u'plone_layout.bodyClass(template, view)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['body_class'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body')

            # <Value u'python:plone_view.patterns_settings()' (48:22)> -> __cache_140386135568208
            __token = 2309
            try:
                __zt_tmp = __attrs_140386135565008
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386135568208 = _static_140386186296528('python', u'plone_view.patterns_settings()', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if (u'id' not in __chain(__cache_140386135568208)):
                __append(u' id="visual-portal-wrapper"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386135568016
            __default_140386135568016 = _DEFAULT_MARKER

            # <Substitution u'body_class' (46:30)> -> __attr_class
            __token = 2214
            try:
                __zt_tmp = __attrs_140386135565008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140386186296528('path', u'body_class', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and (u'class' not in __chain(__cache_140386135568208))):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386135564944
            __default_140386135564944 = _DEFAULT_MARKER

            # <Substitution u"python:isRTL and 'rtl' or 'ltr'" (47:27)> -> __attr_dir
            __token = 2253
            try:
                __zt_tmp = __attrs_140386135565008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_140386186296528('python', u"isRTL and 'rtl' or 'ltr'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_dir is not None) and (u'dir' not in __chain(__cache_140386135568208))):
                __append((u' dir="%s"' % __attr_dir))
            __attr_140386135568272 = __cache_140386135568208
            for (name, value, ) in __attr_140386135568272.items():
                if ((name not in _static_140386184355600) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append(u'>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386177937040
            __attrs_140386177937040 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386177936272
            __default_140386177936272 = _DEFAULT_MARKER

            # <Value u'provider:plone.toolbar' (51:32)> -> __cache_140386177934672
            __token = 2419
            try:
                __zt_tmp = __attrs_140386177937040
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386177934672 = _static_140386186296528('provider', u'plone.toolbar', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.toolbar' (51:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae34446a50> -> __condition
            __expression = __cache_140386177934672

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140386177934672
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae344465d0> name=None at 7fae344461d0> -> __attrs_140386177936016
            __attrs_140386177936016 = _static_140386177934800
            __previous_i18n_domain_140386177936720 = __i18n_domain
            __i18n_domain = u'plone'

            # <header ... (0:0)
            # --------------------------------------------------------
            __append(u'<header id="portal-top">\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386177935696
            __attrs_140386177935696 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386177936464
            __default_140386177936464 = _DEFAULT_MARKER

            # <Value u'provider:plone.portaltop' (54:34)> -> __cache_140386177936592
            __token = 2530
            try:
                __zt_tmp = __attrs_140386177935696
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386177936592 = _static_140386186296528('provider', u'plone.portaltop', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.portaltop' (54:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae344468d0> -> __condition
            __expression = __cache_140386177936592

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140386177936592
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    </header>')
            __i18n_domain = __previous_i18n_domain_140386177936720
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae344460d0> name=None at 7fae34446090> -> __attrs_140386177936656
            __attrs_140386177936656 = _static_140386177933520

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="portal-mainnavigation">')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386177934416
            __default_140386177934416 = _DEFAULT_MARKER

            # <Value u'provider:plone.mainnavigation' (57:59)> -> __cache_140386177937104
            __token = 2633
            try:
                __zt_tmp = __attrs_140386177936656
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386177937104 = _static_140386186296528('provider', u'plone.mainnavigation', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.mainnavigation' (57:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae344464d0> -> __condition
            __expression = __cache_140386177937104

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n      The main navigation\n    ')
            else:
                __content = __cache_140386177937104
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae3145d050> name=None at 7fae3145d9d0> -> __attrs_140386127697296
            __attrs_140386127697296 = _static_140386127695952

            # <aside ... (0:0)
            # --------------------------------------------------------
            __append(u'<aside id="global_statusmessage">\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127697936
            __attrs_140386127697936 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127697808
            __default_140386127697808 = _DEFAULT_MARKER

            # <Value u'provider:plone.globalstatusmessage' (62:42)> -> __cache_140386127697552
            __token = 2783
            try:
                __zt_tmp = __attrs_140386127697936
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386127697552 = _static_140386186296528('provider', u'plone.globalstatusmessage', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.globalstatusmessage' (62:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae3145db10> -> __condition
            __expression = __cache_140386127697552

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140386127697552
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n      ')
            if (__slot_global_statusmessage is None):

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127697744
                __attrs_140386127697744 = _static_140386247937936

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n      </div>')
            else:
                __slot_global_statusmessage(__stream, econtext.copy(), rcontext)
            __append(u'\n    </aside>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae3145d710> name=None at 7fae3145da90> -> __attrs_140386177585936
            __attrs_140386177585936 = _static_140386127697680

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="viewlet-above-content">')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127698768
            __default_140386127698768 = _DEFAULT_MARKER

            # <Value u'provider:plone.abovecontent' (67:59)> -> __cache_140386127696400
            __token = 2960
            try:
                __zt_tmp = __attrs_140386177585936
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386127696400 = _static_140386186296528('provider', u'plone.abovecontent', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.abovecontent' (67:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae3145dfd0> -> __condition
            __expression = __cache_140386127696400

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140386127696400
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae343f17d0> name=None at 7fae343f1390> -> __attrs_140386175265232
            __attrs_140386175265232 = _static_140386177587152

            # <article ... (0:0)
            # --------------------------------------------------------
            __append(u'<article id="portal-column-content">\n\n      ')
            if (__slot_content is None):

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175265488
                __attrs_140386175265488 = _static_140386247937936
                __append(u'\n\n      ')
                __token = None
                render_content(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n\n      ')
            else:
                __slot_content(__stream, econtext.copy(), rcontext)
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386195055760
            __attrs_140386195055760 = _static_140386247937936

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append(u'<footer>\n        ')

            # <Static value=<_ast.Dict object at 0x7fae35df7cd0> name=None at 7fae35df7dd0> -> __attrs_140386204875856
            __attrs_140386204875856 = _static_140386204875984

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="viewlet-below-content">')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204895376
            __default_140386204895376 = _DEFAULT_MARKER

            # <Value u'provider:plone.belowcontent' (115:63)> -> __cache_140386128635152
            __token = 4621
            try:
                __zt_tmp = __attrs_140386204875856
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386128635152 = _static_140386186296528('provider', u'plone.belowcontent', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.belowcontent' (115:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae31542290> -> __condition
            __expression = __cache_140386128635152

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140386128635152
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n      </footer>\n    </article>\n\n\n\n    ')
            if (__slot_column_one_slot is None):

                # <Static value=<_ast.Dict object at 0x7fae341ba490> name=None at 7fae341ba350> -> __attrs_140386204874576
                __attrs_140386204874576 = _static_140386175263888

                # <Value u'sl' (123:26)> -> __condition
                __token = 4794
                try:
                    __zt_tmp = __attrs_140386204874576
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'sl', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<aside id="portal-column-one">\n      ')
                    if (__slot_portlets_one_slot is None):

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127892624
                        __attrs_140386127892624 = _static_140386247937936
                        __append(u'\n        ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127893520
                        __attrs_140386127893520 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127895952
                        __default_140386127895952 = _DEFAULT_MARKER

                        # <Value u'provider:plone.leftcolumn' (125:38)> -> __cache_140386127894352
                        __token = 4892
                        try:
                            __zt_tmp = __attrs_140386127893520
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386127894352 = _static_140386186296528('provider', u'plone.leftcolumn', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'provider:plone.leftcolumn' (125:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae3148da50> -> __condition
                        __expression = __cache_140386127894352

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140386127894352
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n      ')
                    else:
                        __slot_portlets_one_slot(__stream, econtext.copy(), rcontext)
                    __append(u'\n    </aside>')
            else:
                __slot_column_one_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n\n    ')
            if (__slot_column_two_slot is None):

                # <Static value=<_ast.Dict object at 0x7fae3148d9d0> name=None at 7fae3148d890> -> __attrs_140386127894800
                __attrs_140386127894800 = _static_140386127894992

                # <Value u'sr' (131:26)> -> __condition
                __token = 5067
                try:
                    __zt_tmp = __attrs_140386127894800
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'sr', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<aside id="portal-column-two">\n      ')
                    if (__slot_portlets_two_slot is None):

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127895312
                        __attrs_140386127895312 = _static_140386247937936
                        __append(u'\n        ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386135457680
                        __attrs_140386135457680 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386135456400
                        __default_140386135456400 = _DEFAULT_MARKER

                        # <Value u'provider:plone.rightcolumn' (133:38)> -> __cache_140386135454352
                        __token = 5165
                        try:
                            __zt_tmp = __attrs_140386135457680
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386135454352 = _static_140386186296528('provider', u'plone.rightcolumn', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'provider:plone.rightcolumn' (133:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae31bc3190> -> __condition
                        __expression = __cache_140386135454352

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140386135454352
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n      ')
                    else:
                        __slot_portlets_two_slot(__stream, econtext.copy(), rcontext)
                    __append(u'\n    </aside>')
            else:
                __slot_column_two_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae3148de10> name=None at 7fae3148d590> -> __attrs_140386135455632
            __attrs_140386135455632 = _static_140386127896080
            __previous_i18n_domain_140386135457424 = __i18n_domain
            __i18n_domain = u'plone'

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append(u'<footer id="portal-footer-wrapper">\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386135455952
            __attrs_140386135455952 = _static_140386247937936

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386135457168
            __default_140386135457168 = _DEFAULT_MARKER

            # <Value u'provider:plone.portalfooter' (138:34)> -> __cache_140386135456336
            __token = 5328
            try:
                __zt_tmp = __attrs_140386135455952
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386135456336 = _static_140386186296528('provider', u'plone.portalfooter', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.portalfooter' (138:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae31bc3c10> -> __condition
            __expression = __cache_140386135456336

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140386135456336
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    </footer>')
            __i18n_domain = __previous_i18n_domain_140386135457424
            __append(u'\n\n  </body>')
            if (__backup_body_class_140386130455504 is __marker):
                del econtext['body_class']
            else:
                econtext['body_class'] = __backup_body_class_140386130455504
            if (__backup_sr_140386130994256 is __marker):
                del econtext['sr']
            else:
                econtext['sr'] = __backup_sr_140386130994256
            if (__backup_sl_140386130995024 is __marker):
                del econtext['sl']
            else:
                econtext['sl'] = __backup_sl_140386130995024
            if (__backup_isRTL_140386130455888 is __marker):
                del econtext['isRTL']
            else:
                econtext['isRTL'] = __backup_isRTL_140386130455888
            __append(u'\n</html>')
            __i18n_domain = __previous_i18n_domain_140386178040912
            if (__backup_ajax_load_140386134562064 is __marker):
                del econtext['ajax_load']
            else:
                econtext['ajax_load'] = __backup_ajax_load_140386134562064
            if (__backup_ajax_include_head_140386130230480 is __marker):
                del econtext['ajax_include_head']
            else:
                econtext['ajax_include_head'] = __backup_ajax_include_head_140386130230480
            if (__backup_site_properties_140386134561552 is __marker):
                del econtext['site_properties']
            else:
                econtext['site_properties'] = __backup_site_properties_140386134561552
            if (__backup_checkPermission_140386133913424 is __marker):
                del econtext['checkPermission']
            else:
                econtext['checkPermission'] = __backup_checkPermission_140386133913424
            if (__backup_portal_url_140386134093328 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140386134093328
            if (__backup_dummy_140386130227472 is __marker):
                del econtext['dummy']
            else:
                econtext['dummy'] = __backup_dummy_140386130227472
            if (__backup_view_140386133931728 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_140386133931728
            if (__backup_lang_140386134468432 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_140386134468432
            if (__backup_plone_layout_140386134468944 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_140386134468944
            if (__backup_plone_view_140386133913488 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_140386133913488
            if (__backup_context_state_140386177668112 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_140386177668112
            if (__backup_portal_state_140386179279184 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_140386179279184
            __append(u'\n\n')
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
            __token = None
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_content': render_content, u'render_master': render_master, 'render': render, }
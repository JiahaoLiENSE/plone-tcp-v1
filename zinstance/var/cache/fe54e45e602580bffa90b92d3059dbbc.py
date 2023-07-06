# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/browser/templates/main_template.pt'

__tokens = {3333: (u'provider:plone.abovecontenttitle', 83, 73), 3465: (u'context/@@title', 85, 41), 3585: (u'provider:plone.belowcontenttitle', 87, 73), 3729: (u'context/@@description', 90, 40), 3879: (u'provider:plone.abovecontentbody', 94, 70), 4013: (u'nothing', 96, 64), 4165: (u'provider:plone.belowcontentbody', 100, 70), 71: (u'string:&lt;!DOCTYPE ht', 2, 36), 344: (u"python:context.restrictedTraverse('@@plone_portal_state')", 8, 31), 426: (u" python:context.restrictedTraverse('@@plone_context_state'", 9, 23), 506: (u"w python:context.restrictedTraverse('@@plone", 10, 19), 574: (u"ut python:context.restrictedTraverse('@@plone_layou", 11, 20), 641: (u'ang python:portal_state.langua', 12, 11), 687: (u'view nocall:view | nocall: plone', 13, 10), 736: (u'dummy python: plone_layout.mark_view', 14, 10), 794: (u'al_url python:portal_state.porta', 15, 14), 853: (u"mission python:context.restrictedTraverse('portal_membership').checkPe", 16, 18), 950: (u"operties python:context.restrictedTraverse('portal_properties').site_p", 17, 17), 1049: (u"lude_head python:request.get('ajax_include_hea", 18, 18), 1116: (u' ajax_load p', 19, 9), 1195: (u'lang', 21, 27), 1244: (u'provider:plone.httpheaders', 23, 40), 1312: (u'provider:plone.htmlhead', 25, 36), 1367: (u'nothing', 27, 26), 1653: (u'provider:plone.scripts', 34, 32), 1778: (u'provider:plone.htmlhead.links', 37, 33), 1915: (u'portal_state/is_rtl', 42, 26), 1958: (u" python:plone_layout.have_portlets('plone.leftcolumn', view", 43, 22), 2041: (u"r python:plone_layout.have_portlets('plone.rightcolumn', vie", 44, 21), 2133: (u'ss python:plone_layout.bodyClass(template, vi', 45, 28), 2309: (u'  python:plone_view.patterns_settings', 48, 22), 2214: (u'body_class', 46, 30), 2253: (u" python:isRTL and 'rtl' or 'ltr", 47, 27), 2419: (u'provider:plone.toolbar', 51, 32), 2530: (u'provider:plone.portaltop', 54, 34), 2633: (u'provider:plone.mainnavigation', 57, 59), 2783: (u'provider:plone.globalstatusmessage', 62, 42), 2960: (u'provider:plone.abovecontent', 67, 59), 4621: (u'provider:plone.belowcontent', 115, 63), 4794: (u'sl', 123, 26), 4892: (u'provider:plone.leftcolumn', 125, 38), 5067: (u'sr', 131, 26), 5165: (u'provider:plone.rightcolumn', 133, 38), 5328: (u'provider:plone.portalfooter', 138, 34)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140235373954320 = {u'id': u'portal-column-two', }
_static_140235437657424 = {u'id': u'viewlet-above-content-body', }
_static_140235373961616 = {u'id': u'visual-portal-wrapper', u'dir': u"python:isRTL and 'rtl' or 'ltr'", u'class': u'body_class', }
_static_140235423563152 = {u'id': u'viewlet-below-content-body', }
_static_140235373980944 = {u'id': u'portal-top', }
_static_140235373979728 = {u'id': u'global_statusmessage', }
_static_140235423561232 = {u'id': u'content-core', }
_static_140235423440400 = {u'id': u'viewlet-above-content-title', }
_static_140235374056784 = {u'id': u'portal-column-one', }
_static_140235432265296 = {u'id': u'viewlet-above-content', }
_static_140235373906128 = {u'id': u'portal-footer-wrapper', }
_static_140235427350800 = {u'content': u'Plone - http://plone.com', u'name': u'generator', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235385301200 = set([])
_static_140235373956048 = {u'id': u'viewlet-below-content', }
_static_140235374064336 = {u'id': u'content', }
_static_140235423437264 = {u'id': u'viewlet-below-content-title', }
_static_140235489934800 = {}
_static_140235427389584 = {u'lang': u'lang', u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140235435449424 = __compile_zt_expr
_static_140235373979984 = {u'id': u'portal-mainnavigation', }
_static_140235374056464 = {u'id': u'portal-column-content', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374059216
            __attrs_140235374059216 = _static_140235489934800

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div>\n\n\n        ')
            if (__slot_body is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374058768
                __attrs_140235374058768 = _static_140235489934800
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b17a7f2d0> name=None at 7f8b17a7f110> -> __attrs_140235374064400
                __attrs_140235374064400 = _static_140235374064336

                # <article ... (0:0)
                # --------------------------------------------------------
                __append(u'<article id="content">\n\n          ')
                if (__slot_main is None):

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374065488
                    __attrs_140235374065488 = _static_140235489934800
                    __append(u'\n\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374066960
                    __attrs_140235374066960 = _static_140235489934800

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<header>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1a995e10> name=None at 7f8b1a995750> -> __attrs_140235423438160
                    __attrs_140235423438160 = _static_140235423440400

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-above-content-title">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423439632
                    __default_140235423439632 = _DEFAULT_MARKER

                    # <Value u'provider:plone.abovecontenttitle' (83:73)> -> __cache_140235374064848
                    __token = 3333
                    try:
                        __zt_tmp = __attrs_140235423438160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235374064848 = _static_140235435449424('provider', u'plone.abovecontenttitle', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.abovecontenttitle' (83:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a7fb10> -> __condition
                    __expression = __cache_140235374064848

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235374064848
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n            ')
                    if (__slot_content_title is None):

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235423439312
                        __attrs_140235423439312 = _static_140235489934800
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235423440848
                        __attrs_140235423440848 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423439696
                        __default_140235423439696 = _DEFAULT_MARKER

                        # <Value u'context/@@title' (85:41)> -> __cache_140235423439248
                        __token = 3465
                        try:
                            __zt_tmp = __attrs_140235423440848
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235423439248 = _static_140235435449424('path', u'context/@@title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'context/@@title' (85:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1a995a90> -> __condition
                        __expression = __cache_140235423439248

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <h1 ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<h1 />')
                        else:
                            __content = __cache_140235423439248
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n            ')
                    else:
                        __slot_content_title(__stream, econtext.copy(), rcontext)
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1a9951d0> name=None at 7f8b1a9956d0> -> __attrs_140235437654352
                    __attrs_140235437654352 = _static_140235423437264

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-below-content-title">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423438928
                    __default_140235423438928 = _DEFAULT_MARKER

                    # <Value u'provider:plone.belowcontenttitle' (87:73)> -> __cache_140235423438736
                    __token = 3585
                    try:
                        __zt_tmp = __attrs_140235437654352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235423438736 = _static_140235435449424('provider', u'plone.belowcontenttitle', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.belowcontenttitle' (87:73)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1a995290> -> __condition
                    __expression = __cache_140235423438736

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235423438736
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n\n            ')
                    if (__slot_content_description is None):

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235437656912
                        __attrs_140235437656912 = _static_140235489934800
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235437656336
                        __attrs_140235437656336 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235437655760
                        __default_140235437655760 = _DEFAULT_MARKER

                        # <Value u'context/@@description' (90:40)> -> __cache_140235437656272
                        __token = 3729
                        try:
                            __zt_tmp = __attrs_140235437656336
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235437656272 = _static_140235435449424('path', u'context/@@description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'context/@@description' (90:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b724bd0> -> __condition
                        __expression = __cache_140235437656272

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<p />')
                        else:
                            __content = __cache_140235437656272
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n            ')
                    else:
                        __slot_content_description(__stream, econtext.copy(), rcontext)
                    __append(u'\n          </header>\n\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8b1b724d50> name=None at 7f8b1b724f90> -> __attrs_140235423560720
                    __attrs_140235423560720 = _static_140235437657424

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-above-content-body">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235437654800
                    __default_140235437654800 = _DEFAULT_MARKER

                    # <Value u'provider:plone.abovecontentbody' (94:70)> -> __cache_140235437657232
                    __token = 3879
                    try:
                        __zt_tmp = __attrs_140235423560720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235437657232 = _static_140235435449424('provider', u'plone.abovecontentbody', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.abovecontentbody' (94:70)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b724090> -> __condition
                    __expression = __cache_140235437657232

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235437657232
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8b1a9b3610> name=None at 7f8b1a9b3850> -> __attrs_140235423560976
                    __attrs_140235423560976 = _static_140235423561232

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="content-core">\n            ')
                    if (__slot_content_core is None):

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235423563216
                        __attrs_140235423563216 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423562768
                        __default_140235423562768 = _DEFAULT_MARKER

                        # <Value u'nothing' (96:64)> -> __cache_140235423560848
                        __token = 4013
                        try:
                            __zt_tmp = __attrs_140235423563216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235423560848 = _static_140235435449424('path', u'nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'nothing' (96:64)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1a9b34d0> -> __condition
                        __expression = __cache_140235423560848

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n              Page body text\n            ')
                        else:
                            __content = __cache_140235423560848
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    else:
                        __slot_content_core(__stream, econtext.copy(), rcontext)
                    __append(u'\n          </div>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8b1a9b3d90> name=None at 7f8b1a9b3fd0> -> __attrs_140235373956432
                    __attrs_140235373956432 = _static_140235423563152

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="viewlet-below-content-body">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423563472
                    __default_140235423563472 = _DEFAULT_MARKER

                    # <Value u'provider:plone.belowcontentbody' (100:70)> -> __cache_140235423562512
                    __token = 4165
                    try:
                        __zt_tmp = __attrs_140235373956432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235423562512 = _static_140235435449424('provider', u'plone.belowcontentbody', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'provider:plone.belowcontentbody' (100:70)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1a9b3290> -> __condition
                    __expression = __cache_140235423562512

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235423562512
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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235423489104
            __attrs_140235423489104 = _static_140235489934800
            __append(u'\n')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427390096
            __attrs_140235427390096 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427389904
            __default_140235427389904 = _DEFAULT_MARKER

            # <Value u'string:<!DOCTYPE html>' (2:36)> -> __cache_140235427389712
            __token = 71
            try:
                __zt_tmp = __attrs_140235427390096
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235427389712 = _static_140235435449424('string', u'<!DOCTYPE html>', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'string:<!DOCTYPE html>' (2:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ad5a190> -> __condition
            __expression = __cache_140235427389712

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140235427389712
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n')

            # <Static value=<_ast.Dict object at 0x7f8b1ad5a090> name=None at 7f8b1ad5a050> -> __attrs_140235427392784
            __attrs_140235427392784 = _static_140235427389584
            __backup_portal_state_140235423488848 = get('portal_state', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone_portal_state')" (8:31)> -> __value
            __token = 344
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"context.restrictedTraverse('@@plone_portal_state')", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_context_state_140235423488720 = get('context_state', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone_context_state')" (9:23)> -> __value
            __token = 426
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"context.restrictedTraverse('@@plone_context_state')", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_plone_view_140235423487632 = get('plone_view', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone')" (10:19)> -> __value
            __token = 506
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"context.restrictedTraverse('@@plone')", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_plone_layout_140235427391504 = get('plone_layout', __marker)

            # <Value u"python:context.restrictedTraverse('@@plone_layout')" (11:20)> -> __value
            __token = 574
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"context.restrictedTraverse('@@plone_layout')", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_lang_140235427391248 = get('lang', __marker)

            # <Value u'python:portal_state.language()' (12:11)> -> __value
            __token = 641
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u'portal_state.language()', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['lang'] = __value
            __backup_view_140235427391312 = get('view', __marker)

            # <Value u'nocall:view | nocall: plone_view' (13:10)> -> __value
            __token = 687
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('nocall', u'view | nocall: plone_view', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_dummy_140235427391632 = get('dummy', __marker)

            # <Value u'python: plone_layout.mark_view(view)' (14:10)> -> __value
            __token = 736
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u' plone_layout.mark_view(view)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['dummy'] = __value
            __backup_portal_url_140235427391952 = get('portal_url', __marker)

            # <Value u'python:portal_state.portal_url()' (15:14)> -> __value
            __token = 794
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u'portal_state.portal_url()', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_checkPermission_140235427392144 = get('checkPermission', __marker)

            # <Value u"python:context.restrictedTraverse('portal_membership').checkPermission" (16:18)> -> __value
            __token = 853
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"context.restrictedTraverse('portal_membership').checkPermission", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['checkPermission'] = __value
            __backup_site_properties_140235427392464 = get('site_properties', __marker)

            # <Value u"python:context.restrictedTraverse('portal_properties').site_properties" (17:17)> -> __value
            __token = 950
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"context.restrictedTraverse('portal_properties').site_properties", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['site_properties'] = __value
            __backup_ajax_include_head_140235427392656 = get('ajax_include_head', __marker)

            # <Value u"python:request.get('ajax_include_head', False)" (18:18)> -> __value
            __token = 1049
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"request.get('ajax_include_head', False)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['ajax_include_head'] = __value
            __backup_ajax_load_140235427392208 = get('ajax_load', __marker)

            # <Value u'python:False' (19:9)> -> __value
            __token = 1116
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u'False', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['ajax_load'] = __value
            __previous_i18n_domain_140235370085328 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427390480
            __default_140235427390480 = _DEFAULT_MARKER

            # <Substitution u'lang' (21:27)> -> __attr_lang
            __token = 1195
            try:
                __zt_tmp = __attrs_140235427392784
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140235435449424('path', u'lang', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((u' lang="%s"' % __attr_lang))
            __append(u'>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427304208
            __attrs_140235427304208 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374747152
            __default_140235374747152 = _DEFAULT_MARKER

            # <Value u'provider:plone.httpheaders' (23:40)> -> __cache_140235370084176
            __token = 1244
            try:
                __zt_tmp = __attrs_140235427304208
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235370084176 = _static_140235435449424('provider', u'plone.httpheaders', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.httpheaders' (23:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b176b3ad0> -> __condition
            __expression = __cache_140235370084176

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140235370084176
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427303696
            __attrs_140235427303696 = _static_140235489934800

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427305936
            __attrs_140235427305936 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427305808
            __default_140235427305808 = _DEFAULT_MARKER

            # <Value u'provider:plone.htmlhead' (25:36)> -> __cache_140235427304656
            __token = 1312
            try:
                __zt_tmp = __attrs_140235427305936
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235427304656 = _static_140235435449424('provider', u'plone.htmlhead', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.htmlhead' (25:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ad45850> -> __condition
            __expression = __cache_140235427304656

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140235427304656
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427306640
            __attrs_140235427306640 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427307344
            __default_140235427307344 = _DEFAULT_MARKER

            # <Value u'nothing' (27:26)> -> __cache_140235427306192
            __token = 1367
            try:
                __zt_tmp = __attrs_140235427306640
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235427306192 = _static_140235435449424('path', u'nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'nothing' (27:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ad45e50> -> __condition
            __expression = __cache_140235427306192

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n        Various slots where you can insert elements in the header from a template.\n    ')
            else:
                __content = __cache_140235427306192
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    ')
            if (__slot_top_slot is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427305360
                __attrs_140235427305360 = _static_140235489934800
            else:
                __slot_top_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n    ')
            if (__slot_head_slot is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427348624
                __attrs_140235427348624 = _static_140235489934800
            else:
                __slot_head_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n    ')
            if (__slot_style_slot is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427349584
                __attrs_140235427349584 = _static_140235489934800
            else:
                __slot_style_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427351632
            __attrs_140235427351632 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427350288
            __default_140235427350288 = _DEFAULT_MARKER

            # <Value u'provider:plone.scripts' (34:32)> -> __cache_140235427350096
            __token = 1653
            try:
                __zt_tmp = __attrs_140235427351632
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235427350096 = _static_140235435449424('provider', u'plone.scripts', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.scripts' (34:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ad50790> -> __condition
            __expression = __cache_140235427350096

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140235427350096
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    ')
            if (__slot_javascript_head_slot is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427352336
                __attrs_140235427352336 = _static_140235489934800
            else:
                __slot_javascript_head_slot(__stream, econtext.copy(), rcontext)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235427351568
            __attrs_140235427351568 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427351440
            __default_140235427351440 = _DEFAULT_MARKER

            # <Value u'provider:plone.htmlhead.links' (37:33)> -> __cache_140235427351952
            __token = 1778
            try:
                __zt_tmp = __attrs_140235427351568
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235427351952 = _static_140235435449424('provider', u'plone.htmlhead.links', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.htmlhead.links' (37:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ad50cd0> -> __condition
            __expression = __cache_140235427351952

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <link ... (0:0)
                # --------------------------------------------------------
                __append(u'<link />')
            else:
                __content = __cache_140235427351952
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1ad50910> name=None at 7f8b1ad50950> -> __attrs_140235373961424
            __attrs_140235373961424 = _static_140235427350800

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta name="generator" content="Plone - http://plone.com" />\n\n  </head>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b17a66190> name=None at 7f8b1ad50e90> -> __attrs_140235373964496
            __attrs_140235373964496 = _static_140235373961616
            __backup_isRTL_140235370085008 = get('isRTL', __marker)

            # <Value u'portal_state/is_rtl' (42:26)> -> __value
            __token = 1915
            try:
                __zt_tmp = __attrs_140235373964496
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'portal_state/is_rtl', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['isRTL'] = __value
            __backup_sl_140235427304848 = get('sl', __marker)

            # <Value u"python:plone_layout.have_portlets('plone.leftcolumn', view)" (43:22)> -> __value
            __token = 1958
            try:
                __zt_tmp = __attrs_140235373964496
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"plone_layout.have_portlets('plone.leftcolumn', view)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['sl'] = __value
            __backup_sr_140235370086096 = get('sr', __marker)

            # <Value u"python:plone_layout.have_portlets('plone.rightcolumn', view)" (44:21)> -> __value
            __token = 2041
            try:
                __zt_tmp = __attrs_140235373964496
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"plone_layout.have_portlets('plone.rightcolumn', view)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['sr'] = __value
            __backup_body_class_140235370085392 = get('body_class', __marker)

            # <Value u'python:plone_layout.bodyClass(template, view)' (45:28)> -> __value
            __token = 2133
            try:
                __zt_tmp = __attrs_140235373964496
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u'plone_layout.bodyClass(template, view)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['body_class'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body')

            # <Value u'python:plone_view.patterns_settings()' (48:22)> -> __cache_140235373965136
            __token = 2309
            try:
                __zt_tmp = __attrs_140235373964496
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235373965136 = _static_140235435449424('python', u'plone_view.patterns_settings()', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if (u'id' not in __chain(__cache_140235373965136)):
                __append(u' id="visual-portal-wrapper"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373964624
            __default_140235373964624 = _DEFAULT_MARKER

            # <Substitution u'body_class' (46:30)> -> __attr_class
            __token = 2214
            try:
                __zt_tmp = __attrs_140235373964496
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140235435449424('path', u'body_class', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and (u'class' not in __chain(__cache_140235373965136))):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373965200
            __default_140235373965200 = _DEFAULT_MARKER

            # <Substitution u"python:isRTL and 'rtl' or 'ltr'" (47:27)> -> __attr_dir
            __token = 2253
            try:
                __zt_tmp = __attrs_140235373964496
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_140235435449424('python', u"isRTL and 'rtl' or 'ltr'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_dir is not None) and (u'dir' not in __chain(__cache_140235373965136))):
                __append((u' dir="%s"' % __attr_dir))
            __attr_140235373964688 = __cache_140235373965136
            for (name, value, ) in __attr_140235373964688.items():
                if ((name not in _static_140235385301200) and (value is not None)):
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append(u'>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373961552
            __attrs_140235373961552 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373961936
            __default_140235373961936 = _DEFAULT_MARKER

            # <Value u'provider:plone.toolbar' (51:32)> -> __cache_140235373963280
            __token = 2419
            try:
                __zt_tmp = __attrs_140235373961552
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235373963280 = _static_140235435449424('provider', u'plone.toolbar', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.toolbar' (51:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a66890> -> __condition
            __expression = __cache_140235373963280

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140235373963280
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b17a6ad10> name=None at 7f8b17a6aa90> -> __attrs_140235373978384
            __attrs_140235373978384 = _static_140235373980944
            __previous_i18n_domain_140235373977872 = __i18n_domain
            __i18n_domain = u'plone'

            # <header ... (0:0)
            # --------------------------------------------------------
            __append(u'<header id="portal-top">\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373979408
            __attrs_140235373979408 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373980560
            __default_140235373980560 = _DEFAULT_MARKER

            # <Value u'provider:plone.portaltop' (54:34)> -> __cache_140235373978640
            __token = 2530
            try:
                __zt_tmp = __attrs_140235373979408
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235373978640 = _static_140235435449424('provider', u'plone.portaltop', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.portaltop' (54:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a6a490> -> __condition
            __expression = __cache_140235373978640

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140235373978640
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    </header>')
            __i18n_domain = __previous_i18n_domain_140235373977872
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b17a6a950> name=None at 7f8b17a6aed0> -> __attrs_140235373980432
            __attrs_140235373980432 = _static_140235373979984

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="portal-mainnavigation">')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373981264
            __default_140235373981264 = _DEFAULT_MARKER

            # <Value u'provider:plone.mainnavigation' (57:59)> -> __cache_140235373979152
            __token = 2633
            try:
                __zt_tmp = __attrs_140235373980432
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235373979152 = _static_140235435449424('provider', u'plone.mainnavigation', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.mainnavigation' (57:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a6a990> -> __condition
            __expression = __cache_140235373979152

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n      The main navigation\n    ')
            else:
                __content = __cache_140235373979152
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b17a6a850> name=None at 7f8b17a6ac10> -> __attrs_140235432267152
            __attrs_140235432267152 = _static_140235373979728

            # <aside ... (0:0)
            # --------------------------------------------------------
            __append(u'<aside id="global_statusmessage">\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432263952
            __attrs_140235432263952 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235432267664
            __default_140235432267664 = _DEFAULT_MARKER

            # <Value u'provider:plone.globalstatusmessage' (62:42)> -> __cache_140235432266320
            __token = 2783
            try:
                __zt_tmp = __attrs_140235432263952
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235432266320 = _static_140235435449424('provider', u'plone.globalstatusmessage', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.globalstatusmessage' (62:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b200d50> -> __condition
            __expression = __cache_140235432266320

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140235432266320
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n      ')
            if (__slot_global_statusmessage is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432264336
                __attrs_140235432264336 = _static_140235489934800

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n      </div>')
            else:
                __slot_global_statusmessage(__stream, econtext.copy(), rcontext)
            __append(u'\n    </aside>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1b200650> name=None at 7f8b1b200610> -> __attrs_140235381608720
            __attrs_140235381608720 = _static_140235432265296

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="viewlet-above-content">')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235432265552
            __default_140235432265552 = _DEFAULT_MARKER

            # <Value u'provider:plone.abovecontent' (67:59)> -> __cache_140235432267408
            __token = 2960
            try:
                __zt_tmp = __attrs_140235381608720
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235432267408 = _static_140235435449424('provider', u'plone.abovecontent', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.abovecontent' (67:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b200b10> -> __condition
            __expression = __cache_140235432267408

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140235432267408
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b17a7d410> name=None at 7f8b17a7d690> -> __attrs_140235374056592
            __attrs_140235374056592 = _static_140235374056464

            # <article ... (0:0)
            # --------------------------------------------------------
            __append(u'<article id="portal-column-content">\n\n      ')
            if (__slot_content is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374056976
                __attrs_140235374056976 = _static_140235489934800
                __append(u'\n\n      ')
                __token = None
                render_content(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n\n      ')
            else:
                __slot_content(__stream, econtext.copy(), rcontext)
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374057872
            __attrs_140235374057872 = _static_140235489934800

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append(u'<footer>\n        ')

            # <Static value=<_ast.Dict object at 0x7f8b17a64bd0> name=None at 7f8b17a64b10> -> __attrs_140235373955408
            __attrs_140235373955408 = _static_140235373956048

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="viewlet-below-content">')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423562192
            __default_140235423562192 = _DEFAULT_MARKER

            # <Value u'provider:plone.belowcontent' (115:63)> -> __cache_140235374065936
            __token = 4621
            try:
                __zt_tmp = __attrs_140235373955408
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235374065936 = _static_140235435449424('provider', u'plone.belowcontent', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.belowcontent' (115:63)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a7f550> -> __condition
            __expression = __cache_140235374065936

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140235374065936
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n      </footer>\n    </article>\n\n\n\n    ')
            if (__slot_column_one_slot is None):

                # <Static value=<_ast.Dict object at 0x7f8b17a7d550> name=None at 7f8b17a7d5d0> -> __attrs_140235373955792
                __attrs_140235373955792 = _static_140235374056784

                # <Value u'sl' (123:26)> -> __condition
                __token = 4794
                try:
                    __zt_tmp = __attrs_140235373955792
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'sl', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<aside id="portal-column-one">\n      ')
                    if (__slot_portlets_one_slot is None):

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373956752
                        __attrs_140235373956752 = _static_140235489934800
                        __append(u'\n        ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373906000
                        __attrs_140235373906000 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373953360
                        __default_140235373953360 = _DEFAULT_MARKER

                        # <Value u'provider:plone.leftcolumn' (125:38)> -> __cache_140235373953296
                        __token = 4892
                        try:
                            __zt_tmp = __attrs_140235373906000
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235373953296 = _static_140235435449424('provider', u'plone.leftcolumn', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'provider:plone.leftcolumn' (125:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a64590> -> __condition
                        __expression = __cache_140235373953296

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140235373953296
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

                # <Static value=<_ast.Dict object at 0x7f8b17a64510> name=None at 7f8b17a646d0> -> __attrs_140235373905680
                __attrs_140235373905680 = _static_140235373954320

                # <Value u'sr' (131:26)> -> __condition
                __token = 5067
                try:
                    __zt_tmp = __attrs_140235373905680
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'sr', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<aside id="portal-column-two">\n      ')
                    if (__slot_portlets_two_slot is None):

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373904016
                        __attrs_140235373904016 = _static_140235489934800
                        __append(u'\n        ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373905232
                        __attrs_140235373905232 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373904976
                        __default_140235373904976 = _DEFAULT_MARKER

                        # <Value u'provider:plone.rightcolumn' (133:38)> -> __cache_140235373904784
                        __token = 5165
                        try:
                            __zt_tmp = __attrs_140235373905232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235373904784 = _static_140235435449424('provider', u'plone.rightcolumn', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'provider:plone.rightcolumn' (133:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a584d0> -> __condition
                        __expression = __cache_140235373904784

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140235373904784
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

            # <Static value=<_ast.Dict object at 0x7f8b17a588d0> name=None at 7f8b17a58b50> -> __attrs_140235373906064
            __attrs_140235373906064 = _static_140235373906128
            __previous_i18n_domain_140235373905872 = __i18n_domain
            __i18n_domain = u'plone'

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append(u'<footer id="portal-footer-wrapper">\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235423366224
            __attrs_140235423366224 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373907920
            __default_140235373907920 = _DEFAULT_MARKER

            # <Value u'provider:plone.portalfooter' (138:34)> -> __cache_140235373907280
            __token = 5328
            try:
                __zt_tmp = __attrs_140235423366224
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235373907280 = _static_140235435449424('provider', u'plone.portalfooter', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'provider:plone.portalfooter' (138:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a58dd0> -> __condition
            __expression = __cache_140235373907280

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div />')
            else:
                __content = __cache_140235373907280
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n    </footer>')
            __i18n_domain = __previous_i18n_domain_140235373905872
            __append(u'\n\n  </body>')
            if (__backup_body_class_140235370085392 is __marker):
                del econtext['body_class']
            else:
                econtext['body_class'] = __backup_body_class_140235370085392
            if (__backup_sr_140235370086096 is __marker):
                del econtext['sr']
            else:
                econtext['sr'] = __backup_sr_140235370086096
            if (__backup_sl_140235427304848 is __marker):
                del econtext['sl']
            else:
                econtext['sl'] = __backup_sl_140235427304848
            if (__backup_isRTL_140235370085008 is __marker):
                del econtext['isRTL']
            else:
                econtext['isRTL'] = __backup_isRTL_140235370085008
            __append(u'\n</html>')
            __i18n_domain = __previous_i18n_domain_140235370085328
            if (__backup_ajax_load_140235427392208 is __marker):
                del econtext['ajax_load']
            else:
                econtext['ajax_load'] = __backup_ajax_load_140235427392208
            if (__backup_ajax_include_head_140235427392656 is __marker):
                del econtext['ajax_include_head']
            else:
                econtext['ajax_include_head'] = __backup_ajax_include_head_140235427392656
            if (__backup_site_properties_140235427392464 is __marker):
                del econtext['site_properties']
            else:
                econtext['site_properties'] = __backup_site_properties_140235427392464
            if (__backup_checkPermission_140235427392144 is __marker):
                del econtext['checkPermission']
            else:
                econtext['checkPermission'] = __backup_checkPermission_140235427392144
            if (__backup_portal_url_140235427391952 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140235427391952
            if (__backup_dummy_140235427391632 is __marker):
                del econtext['dummy']
            else:
                econtext['dummy'] = __backup_dummy_140235427391632
            if (__backup_view_140235427391312 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_140235427391312
            if (__backup_lang_140235427391248 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_140235427391248
            if (__backup_plone_layout_140235427391504 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_140235427391504
            if (__backup_plone_view_140235423487632 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_140235423487632
            if (__backup_context_state_140235423488720 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_140235423488720
            if (__backup_portal_state_140235423488848 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_140235423488848
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
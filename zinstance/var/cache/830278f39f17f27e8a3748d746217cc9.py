# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.portlets-4.4.8-py2.7.egg/plone/app/portlets/portlets/actions.pt'

__tokens = {266: (u'context/@@plone_portal_state/portal_url', 8, 27), 354: (u'view/showTitle', 10, 44), 400: (u'view/title', 11, 29), 425: (u'view/title', 11, 54), 540: (u'string:actions-${view/category}', 16, 30), 607: (u'view/actionLinks', 17, 33), 687: (u'nocall:link/icon', 19, 29), 759: (u'link/modal|nothing', 21, 31), 813: (u'link/url', 22, 34), 857: (u" python:'pat-plone-modal' if modal else Non", 23, 34), 951: (u'l python:modal if modal else No', 24, 48), 1022: (u'not:icon', 26, 33), 1063: (u'link/title', 27, 31), 1239: (u'icon/absolute_url|icon', 33, 39), 1151: (u'icon', 31, 33), 1303: (u'string:background-image:url($icon_url);', 34, 40), 1188: (u'link/title', 32, 31)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235373358800 = {u'style': u'string:background-image:url($icon_url);', }
_static_140235374093520 = {u'class': u'portletItem', }
_static_140235374095568 = {u'data-pat-plone-modal': u'python:modal if modal else None', u'href': u'#', u'class': u"python:'pat-plone-modal' if modal else None", }
_static_140235451441808 = {u'class': u'portlet portletActions', }
_static_140235428419920 = {u'class': u'portletContent', }
_static_140235435449424 = __compile_zt_expr
_static_140235428417808 = {u'class': u'string:actions-${view/category}', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235423522064 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140235428379984 = {u'class': u'portletHeader', }
_static_140235489934800 = {}

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

            # <Static value=<_ast.Dict object at 0x7f8b1a9a9d10> name=None at 7f8b1a9a9e90> -> __attrs_140235423520784
            __attrs_140235423520784 = _static_140235423522064
            __previous_i18n_domain_140235423521168 = __i18n_domain
            __i18n_domain = u'plone'
            __append(u'\n\n')

            # <Static value=<_ast.Dict object at 0x7f8b1c44a290> name=None at 7f8b1c44a990> -> __attrs_140235451442704
            __attrs_140235451442704 = _static_140235451441808
            __backup_portal_url_140235373353936 = get('portal_url', __marker)

            # <Value u'context/@@plone_portal_state/portal_url' (8:27)> -> __value
            __token = 266
            try:
                __zt_tmp = __attrs_140235451442704
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'context/@@plone_portal_state/portal_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['portal_url'] = __value

            # <aside ... (0:0)
            # --------------------------------------------------------
            __append(u'<aside class="portlet portletActions">\n\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b1ae4bd50> name=None at 7f8b1ae4bb90> -> __attrs_140235428380432
            __attrs_140235428380432 = _static_140235428379984

            # <Value u'view/showTitle' (10:44)> -> __condition
            __token = 354
            try:
                __zt_tmp = __attrs_140235428380432
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'view/showTitle', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="portletHeader">\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235428420816
                __attrs_140235428420816 = _static_140235489934800

                # <Value u'view/title' (11:29)> -> __condition
                __token = 400
                try:
                    __zt_tmp = __attrs_140235428420816
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235428419856
                    __default_140235428419856 = _DEFAULT_MARKER

                    # <Value u'view/title' (11:54)> -> __cache_140235428377936
                    __token = 425
                    try:
                        __zt_tmp = __attrs_140235428420816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235428377936 = _static_140235435449424('path', u'view/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/title' (11:54)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1ae4b950> -> __condition
                    __expression = __cache_140235428377936

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n          Title\n        </span>')
                    else:
                        __content = __cache_140235428377936
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                __append(u'\n  </div>')
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x7f8b1ae55950> name=None at 7f8b1ae55290> -> __attrs_140235428420432
            __attrs_140235428420432 = _static_140235428419920

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="portletContent">\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1ae55110> name=None at 7f8b1ae55c90> -> __attrs_140235374093712
            __attrs_140235374093712 = _static_140235428417808

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append(u'<ul')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235428421520
            __default_140235428421520 = _DEFAULT_MARKER

            # <Substitution u'string:actions-${view/category}' (16:30)> -> __attr_class
            __token = 540
            try:
                __zt_tmp = __attrs_140235374093712
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140235435449424('string', u'actions-${view/category}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374092944
            __attrs_140235374092944 = _static_140235489934800
            __backup_link_140235374113552 = get('link', __marker)

            # <Value u'view/actionLinks' (17:33)> -> __iterator
            __token = 607
            try:
                __zt_tmp = __attrs_140235374092944
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140235435449424('path', u'view/actionLinks', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            (__iterator, ____index_140235374094992, ) = getitem('repeat')(u'link', __iterator)
            econtext['link'] = None
            for __item in __iterator:
                econtext['link'] = __item
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b17a864d0> name=None at 7f8b17a86090> -> __attrs_140235374095056
                __attrs_140235374095056 = _static_140235374093520
                __backup_icon_140235322134288 = get('icon', __marker)

                # <Value u'nocall:link/icon' (19:29)> -> __value
                __token = 687
                try:
                    __zt_tmp = __attrs_140235374095056
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('nocall', u'link/icon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['icon'] = __value

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li class="portletItem">\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b17a86cd0> name=None at 7f8b17a86210> -> __attrs_140235321943440
                __attrs_140235321943440 = _static_140235374095568
                __backup_modal_140235377023632 = get('modal', __marker)

                # <Value u'link/modal|nothing' (21:31)> -> __value
                __token = 759
                try:
                    __zt_tmp = __attrs_140235321943440
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'link/modal|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['modal'] = __value

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321942608
                __default_140235321942608 = _DEFAULT_MARKER

                # <Substitution u'link/url' (22:34)> -> __attr_href
                __token = 813
                try:
                    __zt_tmp = __attrs_140235321943440
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140235435449424('path', u'link/url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321942992
                __default_140235321942992 = _DEFAULT_MARKER

                # <Substitution u"python:'pat-plone-modal' if modal else None" (23:34)> -> __attr_class
                __token = 857
                try:
                    __zt_tmp = __attrs_140235321943440
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140235435449424('python', u"'pat-plone-modal' if modal else None", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321943376
                __default_140235321943376 = _DEFAULT_MARKER

                # <Substitution u'python:modal if modal else None' (24:48)> -> __attr_data_pat_plone_modal
                __token = 951
                try:
                    __zt_tmp = __attrs_140235321943440
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_pat_plone_modal = _static_140235435449424('python', u'modal if modal else None', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_pat_plone_modal is not None):
                    __append((u' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                __append(u'>\n\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321945360
                __attrs_140235321945360 = _static_140235489934800

                # <Value u'not:icon' (26:33)> -> __condition
                __token = 1022
                try:
                    __zt_tmp = __attrs_140235321945360
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('not', u'icon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321942480
                    __default_140235321942480 = _DEFAULT_MARKER

                    # <Value u'link/title' (27:31)> -> __cache_140235321942736
                    __token = 1063
                    try:
                        __zt_tmp = __attrs_140235321945360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235321942736 = _static_140235435449424('path', u'link/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'link/title' (27:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148ca290> -> __condition
                    __expression = __cache_140235321942736

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n              Action\n            ')
                    else:
                        __content = __cache_140235321942736
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                __append(u'\n\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b179d2ed0> name=None at 7f8b179d2c10> -> __attrs_140235373356240
                __attrs_140235373356240 = _static_140235373358800
                __backup_icon_url_140235322542160 = get('icon_url', __marker)

                # <Value u'icon/absolute_url|icon' (33:39)> -> __value
                __token = 1239
                try:
                    __zt_tmp = __attrs_140235373356240
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'icon/absolute_url|icon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['icon_url'] = __value

                # <Value u'icon' (31:33)> -> __condition
                __token = 1151
                try:
                    __zt_tmp = __attrs_140235373356240
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'icon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373356048
                    __default_140235373356048 = _DEFAULT_MARKER

                    # <Substitution u'string:background-image:url($icon_url);' (34:40)> -> __attr_style
                    __token = 1303
                    try:
                        __zt_tmp = __attrs_140235373356240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_140235435449424('string', u'background-image:url($icon_url);', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((u' style="%s"' % __attr_style))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321943888
                    __default_140235321943888 = _DEFAULT_MARKER

                    # <Value u'link/title' (32:31)> -> __cache_140235321945168
                    __token = 1188
                    try:
                        __zt_tmp = __attrs_140235373356240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235321945168 = _static_140235435449424('path', u'link/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'link/title' (32:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148ca6d0> -> __condition
                    __expression = __cache_140235321945168

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n              Action\n            ')
                    else:
                        __content = __cache_140235321945168
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                if (__backup_icon_url_140235322542160 is __marker):
                    del econtext['icon_url']
                else:
                    econtext['icon_url'] = __backup_icon_url_140235322542160
                __append(u'\n\n          </a>')
                if (__backup_modal_140235377023632 is __marker):
                    del econtext['modal']
                else:
                    econtext['modal'] = __backup_modal_140235377023632
                __append(u'\n        </li>')
                if (__backup_icon_140235322134288 is __marker):
                    del econtext['icon']
                else:
                    econtext['icon'] = __backup_icon_140235322134288
                __append(u'\n      ')
                ____index_140235374094992 -= 1
                if (____index_140235374094992 > 0):
                    __append('')
            if (__backup_link_140235374113552 is __marker):
                del econtext['link']
            else:
                econtext['link'] = __backup_link_140235374113552
            __append(u'\n    </ul>\n  </div>\n</aside>')
            if (__backup_portal_url_140235373353936 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140235373353936
            __append(u'\n')
            __i18n_domain = __previous_i18n_domain_140235423521168
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
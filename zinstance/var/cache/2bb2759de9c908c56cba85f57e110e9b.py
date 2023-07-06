# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/nextprevious/nextprevious.pt'

__tokens = {173: (u'view/enabled|nothing', 4, 25), 226: (u' view/isViewTemplate|nothin', 5, 31), 276: (u'python:enabled and isViewTemplate', 6, 20), 391: (u'view/site_url', 10, 32), 463: (u'view/next', 13, 26), 503: (u' view/previou', 14, 29), 543: (u'python:previous is not None or next is not None', 15, 24), 650: (u'previous', 19, 44), 795: (u'previous/url', 22, 35), 999: (u'previous/title', 26, 55), 1108: (u'next', 31, 40), 1241: (u'next/url', 34, 35), 1393: (u'next/title', 37, 55)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235373354768 = {u'class': u'next', }
_static_140235432288656 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140235489934800 = {}
_static_140235373354384 = {u'class': u'arrow', }
_static_140235374582224 = {u'class': u'label', }
_static_140235435449424 = __compile_zt_expr
_static_140235451441296 = {u'class': u'arrow', }
_static_140235374163728 = {u'href': u'next/url', u'title': u'Go to next item', }
_static_140235368758224 = {u'class': u'previous', }
_static_140235431260048 = {u'class': u'pagination', }
_static_140235431389520 = {u'class': u'label', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235368755664 = {u'href': u'previous/url', u'title': u'Go to previous item', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1b206190> name=None at 7f8b1b206e10> -> __attrs_140235377189264
            __attrs_140235377189264 = _static_140235432288656
            __backup_enabled_140235374163920 = get('enabled', __marker)

            # <Value u'view/enabled|nothing' (4:25)> -> __value
            __token = 173
            try:
                __zt_tmp = __attrs_140235377189264
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/enabled|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_140235431277968 = get('isViewTemplate', __marker)

            # <Value u'view/isViewTemplate|nothing' (5:31)> -> __value
            __token = 226
            try:
                __zt_tmp = __attrs_140235377189264
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/isViewTemplate|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value u'python:enabled and isViewTemplate' (6:20)> -> __condition
            __token = 276
            try:
                __zt_tmp = __attrs_140235377189264
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('python', u'enabled and isViewTemplate', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140235431258960 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431257104
                __attrs_140235431257104 = _static_140235489934800
                __backup_portal_url_140235431258896 = get('portal_url', __marker)

                # <Value u'view/site_url' (10:32)> -> __value
                __token = 391
                try:
                    __zt_tmp = __attrs_140235431257104
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/site_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1b10af90> name=None at 7f8b1b10ad10> -> __attrs_140235431257616
                __attrs_140235431257616 = _static_140235431260048
                __backup_next_140235431257168 = get('next', __marker)

                # <Value u'view/next' (13:26)> -> __value
                __token = 463
                try:
                    __zt_tmp = __attrs_140235431257616
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/next', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['next'] = __value
                __backup_previous_140235432291216 = get('previous', __marker)

                # <Value u'view/previous' (14:29)> -> __value
                __token = 503
                try:
                    __zt_tmp = __attrs_140235431257616
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/previous', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value u'python:previous is not None or next is not None' (15:24)> -> __condition
                __token = 543
                try:
                    __zt_tmp = __attrs_140235431257616
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('python', u'previous is not None or next is not None', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<nav class="pagination">\n\n      ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235437657040
                    __attrs_140235437657040 = _static_140235489934800

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul>\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1756fbd0> name=None at 7f8b1756fdd0> -> __attrs_140235368755472
                    __attrs_140235368755472 = _static_140235368758224

                    # <Value u'previous' (19:44)> -> __condition
                    __token = 650
                    try:
                        __zt_tmp = __attrs_140235368755472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'previous', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="previous">\n          ')

                        # <Static value=<_ast.Dict object at 0x7f8b1756f1d0> name=None at 7f8b1756f3d0> -> __attrs_140235373352784
                        __attrs_140235373352784 = _static_140235368755664

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373353104
                        __default_140235373353104 = _DEFAULT_MARKER

                        # <Translate msgid=u'title_previous_item' node=<_ast.Str object at 0x7f8b185388d0> at 7f8b1c440550> -> __attr_title
                        __attr_title = u'Go to previous item'
                        __attr_title = translate(u'title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373352272
                        __default_140235373352272 = _DEFAULT_MARKER

                        # <Substitution u'previous/url' (22:35)> -> __attr_href
                        __token = 795
                        try:
                            __zt_tmp = __attrs_140235373352784
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140235435449424('path', u'previous/url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8b179d1d90> name=None at 7f8b179d1bd0> -> __attrs_140235373352080
                        __attrs_140235373352080 = _static_140235373354384

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="arrow"></span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8b17afd9d0> name=None at 7f8b17afd590> -> __attrs_140235374163152
                        __attrs_140235374163152 = _static_140235374582224

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="label">')
                        __stream_140235424597488_itemtitle = ''
                        __stream_140235373354256 = []
                        __append_140235373354256 = __stream_140235373354256.append
                        __append_140235373354256(u'\n              Previous:\n              ')
                        __stream_140235424597488_itemtitle = []
                        __append_140235424597488_itemtitle = __stream_140235424597488_itemtitle.append

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374163280
                        __attrs_140235374163280 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374165904
                        __default_140235374165904 = _DEFAULT_MARKER

                        # <Value u'previous/title' (26:55)> -> __cache_140235374165456
                        __token = 999
                        try:
                            __zt_tmp = __attrs_140235374163280
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235374165456 = _static_140235435449424('path', u'previous/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'previous/title' (26:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a972d0> -> __condition
                        __expression = __cache_140235374165456

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140235424597488_itemtitle(u'<span />')
                        else:
                            __content = __cache_140235374165456
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140235424597488_itemtitle(__content)
                        __append_140235373354256(u'${itemtitle}')
                        __stream_140235424597488_itemtitle = ''.join(__stream_140235424597488_itemtitle)
                        __append_140235373354256(u'\n            ')
                        __msgid_140235373354256 = __re_whitespace(''.join(__stream_140235373354256)).strip()
                        if u'label_previous_item':
                            __append(translate(u'label_previous_item', mapping={u'itemtitle': __stream_140235424597488_itemtitle, }, default=__msgid_140235373354256, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n          </a>\n        </li>')
                    __append(u'\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b179d1f10> name=None at 7f8b179d1c10> -> __attrs_140235374164048
                    __attrs_140235374164048 = _static_140235373354768

                    # <Value u'next' (31:40)> -> __condition
                    __token = 1108
                    try:
                        __zt_tmp = __attrs_140235374164048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'next', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="next">\n          ')

                        # <Static value=<_ast.Dict object at 0x7f8b17a97710> name=None at 7f8b17a97190> -> __attrs_140235431387408
                        __attrs_140235431387408 = _static_140235374163728

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431390800
                        __default_140235431390800 = _DEFAULT_MARKER

                        # <Translate msgid=u'title_next_item' node=<_ast.Str object at 0x7f8b1b12a990> at 7f8b1b12a410> -> __attr_title
                        __attr_title = u'Go to next item'
                        __attr_title = translate(u'title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431389968
                        __default_140235431389968 = _DEFAULT_MARKER

                        # <Substitution u'next/url' (34:35)> -> __attr_href
                        __token = 1241
                        try:
                            __zt_tmp = __attrs_140235431387408
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140235435449424('path', u'next/url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8b1b12a950> name=None at 7f8b1b12abd0> -> __attrs_140235431388048
                        __attrs_140235431388048 = _static_140235431389520

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="label">')
                        __stream_140235424597248_itemtitle = ''
                        __stream_140235431387280 = []
                        __append_140235431387280 = __stream_140235431387280.append
                        __append_140235431387280(u'\n              Next:\n              ')
                        __stream_140235424597248_itemtitle = []
                        __append_140235424597248_itemtitle = __stream_140235424597248_itemtitle.append

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235451441360
                        __attrs_140235451441360 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451441232
                        __default_140235451441232 = _DEFAULT_MARKER

                        # <Value u'next/title' (37:55)> -> __cache_140235431390352
                        __token = 1393
                        try:
                            __zt_tmp = __attrs_140235451441360
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235431390352 = _static_140235435449424('path', u'next/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'next/title' (37:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b12a5d0> -> __condition
                        __expression = __cache_140235431390352

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140235424597248_itemtitle(u'<span />')
                        else:
                            __content = __cache_140235431390352
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140235424597248_itemtitle(__content)
                        __append_140235431387280(u'${itemtitle}')
                        __stream_140235424597248_itemtitle = ''.join(__stream_140235424597248_itemtitle)
                        __append_140235431387280(u'\n            ')
                        __msgid_140235431387280 = __re_whitespace(''.join(__stream_140235431387280)).strip()
                        if u'label_next_item':
                            __append(translate(u'label_next_item', mapping={u'itemtitle': __stream_140235424597248_itemtitle, }, default=__msgid_140235431387280, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8b1c44a090> name=None at 7f8b1b12a890> -> __attrs_140235451442256
                        __attrs_140235451442256 = _static_140235451441296

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="arrow"></span>\n          </a>\n        </li>')
                    __append(u'\n\n        &nbsp;\n\n      </ul>\n\n    </nav>')
                if (__backup_previous_140235432291216 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_140235432291216
                if (__backup_next_140235431257168 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_140235431257168
                __append(u'\n\n  ')
                if (__backup_portal_url_140235431258896 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_140235431258896
                __append(u'\n\n')
                __i18n_domain = __previous_i18n_domain_140235431258960
            if (__backup_isViewTemplate_140235431277968 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_140235431277968
            if (__backup_enabled_140235374163920 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_140235374163920
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
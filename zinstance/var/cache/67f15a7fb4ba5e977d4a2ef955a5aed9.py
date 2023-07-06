# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/nextprevious/nextprevious.pt'

__tokens = {173: (u'view/enabled|nothing', 4, 25), 226: (u' view/isViewTemplate|nothin', 5, 31), 276: (u'python:enabled and isViewTemplate', 6, 20), 391: (u'view/site_url', 10, 32), 463: (u'view/next', 13, 26), 503: (u' view/previou', 14, 29), 543: (u'python:previous is not None or next is not None', 15, 24), 650: (u'previous', 19, 44), 795: (u'previous/url', 22, 35), 999: (u'previous/title', 26, 55), 1108: (u'next', 31, 40), 1241: (u'next/url', 34, 35), 1393: (u'next/title', 37, 55)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386070734800 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140386069974672 = {u'class': u'pagination', }
_static_140386069897424 = {u'class': u'next', }
_static_140386071890448 = {u'class': u'previous', }
_static_140386069899792 = {u'class': u'arrow', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386069897296 = {u'class': u'label', }
_static_140386069454672 = {u'href': u'previous/url', u'title': u'Go to previous item', }
_static_140386072652048 = {u'class': u'arrow', }
_static_140386186296528 = __compile_zt_expr
_static_140386070428880 = {u'href': u'next/url', u'title': u'Go to next item', }
_static_140386072653328 = {u'class': u'label', }
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

            # <Static value=<_ast.Dict object at 0x7fae2de0a7d0> name=None at 7fae2de0a350> -> __attrs_140386070081680
            __attrs_140386070081680 = _static_140386070734800
            __backup_enabled_140386070733264 = get('enabled', __marker)

            # <Value u'view/enabled|nothing' (4:25)> -> __value
            __token = 173
            try:
                __zt_tmp = __attrs_140386070081680
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/enabled|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_140386070744528 = get('isViewTemplate', __marker)

            # <Value u'view/isViewTemplate|nothing' (5:31)> -> __value
            __token = 226
            try:
                __zt_tmp = __attrs_140386070081680
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/isViewTemplate|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value u'python:enabled and isViewTemplate' (6:20)> -> __condition
            __token = 276
            try:
                __zt_tmp = __attrs_140386070081680
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('python', u'enabled and isViewTemplate', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140386069973520 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069973840
                __attrs_140386069973840 = _static_140386247937936
                __backup_portal_url_140386069973392 = get('portal_url', __marker)

                # <Value u'view/site_url' (10:32)> -> __value
                __token = 391
                try:
                    __zt_tmp = __attrs_140386069973840
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/site_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2dd50e90> name=None at 7fae2dd50bd0> -> __attrs_140386069972688
                __attrs_140386069972688 = _static_140386069974672
                __backup_next_140386069973584 = get('next', __marker)

                # <Value u'view/next' (13:26)> -> __value
                __token = 463
                try:
                    __zt_tmp = __attrs_140386069972688
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/next', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['next'] = __value
                __backup_previous_140386070735696 = get('previous', __marker)

                # <Value u'view/previous' (14:29)> -> __value
                __token = 503
                try:
                    __zt_tmp = __attrs_140386069972688
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/previous', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value u'python:previous is not None or next is not None' (15:24)> -> __condition
                __token = 543
                try:
                    __zt_tmp = __attrs_140386069972688
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('python', u'previous is not None or next is not None', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<nav class="pagination">\n\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069343824
                    __attrs_140386069343824 = _static_140386247937936

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul>\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2df24a10> name=None at 7fae2df24310> -> __attrs_140386069454544
                    __attrs_140386069454544 = _static_140386071890448

                    # <Value u'previous' (19:44)> -> __condition
                    __token = 650
                    try:
                        __zt_tmp = __attrs_140386069454544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'previous', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="previous">\n          ')

                        # <Static value=<_ast.Dict object at 0x7fae2dcd1f50> name=None at 7fae2dcd1c10> -> __attrs_140386069450960
                        __attrs_140386069450960 = _static_140386069454672

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069451088
                        __default_140386069451088 = _DEFAULT_MARKER

                        # <Translate msgid=u'title_previous_item' node=<_ast.Str object at 0x7fae2dcd1890> at 7fae2dcd1050> -> __attr_title
                        __attr_title = u'Go to previous item'
                        __attr_title = translate(u'title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069453456
                        __default_140386069453456 = _DEFAULT_MARKER

                        # <Substitution u'previous/url' (22:35)> -> __attr_href
                        __token = 795
                        try:
                            __zt_tmp = __attrs_140386069450960
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140386186296528('path', u'previous/url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fae2dd3ea10> name=None at 7fae2dd3e7d0> -> __attrs_140386069901264
                        __attrs_140386069901264 = _static_140386069899792

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="arrow"></span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fae2dd3e050> name=None at 7fae2dd3ea50> -> __attrs_140386069899984
                        __attrs_140386069899984 = _static_140386069897296

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="label">')
                        __stream_140386072470064_itemtitle = ''
                        __stream_140386069900944 = []
                        __append_140386069900944 = __stream_140386069900944.append
                        __append_140386069900944(u'\n              Previous:\n              ')
                        __stream_140386072470064_itemtitle = []
                        __append_140386072470064_itemtitle = __stream_140386072470064_itemtitle.append

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070429584
                        __attrs_140386070429584 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070428752
                        __default_140386070428752 = _DEFAULT_MARKER

                        # <Value u'previous/title' (26:55)> -> __cache_140386070425872
                        __token = 999
                        try:
                            __zt_tmp = __attrs_140386070429584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386070425872 = _static_140386186296528('path', u'previous/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'previous/title' (26:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2ddbf650> -> __condition
                        __expression = __cache_140386070425872

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140386072470064_itemtitle(u'<span />')
                        else:
                            __content = __cache_140386070425872
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140386072470064_itemtitle(__content)
                        __append_140386069900944(u'${itemtitle}')
                        __stream_140386072470064_itemtitle = ''.join(__stream_140386072470064_itemtitle)
                        __append_140386069900944(u'\n            ')
                        __msgid_140386069900944 = __re_whitespace(''.join(__stream_140386069900944)).strip()
                        if u'label_previous_item':
                            __append(translate(u'label_previous_item', mapping={u'itemtitle': __stream_140386072470064_itemtitle, }, default=__msgid_140386069900944, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n          </a>\n        </li>')
                    __append(u'\n\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2dd3e0d0> name=None at 7fae2dcd1310> -> __attrs_140386070429136
                    __attrs_140386070429136 = _static_140386069897424

                    # <Value u'next' (31:40)> -> __condition
                    __token = 1108
                    try:
                        __zt_tmp = __attrs_140386070429136
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'next', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li class="next">\n          ')

                        # <Static value=<_ast.Dict object at 0x7fae2ddbfcd0> name=None at 7fae2ddbf3d0> -> __attrs_140386070428816
                        __attrs_140386070428816 = _static_140386070428880

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070428944
                        __default_140386070428944 = _DEFAULT_MARKER

                        # <Translate msgid=u'title_next_item' node=<_ast.Str object at 0x7fae2ddbf510> at 7fae2ddbfed0> -> __attr_title
                        __attr_title = u'Go to next item'
                        __attr_title = translate(u'title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070427088
                        __default_140386070427088 = _DEFAULT_MARKER

                        # <Substitution u'next/url' (34:35)> -> __attr_href
                        __token = 1241
                        try:
                            __zt_tmp = __attrs_140386070428816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140386186296528('path', u'next/url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))
                        __append(u'>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fae2dfdee10> name=None at 7fae3afd98d0> -> __attrs_140386072650768
                        __attrs_140386072650768 = _static_140386072653328

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="label">')
                        __stream_140386072469824_itemtitle = ''
                        __stream_140386070485264 = []
                        __append_140386070485264 = __stream_140386070485264.append
                        __append_140386070485264(u'\n              Next:\n              ')
                        __stream_140386072469824_itemtitle = []
                        __append_140386072469824_itemtitle = __stream_140386072469824_itemtitle.append

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072649872
                        __attrs_140386072649872 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072652496
                        __default_140386072652496 = _DEFAULT_MARKER

                        # <Value u'next/title' (37:55)> -> __cache_140386072649808
                        __token = 1393
                        try:
                            __zt_tmp = __attrs_140386072649872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386072649808 = _static_140386186296528('path', u'next/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'next/title' (37:55)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dfdee90> -> __condition
                        __expression = __cache_140386072649808

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140386072469824_itemtitle(u'<span />')
                        else:
                            __content = __cache_140386072649808
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140386072469824_itemtitle(__content)
                        __append_140386070485264(u'${itemtitle}')
                        __stream_140386072469824_itemtitle = ''.join(__stream_140386072469824_itemtitle)
                        __append_140386070485264(u'\n            ')
                        __msgid_140386070485264 = __re_whitespace(''.join(__stream_140386070485264)).strip()
                        if u'label_next_item':
                            __append(translate(u'label_next_item', mapping={u'itemtitle': __stream_140386072469824_itemtitle, }, default=__msgid_140386070485264, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n            ')

                        # <Static value=<_ast.Dict object at 0x7fae2dfde910> name=None at 7fae2dfde990> -> __attrs_140386069993616
                        __attrs_140386069993616 = _static_140386072652048

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="arrow"></span>\n          </a>\n        </li>')
                    __append(u'\n\n        &nbsp;\n\n      </ul>\n\n    </nav>')
                if (__backup_previous_140386070735696 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_140386070735696
                if (__backup_next_140386069973584 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_140386069973584
                __append(u'\n\n  ')
                if (__backup_portal_url_140386069973392 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_140386069973392
                __append(u'\n\n')
                __i18n_domain = __previous_i18n_domain_140386069973520
            if (__backup_isViewTemplate_140386070744528 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_140386070744528
            if (__backup_enabled_140386070733264 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_140386070733264
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
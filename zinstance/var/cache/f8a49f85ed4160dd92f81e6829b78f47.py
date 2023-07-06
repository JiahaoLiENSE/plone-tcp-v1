# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/keywords.pt'

__tokens = {123: (u'context/Subject|nothing', 5, 28), 175: (u' nocall:modules/Products.PythonScripts.standard/url_quot', 6, 27), 255: (u'categories', 7, 20), 469: (u'categories', 10, 29), 617: (u'python:url_quote(category)', 15, 31), 675: (u'string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', 16, 30), 576: (u'category', 14, 22)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386186297040 = __C2ZContextWrapper
_static_140386070425872 = {u'href': u'', u'class': u'link-category', u'rel': u'nofollow', }
_static_140386186296528 = __compile_zt_expr
_static_140386070734480 = {u'id': u'categories-filed-under', }
_static_140386077788816 = {u'role': u'navigation', u'id': u'category', u'class': u'documentByLine', }
_static_140386070732880 = {u'aria-labelledby': u'categories-filed-under', }
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

            # <Static value=<_ast.Dict object at 0x7fae2e4c4a90> name=None at 7fae2e4c4710> -> __attrs_140386077787536
            __attrs_140386077787536 = _static_140386077788816
            __backup_categories_140386071497552 = get('categories', __marker)

            # <Value u'context/Subject|nothing' (5:28)> -> __value
            __token = 123
            try:
                __zt_tmp = __attrs_140386077787536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'context/Subject|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['categories'] = __value
            __backup_url_quote_140386069148560 = get('url_quote', __marker)

            # <Value u'nocall:modules/Products.PythonScripts.standard/url_quote' (6:27)> -> __value
            __token = 175
            try:
                __zt_tmp = __attrs_140386077787536
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('nocall', u'modules/Products.PythonScripts.standard/url_quote', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['url_quote'] = __value

            # <Value u'categories' (7:20)> -> __condition
            __token = 255
            try:
                __zt_tmp = __attrs_140386077787536
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'categories', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140386077787984 = __i18n_domain
                __i18n_domain = u'plone'

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append(u'<nav id="category" class="documentByLine" role="navigation">\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2de0a690> name=None at 7fae2de0a6d0> -> __attrs_140386070735760
                __attrs_140386070735760 = _static_140386070734480

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span id="categories-filed-under">')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070735696
                __attrs_140386070735696 = _static_140386247937936
                __stream_140386070735824 = []
                __append_140386070735824 = __stream_140386070735824.append
                __append_140386070735824(u'Filed under:')
                __msgid_140386070735824 = __re_whitespace(''.join(__stream_140386070735824)).strip()
                if u'label_filed_under':
                    __append(translate(u'label_filed_under', mapping=None, default=__msgid_140386070735824, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</span>\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2de0a050> name=None at 7fae2de0ae10> -> __attrs_140386070735056
                __attrs_140386070735056 = _static_140386070732880

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul aria-labelledby="categories-filed-under">\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071780176
                __attrs_140386071780176 = _static_140386247937936
                __backup_category_140386070733264 = get('category', __marker)

                # <Value u'categories' (10:29)> -> __iterator
                __token = 469
                try:
                    __zt_tmp = __attrs_140386071780176
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'categories', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386071778256, ) = getitem('repeat')(u'category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae2ddbf110> name=None at 7fae2ddbf090> -> __attrs_140386070426960
                    __attrs_140386070426960 = _static_140386070425872
                    __backup_quotedCat_140386070520848 = get('quotedCat', __marker)

                    # <Value u'python:url_quote(category)' (15:31)> -> __value
                    __token = 617
                    try:
                        __zt_tmp = __attrs_140386070426960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u'url_quote(category)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['quotedCat'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070428560
                    __default_140386070428560 = _DEFAULT_MARKER

                    # <Substitution u'string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}' (16:30)> -> __attr_href
                    __token = 675
                    try:
                        __zt_tmp = __attrs_140386070426960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('string', u'${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u' class="link-category" rel="nofollow">')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070427344
                    __default_140386070427344 = _DEFAULT_MARKER

                    # <Value u'category' (14:22)> -> __cache_140386071778896
                    __token = 576
                    try:
                        __zt_tmp = __attrs_140386070426960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386071778896 = _static_140386186296528('path', u'category', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'category' (14:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2df09710> -> __condition
                    __expression = __cache_140386071778896

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n        Category\n        ')
                    else:
                        __content = __cache_140386071778896
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</a>')
                    if (__backup_quotedCat_140386070520848 is __marker):
                        del econtext['quotedCat']
                    else:
                        econtext['quotedCat'] = __backup_quotedCat_140386070520848
                    __append(u'\n    </li>')
                    ____index_140386071778256 -= 1
                    if (____index_140386071778256 > 0):
                        __append('\n    ')
                if (__backup_category_140386070733264 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_140386070733264
                __append(u'\n  </ul>\n</nav>')
                __i18n_domain = __previous_i18n_domain_140386077787984
            if (__backup_url_quote_140386069148560 is __marker):
                del econtext['url_quote']
            else:
                econtext['url_quote'] = __backup_url_quote_140386069148560
            if (__backup_categories_140386071497552 is __marker):
                del econtext['categories']
            else:
                econtext['categories'] = __backup_categories_140386071497552
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
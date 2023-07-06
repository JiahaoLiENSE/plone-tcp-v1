# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/searchbox.pt'

__tokens = {89: (u'view/navigation_root_url', 3, 37), 236: (u'string:${navigation_root_url}/@@search', 8, 33), 321: (u' string:ajaxUrl:${navigation_root_url}/@@ajax-searc', 9, 45), 405: (u"s python: view.livesearch and 'pat-livesearch' or ", 10, 30), 872: (u'view/folder_path', 22, 41), 932: (u' request/form/path|nothin', 23, 42), 1620: (u'request/form/SearchableText|nothing', 41, 37), 2001: (u'string:${navigation_root_url}/@@search', 55, 32)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235451421072 = {u'name': u'SearchableText', u'title': u'Search Site', u'placeholder': u'Search Site', u'value': u'', u'class': u'searchField', u'type': u'text', u'id': u'searchGadget', u'size': u'18', }
_static_140235385295888 = {u'type': u'submit', u'class': u'searchButton', u'value': u'Search', }
_static_140235385309200 = {u'class': u'searchSection', }
_static_140235435449424 = __compile_zt_expr
_static_140235426107984 = {u'action': u'@@search', u'data-pat-livesearch': u'string:ajaxUrl:${navigation_root_url}/@@ajax-search', u'role': u'search', u'id': u'searchGadget_form', u'class': u"python: view.livesearch and 'pat-livesearch' or ''", }
_static_140235385310032 = {u'class': u'hiddenStructure', u'for': u'searchGadget', }
_static_140235426072656 = {u'id': u'portal-searchbox', }
_static_140235373800720 = {u'class': u'LSBox', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235373787280 = {u'href': u'#', }
_static_140235373799888 = {u'id': u'portal-advanced-search', u'class': u'hiddenStructure', }
_static_140235451424656 = {u'style': u'cursor: pointer', u'for': u'searchbox_currentfolder_only', }
_static_140235451419856 = {u'checked': u'request/form/path|nothing', u'name': u'path', u'value': u'view/folder_path', u'class': u'noborder', u'type': u'checkbox', u'id': u'searchbox_currentfolder_only', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1ac18850> name=None at 7f8b1ac18a90> -> __attrs_140235426110224
            __attrs_140235426110224 = _static_140235426072656
            __backup_navigation_root_url_140235451442000 = get('navigation_root_url', __marker)

            # <Value u'view/navigation_root_url' (3:37)> -> __value
            __token = 89
            try:
                __zt_tmp = __attrs_140235426110224
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/navigation_root_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['navigation_root_url'] = __value
            __previous_i18n_domain_140235426108688 = __i18n_domain
            __i18n_domain = u'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="portal-searchbox">\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1ac21250> name=None at 7f8b1ac21f10> -> __attrs_140235373800144
            __attrs_140235373800144 = _static_140235426107984

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form id="searchGadget_form"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373800336
            __default_140235373800336 = _DEFAULT_MARKER

            # <Substitution u'string:${navigation_root_url}/@@search' (8:33)> -> __attr_action
            __token = 236
            try:
                __zt_tmp = __attrs_140235373800144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140235435449424('string', u'${navigation_root_url}/@@search', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', u'@@search', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))
            __append(u' role="search"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373798608
            __default_140235373798608 = _DEFAULT_MARKER

            # <Substitution u'string:ajaxUrl:${navigation_root_url}/@@ajax-search' (9:45)> -> __attr_data_pat_livesearch
            __token = 321
            try:
                __zt_tmp = __attrs_140235373800144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_livesearch = _static_140235435449424('string', u'ajaxUrl:${navigation_root_url}/@@ajax-search', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_data_pat_livesearch = __quote(__attr_data_pat_livesearch, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_pat_livesearch is not None):
                __append((u' data-pat-livesearch="%s"' % __attr_data_pat_livesearch))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373799184
            __default_140235373799184 = _DEFAULT_MARKER

            # <Substitution u"python: view.livesearch and 'pat-livesearch' or ''" (10:30)> -> __attr_class
            __token = 405
            try:
                __zt_tmp = __attrs_140235373800144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140235435449424('python', u" view.livesearch and 'pat-livesearch' or ''", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f8b17a3ed10> name=None at 7f8b17a3e7d0> -> __attrs_140235373799824
            __attrs_140235373799824 = _static_140235373800720

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="LSBox">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8b18538b50> name=None at 7f8b17a3e850> -> __attrs_140235385307728
            __attrs_140235385307728 = _static_140235385310032

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label class="hiddenStructure" for="searchGadget">')
            __stream_140235373800080 = []
            __append_140235373800080 = __stream_140235373800080.append
            __append_140235373800080(u'Search Site')
            __msgid_140235373800080 = __re_whitespace(''.join(__stream_140235373800080)).strip()
            if u'text_search':
                __append(translate(u'text_search', mapping=None, default=__msgid_140235373800080, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n             \n        ')

            # <Static value=<_ast.Dict object at 0x7f8b18538810> name=None at 7f8b18538ad0> -> __attrs_140235451419472
            __attrs_140235451419472 = _static_140235385309200

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="searchSection">\n            ')

            # <Static value=<_ast.Dict object at 0x7f8b1c444cd0> name=None at 7f8b1c444a10> -> __attrs_140235423366864
            __attrs_140235423366864 = _static_140235451419856

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input id="searchbox_currentfolder_only" class="noborder" type="checkbox" name="path"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423366800
            __default_140235423366800 = _DEFAULT_MARKER

            # <Substitution u'view/folder_path' (22:41)> -> __attr_value
            __token = 872
            try:
                __zt_tmp = __attrs_140235423366864
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140235435449424('path', u'view/folder_path', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235423364432
            __default_140235423364432 = _DEFAULT_MARKER

            # <Boolean u'request/form/path|nothing' (23:42)> -> __attr_checked
            __token = 932
            try:
                __zt_tmp = __attrs_140235423366864
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_140235435449424('path', u'request/form/path|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if (__attr_checked is _DEFAULT_MARKER):
                __attr_checked = None
            else:
                if __attr_checked:
                    __attr_checked = u'checked'
                else:
                    __attr_checked = None
            if (__attr_checked is not None):
                __append((u' checked="%s"' % __attr_checked))
            __append(u' />\n            ')

            # <Static value=<_ast.Dict object at 0x7f8b1c445f90> name=None at 7f8b1c4451d0> -> __attrs_140235451424336
            __attrs_140235451424336 = _static_140235451424656

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label for="searchbox_currentfolder_only" style="cursor: pointer">')
            __stream_140235423366032 = []
            __append_140235423366032 = __stream_140235423366032.append
            __append_140235423366032(u'\n                only in current section\n            ')
            __msgid_140235423366032 = __re_whitespace(''.join(__stream_140235423366032)).strip()
            if u'label_searchbox_currentfolder_only':
                __append(translate(u'label_searchbox_currentfolder_only', mapping=None, default=__msgid_140235423366032, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n        </div>\n             \n        ')

            # <Static value=<_ast.Dict object at 0x7f8b1c445190> name=None at 7f8b1c4457d0> -> __attrs_140235385295120
            __attrs_140235385295120 = _static_140235451421072

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input name="SearchableText" type="text" size="18"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385298704
            __default_140235385298704 = _DEFAULT_MARKER

            # <Substitution u'request/form/SearchableText|nothing' (41:37)> -> __attr_value
            __token = 1620
            try:
                __zt_tmp = __attrs_140235385295120
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140235435449424('path', u'request/form/SearchableText|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' id="searchGadget"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385295504
            __default_140235385295504 = _DEFAULT_MARKER

            # <Translate msgid=u'title_search_site' node=<_ast.Str object at 0x7f8b18535f90> at 7f8b18535150> -> __attr_title
            __attr_title = u'Search Site'
            __attr_title = translate(u'title_search_site', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385298256
            __default_140235385298256 = _DEFAULT_MARKER

            # <Translate msgid=u'title_search_site' node=<_ast.Str object at 0x7f8b18535d90> at 7f8b18535bd0> -> __attr_placeholder
            __attr_placeholder = u'Search Site'
            __attr_placeholder = translate(u'title_search_site', default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_placeholder is not None):
                __append((u' placeholder="%s"' % __attr_placeholder))
            __append(u' class="searchField" />\n\n        ')

            # <Static value=<_ast.Dict object at 0x7f8b18535410> name=None at 7f8b185358d0> -> __attrs_140235426113232
            __attrs_140235426113232 = _static_140235385295888

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input class="searchButton" type="submit"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235426112272
            __default_140235426112272 = _DEFAULT_MARKER

            # <Translate msgid=u'label_search' node=<_ast.Str object at 0x7f8b1ac22090> at 7f8b1ac22610> -> __attr_value
            __attr_value = u'Search'
            __attr_value = translate(u'label_search', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />\n\n         </div>\n    </form>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b17a3e9d0> name=None at 7f8b17a3e8d0> -> __attrs_140235373785552
            __attrs_140235373785552 = _static_140235373799888

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="portal-advanced-search" class="hiddenStructure">\n        ')

            # <Static value=<_ast.Dict object at 0x7f8b17a3b890> name=None at 7f8b17a3bc50> -> __attrs_140235373781968
            __attrs_140235373781968 = _static_140235373787280

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235373783568
            __default_140235373783568 = _DEFAULT_MARKER

            # <Substitution u'string:${navigation_root_url}/@@search' (55:32)> -> __attr_href
            __token = 2001
            try:
                __zt_tmp = __attrs_140235373781968
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140235435449424('string', u'${navigation_root_url}/@@search', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>')
            __stream_140235373787728 = []
            __append_140235373787728 = __stream_140235373787728.append
            __append_140235373787728(u'\n            Advanced Search&hellip;\n        ')
            __msgid_140235373787728 = __re_whitespace(''.join(__stream_140235373787728)).strip()
            if u'label_advanced_search':
                __append(translate(u'label_advanced_search', mapping=None, default=__msgid_140235373787728, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n    </div>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140235426108688
            if (__backup_navigation_root_url_140235451442000 is __marker):
                del econtext['navigation_root_url']
            else:
                econtext['navigation_root_url'] = __backup_navigation_root_url_140235451442000
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
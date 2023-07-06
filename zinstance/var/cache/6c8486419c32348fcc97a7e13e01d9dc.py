# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/searchbox.pt'

__tokens = {89: (u'view/navigation_root_url', 3, 37), 236: (u'string:${navigation_root_url}/@@search', 8, 33), 321: (u' string:ajaxUrl:${navigation_root_url}/@@ajax-searc', 9, 45), 405: (u"s python: view.livesearch and 'pat-livesearch' or ", 10, 30), 872: (u'view/folder_path', 22, 41), 932: (u' request/form/path|nothin', 23, 42), 1620: (u'request/form/SearchableText|nothing', 41, 37), 2001: (u'string:${navigation_root_url}/@@search', 55, 32)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386071109776 = {u'name': u'SearchableText', u'title': u'Search Site', u'placeholder': u'Search Site', u'value': u'', u'class': u'searchField', u'type': u'text', u'id': u'searchGadget', u'size': u'18', }
_static_140386071809488 = {u'href': u'#', }
_static_140386072587280 = {u'checked': u'request/form/path|nothing', u'name': u'path', u'value': u'view/folder_path', u'class': u'noborder', u'type': u'checkbox', u'id': u'searchbox_currentfolder_only', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386079223056 = {u'id': u'portal-advanced-search', u'class': u'hiddenStructure', }
_static_140386079221456 = {u'class': u'hiddenStructure', u'for': u'searchGadget', }
_static_140386073255056 = {u'id': u'portal-searchbox', }
_static_140386070733840 = {u'action': u'@@search', u'data-pat-livesearch': u'string:ajaxUrl:${navigation_root_url}/@@ajax-search', u'role': u'search', u'id': u'searchGadget_form', u'class': u"python: view.livesearch and 'pat-livesearch' or ''", }
_static_140386186296528 = __compile_zt_expr
_static_140386070735440 = {u'class': u'LSBox', }
_static_140386070710928 = {u'style': u'cursor: pointer', u'for': u'searchbox_currentfolder_only', }
_static_140386072586448 = {u'class': u'searchSection', }
_static_140386078147280 = {u'type': u'submit', u'class': u'searchButton', u'value': u'Search', }

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

            # <Static value=<_ast.Dict object at 0x7fae2e071c90> name=None at 7fae2e071710> -> __attrs_140386073253328
            __attrs_140386073253328 = _static_140386073255056
            __backup_navigation_root_url_140386071495440 = get('navigation_root_url', __marker)

            # <Value u'view/navigation_root_url' (3:37)> -> __value
            __token = 89
            try:
                __zt_tmp = __attrs_140386073253328
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/navigation_root_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['navigation_root_url'] = __value
            __previous_i18n_domain_140386073253584 = __i18n_domain
            __i18n_domain = u'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="portal-searchbox">\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2de0a410> name=None at 7fae2de0ad10> -> __attrs_140386070736400
            __attrs_140386070736400 = _static_140386070733840

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form id="searchGadget_form"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070734288
            __default_140386070734288 = _DEFAULT_MARKER

            # <Substitution u'string:${navigation_root_url}/@@search' (8:33)> -> __attr_action
            __token = 236
            try:
                __zt_tmp = __attrs_140386070736400
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140386186296528('string', u'${navigation_root_url}/@@search', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', u'@@search', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))
            __append(u' role="search"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070734928
            __default_140386070734928 = _DEFAULT_MARKER

            # <Substitution u'string:ajaxUrl:${navigation_root_url}/@@ajax-search' (9:45)> -> __attr_data_pat_livesearch
            __token = 321
            try:
                __zt_tmp = __attrs_140386070736400
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_pat_livesearch = _static_140386186296528('string', u'ajaxUrl:${navigation_root_url}/@@ajax-search', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_data_pat_livesearch = __quote(__attr_data_pat_livesearch, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_pat_livesearch is not None):
                __append((u' data-pat-livesearch="%s"' % __attr_data_pat_livesearch))

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070734160
            __default_140386070734160 = _DEFAULT_MARKER

            # <Substitution u"python: view.livesearch and 'pat-livesearch' or ''" (10:30)> -> __attr_class
            __token = 405
            try:
                __zt_tmp = __attrs_140386070736400
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140386186296528('python', u" view.livesearch and 'pat-livesearch' or ''", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae2de0aa50> name=None at 7fae2de0a6d0> -> __attrs_140386079223568
            __attrs_140386079223568 = _static_140386070735440

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="LSBox">\n        ')

            # <Static value=<_ast.Dict object at 0x7fae2e6226d0> name=None at 7fae2e622d50> -> __attrs_140386072584336
            __attrs_140386072584336 = _static_140386079221456

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label class="hiddenStructure" for="searchGadget">')
            __stream_140386079221264 = []
            __append_140386079221264 = __stream_140386079221264.append
            __append_140386079221264(u'Search Site')
            __msgid_140386079221264 = __re_whitespace(''.join(__stream_140386079221264)).strip()
            if u'text_search':
                __append(translate(u'text_search', mapping=None, default=__msgid_140386079221264, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n             \n        ')

            # <Static value=<_ast.Dict object at 0x7fae2dfce8d0> name=None at 7fae2dfce2d0> -> __attrs_140386072584592
            __attrs_140386072584592 = _static_140386072586448

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="searchSection">\n            ')

            # <Static value=<_ast.Dict object at 0x7fae2dfcec10> name=None at 7fae2dfce9d0> -> __attrs_140386070710032
            __attrs_140386070710032 = _static_140386072587280

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input id="searchbox_currentfolder_only" class="noborder" type="checkbox" name="path"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070709904
            __default_140386070709904 = _DEFAULT_MARKER

            # <Substitution u'view/folder_path' (22:41)> -> __attr_value
            __token = 872
            try:
                __zt_tmp = __attrs_140386070710032
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140386186296528('path', u'view/folder_path', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070709264
            __default_140386070709264 = _DEFAULT_MARKER

            # <Boolean u'request/form/path|nothing' (23:42)> -> __attr_checked
            __token = 932
            try:
                __zt_tmp = __attrs_140386070710032
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_checked = _static_140386186296528('path', u'request/form/path|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
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

            # <Static value=<_ast.Dict object at 0x7fae2de04a90> name=None at 7fae2de04310> -> __attrs_140386071112656
            __attrs_140386071112656 = _static_140386070710928

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label for="searchbox_currentfolder_only" style="cursor: pointer">')
            __stream_140386070710736 = []
            __append_140386070710736 = __stream_140386070710736.append
            __append_140386070710736(u'\n                only in current section\n            ')
            __msgid_140386070710736 = __re_whitespace(''.join(__stream_140386070710736)).strip()
            if u'label_searchbox_currentfolder_only':
                __append(translate(u'label_searchbox_currentfolder_only', mapping=None, default=__msgid_140386070710736, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n        </div>\n             \n        ')

            # <Static value=<_ast.Dict object at 0x7fae2de66090> name=None at 7fae2de66d10> -> __attrs_140386078148944
            __attrs_140386078148944 = _static_140386071109776

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input name="SearchableText" type="text" size="18"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179410448
            __default_140386179410448 = _DEFAULT_MARKER

            # <Substitution u'request/form/SearchableText|nothing' (41:37)> -> __attr_value
            __token = 1620
            try:
                __zt_tmp = __attrs_140386078148944
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140386186296528('path', u'request/form/SearchableText|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' id="searchGadget"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179411664
            __default_140386179411664 = _DEFAULT_MARKER

            # <Translate msgid=u'title_search_site' node=<_ast.Str object at 0x7fae345aed50> at 7fae345ae510> -> __attr_title
            __attr_title = u'Search Site'
            __attr_title = translate(u'title_search_site', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179408912
            __default_140386179408912 = _DEFAULT_MARKER

            # <Translate msgid=u'title_search_site' node=<_ast.Str object at 0x7fae345aebd0> at 7fae345ae190> -> __attr_placeholder
            __attr_placeholder = u'Search Site'
            __attr_placeholder = translate(u'title_search_site', default=__attr_placeholder, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_placeholder is not None):
                __append((u' placeholder="%s"' % __attr_placeholder))
            __append(u' class="searchField" />\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae2e51c2d0> name=None at 7fae2e51ce90> -> __attrs_140386078147472
            __attrs_140386078147472 = _static_140386078147280

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input class="searchButton" type="submit"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078147088
            __default_140386078147088 = _DEFAULT_MARKER

            # <Translate msgid=u'label_search' node=<_ast.Str object at 0x7fae2e51c150> at 7fae2e51ca50> -> __attr_value
            __attr_value = u'Search'
            __attr_value = translate(u'label_search', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />\n\n         </div>\n    </form>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2e622d10> name=None at 7fae2e622ad0> -> __attrs_140386071807376
            __attrs_140386071807376 = _static_140386079223056

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="portal-advanced-search" class="hiddenStructure">\n        ')

            # <Static value=<_ast.Dict object at 0x7fae2df10dd0> name=None at 7fae2df10290> -> __attrs_140386069900112
            __attrs_140386069900112 = _static_140386071809488

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071809232
            __default_140386071809232 = _DEFAULT_MARKER

            # <Substitution u'string:${navigation_root_url}/@@search' (55:32)> -> __attr_href
            __token = 2001
            try:
                __zt_tmp = __attrs_140386069900112
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140386186296528('string', u'${navigation_root_url}/@@search', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u'>')
            __stream_140386071808592 = []
            __append_140386071808592 = __stream_140386071808592.append
            __append_140386071808592(u'\n            Advanced Search&hellip;\n        ')
            __msgid_140386071808592 = __re_whitespace(''.join(__stream_140386071808592)).strip()
            if u'label_advanced_search':
                __append(translate(u'label_advanced_search', mapping=None, default=__msgid_140386071808592, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</a>\n    </div>\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140386073253584
            if (__backup_navigation_root_url_140386071495440 is __marker):
                del econtext['navigation_root_url']
            else:
                econtext['navigation_root_url'] = __backup_navigation_root_url_140386071495440
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
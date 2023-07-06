# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/document_relateditems.pt'

__tokens = {76: (u'view/related_items', 3, 25), 116: (u'related', 4, 20), 275: (u'nocall:context/@@plone', 7, 37), 337: (u' nocall:context/@@plone_layou', 8, 38), 409: (u'g nocall:plone_view/normalizeStri', 9, 40), 483: (u'te nocall:context/@@plone_context_st', 10, 37), 562: (u"ion python:context.portal_registry.get('types_use_view_action_in_listings',", 11, 38), 767: (u'related', 14, 31), 827: (u'item/Description', 15, 50), 894: (u' item/portal_typ', 16, 49), 961: (u"  python:'contenttype-' + normalizeString(item_typ", 17, 48), 1062: (u'   item/review_state|python: context_state.workflow_stat', 18, 47), 1169: (u"ass python: 'state-' + normalizeString(item_wf_st", 19, 46), 1269: (u'     item/getURL|item/absolut', 20, 45), 1349: (u"      python:(item_type in use_view_action) and item_url+'/view' or it", 21, 44), 1470: (u'e      python:item.', 22, 43), 1550: (u'item_type', 23, 52), 1601: (u'item_url', 24, 39), 1695: (u"python:item.getURL() +'/@@images/image/icon'", 26, 42), 1778: (u'item_has_image', 27, 37), 1837: (u'string:$getIcon', 28, 43), 1856: (u' item/Descriptio', 28, 62), 1922: (u'string:$item_type_class $item_wf_state_class url', 29, 46), 2010: (u'item/pretty_title_or_id', 30, 37), 2158: (u'item/Description', 33, 37)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235368758480 = {u'class': u'relatedItems', }
_static_140235489934800 = {}
_static_140235435449424 = __compile_zt_expr
_static_140235426047312 = {u'class': u'visualClear', u'id': u'clear-space-before-relatedItemBox', }
_static_140235385294992 = {u'src': u'string:$getIcon', u'alt': u'item/Description', u'class': u'thumb-icon', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235427390352 = {u'href': u'item_url', }
_static_140235426049872 = {u'id': u'relatedItemBox', }
_static_140235451442960 = {u'title': u'item_type', }
_static_140235374148368 = {u'class': u'string:$item_type_class $item_wf_state_class url', }
_static_140235374149456 = {u'class': u'discreet', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1756fcd0> name=None at 7f8b1756fbd0> -> __attrs_140235368755472
            __attrs_140235368755472 = _static_140235368758480
            __backup_related_140235451427024 = get('related', __marker)

            # <Value u'view/related_items' (3:25)> -> __value
            __token = 76
            try:
                __zt_tmp = __attrs_140235368755472
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/related_items', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['related'] = __value

            # <Value u'related' (4:20)> -> __condition
            __token = 116
            try:
                __zt_tmp = __attrs_140235368755472
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'related', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140235368757392 = __i18n_domain
                __i18n_domain = u'plone'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="relatedItems">\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1ac12550> name=None at 7f8b1ac12610> -> __attrs_140235426049360
                __attrs_140235426049360 = _static_140235426047312

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear" id="clear-space-before-relatedItemBox"><!-- --></div>\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1ac12f50> name=None at 7f8b1ac12c10> -> __attrs_140235432289744
                __attrs_140235432289744 = _static_140235426049872
                __backup_plone_view_140235374586128 = get('plone_view', __marker)

                # <Value u'nocall:context/@@plone' (7:37)> -> __value
                __token = 275
                try:
                    __zt_tmp = __attrs_140235432289744
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('nocall', u'context/@@plone', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['plone_view'] = __value
                __backup_plone_layout_140235368755408 = get('plone_layout', __marker)

                # <Value u'nocall:context/@@plone_layout' (8:38)> -> __value
                __token = 337
                try:
                    __zt_tmp = __attrs_140235432289744
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('nocall', u'context/@@plone_layout', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['plone_layout'] = __value
                __backup_normalizeString_140235368759184 = get('normalizeString', __marker)

                # <Value u'nocall:plone_view/normalizeString' (9:40)> -> __value
                __token = 409
                try:
                    __zt_tmp = __attrs_140235432289744
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('nocall', u'plone_view/normalizeString', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['normalizeString'] = __value
                __backup_context_state_140235426048720 = get('context_state', __marker)

                # <Value u'nocall:context/@@plone_context_state' (10:37)> -> __value
                __token = 483
                try:
                    __zt_tmp = __attrs_140235432289744
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('nocall', u'context/@@plone_context_state', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['context_state'] = __value
                __backup_use_view_action_140235432291984 = get('use_view_action', __marker)

                # <Value u"python:context.portal_registry.get('types_use_view_action_in_listings', [])" (11:38)> -> __value
                __token = 562
                try:
                    __zt_tmp = __attrs_140235432289744
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u"context.portal_registry.get('types_use_view_action_in_listings', [])", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['use_view_action'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="relatedItemBox">\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432290448
                __attrs_140235432290448 = _static_140235489934800

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header>')
                __stream_140235432290896 = []
                __append_140235432290896 = __stream_140235432290896.append
                __append_140235432290896(u'Related content')
                __msgid_140235432290896 = __re_whitespace(''.join(__stream_140235432290896)).strip()
                if u'label_related_items':
                    __append(translate(u'label_related_items', mapping=None, default=__msgid_140235432290896, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235451443216
                __attrs_140235451443216 = _static_140235489934800

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235451442512
                __attrs_140235451442512 = _static_140235489934800
                __backup_item_140235377189328 = get('item', __marker)

                # <Value u'related' (14:31)> -> __iterator
                __token = 767
                try:
                    __zt_tmp = __attrs_140235451442512
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140235435449424('path', u'related', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                (__iterator, ____index_140235451444432, ) = getitem('repeat')(u'item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1c44a710> name=None at 7f8b1c44a490> -> __attrs_140235432290576
                    __attrs_140235432290576 = _static_140235451442960
                    __backup_desc_140235385322384 = get('desc', __marker)

                    # <Value u'item/Description' (15:50)> -> __value
                    __token = 827
                    try:
                        __zt_tmp = __attrs_140235432290576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'item/Description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['desc'] = __value
                    __backup_item_type_140235426067408 = get('item_type', __marker)

                    # <Value u'item/portal_type' (16:49)> -> __value
                    __token = 894
                    try:
                        __zt_tmp = __attrs_140235432290576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'item/portal_type', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['item_type'] = __value
                    __backup_item_type_class_140235374587536 = get('item_type_class', __marker)

                    # <Value u"python:'contenttype-' + normalizeString(item_type)" (17:48)> -> __value
                    __token = 961
                    try:
                        __zt_tmp = __attrs_140235432290576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"'contenttype-' + normalizeString(item_type)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value
                    __backup_item_wf_state_140235374064848 = get('item_wf_state', __marker)

                    # <Value u'item/review_state|python: context_state.workflow_state()' (18:47)> -> __value
                    __token = 1062
                    try:
                        __zt_tmp = __attrs_140235432290576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'item/review_state|python: context_state.workflow_state()', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['item_wf_state'] = __value
                    __backup_item_wf_state_class_140235374585872 = get('item_wf_state_class', __marker)

                    # <Value u"python: 'state-' + normalizeString(item_wf_state)" (19:46)> -> __value
                    __token = 1169
                    try:
                        __zt_tmp = __attrs_140235432290576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u" 'state-' + normalizeString(item_wf_state)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['item_wf_state_class'] = __value
                    __backup_item_url_140235374580304 = get('item_url', __marker)

                    # <Value u'item/getURL|item/absolute_url' (20:45)> -> __value
                    __token = 1269
                    try:
                        __zt_tmp = __attrs_140235432290576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'item/getURL|item/absolute_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_url_140235432668176 = get('item_url', __marker)

                    # <Value u"python:(item_type in use_view_action) and item_url+'/view' or item_url" (21:44)> -> __value
                    __token = 1349
                    try:
                        __zt_tmp = __attrs_140235432290576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"(item_type in use_view_action) and item_url+'/view' or item_url", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_has_image_140235373756816 = get('item_has_image', __marker)

                    # <Value u'python:item.getIcon' (22:43)> -> __value
                    __token = 1470
                    try:
                        __zt_tmp = __attrs_140235432290576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u'item.getIcon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['item_has_image'] = __value

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235432289488
                    __default_140235432289488 = _DEFAULT_MARKER

                    # <Substitution u'item_type' (23:52)> -> __attr_title
                    __token = 1550
                    try:
                        __zt_tmp = __attrs_140235432290576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140235435449424('path', u'item_type', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8b1ad5a390> name=None at 7f8b1ad5ad10> -> __attrs_140235427389584
                    __attrs_140235427389584 = _static_140235427390352

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235427392976
                    __default_140235427392976 = _DEFAULT_MARKER

                    # <Substitution u'item_url' (24:39)> -> __attr_href
                    __token = 1601
                    try:
                        __zt_tmp = __attrs_140235427389584
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140235435449424('path', u'item_url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))
                    __append(u'>\n                 ')

                    # <Static value=<_ast.Dict object at 0x7f8b18535090> name=None at 7f8b18535850> -> __attrs_140235374137680
                    __attrs_140235374137680 = _static_140235385294992
                    __backup_getIcon_140235368756432 = get('getIcon', __marker)

                    # <Value u"python:item.getURL() +'/@@images/image/icon'" (26:42)> -> __value
                    __token = 1695
                    try:
                        __zt_tmp = __attrs_140235374137680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"item.getURL() +'/@@images/image/icon'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['getIcon'] = __value

                    # <Value u'item_has_image' (27:37)> -> __condition
                    __token = 1778
                    try:
                        __zt_tmp = __attrs_140235374137680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'item_has_image', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<img class="thumb-icon"')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385298192
                        __default_140235385298192 = _DEFAULT_MARKER

                        # <Substitution u'string:$getIcon' (28:43)> -> __attr_src
                        __token = 1837
                        try:
                            __zt_tmp = __attrs_140235374137680
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_140235435449424('string', u'$getIcon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((u' src="%s"' % __attr_src))

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235385295888
                        __default_140235385295888 = _DEFAULT_MARKER

                        # <Substitution u'item/Description' (28:62)> -> __attr_alt
                        __token = 1856
                        try:
                            __zt_tmp = __attrs_140235374137680
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_140235435449424('path', u'item/Description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((u' alt="%s"' % __attr_alt))
                        __append(u'>')
                    if (__backup_getIcon_140235368756432 is __marker):
                        del econtext['getIcon']
                    else:
                        econtext['getIcon'] = __backup_getIcon_140235368756432
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f8b17a93b10> name=None at 7f8b17a930d0> -> __attrs_140235374146704
                    __attrs_140235374146704 = _static_140235374148368

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374147024
                    __default_140235374147024 = _DEFAULT_MARKER

                    # <Substitution u'string:$item_type_class $item_wf_state_class url' (29:46)> -> __attr_class
                    __token = 1922
                    try:
                        __zt_tmp = __attrs_140235374146704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140235435449424('string', u'$item_type_class $item_wf_state_class url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374147216
                    __default_140235374147216 = _DEFAULT_MARKER

                    # <Value u'item/pretty_title_or_id' (30:37)> -> __cache_140235374147920
                    __token = 2010
                    try:
                        __zt_tmp = __attrs_140235374146704
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235374147920 = _static_140235435449424('path', u'item/pretty_title_or_id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'item/pretty_title_or_id' (30:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a93410> -> __condition
                    __expression = __cache_140235374147920

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                          Item Title')
                    else:
                        __content = __cache_140235374147920
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f8b17a93f50> name=None at 7f8b17a932d0> -> __attrs_140235374148816
                    __attrs_140235374148816 = _static_140235374149456

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="discreet">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374147408
                    __default_140235374147408 = _DEFAULT_MARKER

                    # <Value u'item/Description' (33:37)> -> __cache_140235374145680
                    __token = 2158
                    try:
                        __zt_tmp = __attrs_140235374148816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235374145680 = _static_140235435449424('path', u'item/Description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'item/Description' (33:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17a93f10> -> __condition
                    __expression = __cache_140235374145680

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'description')
                    else:
                        __content = __cache_140235374145680
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>\n               </a>\n            </span>')
                    if (__backup_item_has_image_140235373756816 is __marker):
                        del econtext['item_has_image']
                    else:
                        econtext['item_has_image'] = __backup_item_has_image_140235373756816
                    if (__backup_item_url_140235432668176 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_140235432668176
                    if (__backup_item_url_140235374580304 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_140235374580304
                    if (__backup_item_wf_state_class_140235374585872 is __marker):
                        del econtext['item_wf_state_class']
                    else:
                        econtext['item_wf_state_class'] = __backup_item_wf_state_class_140235374585872
                    if (__backup_item_wf_state_140235374064848 is __marker):
                        del econtext['item_wf_state']
                    else:
                        econtext['item_wf_state'] = __backup_item_wf_state_140235374064848
                    if (__backup_item_type_class_140235374587536 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_140235374587536
                    if (__backup_item_type_140235426067408 is __marker):
                        del econtext['item_type']
                    else:
                        econtext['item_type'] = __backup_item_type_140235426067408
                    if (__backup_desc_140235385322384 is __marker):
                        del econtext['desc']
                    else:
                        econtext['desc'] = __backup_desc_140235385322384
                    __append(u'\n          </li>')
                    ____index_140235451444432 -= 1
                    if (____index_140235451444432 > 0):
                        __append('\n          ')
                if (__backup_item_140235377189328 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_140235377189328
                __append(u'\n        </ul>\n    </div>')
                if (__backup_use_view_action_140235432291984 is __marker):
                    del econtext['use_view_action']
                else:
                    econtext['use_view_action'] = __backup_use_view_action_140235432291984
                if (__backup_context_state_140235426048720 is __marker):
                    del econtext['context_state']
                else:
                    econtext['context_state'] = __backup_context_state_140235426048720
                if (__backup_normalizeString_140235368759184 is __marker):
                    del econtext['normalizeString']
                else:
                    econtext['normalizeString'] = __backup_normalizeString_140235368759184
                if (__backup_plone_layout_140235368755408 is __marker):
                    del econtext['plone_layout']
                else:
                    econtext['plone_layout'] = __backup_plone_layout_140235368755408
                if (__backup_plone_view_140235374586128 is __marker):
                    del econtext['plone_view']
                else:
                    econtext['plone_view'] = __backup_plone_view_140235374586128
                __append(u'\n</div>')
                __i18n_domain = __previous_i18n_domain_140235368757392
            if (__backup_related_140235451427024 is __marker):
                del econtext['related']
            else:
                econtext['related'] = __backup_related_140235451427024
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
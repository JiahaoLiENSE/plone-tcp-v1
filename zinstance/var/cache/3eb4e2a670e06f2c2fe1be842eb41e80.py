# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.layout-3.5.2-py2.7.egg/plone/app/layout/viewlets/menu.pt'

__tokens = {40: (u'context/@@plone', 1, 40), 91: (u'ploneview/showToolbar', 2, 33), 187: (u'options/actions', 4, 34), 375: (u'action/id', 7, 29), 409: (u"python:actionid != 'history'", 8, 23), 232: (u'string:contentview-${action/id}', 5, 27), 294: (u" python: action.get('selected') and 'active' or '", 6, 29), 472: (u'action/selected|nothing', 9, 32), 551: (u'action/url', 11, 32), 596: (u' action/link_target|nothin', 12, 33), 656: (u's action/cssClass|nothi', 13, 31), 723: (u'string:icon-${action/id}${action/cssClass|nothing}  toolbar-menu-icon', 14, 38), 906: (u'action/title', 17, 29), 1165: (u'action/id', 23, 29), 1199: (u"python:actionid == 'history'", 24, 23), 1022: (u'string:contentview-${action/id}', 21, 27), 1084: (u" python: action.get('selected') and 'active' or '", 22, 29), 1262: (u'action/selected|nothing', 25, 32), 1316: (u' view/locked_ico', 26, 29), 1388: (u'action/url', 28, 32), 1433: (u' action/link_target|nothin', 29, 33), 1493: (u's action/cssClass|nothi', 30, 31), 1559: (u"python:locked and 'icon-lock' or 'icon-history'", 31, 38), 1807: (u'context/ModificationDate', 35, 29)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386072526160 = {u'class': u'icon-folderContents toolbar-menu-icon', u'aria-hidden': u'true', }
_static_140386070895760 = {u'href': u'#', u'target': u'action/link_target|nothing', u'class': u'action/cssClass|nothing', }
_static_140386071781328 = {u'id': u'string:contentview-${action/id}', u'class': u"python: action.get('selected') and 'active' or ''", }
_static_140386072950608 = {u'href': u'#', u'target': u'action/link_target|nothing', u'class': u'action/cssClass|nothing', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386070893968 = {u'id': u'string:contentview-${action/id}', u'class': u"python: action.get('selected') and 'active' or ''", }
_static_140386071189456 = {u'class': u'icon-folderContents', u'aria-hidden': u'true', }
_static_140386186296528 = __compile_zt_expr
_static_140386079221520 = {u'data-pat-moment': u'format:relative;', u'class': u'pat-moment', }
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071780944
            __attrs_140386071780944 = _static_140386247937936
            __backup_ploneview_140386079222608 = get('ploneview', __marker)

            # <Value u'context/@@plone' (1:40)> -> __value
            __token = 40
            try:
                __zt_tmp = __attrs_140386071780944
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'context/@@plone', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['ploneview'] = __value

            # <Value u'ploneview/showToolbar' (2:33)> -> __condition
            __token = 91
            try:
                __zt_tmp = __attrs_140386071780944
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'ploneview/showToolbar', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140386071780240 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071777936
                __attrs_140386071777936 = _static_140386247937936
                __backup_action_140386071778832 = get('action', __marker)

                # <Value u'options/actions' (4:34)> -> __iterator
                __token = 187
                try:
                    __zt_tmp = __attrs_140386071777936
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'options/actions', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386071779600, ) = getitem('repeat')(u'action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae2df09fd0> name=None at 7fae2df09090> -> __attrs_140386179408208
                    __attrs_140386179408208 = _static_140386071781328
                    __backup_actionid_140386078097680 = get('actionid', __marker)

                    # <Value u'action/id' (7:29)> -> __value
                    __token = 375
                    try:
                        __zt_tmp = __attrs_140386179408208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'action/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['actionid'] = __value

                    # <Value u"python:actionid != 'history'" (8:23)> -> __condition
                    __token = 409
                    try:
                        __zt_tmp = __attrs_140386179408208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('python', u"actionid != 'history'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179409168
                        __default_140386179409168 = _DEFAULT_MARKER

                        # <Substitution u'string:contentview-${action/id}' (5:27)> -> __attr_id
                        __token = 232
                        try:
                            __zt_tmp = __attrs_140386179408208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140386186296528('string', u'contentview-${action/id}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179411408
                        __default_140386179411408 = _DEFAULT_MARKER

                        # <Substitution u"python: action.get('selected') and 'active' or ''" (6:29)> -> __attr_class
                        __token = 294
                        try:
                            __zt_tmp = __attrs_140386179408208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140386186296528('python', u" action.get('selected') and 'active' or ''", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>\n      ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070896592
                        __attrs_140386070896592 = _static_140386247937936
                        __backup_selected_140386128026064 = get('selected', __marker)

                        # <Value u'action/selected|nothing' (9:32)> -> __value
                        __token = 472
                        try:
                            __zt_tmp = __attrs_140386070896592
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('path', u'action/selected|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['selected'] = __value
                        __append(u'\n        ')

                        # <Static value=<_ast.Dict object at 0x7fae2de31c90> name=None at 7fae2de314d0> -> __attrs_140386071190736
                        __attrs_140386071190736 = _static_140386070895760

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070895248
                        __default_140386070895248 = _DEFAULT_MARKER

                        # <Substitution u'action/url' (11:32)> -> __attr_href
                        __token = 551
                        try:
                            __zt_tmp = __attrs_140386071190736
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140386186296528('path', u'action/url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070896272
                        __default_140386070896272 = _DEFAULT_MARKER

                        # <Substitution u'action/link_target|nothing' (12:33)> -> __attr_target
                        __token = 596
                        try:
                            __zt_tmp = __attrs_140386071190736
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_target = _static_140386186296528('path', u'action/link_target|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_target is not None):
                            __append((u' target="%s"' % __attr_target))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071188880
                        __default_140386071188880 = _DEFAULT_MARKER

                        # <Substitution u'action/cssClass|nothing' (13:31)> -> __attr_class
                        __token = 656
                        try:
                            __zt_tmp = __attrs_140386071190736
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140386186296528('path', u'action/cssClass|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>\n          ')

                        # <Static value=<_ast.Dict object at 0x7fae2de797d0> name=None at 7fae2de79ad0> -> __attrs_140386078070480
                        __attrs_140386078070480 = _static_140386071189456

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078137168
                        __default_140386078137168 = _DEFAULT_MARKER

                        # <Substitution u'string:icon-${action/id}${action/cssClass|nothing}  toolbar-menu-icon' (14:38)> -> __attr_class
                        __token = 723
                        try:
                            __zt_tmp = __attrs_140386078070480
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140386186296528('string', u'icon-${action/id}${action/cssClass|nothing}  toolbar-menu-icon', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', u'icon-folderContents', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u' aria-hidden="true">\n          </span>\n          ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078070672
                        __attrs_140386078070672 = _static_140386247937936

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078070352
                        __default_140386078070352 = _DEFAULT_MARKER

                        # <Value u'action/title' (17:29)> -> __cache_140386078071312
                        __token = 906
                        try:
                            __zt_tmp = __attrs_140386078070672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386078071312 = _static_140386186296528('path', u'action/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'action/title' (17:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e509510> -> __condition
                        __expression = __cache_140386078071312

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'View name')
                        else:
                            __content = __cache_140386078071312
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n        </a>\n      ')
                        if (__backup_selected_140386128026064 is __marker):
                            del econtext['selected']
                        else:
                            econtext['selected'] = __backup_selected_140386128026064
                        __append(u'\n    </li>')
                    if (__backup_actionid_140386078097680 is __marker):
                        del econtext['actionid']
                    else:
                        econtext['actionid'] = __backup_actionid_140386078097680
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae2de31590> name=None at 7fae2de31a10> -> __attrs_140386078070224
                    __attrs_140386078070224 = _static_140386070893968
                    __backup_actionid_140386071548944 = get('actionid', __marker)

                    # <Value u'action/id' (23:29)> -> __value
                    __token = 1165
                    try:
                        __zt_tmp = __attrs_140386078070224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'action/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['actionid'] = __value

                    # <Value u"python:actionid == 'history'" (24:23)> -> __condition
                    __token = 1199
                    try:
                        __zt_tmp = __attrs_140386078070224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('python', u"actionid == 'history'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078069456
                        __default_140386078069456 = _DEFAULT_MARKER

                        # <Substitution u'string:contentview-${action/id}' (21:27)> -> __attr_id
                        __token = 1022
                        try:
                            __zt_tmp = __attrs_140386078070224
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140386186296528('string', u'contentview-${action/id}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078069712
                        __default_140386078069712 = _DEFAULT_MARKER

                        # <Substitution u"python: action.get('selected') and 'active' or ''" (22:29)> -> __attr_class
                        __token = 1084
                        try:
                            __zt_tmp = __attrs_140386078070224
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140386186296528('python', u" action.get('selected') and 'active' or ''", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>\n      ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072949776
                        __attrs_140386072949776 = _static_140386247937936
                        __backup_selected_140386070736080 = get('selected', __marker)

                        # <Value u'action/selected|nothing' (25:32)> -> __value
                        __token = 1262
                        try:
                            __zt_tmp = __attrs_140386072949776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('path', u'action/selected|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['selected'] = __value
                        __backup_locked_140386071838864 = get('locked', __marker)

                        # <Value u'view/locked_icon' (26:29)> -> __value
                        __token = 1316
                        try:
                            __zt_tmp = __attrs_140386072949776
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('path', u'view/locked_icon', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['locked'] = __value
                        __append(u'\n        ')

                        # <Static value=<_ast.Dict object at 0x7fae2e027750> name=None at 7fae2e027b90> -> __attrs_140386072526544
                        __attrs_140386072526544 = _static_140386072950608

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<a')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072526608
                        __default_140386072526608 = _DEFAULT_MARKER

                        # <Substitution u'action/url' (28:32)> -> __attr_href
                        __token = 1388
                        try:
                            __zt_tmp = __attrs_140386072526544
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140386186296528('path', u'action/url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((u' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072525904
                        __default_140386072525904 = _DEFAULT_MARKER

                        # <Substitution u'action/link_target|nothing' (29:33)> -> __attr_target
                        __token = 1433
                        try:
                            __zt_tmp = __attrs_140386072526544
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_target = _static_140386186296528('path', u'action/link_target|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_target is not None):
                            __append((u' target="%s"' % __attr_target))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072525328
                        __default_140386072525328 = _DEFAULT_MARKER

                        # <Substitution u'action/cssClass|nothing' (30:31)> -> __attr_class
                        __token = 1493
                        try:
                            __zt_tmp = __attrs_140386072526544
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140386186296528('path', u'action/cssClass|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u'>\n          ')

                        # <Static value=<_ast.Dict object at 0x7fae2dfbfd50> name=None at 7fae2dfbf150> -> __attrs_140386079223568
                        __attrs_140386079223568 = _static_140386072526160

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079219856
                        __default_140386079219856 = _DEFAULT_MARKER

                        # <Substitution u"python:locked and 'icon-lock' or 'icon-history'" (31:38)> -> __attr_class
                        __token = 1559
                        try:
                            __zt_tmp = __attrs_140386079223568
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140386186296528('python', u"locked and 'icon-lock' or 'icon-history'", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', u'icon-folderContents toolbar-menu-icon', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((u' class="%s"' % __attr_class))
                        __append(u' aria-hidden="true">\n          </span>\n          ')

                        # <Static value=<_ast.Dict object at 0x7fae2e622710> name=None at 7fae2e6223d0> -> __attrs_140386078120848
                        __attrs_140386078120848 = _static_140386079221520

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span class="pat-moment" data-pat-moment="format:relative;">')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079220496
                        __default_140386079220496 = _DEFAULT_MARKER

                        # <Value u'context/ModificationDate' (35:29)> -> __cache_140386079219792
                        __token = 1807
                        try:
                            __zt_tmp = __attrs_140386078120848
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386079219792 = _static_140386186296528('path', u'context/ModificationDate', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'context/ModificationDate' (35:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e622290> -> __condition
                        __expression = __cache_140386079219792

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Modified')
                        else:
                            __content = __cache_140386079219792
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n        </a>\n      ')
                        if (__backup_locked_140386071838864 is __marker):
                            del econtext['locked']
                        else:
                            econtext['locked'] = __backup_locked_140386071838864
                        if (__backup_selected_140386070736080 is __marker):
                            del econtext['selected']
                        else:
                            econtext['selected'] = __backup_selected_140386070736080
                        __append(u'\n    </li>')
                    if (__backup_actionid_140386071548944 is __marker):
                        del econtext['actionid']
                    else:
                        econtext['actionid'] = __backup_actionid_140386071548944
                    __append(u'\n  ')
                    ____index_140386071779600 -= 1
                    if (____index_140386071779600 > 0):
                        __append('')
                if (__backup_action_140386071778832 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140386071778832
                __append(u'\n')
                __i18n_domain = __previous_i18n_domain_140386071780240
            if (__backup_ploneview_140386079222608 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_140386079222608
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
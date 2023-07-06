# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.contenttypes-2.2.3-py2.7.egg/plone/app/contenttypes/browser/templates/listing.pt'

__tokens = {524: (u'view/text', 15, 23), 556: (u'text', 16, 21), 590: (u'view/text_class', 17, 28), 667: (u'text', 18, 59), 775: (u'view/batch', 22, 31), 828: (u' view/get_thumb_scale_lis', 23, 41), 897: (u'e view/get_thumb_scale_tab', 24, 41), 969: (u'ry view/get_thumb_scale_summ', 25, 42), 1033: (u"ass python:'thumb-%s pull-right' % thumb_scale_", 26, 31), 1116: (u'cons view/show_', 27, 30), 1169: (u'batch', 28, 30), 1265: (u'context/@@plone_portal_state/portal', 30, 31), 1337: (u' portal/@@image_scal', 31, 35), 6772: (u'context/batch_macros/macros/navigation', 126, 30), 6772: (u'context/batch_macros/macros/navigation', 126, 30), 6953: (u'not: batch', 132, 27), 6990: (u'view/no_items_message', 133, 25), 3920: (u'item_is_event', 73, 46), 3995: (u'python:view.formatted_date(obj)', 74, 59), 4077: (u'item/location', 75, 47), 4192: (u'string:${item/location}', 76, 47), 4386: (u'view/show_about', 79, 47), 4552: (u'python:view.pas_member.info(item_creator)', 82, 49), 4655: (u' author/usernam', 83, 60), 4731: (u'm string:?author=${author/usernam', 84, 58), 4825: (u"id python:'/' in creator_short_f", 85, 57), 4911: (u'_id python:(creator_short_form, creator_long_form)[creator_is_ope', 86, 49), 4489: (u'item_creator', 81, 51), 5302: (u'not:author', 91, 46), 5133: (u'string:${view/navigation_root_url}/author/${item_creator}', 89, 52), 5237: (u'author/name_or_id', 90, 45), 5566: (u"python: item_type != 'Event'", 98, 51), 5776: (u'python:view.toLocalizedTime(item_modified,long_format=1)', 101, 47), 6099: (u'nothing', 107, 50), 2544: (u"python:'vevent' if item_is_event else None", 52, 78), 2653: (u'item_type', 53, 64), 2705: (u"python:item_type == 'File' and showicons", 54, 40), 2793: (u'item_link', 55, 46), 2850: (u' string:$item_type_class $item_wf_state_class ur', 56, 46), 2946: (u'e item_ty', 57, 45), 3060: (u'item/MimeTypeIcon', 59, 52), 3153: (u'item_link', 61, 46), 3213: (u' string:$item_type_class $item_wf_state_class ur', 62, 49), 3312: (u'e item_ty', 63, 48), 3363: (u'item_title', 64, 38), 3511: (u'python: item_has_image and thumb_scale_list', 67, 40), 3459: (u'item_link', 66, 46), 3610: (u"python:image_scale.tag(item, 'image', scale=thumb_scale_list, css_class=img_class)", 68, 53), 1396: (u'batch', 32, 35), 1472: (u'item/getObject', 33, 39), 1512: (u' item/getUR', 34, 24), 1548: (u'd item/get', 35, 22), 1586: (u'le item/Ti', 36, 24), 1624: (u'tle python:item_title or ite', 37, 23), 1686: (u'tion item/Descri', 38, 28), 1729: (u'_type item/Port', 39, 20), 1775: (u'dified item/Modificat', 40, 23), 1826: (u'created item/Crea', 41, 21), 1874: (u'wf_state item/rev', 42, 21), 1928: (u"ate_class python:'state-' + view.normalizeString(item", 43, 26), 2011: (u'em_creator i', 44, 18), 2050: (u"  item_link python:item_type in view.use_view_action and item_url+'/view'", 45, 14), 2154: (u'tem_is_event python:view.', 46, 17), 2211: (u'tem_has_image pytho', 47, 17), 2263: (u"tem_type_class python:('contenttype-' + view.normalizeString(item_type)) if sh", 48, 17), 6494: (u'item_description', 116, 37), 6547: (u'item_description', 117, 35), 251: (u'context/@@main_template/macros/master', 6, 21), 251: (u'context/@@main_template/macros/master', 6, 21)}

from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140235322994320 = {u'class': u'discreet', }
_static_140235320936144 = {u'class': u'description discreet', }
_static_140235489934800 = {}
_static_140235322089424 = u'master'
_static_140235319959056 = u'navigation'
_static_140235320004752 = {u'class': u"python:'vevent' if item_is_event else None", }
_static_140235320864208 = {u'href': u'string:${view/navigation_root_url}/author/${item_creator}', }
_static_140235319871248 = {u'class': u'entries', }
_static_140235320936976 = {u'class': u'documentByLine', }
_static_140235322614928 = {u'href': u'item_link', u'class': u'string:$item_type_class $item_wf_state_class url', u'title': u'item_type', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235323063760 = {u'href': u'item_link', u'class': u'string:$item_type_class $item_wf_state_class url', u'title': u'item_type', }
_static_140235319823952 = {u'id': u'parent-fieldname-text', u'class': u'stx', }
_static_140235435449424 = __compile_zt_expr
_static_140235320008016 = {u'class': u'summary', u'title': u'item_type', }
_static_140235322614288 = {u'href': u'item_link', }
_static_140235314682704 = {u'class': u'entry', }
_static_140235319943696 = {u'class': u'location', }
_static_140235323063568 = {u'src': u'item/MimeTypeIcon', u'class': u'mime-icon', }

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

    def render_text_field_view(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_inside = econtext[u'__slot_inside'].pop()
        except:
            __slot_inside = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8b146c4e50> name=None at 7f8b146c4410> -> __attrs_140235319741392
            __attrs_140235319741392 = _static_140235319823952
            __backup_text_140235319974544 = get('text', __marker)

            # <Value u'view/text' (15:23)> -> __value
            __token = 524
            try:
                __zt_tmp = __attrs_140235319741392
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/text', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['text'] = __value

            # <Value u'text' (16:21)> -> __condition
            __token = 556
            try:
                __zt_tmp = __attrs_140235319741392
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'text', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="parent-fieldname-text"')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235319740560
                __default_140235319740560 = _DEFAULT_MARKER

                # <Substitution u'view/text_class' (17:28)> -> __attr_class
                __token = 590
                try:
                    __zt_tmp = __attrs_140235319741392
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140235435449424('path', u'view/text_class', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', u'stx', _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>\n    ')
                if (__slot_inside is None):

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235320908880
                    __attrs_140235320908880 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235320906832
                    __default_140235320906832 = _DEFAULT_MARKER

                    # <Value u'text' (18:59)> -> __cache_140235320909712
                    __token = 667
                    try:
                        __zt_tmp = __attrs_140235320908880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235320909712 = _static_140235435449424('path', u'text', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'text' (18:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b147cddd0> -> __condition
                    __expression = __cache_140235320909712

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div>The body</div>')
                    else:
                        __content = __cache_140235320909712
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                else:
                    __slot_inside(__stream, econtext.copy(), rcontext)
                __append(u'\n  </div>')
            if (__backup_text_140235319974544 is __marker):
                del econtext['text']
            else:
                econtext['text'] = __backup_text_140235319974544
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_listing(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_entries = econtext[u'__slot_entries'].pop()
        except:
            __slot_entries = None

        try:
            __slot_no_items_in_listing = econtext[u'__slot_no_items_in_listing'].pop()
        except:
            __slot_no_items_in_listing = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235320909392
            __attrs_140235320909392 = _static_140235489934800
            __append(u'\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322042064
            __attrs_140235322042064 = _static_140235489934800
            __backup_batch_140235323175568 = get('batch', __marker)

            # <Value u'view/batch' (22:31)> -> __value
            __token = 775
            try:
                __zt_tmp = __attrs_140235322042064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/batch', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['batch'] = __value
            __backup_thumb_scale_list_140235323178832 = get('thumb_scale_list', __marker)

            # <Value u'view/get_thumb_scale_list' (23:41)> -> __value
            __token = 828
            try:
                __zt_tmp = __attrs_140235322042064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/get_thumb_scale_list', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['thumb_scale_list'] = __value
            __backup_thumb_scale_table_140235319973456 = get('thumb_scale_table', __marker)

            # <Value u'view/get_thumb_scale_table' (24:41)> -> __value
            __token = 897
            try:
                __zt_tmp = __attrs_140235322042064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/get_thumb_scale_table', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['thumb_scale_table'] = __value
            __backup_thumb_scale_summary_140235323176208 = get('thumb_scale_summary', __marker)

            # <Value u'view/get_thumb_scale_summary' (25:42)> -> __value
            __token = 969
            try:
                __zt_tmp = __attrs_140235322042064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/get_thumb_scale_summary', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['thumb_scale_summary'] = __value
            __backup_img_class_140235323177808 = get('img_class', __marker)

            # <Value u"python:'thumb-%s pull-right' % thumb_scale_list" (26:31)> -> __value
            __token = 1033
            try:
                __zt_tmp = __attrs_140235322042064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"'thumb-%s pull-right' % thumb_scale_list", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['img_class'] = __value
            __backup_showicons_140235323175440 = get('showicons', __marker)

            # <Value u'view/show_icons' (27:30)> -> __value
            __token = 1116
            try:
                __zt_tmp = __attrs_140235322042064
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/show_icons', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['showicons'] = __value
            __append(u'\n      ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235320893712
            __attrs_140235320893712 = _static_140235489934800

            # <Value u'batch' (28:30)> -> __condition
            __token = 1169
            try:
                __zt_tmp = __attrs_140235320893712
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'batch', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __append(u'\n        ')
                if (__slot_entries is None):

                    # <Static value=<_ast.Dict object at 0x7f8b146d0710> name=None at 7f8b146d0c10> -> __attrs_140235319869776
                    __attrs_140235319869776 = _static_140235319871248
                    __backup_portal_140235323177424 = get('portal', __marker)

                    # <Value u'context/@@plone_portal_state/portal' (30:31)> -> __value
                    __token = 1265
                    try:
                        __zt_tmp = __attrs_140235319869776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'context/@@plone_portal_state/portal', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['portal'] = __value
                    __backup_image_scale_140235323178896 = get('image_scale', __marker)

                    # <Value u'portal/@@image_scale' (31:35)> -> __value
                    __token = 1337
                    try:
                        __zt_tmp = __attrs_140235319869776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'portal/@@image_scale', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['image_scale'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="entries">\n          ')
                    __token = None
                    render_entries(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append(u'\n        </div>')
                    if (__backup_image_scale_140235323178896 is __marker):
                        del econtext['image_scale']
                    else:
                        econtext['image_scale'] = __backup_image_scale_140235323178896
                    if (__backup_portal_140235323177424 is __marker):
                        del econtext['portal']
                    else:
                        econtext['portal'] = __backup_portal_140235323177424
                else:
                    __slot_entries(__stream, econtext.copy(), rcontext)
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235319955536
                __attrs_140235319955536 = _static_140235489934800
                __backup_macroname_140235368192672 = get('macroname', __marker)

                # <Static value=<_ast.Str object at 0x7f8b146e5e10> name=None at 7f8b146e5d50> -> __value
                __value = _static_140235319959056
                econtext['macroname'] = __value

                # <Value u'context/batch_macros/macros/navigation' (126:30)> -> __macro
                __token = 6772
                try:
                    __zt_tmp = __attrs_140235319955536
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140235435449424('path', u'context/batch_macros/macros/navigation', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __token = 6772
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140235368192672 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140235368192672
                __append(u'\n\n      ')
            __append(u'\n\n      ')
            if (__slot_no_items_in_listing is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322043536
                __attrs_140235322043536 = _static_140235489934800
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b149cae90> name=None at 7f8b146f1890> -> __attrs_140235319990352
                __attrs_140235319990352 = _static_140235322994320

                # <Value u'not: batch' (132:27)> -> __condition
                __token = 6953
                try:
                    __zt_tmp = __attrs_140235319990352
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('not', u' batch', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="discreet">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235320005904
                    __default_140235320005904 = _DEFAULT_MARKER

                    # <Value u'view/no_items_message' (133:25)> -> __cache_140235314680912
                    __token = 6990
                    try:
                        __zt_tmp = __attrs_140235319990352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235314680912 = _static_140235435449424('path', u'view/no_items_message', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/no_items_message' (133:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b141dd710> -> __condition
                    __expression = __cache_140235314680912

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n          There are currently no items in this folder.\n        ')
                    else:
                        __content = __cache_140235314680912
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</p>')
                __append(u'\n      ')
            else:
                __slot_no_items_in_listing(__stream, econtext.copy(), rcontext)
            __append(u'\n\n    ')
            if (__backup_showicons_140235323175440 is __marker):
                del econtext['showicons']
            else:
                econtext['showicons'] = __backup_showicons_140235323175440
            if (__backup_img_class_140235323177808 is __marker):
                del econtext['img_class']
            else:
                econtext['img_class'] = __backup_img_class_140235323177808
            if (__backup_thumb_scale_summary_140235323176208 is __marker):
                del econtext['thumb_scale_summary']
            else:
                econtext['thumb_scale_summary'] = __backup_thumb_scale_summary_140235323176208
            if (__backup_thumb_scale_table_140235319973456 is __marker):
                del econtext['thumb_scale_table']
            else:
                econtext['thumb_scale_table'] = __backup_thumb_scale_table_140235319973456
            if (__backup_thumb_scale_list_140235323178832 is __marker):
                del econtext['thumb_scale_list']
            else:
                econtext['thumb_scale_list'] = __backup_thumb_scale_list_140235323178832
            if (__backup_batch_140235323175568 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_140235323175568
            __append(u'\n  ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322564240
            __attrs_140235322564240 = _static_140235489934800
            __append(u'\n\n  ')
            __token = None
            render_text_field_view(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n  ')
            __token = None
            render_listing(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_document_byline(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_description_slot = econtext[u'__slot_description_slot'].pop()
        except:
            __slot_description_slot = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235320937168
            __attrs_140235320937168 = _static_140235489934800
            __append(u'\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8b147d4a10> name=None at 7f8b147d4350> -> __attrs_140235320937104
            __attrs_140235320937104 = _static_140235320936976

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="documentByLine">\n                        ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235320936336
            __attrs_140235320936336 = _static_140235489934800

            # <Value u'item_is_event' (73:46)> -> __condition
            __token = 3920
            try:
                __zt_tmp = __attrs_140235320936336
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'item_is_event', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __append(u'\n                          ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235319943440
                __attrs_140235319943440 = _static_140235489934800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235319945616
                __default_140235319945616 = _DEFAULT_MARKER

                # <Value u'python:view.formatted_date(obj)' (74:59)> -> __cache_140235319944912
                __token = 3995
                try:
                    __zt_tmp = __attrs_140235319943440
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235319944912 = _static_140235435449424('python', u'view.formatted_date(obj)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:view.formatted_date(obj)' (74:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b146e2810> -> __condition
                __expression = __cache_140235319944912

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140235319944912
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n                          ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235319946448
                __attrs_140235319946448 = _static_140235489934800

                # <Value u'item/location' (75:47)> -> __condition
                __token = 4077
                try:
                    __zt_tmp = __attrs_140235319946448
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'item/location', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140235316295392_location = ''
                    __stream_140235319946064 = []
                    __append_140235319946064 = __stream_140235319946064.append
                    __append_140235319946064(u'&mdash;\n                            ')
                    __stream_140235316295392_location = []
                    __append_140235316295392_location = __stream_140235316295392_location.append

                    # <Static value=<_ast.Dict object at 0x7f8b146e2210> name=None at 7f8b146e2790> -> __attrs_140235319946256
                    __attrs_140235319946256 = _static_140235319943696

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140235316295392_location(u'<span class="location">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235319947024
                    __default_140235319947024 = _DEFAULT_MARKER

                    # <Value u'string:${item/location}' (76:47)> -> __cache_140235319944848
                    __token = 4192
                    try:
                        __zt_tmp = __attrs_140235319946256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235319944848 = _static_140235435449424('string', u'${item/location}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'string:${item/location}' (76:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b146e22d0> -> __condition
                    __expression = __cache_140235319944848

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140235316295392_location(u'Oslo')
                    else:
                        __content = __cache_140235319944848
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140235316295392_location(__content)
                    __append_140235316295392_location(u'</span>')
                    __append_140235319946064(u'${location}')
                    __stream_140235316295392_location = ''.join(__stream_140235316295392_location)
                    __append_140235319946064(u',\n                          ')
                    __msgid_140235319946064 = __re_whitespace(''.join(__stream_140235319946064)).strip()
                    if u'label_event_byline_location':
                        __append(translate(u'label_event_byline_location', mapping={u'location': __stream_140235316295392_location, }, default=__msgid_140235319946064, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>')
                __append(u'\n                        ')
            __append(u'\n                        ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235319944976
            __attrs_140235319944976 = _static_140235489934800

            # <Value u'view/show_about' (79:47)> -> __condition
            __token = 4386
            try:
                __zt_tmp = __attrs_140235319944976
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'view/show_about', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __append(u'\n                          &mdash;\n                          ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235320861264
                __attrs_140235320861264 = _static_140235489934800
                __backup_author_140235320038480 = get('author', __marker)

                # <Value u'python:view.pas_member.info(item_creator)' (82:49)> -> __value
                __token = 4552
                try:
                    __zt_tmp = __attrs_140235320861264
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u'view.pas_member.info(item_creator)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['author'] = __value
                __backup_creator_short_form_140235432291408 = get('creator_short_form', __marker)

                # <Value u'author/username' (83:60)> -> __value
                __token = 4655
                try:
                    __zt_tmp = __attrs_140235320861264
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'author/username', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['creator_short_form'] = __value
                __backup_creator_long_form_140235320899408 = get('creator_long_form', __marker)

                # <Value u'string:?author=${author/username}' (84:58)> -> __value
                __token = 4731
                try:
                    __zt_tmp = __attrs_140235320861264
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('string', u'?author=${author/username}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['creator_long_form'] = __value
                __backup_creator_is_openid_140235320899664 = get('creator_is_openid', __marker)

                # <Value u"python:'/' in creator_short_form" (85:57)> -> __value
                __token = 4825
                try:
                    __zt_tmp = __attrs_140235320861264
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u"'/' in creator_short_form", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['creator_is_openid'] = __value
                __backup_creator_id_140235320900368 = get('creator_id', __marker)

                # <Value u'python:(creator_short_form, creator_long_form)[creator_is_openid]' (86:49)> -> __value
                __token = 4911
                try:
                    __zt_tmp = __attrs_140235320861264
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u'(creator_short_form, creator_long_form)[creator_is_openid]', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['creator_id'] = __value

                # <Value u'item_creator' (81:51)> -> __condition
                __token = 4489
                try:
                    __zt_tmp = __attrs_140235320861264
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'item_creator', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n                          ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235320864336
                    __attrs_140235320864336 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140235316295632_author = ''
                    __stream_140235320863632 = []
                    __append_140235320863632 = __stream_140235320863632.append
                    __append_140235320863632(u'\n                            by\n                            ')
                    __stream_140235316295632_author = []
                    __append_140235316295632_author = __stream_140235316295632_author.append

                    # <Static value=<_ast.Dict object at 0x7f8b147c2dd0> name=None at 7f8b147c2d90> -> __attrs_140235322990672
                    __attrs_140235322990672 = _static_140235320864208

                    # <Negate value=<Value u'not:author' (91:46)> at 7f8b149cac90> -> __cache_140235322993808

                    # <Value u'not:author' (91:46)> -> __cache_140235322993808
                    __token = 5302
                    try:
                        __zt_tmp = __attrs_140235322990672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235322993808 = _static_140235435449424('not', u'author', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __cache_140235322993808 = not __cache_140235322993808
                    __condition = __cache_140235322993808
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append_140235316295632_author(u'<a')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322993424
                        __default_140235322993424 = _DEFAULT_MARKER

                        # <Substitution u'string:${view/navigation_root_url}/author/${item_creator}' (89:52)> -> __attr_href
                        __token = 5133
                        try:
                            __zt_tmp = __attrs_140235322990672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140235435449424('string', u'${view/navigation_root_url}/author/${item_creator}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append_140235316295632_author((u' href="%s"' % __attr_href))
                        __append_140235316295632_author(u'>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235320861584
                    __default_140235320861584 = _DEFAULT_MARKER

                    # <Value u'author/name_or_id' (90:45)> -> __cache_140235320861840
                    __token = 5237
                    try:
                        __zt_tmp = __attrs_140235322990672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235320861840 = _static_140235435449424('path', u'author/name_or_id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'author/name_or_id' (90:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b147c2ed0> -> __condition
                    __expression = __cache_140235320861840

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append_140235316295632_author(u'\n                              Bob Dobalina\n                            ')
                    else:
                        __content = __cache_140235320861840
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140235316295632_author(__content)
                    __condition = __cache_140235322993808
                    if __condition:
                        __append_140235316295632_author(u'</a>')
                    __append_140235320863632(u'${author}')
                    __stream_140235316295632_author = ''.join(__stream_140235316295632_author)
                    __append_140235320863632(u'\n                          ')
                    __msgid_140235320863632 = __re_whitespace(''.join(__stream_140235320863632)).strip()
                    if u'label_by_author':
                        __append(translate(u'label_by_author', mapping={u'author': __stream_140235316295632_author, }, default=__msgid_140235320863632, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n                          ')
                if (__backup_creator_id_140235320900368 is __marker):
                    del econtext['creator_id']
                else:
                    econtext['creator_id'] = __backup_creator_id_140235320900368
                if (__backup_creator_is_openid_140235320899664 is __marker):
                    del econtext['creator_is_openid']
                else:
                    econtext['creator_is_openid'] = __backup_creator_is_openid_140235320899664
                if (__backup_creator_long_form_140235320899408 is __marker):
                    del econtext['creator_long_form']
                else:
                    econtext['creator_long_form'] = __backup_creator_long_form_140235320899408
                if (__backup_creator_short_form_140235432291408 is __marker):
                    del econtext['creator_short_form']
                else:
                    econtext['creator_short_form'] = __backup_creator_short_form_140235432291408
                if (__backup_author_140235320038480 is __marker):
                    del econtext['author']
                else:
                    econtext['author'] = __backup_author_140235320038480
                __append(u'\n\n                          ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235320863248
                __attrs_140235320863248 = _static_140235489934800

                # <Value u"python: item_type != 'Event'" (98:51)> -> __condition
                __token = 5566
                try:
                    __zt_tmp = __attrs_140235320863248
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('python', u" item_type != 'Event'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n                            &mdash;\n                            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322994128
                    __attrs_140235322994128 = _static_140235489934800
                    __stream_140235322992016 = []
                    __append_140235322992016 = __stream_140235322992016.append
                    __append_140235322992016(u'last modified')
                    __msgid_140235322992016 = __re_whitespace(''.join(__stream_140235322992016)).strip()
                    if u'box_last_modified':
                        __append(translate(u'box_last_modified', mapping=None, default=__msgid_140235322992016, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322993296
                    __attrs_140235322993296 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322994256
                    __default_140235322994256 = _DEFAULT_MARKER

                    # <Value u'python:view.toLocalizedTime(item_modified,long_format=1)' (101:47)> -> __cache_140235322992528
                    __token = 5776
                    try:
                        __zt_tmp = __attrs_140235322993296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235322992528 = _static_140235435449424('python', u'view.toLocalizedTime(item_modified,long_format=1)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'python:view.toLocalizedTime(item_modified,long_format=1)' (101:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b149caa10> -> __condition
                    __expression = __cache_140235322992528

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n                              August 16, 2001 at 23:35:59\n                            </span>')
                    else:
                        __content = __cache_140235322992528
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                          ')
                __append(u'\n\n                          ')
                if (__slot_description_slot is None):

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322994064
                    __attrs_140235322994064 = _static_140235489934800
                    __append(u'\n                            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235319991952
                    __attrs_140235319991952 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235319991568
                    __default_140235319991568 = _DEFAULT_MARKER

                    # <Value u'nothing' (107:50)> -> __cache_140235322991120
                    __token = 6099
                    try:
                        __zt_tmp = __attrs_140235319991952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235322991120 = _static_140235435449424('path', u'nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'nothing' (107:50)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b149cabd0> -> __condition
                    __expression = __cache_140235322991120

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                              Place custom listing info for custom types here\n                            ')
                    else:
                        __content = __cache_140235322991120
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                          ')
                else:
                    __slot_description_slot(__stream, econtext.copy(), rcontext)
                __append(u'\n                        ')
            __append(u'\n                      </div>\n                    ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_listitem(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8b146f1090> name=None at 7f8b146f17d0> -> __attrs_140235320005584
            __attrs_140235320005584 = _static_140235320004752

            # <header ... (0:0)
            # --------------------------------------------------------
            __append(u'<header')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235320004688
            __default_140235320004688 = _DEFAULT_MARKER

            # <Substitution u"python:'vevent' if item_is_event else None" (52:78)> -> __attr_class
            __token = 2544
            try:
                __zt_tmp = __attrs_140235320005584
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140235435449424('python', u"'vevent' if item_is_event else None", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))
            __append(u'>\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8b146f1d50> name=None at 7f8b146f19d0> -> __attrs_140235320008144
            __attrs_140235320008144 = _static_140235320008016

            # <span ... (0:0)
            # --------------------------------------------------------
            __append(u'<span class="summary"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235320008656
            __default_140235320008656 = _DEFAULT_MARKER

            # <Substitution u'item_type' (53:64)> -> __attr_title
            __token = 2653
            try:
                __zt_tmp = __attrs_140235320008144
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140235435449424('path', u'item_type', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u'>\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8b149dbdd0> name=None at 7f8b149dbe50> -> __attrs_140235323064080
            __attrs_140235323064080 = _static_140235323063760

            # <Value u"python:item_type == 'File' and showicons" (54:40)> -> __condition
            __token = 2705
            try:
                __zt_tmp = __attrs_140235323064080
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('python', u"item_type == 'File' and showicons", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235323062160
                __default_140235323062160 = _DEFAULT_MARKER

                # <Substitution u'item_link' (55:46)> -> __attr_href
                __token = 2793
                try:
                    __zt_tmp = __attrs_140235323064080
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140235435449424('path', u'item_link', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235323064272
                __default_140235323064272 = _DEFAULT_MARKER

                # <Substitution u'string:$item_type_class $item_wf_state_class url' (56:46)> -> __attr_class
                __token = 2850
                try:
                    __zt_tmp = __attrs_140235323064080
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140235435449424('string', u'$item_type_class $item_wf_state_class url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235323063632
                __default_140235323063632 = _DEFAULT_MARKER

                # <Substitution u'item_type' (57:45)> -> __attr_title
                __token = 2946
                try:
                    __zt_tmp = __attrs_140235323064080
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140235435449424('path', u'item_type', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_title is not None):
                    __append((u' title="%s"' % __attr_title))
                __append(u'>\n                         ')

                # <Static value=<_ast.Dict object at 0x7f8b149dbd10> name=None at 7f8b149db2d0> -> __attrs_140235322614864
                __attrs_140235322614864 = _static_140235323063568

                # <img ... (0:0)
                # --------------------------------------------------------
                __append(u'<img class="mime-icon"')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235323064208
                __default_140235323064208 = _DEFAULT_MARKER

                # <Substitution u'item/MimeTypeIcon' (59:52)> -> __attr_src
                __token = 3060
                try:
                    __zt_tmp = __attrs_140235322614864
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_140235435449424('path', u'item/MimeTypeIcon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((u' src="%s"' % __attr_src))
                __append(u'>\n                      </a>')
            __append(u'\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8b1496e490> name=None at 7f8b1496e950> -> __attrs_140235322614160
            __attrs_140235322614160 = _static_140235322614928

            # <a ... (0:0)
            # --------------------------------------------------------
            __append(u'<a')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322617424
            __default_140235322617424 = _DEFAULT_MARKER

            # <Substitution u'item_link' (61:46)> -> __attr_href
            __token = 3153
            try:
                __zt_tmp = __attrs_140235322614160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140235435449424('path', u'item_link', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322614800
            __default_140235322614800 = _DEFAULT_MARKER

            # <Substitution u'string:$item_type_class $item_wf_state_class url' (62:49)> -> __attr_class
            __token = 3213
            try:
                __zt_tmp = __attrs_140235322614160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140235435449424('string', u'$item_type_class $item_wf_state_class url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322614672
            __default_140235322614672 = _DEFAULT_MARKER

            # <Substitution u'item_type' (63:48)> -> __attr_title
            __token = 3312
            try:
                __zt_tmp = __attrs_140235322614160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140235435449424('path', u'item_type', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((u' title="%s"' % __attr_title))
            __append(u'>')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322615952
            __default_140235322615952 = _DEFAULT_MARKER

            # <Value u'item_title' (64:38)> -> __cache_140235320007056
            __token = 3363
            try:
                __zt_tmp = __attrs_140235322614160
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235320007056 = _static_140235435449424('path', u'item_title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'item_title' (64:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1496e5d0> -> __condition
            __expression = __cache_140235320007056

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'Item Title\n                      ')
            else:
                __content = __cache_140235320007056
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</a>\n                      ')

            # <Static value=<_ast.Dict object at 0x7f8b1496e210> name=None at 7f8b1496e290> -> __attrs_140235322615888
            __attrs_140235322615888 = _static_140235322614288

            # <Value u'python: item_has_image and thumb_scale_list' (67:40)> -> __condition
            __token = 3511
            try:
                __zt_tmp = __attrs_140235322615888
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('python', u' item_has_image and thumb_scale_list', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322617488
                __default_140235322617488 = _DEFAULT_MARKER

                # <Substitution u'item_link' (66:46)> -> __attr_href
                __token = 3459
                try:
                    __zt_tmp = __attrs_140235322615888
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140235435449424('path', u'item_link', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>\n                         ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235320934608
                __attrs_140235320934608 = _static_140235489934800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235320938320
                __default_140235320938320 = _DEFAULT_MARKER

                # <Value u"python:image_scale.tag(item, 'image', scale=thumb_scale_list, css_class=img_class)" (68:53)> -> __cache_140235320937936
                __token = 3610
                try:
                    __zt_tmp = __attrs_140235320934608
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235320937936 = _static_140235435449424('python', u"image_scale.tag(item, 'image', scale=thumb_scale_list, css_class=img_class)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u"python:image_scale.tag(item, 'image', scale=thumb_scale_list, css_class=img_class)" (68:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b147d43d0> -> __condition
                __expression = __cache_140235320937936

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<img />')
                else:
                    __content = __cache_140235320937936
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n                      </a>')
            __append(u'\n                    </span>\n                    ')
            __token = None
            render_document_byline(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n                  </header>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_entries(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_entry = econtext[u'__slot_entry'].pop()
        except:
            __slot_entry = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235319959184
            __attrs_140235319959184 = _static_140235489934800
            __backup_item_140235323175376 = get('item', __marker)

            # <Value u'batch' (32:35)> -> __iterator
            __token = 1396
            try:
                __zt_tmp = __attrs_140235319959184
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140235435449424('path', u'batch', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            (__iterator, ____index_140235319955792, ) = getitem('repeat')(u'item', __iterator)
            econtext['item'] = None
            for __item in __iterator:
                econtext['item'] = __item
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235323177552
                __attrs_140235323177552 = _static_140235489934800
                __backup_obj_140235323177104 = get('obj', __marker)

                # <Value u'item/getObject' (33:39)> -> __value
                __token = 1472
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'item/getObject', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['obj'] = __value
                __backup_item_url_140235323176144 = get('item_url', __marker)

                # <Value u'item/getURL' (34:24)> -> __value
                __token = 1512
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'item/getURL', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_url'] = __value
                __backup_item_id_140235322883472 = get('item_id', __marker)

                # <Value u'item/getId' (35:22)> -> __value
                __token = 1548
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'item/getId', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_id'] = __value
                __backup_item_title_140235322089808 = get('item_title', __marker)

                # <Value u'item/Title' (36:24)> -> __value
                __token = 1586
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'item/Title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_title'] = __value
                __backup_item_title_140235431401232 = get('item_title', __marker)

                # <Value u'python:item_title or item_id' (37:23)> -> __value
                __token = 1624
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u'item_title or item_id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_title'] = __value
                __backup_item_description_140235320037520 = get('item_description', __marker)

                # <Value u'item/Description' (38:28)> -> __value
                __token = 1686
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'item/Description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_description'] = __value
                __backup_item_type_140235320040016 = get('item_type', __marker)

                # <Value u'item/PortalType' (39:20)> -> __value
                __token = 1729
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'item/PortalType', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_type'] = __value
                __backup_item_modified_140235320037456 = get('item_modified', __marker)

                # <Value u'item/ModificationDate' (40:23)> -> __value
                __token = 1775
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'item/ModificationDate', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_modified'] = __value
                __backup_item_created_140235320039760 = get('item_created', __marker)

                # <Value u'item/CreationDate' (41:21)> -> __value
                __token = 1826
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'item/CreationDate', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_created'] = __value
                __backup_item_wf_state_140235320040208 = get('item_wf_state', __marker)

                # <Value u'item/review_state' (42:21)> -> __value
                __token = 1874
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'item/review_state', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_wf_state'] = __value
                __backup_item_wf_state_class_140235320039312 = get('item_wf_state_class', __marker)

                # <Value u"python:'state-' + view.normalizeString(item_wf_state)" (43:26)> -> __value
                __token = 1928
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u"'state-' + view.normalizeString(item_wf_state)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_wf_state_class'] = __value
                __backup_item_creator_140235320038992 = get('item_creator', __marker)

                # <Value u'item/Creator' (44:18)> -> __value
                __token = 2011
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'item/Creator', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_creator'] = __value
                __backup_item_link_140235320041040 = get('item_link', __marker)

                # <Value u"python:item_type in view.use_view_action and item_url+'/view' or item_url" (45:14)> -> __value
                __token = 2050
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u"item_type in view.use_view_action and item_url+'/view' or item_url", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_link'] = __value
                __backup_item_is_event_140235320039440 = get('item_is_event', __marker)

                # <Value u'python:view.is_event(obj)' (46:17)> -> __value
                __token = 2154
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u'view.is_event(obj)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_is_event'] = __value
                __backup_item_has_image_140235320037840 = get('item_has_image', __marker)

                # <Value u'python:item.getIcon' (47:17)> -> __value
                __token = 2211
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u'item.getIcon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_has_image'] = __value
                __backup_item_type_class_140235320038928 = get('item_type_class', __marker)

                # <Value u"python:('contenttype-' + view.normalizeString(item_type)) if showicons else '' " (48:17)> -> __value
                __token = 2263
                try:
                    __zt_tmp = __attrs_140235323177552
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u"('contenttype-' + view.normalizeString(item_type)) if showicons else '' ", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['item_type_class'] = __value
                __append(u'\n              ')
                if (__slot_entry is None):

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235314682448
                    __attrs_140235314682448 = _static_140235489934800
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8b141ddb50> name=None at 7f8b141dd590> -> __attrs_140235314682256
                    __attrs_140235314682256 = _static_140235314682704

                    # <article ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<article class="entry">\n                  ')
                    __token = None
                    render_listitem(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f8b147d46d0> name=None at 7f8b147d4250> -> __attrs_140235320861712
                    __attrs_140235320861712 = _static_140235320936144

                    # <Value u'item_description' (116:37)> -> __condition
                    __token = 6494
                    try:
                        __zt_tmp = __attrs_140235320861712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'item_description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p class="description discreet">')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235320935056
                        __default_140235320935056 = _DEFAULT_MARKER

                        # <Value u'item_description' (117:35)> -> __cache_140235322616784
                        __token = 6547
                        try:
                            __zt_tmp = __attrs_140235320861712
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235322616784 = _static_140235435449424('path', u'item_description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'item_description' (117:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1496ecd0> -> __condition
                        __expression = __cache_140235322616784

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                    description\n                  ')
                        else:
                            __content = __cache_140235322616784
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</p>')
                    __append(u'\n                </article>\n              ')
                else:
                    __slot_entry(__stream, econtext.copy(), rcontext)
                __append(u'\n            ')
                if (__backup_item_type_class_140235320038928 is __marker):
                    del econtext['item_type_class']
                else:
                    econtext['item_type_class'] = __backup_item_type_class_140235320038928
                if (__backup_item_has_image_140235320037840 is __marker):
                    del econtext['item_has_image']
                else:
                    econtext['item_has_image'] = __backup_item_has_image_140235320037840
                if (__backup_item_is_event_140235320039440 is __marker):
                    del econtext['item_is_event']
                else:
                    econtext['item_is_event'] = __backup_item_is_event_140235320039440
                if (__backup_item_link_140235320041040 is __marker):
                    del econtext['item_link']
                else:
                    econtext['item_link'] = __backup_item_link_140235320041040
                if (__backup_item_creator_140235320038992 is __marker):
                    del econtext['item_creator']
                else:
                    econtext['item_creator'] = __backup_item_creator_140235320038992
                if (__backup_item_wf_state_class_140235320039312 is __marker):
                    del econtext['item_wf_state_class']
                else:
                    econtext['item_wf_state_class'] = __backup_item_wf_state_class_140235320039312
                if (__backup_item_wf_state_140235320040208 is __marker):
                    del econtext['item_wf_state']
                else:
                    econtext['item_wf_state'] = __backup_item_wf_state_140235320040208
                if (__backup_item_created_140235320039760 is __marker):
                    del econtext['item_created']
                else:
                    econtext['item_created'] = __backup_item_created_140235320039760
                if (__backup_item_modified_140235320037456 is __marker):
                    del econtext['item_modified']
                else:
                    econtext['item_modified'] = __backup_item_modified_140235320037456
                if (__backup_item_type_140235320040016 is __marker):
                    del econtext['item_type']
                else:
                    econtext['item_type'] = __backup_item_type_140235320040016
                if (__backup_item_description_140235320037520 is __marker):
                    del econtext['item_description']
                else:
                    econtext['item_description'] = __backup_item_description_140235320037520
                if (__backup_item_title_140235431401232 is __marker):
                    del econtext['item_title']
                else:
                    econtext['item_title'] = __backup_item_title_140235431401232
                if (__backup_item_title_140235322089808 is __marker):
                    del econtext['item_title']
                else:
                    econtext['item_title'] = __backup_item_title_140235322089808
                if (__backup_item_id_140235322883472 is __marker):
                    del econtext['item_id']
                else:
                    econtext['item_id'] = __backup_item_id_140235322883472
                if (__backup_item_url_140235323176144 is __marker):
                    del econtext['item_url']
                else:
                    econtext['item_url'] = __backup_item_url_140235323176144
                if (__backup_obj_140235323177104 is __marker):
                    del econtext['obj']
                else:
                    econtext['obj'] = __backup_obj_140235323177104
                __append(u'\n          ')
                ____index_140235319955792 -= 1
                if (____index_140235319955792 > 0):
                    __append('')
            if (__backup_item_140235323175376 is __marker):
                del econtext['item']
            else:
                econtext['item'] = __backup_item_140235323175376
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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322019792
            __attrs_140235322019792 = _static_140235489934800
            __previous_i18n_domain_140235322017552 = __i18n_domain
            __i18n_domain = u'plone'
            __backup_macroname_140235315846992 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8b148edfd0> name=None at 7f8b1aa94b90> -> __value
            __value = _static_140235322089424
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235320038032
                __attrs_140235320038032 = _static_140235489934800
                __append(u'\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n')
            _slots = econtext[u'__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value u'context/@@main_template/macros/master' (6:21)> -> __macro
            __token = 251
            try:
                __zt_tmp = __attrs_140235322019792
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140235435449424('path', u'context/@@main_template/macros/master', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __token = 251
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140235315846992 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140235315846992
            __i18n_domain = __previous_i18n_domain_140235322017552
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_text_field_view': render_text_field_view, u'render_listing': render_listing, u'render_content_core': render_content_core, u'render_document_byline': render_document_byline, u'render_listitem': render_listitem, u'render_entries': render_entries, 'render': render, }
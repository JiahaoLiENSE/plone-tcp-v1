# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.z3cform-3.2.4-py2.7.egg/plone/app/z3cform/templates/macros.pt'

__tokens = {5388: (u'view/widgets/values', 97, 62), 386: (u'view/label | nothing', 12, 33), 421: (u'view/label', 12, 68), 4796: (u'show_default_label|nothing', 87, 57), 4872: (u' has_groups|nothin', 88, 48), 4967: (u'not:show_default_label', 90, 72), 5046: (u'show_default_label', 92, 53), 5123: (u'string:fieldsetlegend-default', 93, 57), 5205: (u'default_fieldset_label', 94, 51), 6059: (u'has_groups', 108, 74), 6040: (u'groups', 108, 55), 6174: (u'nocall:context/@@plone/normalizeString', 110, 62), 6274: (u' group/labe', 111, 60), 6346: (u"e python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_lab", 112, 58), 6507: (u'me python:normalizeString(fieldset_na', 113, 57), 6603: (u'string:fieldset-${fieldset_name}', 114, 53), 6692: (u' string:kssattr-fieldset-${fieldset_name', 115, 55), 6797: (u't fieldset_na', 116, 62), 6877: (u'fieldset_label', 118, 61), 6958: (u'string:fieldsetlegend-${fieldset_name}', 119, 65), 7057: (u'fieldset_label', 120, 59), 7223: (u'group/description|nothing', 123, 71), 7306: (u'group_description', 124, 56), 7389: (u'group_description', 125, 64), 7575: (u'group/widgets/errors', 129, 68), 7661: (u'errors', 130, 64), 7736: (u'errors', 131, 67), 7873: (u'not:nocall:error/widget', 133, 61), 7967: (u'error/render', 134, 69), 8144: (u'nocall:group', 138, 62), 8225: (u'context/@@ploneform-macros/widget_rendering', 139, 66), 8225: (u'context/@@ploneform-macros/widget_rendering', 139, 66), 8744: (u'view/actions/values|nothing', 152, 69), 8832: (u'view/actions/values', 153, 58), 8934: (u'action/render', 154, 80), 5645: (u'widget/@@ploneform-render-widget', 100, 81), 569: (u'view/status', 17, 43), 627: (u" python:view.widgets.errors or status == getattr(view, 'formErrorsMessage', None", 18, 45), 721: (u'status', 18, 139), 797: (u'has_error', 19, 67), 994: (u'status', 23, 41), 1097: (u'not:has_error', 25, 66), 1298: (u'status', 29, 41), 1409: (u'view/widgets/errors', 33, 43), 1441: (u'errors', 33, 75), 1495: (u'errors', 34, 45), 1597: (u'not:nocall:error/widget', 36, 44), 1674: (u'error/render', 37, 52), 1971: (u'view/description | nothing', 45, 46), 2036: (u'description', 46, 37), 2094: (u'description', 47, 45), 2435: (u'view/groups | nothing', 54, 41), 2501: (u' view/form_name | nothin', 55, 43), 2571: (u's view/css_class | strin', 56, 43), 2653: (u'el view/default_fieldset_label | form_n', 57, 54), 2747: (u'ing view/enable_form_tabbing | python:', 58, 50), 2845: (u'tion view/enable_unload_protection|python', 59, 54), 2939: (u"ction python:enable_unload_protection and 'pat-formunload", 60, 46), 3042: (u'groups python:bool(', 61, 38), 3109: (u"tabbing python:(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autoto", 62, 39), 3248: (u'lt_label python:has_groups and default_fieldset_label and len(view', 63, 44), 3368: (u'_name_raw python:view.__name__ or request.getURL().spli', 64, 43), 3473: (u"_view_name python:'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('", 65, 38), 3781: (u"s python:'rowlike {0} {1} {2} kssattr-formname-{3} {4}'.format(unload_protection, form_tabbing, form_class, form_view_name_raw, form_view_nam", 69, 42), 3651: (u'view/action|request/getURL', 67, 45), 4070: (u'thod view/method|string', 72, 40), 3724: (u' view/enctyp', 68, 45), 3964: (u'id view', 70, 38), 4015: (u'ame form_', 71, 39), 4362: (u'request/fieldset | python:None', 79, 55), 4435: (u'python:has_groups and enable_form_tabbing and current_fieldset is not None', 80, 41), 4559: (u'current_fieldset', 81, 48), 9161: (u'view/enableCSRFProtection|nothing', 160, 46), 9241: (u'context/@@authenticator/authenticator', 161, 45)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235321920336 = {u'id': u'fieldset-default', }
_static_140235322885392 = {u'class': u'discreet', }
_static_140235373293968 = {u'name': u'form_name', u'data-pat-autotoc': u'levels: legend; section: fieldset; className: autotabs', u'class': u'rowlike enableUnloadProtection', u'method': u'post', u'action': u'.', u'id': u'view/id', u'enctype': u'view/enctype', }
_static_140235489934800 = {}
_static_140235322824528 = {u'role': u'status', u'class': u'portalMessage info', }
_static_140235322709264 = {u'id': u'string:fieldsetlegend-${fieldset_name}', }
_static_140235435449424 = __compile_zt_expr
_static_140235322110352 = {u'type': u'hidden', u'name': u'fieldset', u'value': u'current_fieldset', }
_static_140235322884496 = {u'class': u'field error', }
_static_140235322693968 = {u'id': u'string:fieldsetlegend-default', }
_static_140235322605136 = {u'xmlns': u'http://www.w3.org/1999/xhtml', }
_static_140235323429584 = {u'type': u'submit', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235431391056 = {u'role': u'alert', u'class': u'portalMessage error', }
_static_140235322637392 = {u'data-fieldset': u'fieldset_name', u'id': u'string:fieldset-${fieldset_name}', u'class': u'string:kssattr-fieldset-${fieldset_name}', }
_static_140235322487248 = {u'class': u'field error', }
_static_140235322044624 = {u'class': u'form', }
_static_140235322488016 = {u'class': u'formControls', }
_static_140235322489616 = u'widget_rendering'

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

    def render_widget_rendering(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_field = econtext[u'__slot_field'].pop()
        except:
            __slot_field = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322692368
            __attrs_140235322692368 = _static_140235489934800
            __append(u'\n                                  ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322637712
            __attrs_140235322637712 = _static_140235489934800
            __backup_widget_140235322692944 = get('widget', __marker)

            # <Value u'view/widgets/values' (97:62)> -> __iterator
            __token = 5388
            try:
                __zt_tmp = __attrs_140235322637712
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140235435449424('path', u'view/widgets/values', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            (__iterator, ____index_140235322637072, ) = getitem('repeat')(u'widget', __iterator)
            econtext['widget'] = None
            for __item in __iterator:
                econtext['widget'] = __item
                __append(u'\n                                      ')
                if (__slot_field is None):

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322635664
                    __attrs_140235322635664 = _static_140235489934800
                    __append(u'\n                                          ')
                    __token = None
                    render_field(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    __append(u'\n                                      ')
                else:
                    __slot_field(__stream, econtext.copy(), rcontext)
                __append(u'\n                                  ')
                ____index_140235322637072 -= 1
                if (____index_140235322637072 > 0):
                    __append('')
            if (__backup_widget_140235322692944 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140235322692944
            __append(u'\n                              ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_form(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_title = econtext[u'__slot_title'].pop()
        except:
            __slot_title = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8b148e30d0> name=None at 7f8b148e3190> -> __attrs_140235322046096
            __attrs_140235322046096 = _static_140235322044624

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="form">\n\n            ')
            if (__slot_title is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322047824
                __attrs_140235322047824 = _static_140235489934800
                __append(u'\n              ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322028944
                __attrs_140235322028944 = _static_140235489934800

                # <Value u'view/label | nothing' (12:33)> -> __condition
                __token = 386
                try:
                    __zt_tmp = __attrs_140235322028944
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/label | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h3>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322028432
                    __default_140235322028432 = _DEFAULT_MARKER

                    # <Value u'view/label' (12:68)> -> __cache_140235322029520
                    __token = 421
                    try:
                        __zt_tmp = __attrs_140235322028944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235322029520 = _static_140235435449424('path', u'view/label', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'view/label' (12:68)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148dfc10> -> __condition
                    __expression = __cache_140235322029520

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235322029520
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</h3>')
                __append(u'\n            ')
            else:
                __slot_title(__stream, econtext.copy(), rcontext)
            __append(u'\n\n            ')
            __token = None
            render_titlelessform(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n        </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_fields(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321917776
            __attrs_140235321917776 = _static_140235489934800
            __backup_show_default_label_140235322112272 = get('show_default_label', __marker)

            # <Value u'show_default_label|nothing' (87:57)> -> __value
            __token = 4796
            try:
                __zt_tmp = __attrs_140235321917776
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'show_default_label|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['show_default_label'] = __value
            __backup_has_groups_140235321919440 = get('has_groups', __marker)

            # <Value u'has_groups|nothing' (88:48)> -> __value
            __token = 4872
            try:
                __zt_tmp = __attrs_140235321917776
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'has_groups|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['has_groups'] = __value
            __append(u'\n\n                          ')

            # <Static value=<_ast.Dict object at 0x7f8b148c4b50> name=None at 7f8b148c4090> -> __attrs_140235322693328
            __attrs_140235322693328 = _static_140235321920336

            # <Negate value=<Value u'not:show_default_label' (90:72)> at 7f8b148c4d90> -> __cache_140235321920912

            # <Value u'not:show_default_label' (90:72)> -> __cache_140235321920912
            __token = 4967
            try:
                __zt_tmp = __attrs_140235322693328
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235321920912 = _static_140235435449424('not', u'show_default_label', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __cache_140235321920912 = not __cache_140235321920912
            __condition = __cache_140235321920912
            if __condition:

                # <fieldset ... (0:0)
                # --------------------------------------------------------
                __append(u'<fieldset id="fieldset-default">')
            __append(u'\n\n                              ')

            # <Static value=<_ast.Dict object at 0x7f8b14981950> name=None at 7f8b149811d0> -> __attrs_140235322695056
            __attrs_140235322695056 = _static_140235322693968

            # <Value u'show_default_label' (92:53)> -> __condition
            __token = 5046
            try:
                __zt_tmp = __attrs_140235322695056
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'show_default_label', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:

                # <legend ... (0:0)
                # --------------------------------------------------------
                __append(u'<legend')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322692240
                __default_140235322692240 = _DEFAULT_MARKER

                # <Substitution u'string:fieldsetlegend-default' (93:57)> -> __attr_id
                __token = 5123
                try:
                    __zt_tmp = __attrs_140235322695056
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140235435449424('string', u'fieldsetlegend-default', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((u' id="%s"' % __attr_id))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322692176
                __default_140235322692176 = _DEFAULT_MARKER

                # <Value u'default_fieldset_label' (94:51)> -> __cache_140235322693648
                __token = 5205
                try:
                    __zt_tmp = __attrs_140235322695056
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235322693648 = _static_140235435449424('path', u'default_fieldset_label', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'default_fieldset_label' (94:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b149813d0> -> __condition
                __expression = __cache_140235322693648

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(u'Form name')
                else:
                    __content = __cache_140235322693648
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</legend>')
            __append(u'\n\n                              ')
            __token = None
            render_widget_rendering(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n                          ')
            __condition = __cache_140235321920912
            if __condition:
                __append(u'</fieldset>')
            __append(u'\n\n                          <!-- Secondary fieldsets -->\n                          ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322638288
            __attrs_140235322638288 = _static_140235489934800

            # <Value u'has_groups' (108:74)> -> __condition
            __token = 6059
            try:
                __zt_tmp = __attrs_140235322638288
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'has_groups', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __backup_group_140235321920016 = get('group', __marker)

                # <Value u'groups' (108:55)> -> __iterator
                __token = 6040
                try:
                    __zt_tmp = __attrs_140235322638288
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140235435449424('path', u'groups', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                (__iterator, ____index_140235322635600, ) = getitem('repeat')(u'group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item
                    __append(u'\n                              ')

                    # <Static value=<_ast.Dict object at 0x7f8b14973c50> name=None at 7f8b14973a90> -> __attrs_140235322708176
                    __attrs_140235322708176 = _static_140235322637392
                    __backup_normalizeString_140235322691664 = get('normalizeString', __marker)

                    # <Value u'nocall:context/@@plone/normalizeString' (110:62)> -> __value
                    __token = 6174
                    try:
                        __zt_tmp = __attrs_140235322708176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('nocall', u'context/@@plone/normalizeString', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['normalizeString'] = __value
                    __backup_fieldset_label_140235322638160 = get('fieldset_label', __marker)

                    # <Value u'group/label' (111:60)> -> __value
                    __token = 6274
                    try:
                        __zt_tmp = __attrs_140235322708176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'group/label', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['fieldset_label'] = __value
                    __backup_fieldset_name_140235322692624 = get('fieldset_name', __marker)

                    # <Value u"python:getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label" (112:58)> -> __value
                    __token = 6346
                    try:
                        __zt_tmp = __attrs_140235322708176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"getattr(group, '__name__', False) or getattr(group.label, 'default', False) or fieldset_label", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value
                    __backup_fieldset_name_140235322635344 = get('fieldset_name', __marker)

                    # <Value u'python:normalizeString(fieldset_name)' (113:57)> -> __value
                    __token = 6507
                    try:
                        __zt_tmp = __attrs_140235322708176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u'normalizeString(fieldset_name)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['fieldset_name'] = __value

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<fieldset')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322708880
                    __default_140235322708880 = _DEFAULT_MARKER

                    # <Substitution u'string:fieldset-${fieldset_name}' (114:53)> -> __attr_id
                    __token = 6603
                    try:
                        __zt_tmp = __attrs_140235322708176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140235435449424('string', u'fieldset-${fieldset_name}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322711888
                    __default_140235322711888 = _DEFAULT_MARKER

                    # <Substitution u'string:kssattr-fieldset-${fieldset_name}' (115:55)> -> __attr_class
                    __token = 6692
                    try:
                        __zt_tmp = __attrs_140235322708176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140235435449424('string', u'kssattr-fieldset-${fieldset_name}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322709584
                    __default_140235322709584 = _DEFAULT_MARKER

                    # <Substitution u'fieldset_name' (116:62)> -> __attr_data_fieldset
                    __token = 6797
                    try:
                        __zt_tmp = __attrs_140235322708176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_fieldset = _static_140235435449424('path', u'fieldset_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_data_fieldset = __quote(__attr_data_fieldset, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_data_fieldset is not None):
                        __append((u' data-fieldset="%s"' % __attr_data_fieldset))
                    __append(u'>\n\n                                      ')

                    # <Static value=<_ast.Dict object at 0x7f8b14985510> name=None at 7f8b149859d0> -> __attrs_140235322710672
                    __attrs_140235322710672 = _static_140235322709264

                    # <Value u'fieldset_label' (118:61)> -> __condition
                    __token = 6877
                    try:
                        __zt_tmp = __attrs_140235322710672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'fieldset_label', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <legend ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<legend')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322710032
                        __default_140235322710032 = _DEFAULT_MARKER

                        # <Substitution u'string:fieldsetlegend-${fieldset_name}' (119:65)> -> __attr_id
                        __token = 6958
                        try:
                            __zt_tmp = __attrs_140235322710672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140235435449424('string', u'fieldsetlegend-${fieldset_name}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((u' id="%s"' % __attr_id))
                        __append(u'>')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322711568
                        __default_140235322711568 = _DEFAULT_MARKER

                        # <Value u'fieldset_label' (120:59)> -> __cache_140235322711312
                        __token = 7057
                        try:
                            __zt_tmp = __attrs_140235322710672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235322711312 = _static_140235435449424('path', u'fieldset_label', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'fieldset_label' (120:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b149855d0> -> __condition
                        __expression = __cache_140235322711312

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Form name')
                        else:
                            __content = __cache_140235322711312
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</legend>')
                    __append(u'\n\n                                      ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235379952528
                    __attrs_140235379952528 = _static_140235489934800
                    __backup_group_description_140235322634768 = get('group_description', __marker)

                    # <Value u'group/description|nothing' (123:71)> -> __value
                    __token = 7223
                    try:
                        __zt_tmp = __attrs_140235379952528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'group/description|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['group_description'] = __value

                    # <Value u'group_description' (124:56)> -> __condition
                    __token = 7306
                    try:
                        __zt_tmp = __attrs_140235379952528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'group_description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p>')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235379950160
                        __default_140235379950160 = _DEFAULT_MARKER

                        # <Value u'group_description' (125:64)> -> __cache_140235379950992
                        __token = 7389
                        try:
                            __zt_tmp = __attrs_140235379952528
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235379950992 = _static_140235435449424('path', u'group_description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'group_description' (125:64)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1801c650> -> __condition
                        __expression = __cache_140235379950992

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                                          Description\n                                      ')
                        else:
                            __content = __cache_140235379950992
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</p>')
                    if (__backup_group_description_140235322634768 is __marker):
                        del econtext['group_description']
                    else:
                        econtext['group_description'] = __backup_group_description_140235322634768
                    __append(u'\n\n                                      ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235379951888
                    __attrs_140235379951888 = _static_140235489934800
                    __backup_errors_140235322636048 = get('errors', __marker)

                    # <Value u'group/widgets/errors' (129:68)> -> __value
                    __token = 7575
                    try:
                        __zt_tmp = __attrs_140235379951888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'group/widgets/errors', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['errors'] = __value

                    # <Value u'errors' (130:64)> -> __condition
                    __token = 7661
                    try:
                        __zt_tmp = __attrs_140235379951888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'errors', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:
                        __backup_error_140235322694352 = get('error', __marker)

                        # <Value u'errors' (131:67)> -> __iterator
                        __token = 7736
                        try:
                            __zt_tmp = __attrs_140235379951888
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140235435449424('path', u'errors', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        (__iterator, ____index_140235379953040, ) = getitem('repeat')(u'error', __iterator)
                        econtext['error'] = None
                        for __item in __iterator:
                            econtext['error'] = __item
                            __append(u'\n                                          ')

                            # <Static value=<_ast.Dict object at 0x7f8b1494f1d0> name=None at 7f8b1801c9d0> -> __attrs_140235322487376
                            __attrs_140235322487376 = _static_140235322487248

                            # <Value u'not:nocall:error/widget' (133:61)> -> __condition
                            __token = 7873
                            try:
                                __zt_tmp = __attrs_140235322487376
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('not', u'nocall:error/widget', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<div class="field error">')

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235379949712
                                __default_140235379949712 = _DEFAULT_MARKER

                                # <Value u'error/render' (134:69)> -> __cache_140235379950864
                                __token = 7967
                                try:
                                    __zt_tmp = __attrs_140235322487376
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140235379950864 = _static_140235435449424('path', u'error/render', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                                # <BinOp left=<Value u'error/render' (134:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1801cc90> -> __condition
                                __expression = __cache_140235379950864

                                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140235379950864
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'</div>')
                            __append(u'\n                                      ')
                            ____index_140235379953040 -= 1
                            if (____index_140235379953040 > 0):
                                __append('')
                        if (__backup_error_140235322694352 is __marker):
                            del econtext['error']
                        else:
                            econtext['error'] = __backup_error_140235322694352
                    if (__backup_errors_140235322636048 is __marker):
                        del econtext['errors']
                    else:
                        econtext['errors'] = __backup_errors_140235322636048
                    __append(u'\n\n                                      ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322711120
                    __attrs_140235322711120 = _static_140235489934800
                    __backup_view_140235322634640 = get('view', __marker)

                    # <Value u'nocall:group' (138:62)> -> __value
                    __token = 8144
                    try:
                        __zt_tmp = __attrs_140235322711120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('nocall', u'group', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['view'] = __value
                    __append(u'\n                                          ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322489488
                    __attrs_140235322489488 = _static_140235489934800
                    __backup_macroname_140235361686864 = get('macroname', __marker)

                    # <Static value=<_ast.Str object at 0x7f8b1494fb10> name=None at 7f8b1494fcd0> -> __value
                    __value = _static_140235322489616
                    econtext['macroname'] = __value

                    # <Value u'context/@@ploneform-macros/widget_rendering' (139:66)> -> __macro
                    __token = 8225
                    try:
                        __zt_tmp = __attrs_140235322489488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __macro = _static_140235435449424('path', u'context/@@ploneform-macros/widget_rendering', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __token = 8225
                    __m = __macro.include
                    __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                    econtext.update(rcontext)
                    if (__backup_macroname_140235361686864 is __marker):
                        del econtext['macroname']
                    else:
                        econtext['macroname'] = __backup_macroname_140235361686864
                    __append(u'\n                                      ')
                    if (__backup_view_140235322634640 is __marker):
                        del econtext['view']
                    else:
                        econtext['view'] = __backup_view_140235322634640
                    __append(u'\n\n                              </fieldset>')
                    if (__backup_fieldset_name_140235322635344 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140235322635344
                    if (__backup_fieldset_name_140235322692624 is __marker):
                        del econtext['fieldset_name']
                    else:
                        econtext['fieldset_name'] = __backup_fieldset_name_140235322692624
                    if (__backup_fieldset_label_140235322638160 is __marker):
                        del econtext['fieldset_label']
                    else:
                        econtext['fieldset_label'] = __backup_fieldset_label_140235322638160
                    if (__backup_normalizeString_140235322691664 is __marker):
                        del econtext['normalizeString']
                    else:
                        econtext['normalizeString'] = __backup_normalizeString_140235322691664
                    __append(u'\n                          ')
                    ____index_140235322635600 -= 1
                    if (____index_140235322635600 > 0):
                        __append('')
                if (__backup_group_140235321920016 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_140235321920016
            __append(u'\n\n                      ')
            if (__backup_has_groups_140235321919440 is __marker):
                del econtext['has_groups']
            else:
                econtext['has_groups'] = __backup_has_groups_140235321919440
            if (__backup_show_default_label_140235322112272 is __marker):
                del econtext['show_default_label']
            else:
                econtext['show_default_label'] = __backup_show_default_label_140235322112272
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_actions(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235379952464
            __attrs_140235379952464 = _static_140235489934800
            __append(u'\n                            ')

            # <Static value=<_ast.Dict object at 0x7f8b1494f4d0> name=None at 7f8b1494fd50> -> __attrs_140235322488720
            __attrs_140235322488720 = _static_140235322488016

            # <Value u'view/actions/values|nothing' (152:69)> -> __condition
            __token = 8744
            try:
                __zt_tmp = __attrs_140235322488720
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'view/actions/values|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="formControls">\n                                ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322489744
                __attrs_140235322489744 = _static_140235489934800
                __backup_action_140235322111952 = get('action', __marker)

                # <Value u'view/actions/values' (153:58)> -> __iterator
                __token = 8832
                try:
                    __zt_tmp = __attrs_140235322489744
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140235435449424('path', u'view/actions/values', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                (__iterator, ____index_140235323432080, ) = getitem('repeat')(u'action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append(u'\n                                    ')

                    # <Static value=<_ast.Dict object at 0x7f8b14a352d0> name=None at 7f8b14a353d0> -> __attrs_140235323429904
                    __attrs_140235323429904 = _static_140235323429584

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235323431760
                    __default_140235323431760 = _DEFAULT_MARKER

                    # <Value u'action/render' (154:80)> -> __cache_140235323430224
                    __token = 8934
                    try:
                        __zt_tmp = __attrs_140235323429904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235323430224 = _static_140235435449424('path', u'action/render', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'action/render' (154:80)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b14a35950> -> __condition
                    __expression = __cache_140235323430224

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="submit" />')
                    else:
                        __content = __cache_140235323430224
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                                ')
                    ____index_140235323432080 -= 1
                    if (____index_140235323432080 > 0):
                        __append('')
                if (__backup_action_140235322111952 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140235322111952
                __append(u'\n                            </div>')
            __append(u'\n                        ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_field(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322634320
            __attrs_140235322634320 = _static_140235489934800
            __append(u'\n                                              ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322635792
            __attrs_140235322635792 = _static_140235489934800

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322636112
            __default_140235322636112 = _DEFAULT_MARKER

            # <Value u'widget/@@ploneform-render-widget' (100:81)> -> __cache_140235322637648
            __token = 5645
            try:
                __zt_tmp = __attrs_140235322635792
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235322637648 = _static_140235435449424('path', u'widget/@@ploneform-render-widget', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'widget/@@ploneform-render-widget' (100:81)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b14973b90> -> __condition
            __expression = __cache_140235322637648

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140235322637648
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'\n                                          ')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_titlelessform(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_formtop = econtext[u'__slot_formtop'].pop()
        except:
            __slot_formtop = None

        try:
            __slot_fields = econtext[u'__slot_fields'].pop()
        except:
            __slot_fields = None

        try:
            __slot_belowfields = econtext[u'__slot_belowfields'].pop()
        except:
            __slot_belowfields = None

        try:
            __slot_description = econtext[u'__slot_description'].pop()
        except:
            __slot_description = None

        try:
            __slot_actions = econtext[u'__slot_actions'].pop()
        except:
            __slot_actions = None

        try:
            __slot_formbottom = econtext[u'__slot_formbottom'].pop()
        except:
            __slot_formbottom = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373295760
            __attrs_140235373295760 = _static_140235489934800
            __append(u'\n\n                ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373295312
            __attrs_140235373295312 = _static_140235489934800
            __backup_status_140235322048464 = get('status', __marker)

            # <Value u'view/status' (17:43)> -> __value
            __token = 569
            try:
                __zt_tmp = __attrs_140235373295312
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/status', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['status'] = __value
            __backup_has_error_140235322029328 = get('has_error', __marker)

            # <Value u"python:view.widgets.errors or status == getattr(view, 'formErrorsMessage', None)" (18:45)> -> __value
            __token = 627
            try:
                __zt_tmp = __attrs_140235373295312
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"view.widgets.errors or status == getattr(view, 'formErrorsMessage', None)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['has_error'] = __value

            # <Value u'status' (18:139)> -> __condition
            __token = 721
            try:
                __zt_tmp = __attrs_140235373295312
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'status', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8b1b12af50> name=None at 7f8b14961550> -> __attrs_140235322131152
                __attrs_140235322131152 = _static_140235431391056

                # <Value u'has_error' (19:67)> -> __condition
                __token = 797
                try:
                    __zt_tmp = __attrs_140235322131152
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'has_error', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <dl ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dl class="portalMessage error" role="alert">\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322132112
                    __attrs_140235322132112 = _static_140235489934800
                    __previous_i18n_domain_140235322823312 = __i18n_domain
                    __i18n_domain = u'plone'

                    # <dt ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dt>')
                    __stream_140235322133648 = []
                    __append_140235322133648 = __stream_140235322133648.append
                    __append_140235322133648(u'\n                            Error\n                        ')
                    __msgid_140235322133648 = __re_whitespace(''.join(__stream_140235322133648)).strip()
                    if __msgid_140235322133648:
                        __append(translate(__msgid_140235322133648, mapping=None, default=__msgid_140235322133648, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</dt>')
                    __i18n_domain = __previous_i18n_domain_140235322823312
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322825936
                    __attrs_140235322825936 = _static_140235489934800

                    # <dd ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dd>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322825616
                    __default_140235322825616 = _DEFAULT_MARKER

                    # <Value u'status' (23:41)> -> __cache_140235322824592
                    __token = 994
                    try:
                        __zt_tmp = __attrs_140235322825936
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235322824592 = _static_140235435449424('path', u'status', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'status' (23:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b149a1110> -> __condition
                    __expression = __cache_140235322824592

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235322824592
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</dd>\n                    </dl>')
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8b149a1750> name=None at 7f8b149a1a50> -> __attrs_140235322825808
                __attrs_140235322825808 = _static_140235322824528

                # <Value u'not:has_error' (25:66)> -> __condition
                __token = 1097
                try:
                    __zt_tmp = __attrs_140235322825808
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('not', u'has_error', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <dl ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dl class="portalMessage info" role="status">\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235357505488
                    __attrs_140235357505488 = _static_140235489934800
                    __previous_i18n_domain_140235357507280 = __i18n_domain
                    __i18n_domain = u'plone'

                    # <dt ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dt>')
                    __stream_140235357505296 = []
                    __append_140235357505296 = __stream_140235357505296.append
                    __append_140235357505296(u'\n                            Info\n                        ')
                    __msgid_140235357505296 = __re_whitespace(''.join(__stream_140235357505296)).strip()
                    if __msgid_140235357505296:
                        __append(translate(__msgid_140235357505296, mapping=None, default=__msgid_140235357505296, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</dt>')
                    __i18n_domain = __previous_i18n_domain_140235357507280
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235357506128
                    __attrs_140235357506128 = _static_140235489934800

                    # <dd ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<dd>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235357506832
                    __default_140235357506832 = _DEFAULT_MARKER

                    # <Value u'status' (29:41)> -> __cache_140235357505552
                    __token = 1298
                    try:
                        __zt_tmp = __attrs_140235357506128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235357505552 = _static_140235435449424('path', u'status', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'status' (29:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b16ab4d50> -> __condition
                    __expression = __cache_140235357505552

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140235357505552
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</dd>\n                    </dl>')
                __append(u'\n                ')
            if (__backup_has_error_140235322029328 is __marker):
                del econtext['has_error']
            else:
                econtext['has_error'] = __backup_has_error_140235322029328
            if (__backup_status_140235322048464 is __marker):
                del econtext['status']
            else:
                econtext['status'] = __backup_status_140235322048464
            __append(u'\n\n                ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322133712
            __attrs_140235322133712 = _static_140235489934800
            __backup_errors_140235322045136 = get('errors', __marker)

            # <Value u'view/widgets/errors' (33:43)> -> __value
            __token = 1409
            try:
                __zt_tmp = __attrs_140235322133712
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/widgets/errors', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['errors'] = __value

            # <Value u'errors' (33:75)> -> __condition
            __token = 1441
            try:
                __zt_tmp = __attrs_140235322133712
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'errors', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:
                __append(u'\n                    ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235357506768
                __attrs_140235357506768 = _static_140235489934800
                __backup_error_140235322131984 = get('error', __marker)

                # <Value u'errors' (34:45)> -> __iterator
                __token = 1495
                try:
                    __zt_tmp = __attrs_140235357506768
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140235435449424('path', u'errors', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                (__iterator, ____index_140235357504144, ) = getitem('repeat')(u'error', __iterator)
                econtext['error'] = None
                for __item in __iterator:
                    econtext['error'] = __item
                    __append(u'\n                        ')

                    # <Static value=<_ast.Dict object at 0x7f8b149b0190> name=None at 7f8b149b0390> -> __attrs_140235322887120
                    __attrs_140235322887120 = _static_140235322884496

                    # <Value u'not:nocall:error/widget' (36:44)> -> __condition
                    __token = 1597
                    try:
                        __zt_tmp = __attrs_140235322887120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('not', u'nocall:error/widget', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div class="field error">')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322886352
                        __default_140235322886352 = _DEFAULT_MARKER

                        # <Value u'error/render' (37:52)> -> __cache_140235322887760
                        __token = 1674
                        try:
                            __zt_tmp = __attrs_140235322887120
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235322887760 = _static_140235435449424('path', u'error/render', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'error/render' (37:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b149b0150> -> __condition
                        __expression = __cache_140235322887760

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'\n                             Error\n                        ')
                        else:
                            __content = __cache_140235322887760
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</div>')
                    __append(u'\n                    ')
                    ____index_140235357504144 -= 1
                    if (____index_140235357504144 > 0):
                        __append('')
                if (__backup_error_140235322131984 is __marker):
                    del econtext['error']
                else:
                    econtext['error'] = __backup_error_140235322131984
                __append(u'\n                ')
            if (__backup_errors_140235322045136 is __marker):
                del econtext['errors']
            else:
                econtext['errors'] = __backup_errors_140235322045136
            __append(u'\n\n                ')
            if (__slot_description is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235357503632
                __attrs_140235357503632 = _static_140235489934800
                __append(u'\n                  ')

                # <Static value=<_ast.Dict object at 0x7f8b149b0510> name=None at 7f8b149b0790> -> __attrs_140235321892432
                __attrs_140235321892432 = _static_140235322885392
                __backup_description_140235373294608 = get('description', __marker)

                # <Value u'view/description | nothing' (45:46)> -> __value
                __token = 1971
                try:
                    __zt_tmp = __attrs_140235321892432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/description | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['description'] = __value

                # <Value u'description' (46:37)> -> __condition
                __token = 2036
                try:
                    __zt_tmp = __attrs_140235321892432
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p  class="discreet">')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322885328
                    __default_140235322885328 = _DEFAULT_MARKER

                    # <Value u'description' (47:45)> -> __cache_140235322887248
                    __token = 2094
                    try:
                        __zt_tmp = __attrs_140235321892432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235322887248 = _static_140235435449424('path', u'description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'description' (47:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b149b0650> -> __condition
                    __expression = __cache_140235322887248

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                          Description\n                  ')
                    else:
                        __content = __cache_140235322887248
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</p>')
                if (__backup_description_140235373294608 is __marker):
                    del econtext['description']
                else:
                    econtext['description'] = __backup_description_140235373294608
                __append(u'\n                ')
            else:
                __slot_description(__stream, econtext.copy(), rcontext)
            __append(u'\n\n                ')

            # <Static value=<_ast.Dict object at 0x7f8b179c3190> name=None at 7f8b16ab4890> -> __attrs_140235424615440
            __attrs_140235424615440 = _static_140235373293968
            __backup_groups_140235373294800 = get('groups', __marker)

            # <Value u'view/groups | nothing' (54:41)> -> __value
            __token = 2435
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/groups | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['groups'] = __value
            __backup_form_name_140235373297360 = get('form_name', __marker)

            # <Value u'view/form_name | nothing' (55:43)> -> __value
            __token = 2501
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/form_name | nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['form_name'] = __value
            __backup_form_class_140235322823184 = get('form_class', __marker)

            # <Value u'view/css_class | string:' (56:43)> -> __value
            __token = 2571
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/css_class | string:', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['form_class'] = __value
            __backup_default_fieldset_label_140235322133264 = get('default_fieldset_label', __marker)

            # <Value u'view/default_fieldset_label | form_name' (57:54)> -> __value
            __token = 2653
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/default_fieldset_label | form_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['default_fieldset_label'] = __value
            __backup_enable_form_tabbing_140235322045968 = get('enable_form_tabbing', __marker)

            # <Value u'view/enable_form_tabbing | python:True' (58:50)> -> __value
            __token = 2747
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/enable_form_tabbing | python:True', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['enable_form_tabbing'] = __value
            __backup_enable_unload_protection_140235373294928 = get('enable_unload_protection', __marker)

            # <Value u'view/enable_unload_protection|python:True' (59:54)> -> __value
            __token = 2845
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'view/enable_unload_protection|python:True', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['enable_unload_protection'] = __value
            __backup_unload_protection_140235322131024 = get('unload_protection', __marker)

            # <Value u"python:enable_unload_protection and 'pat-formunloadalert'" (60:46)> -> __value
            __token = 2939
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"enable_unload_protection and 'pat-formunloadalert'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['unload_protection'] = __value
            __backup_has_groups_140235322823888 = get('has_groups', __marker)

            # <Value u'python:bool(groups)' (61:38)> -> __value
            __token = 3042
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u'bool(groups)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['has_groups'] = __value
            __backup_form_tabbing_140235322885904 = get('form_tabbing', __marker)

            # <Value u"python:(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autotoc' or ''" (62:39)> -> __value
            __token = 3109
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"(has_groups and enable_form_tabbing) and 'enableFormTabbing pat-autotoc' or ''", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['form_tabbing'] = __value
            __backup_show_default_label_140235424615504 = get('show_default_label', __marker)

            # <Value u'python:has_groups and default_fieldset_label and len(view.widgets)' (63:44)> -> __value
            __token = 3248
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u'has_groups and default_fieldset_label and len(view.widgets)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['show_default_label'] = __value
            __backup_form_view_name_raw_140235424613648 = get('form_view_name_raw', __marker)

            # <Value u"python:view.__name__ or request.getURL().split('/')[-1]" (64:43)> -> __value
            __token = 3368
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"view.__name__ or request.getURL().split('/')[-1]", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['form_view_name_raw'] = __value
            __backup_form_view_name_140235424615952 = get('form_view_name', __marker)

            # <Value u"python:'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('++') if x])" (65:38)> -> __value
            __token = 3473
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"'-'.join(['view', 'name'] + [x for x in form_view_name_raw.split('++') if x])", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['form_view_name'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form data-pat-autotoc="levels: legend; section: fieldset; className: autotabs"')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321891856
            __default_140235321891856 = _DEFAULT_MARKER

            # <Substitution u"python:'rowlike {0} {1} {2} kssattr-formname-{3} {4}'.format(unload_protection, form_tabbing, form_class, form_view_name_raw, form_view_name)" (69:42)> -> __attr_class
            __token = 3781
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140235435449424('python', u"'rowlike {0} {1} {2} kssattr-formname-{3} {4}'.format(unload_protection, form_tabbing, form_class, form_view_name_raw, form_view_name)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', u'rowlike enableUnloadProtection', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321892304
            __default_140235321892304 = _DEFAULT_MARKER

            # <Substitution u'view/action|request/getURL' (67:45)> -> __attr_action
            __token = 3651
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140235435449424('path', u'view/action|request/getURL', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', u'.', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321890448
            __default_140235321890448 = _DEFAULT_MARKER

            # <Substitution u'view/method|string:post' (72:40)> -> __attr_method
            __token = 4070
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_method = _static_140235435449424('path', u'view/method|string:post', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_method = __quote(__attr_method, '"', '&quot;', u'post', _DEFAULT_MARKER)
            if (__attr_method is not None):
                __append((u' method="%s"' % __attr_method))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321889424
            __default_140235321889424 = _DEFAULT_MARKER

            # <Substitution u'view/enctype' (68:45)> -> __attr_enctype
            __token = 3724
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_enctype = _static_140235435449424('path', u'view/enctype', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_enctype = __quote(__attr_enctype, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_enctype is not None):
                __append((u' enctype="%s"' % __attr_enctype))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424612560
            __default_140235424612560 = _DEFAULT_MARKER

            # <Substitution u'view/id' (70:38)> -> __attr_id
            __token = 3964
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140235435449424('path', u'view/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424614544
            __default_140235424614544 = _DEFAULT_MARKER

            # <Substitution u'form_name' (71:39)> -> __attr_name
            __token = 4015
            try:
                __zt_tmp = __attrs_140235424615440
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140235435449424('path', u'form_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((u' name="%s"' % __attr_name))
            __append(u'>\n\n                    ')
            if (__slot_formtop is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322110864
                __attrs_140235322110864 = _static_140235489934800
            else:
                __slot_formtop(__stream, econtext.copy(), rcontext)
            __append(u'\n\n                    ')
            if (__slot_fields is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322113680
                __attrs_140235322113680 = _static_140235489934800
                __append(u'\n                      ')

                # <Static value=<_ast.Dict object at 0x7f8b148f3190> name=None at 7f8b148f35d0> -> __attrs_140235322111056
                __attrs_140235322111056 = _static_140235322110352
                __backup_current_fieldset_140235322113168 = get('current_fieldset', __marker)

                # <Value u'request/fieldset | python:None' (79:55)> -> __value
                __token = 4362
                try:
                    __zt_tmp = __attrs_140235322111056
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'request/fieldset | python:None', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['current_fieldset'] = __value

                # <Value u'python:has_groups and enable_form_tabbing and current_fieldset is not None' (80:41)> -> __condition
                __token = 4435
                try:
                    __zt_tmp = __attrs_140235322111056
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('python', u'has_groups and enable_form_tabbing and current_fieldset is not None', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden" name="fieldset"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322113616
                    __default_140235322113616 = _DEFAULT_MARKER

                    # <Substitution u'current_fieldset' (81:48)> -> __attr_value
                    __token = 4559
                    try:
                        __zt_tmp = __attrs_140235322111056
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140235435449424('path', u'current_fieldset', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />')
                if (__backup_current_fieldset_140235322113168 is __marker):
                    del econtext['current_fieldset']
                else:
                    econtext['current_fieldset'] = __backup_current_fieldset_140235322113168
                __append(u'\n\n                      <!-- Default fieldset -->\n                      ')
                __token = None
                render_fields(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n                    ')
            else:
                __slot_fields(__stream, econtext.copy(), rcontext)
            __append(u'\n\n                    ')
            if (__slot_belowfields is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321917840
                __attrs_140235321917840 = _static_140235489934800
            else:
                __slot_belowfields(__stream, econtext.copy(), rcontext)
            __append(u'\n\n                    ')
            if (__slot_actions is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322691792
                __attrs_140235322691792 = _static_140235489934800
                __append(u'\n                        ')
                __token = None
                render_actions(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n                    ')
            else:
                __slot_actions(__stream, econtext.copy(), rcontext)
            __append(u'\n\n                    ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322489168
            __attrs_140235322489168 = _static_140235489934800

            # <Value u'view/enableCSRFProtection|nothing' (160:46)> -> __condition
            __token = 9161
            try:
                __zt_tmp = __attrs_140235322489168
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('path', u'view/enableCSRFProtection|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322488528
                __default_140235322488528 = _DEFAULT_MARKER

                # <Value u'context/@@authenticator/authenticator' (161:45)> -> __cache_140235322112208
                __token = 9241
                try:
                    __zt_tmp = __attrs_140235322489168
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235322112208 = _static_140235435449424('path', u'context/@@authenticator/authenticator', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'context/@@authenticator/authenticator' (161:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1801c310> -> __condition
                __expression = __cache_140235322112208

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140235322112208
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append(u'\n                    ')
            if (__slot_formbottom is None):

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322488912
                __attrs_140235322488912 = _static_140235489934800
            else:
                __slot_formbottom(__stream, econtext.copy(), rcontext)
            __append(u'\n\n                </form>')
            if (__backup_form_view_name_140235424615952 is __marker):
                del econtext['form_view_name']
            else:
                econtext['form_view_name'] = __backup_form_view_name_140235424615952
            if (__backup_form_view_name_raw_140235424613648 is __marker):
                del econtext['form_view_name_raw']
            else:
                econtext['form_view_name_raw'] = __backup_form_view_name_raw_140235424613648
            if (__backup_show_default_label_140235424615504 is __marker):
                del econtext['show_default_label']
            else:
                econtext['show_default_label'] = __backup_show_default_label_140235424615504
            if (__backup_form_tabbing_140235322885904 is __marker):
                del econtext['form_tabbing']
            else:
                econtext['form_tabbing'] = __backup_form_tabbing_140235322885904
            if (__backup_has_groups_140235322823888 is __marker):
                del econtext['has_groups']
            else:
                econtext['has_groups'] = __backup_has_groups_140235322823888
            if (__backup_unload_protection_140235322131024 is __marker):
                del econtext['unload_protection']
            else:
                econtext['unload_protection'] = __backup_unload_protection_140235322131024
            if (__backup_enable_unload_protection_140235373294928 is __marker):
                del econtext['enable_unload_protection']
            else:
                econtext['enable_unload_protection'] = __backup_enable_unload_protection_140235373294928
            if (__backup_enable_form_tabbing_140235322045968 is __marker):
                del econtext['enable_form_tabbing']
            else:
                econtext['enable_form_tabbing'] = __backup_enable_form_tabbing_140235322045968
            if (__backup_default_fieldset_label_140235322133264 is __marker):
                del econtext['default_fieldset_label']
            else:
                econtext['default_fieldset_label'] = __backup_default_fieldset_label_140235322133264
            if (__backup_form_class_140235322823184 is __marker):
                del econtext['form_class']
            else:
                econtext['form_class'] = __backup_form_class_140235322823184
            if (__backup_form_name_140235373297360 is __marker):
                del econtext['form_name']
            else:
                econtext['form_name'] = __backup_form_name_140235373297360
            if (__backup_groups_140235373294800 is __marker):
                del econtext['groups']
            else:
                econtext['groups'] = __backup_groups_140235373294800
            __append(u'\n            ')
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

            # <Static value=<_ast.Dict object at 0x7f8b1496be50> name=None at 7f8b148c1710> -> __attrs_140235322426512
            __attrs_140235322426512 = _static_140235322605136
            __previous_i18n_domain_140235322834640 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml">\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322047120
            __attrs_140235322047120 = _static_140235489934800

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n        ')
            __token = None
            render_form(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n    </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140235322834640
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_widget_rendering': render_widget_rendering, u'render_form': render_form, u'render_fields': render_fields, u'render_actions': render_actions, u'render_field': render_field, u'render_titlelessform': render_titlelessform, 'render': render, }
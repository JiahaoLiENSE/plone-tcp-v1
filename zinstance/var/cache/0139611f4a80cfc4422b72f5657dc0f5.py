# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.z3cform-3.2.4-py2.7.egg/plone/app/z3cform/templates/widget.pt'

__tokens = {89: (u'nocall:context', 4, 22), 126: (u" python:widget.mode == 'hidden", 5, 21), 178: (u'r widget/err', 6, 19), 218: (u"ss python:error and ' error' or", 7, 24), 278: (u"ues python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', ", 8, 24), 372: (u"lass python: (widget.value in empty_values) and ' empty' ", 9, 22), 457: (u'lass  widget/wrapper_css_class|n', 10, 21), 521: (u'_class string:kssattr-fieldname-${widge', 11, 24), 646: (u'string:field pat-inlinevalidation ${fieldname_class}${error_class}${empty_class} ${wrapper_css_class}', 13, 25), 782: (u' widget/nam', 14, 33), 816: (u'd string:formfield-${widget/i', 15, 20), 950: (u'python: not hidden and widget.label', 18, 23), 916: (u'widget/id', 17, 28), 1033: (u'widget/label', 19, 45), 1149: (u"python:widget.required and widget.mode == 'input'", 22, 29), 1336: (u"python: getattr(widget, 'description', widget.field.description)", 26, 36), 1507: (u'python:description and not hidden', 29, 27), 1467: (u'description', 28, 35), 1666: (u'error/render|nothing', 35, 32), 1761: (u'widget/render', 39, 46)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140235489934800 = {}
_static_140235322046096 = {u'class': u'fieldErrorBox', }
_static_140235323208016 = {u'data-fieldname': u'widget/name', u'class': u'string:field pat-inlinevalidation ${fieldname_class}${error_class}${empty_class} ${wrapper_css_class}', u'data-pat-inlinevalidation': u'{"type":"z3c.form"}', u'id': u'string:formfield-${widget/id}', }
_static_140235322710096 = {u'class': u'required horizontal', u'title': u'Required', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235435449424 = __compile_zt_expr
_static_140235322047824 = {u'type': u'text', }
_static_140235322708944 = {u'class': u'formHelp', }
_static_140235321890384 = {u'class': u'horizontal', u'for': u'', }

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

    def render_widget_wrapper(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_widget = econtext[u'__slot_widget'].pop()
        except:
            __slot_widget = None

        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Static value=<_ast.Dict object at 0x7f8b149ff150> name=None at 7f8b149ff890> -> __attrs_140235321890768
            __attrs_140235321890768 = _static_140235323208016
            __backup_widget_140235322045136 = get('widget', __marker)

            # <Value u'nocall:context' (4:22)> -> __value
            __token = 89
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('nocall', u'context', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['widget'] = __value
            __backup_hidden_140235320016848 = get('hidden', __marker)

            # <Value u"python:widget.mode == 'hidden'" (5:21)> -> __value
            __token = 126
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"widget.mode == 'hidden'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['hidden'] = __value
            __backup_error_140235321015824 = get('error', __marker)

            # <Value u'widget/error' (6:19)> -> __value
            __token = 178
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'widget/error', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_error_class_140235320935504 = get('error_class', __marker)

            # <Value u"python:error and ' error' or ''" (7:24)> -> __value
            __token = 218
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u"error and ' error' or ''", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['error_class'] = __value
            __backup_empty_values_140235319853584 = get('empty_values', __marker)

            # <Value u"python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))" (8:24)> -> __value
            __token = 278
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u" (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['empty_values'] = __value
            __backup_empty_class_140235319678096 = get('empty_class', __marker)

            # <Value u"python: (widget.value in empty_values) and ' empty' or ''" (9:22)> -> __value
            __token = 372
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('python', u" (widget.value in empty_values) and ' empty' or ''", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['empty_class'] = __value
            __backup_wrapper_css_class_140235319702544 = get('wrapper_css_class', __marker)

            # <Value u'widget/wrapper_css_class|nothing' (10:21)> -> __value
            __token = 457
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('path', u'widget/wrapper_css_class|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['wrapper_css_class'] = __value
            __backup_fieldname_class_140235319855632 = get('fieldname_class', __marker)

            # <Value u'string:kssattr-fieldname-${widget/name}' (11:24)> -> __value
            __token = 521
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140235435449424('string', u'kssattr-fieldname-${widget/name}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            econtext['fieldname_class'] = __value
            __previous_i18n_domain_140235321890256 = __i18n_domain
            __i18n_domain = u'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div data-pat-inlinevalidation=\'{"type":"z3c.form"}\'')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235323209040
            __default_140235323209040 = _DEFAULT_MARKER

            # <Substitution u'string:field pat-inlinevalidation ${fieldname_class}${error_class}${empty_class} ${wrapper_css_class}' (13:25)> -> __attr_class
            __token = 646
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140235435449424('string', u'field pat-inlinevalidation ${fieldname_class}${error_class}${empty_class} ${wrapper_css_class}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((u' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235323211024
            __default_140235323211024 = _DEFAULT_MARKER

            # <Substitution u'widget/name' (14:33)> -> __attr_data_fieldname
            __token = 782
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_fieldname = _static_140235435449424('path', u'widget/name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_data_fieldname = __quote(__attr_data_fieldname, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_data_fieldname is not None):
                __append((u' data-fieldname="%s"' % __attr_data_fieldname))

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235323209808
            __default_140235323209808 = _DEFAULT_MARKER

            # <Substitution u'string:formfield-${widget/id}' (15:20)> -> __attr_id
            __token = 816
            try:
                __zt_tmp = __attrs_140235321890768
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140235435449424('string', u'formfield-${widget/id}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((u' id="%s"' % __attr_id))
            __append(u'>\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b148bd650> name=None at 7f8b148bd310> -> __attrs_140235322797968
            __attrs_140235322797968 = _static_140235321890384

            # <Value u'python: not hidden and widget.label' (18:23)> -> __condition
            __token = 950
            try:
                __zt_tmp = __attrs_140235322797968
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140235435449424('python', u' not hidden and widget.label', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            if __condition:

                # <label ... (0:0)
                # --------------------------------------------------------
                __append(u'<label')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321891280
                __default_140235321891280 = _DEFAULT_MARKER

                # <Substitution u'widget/id' (17:28)> -> __attr_for
                __token = 916
                try:
                    __zt_tmp = __attrs_140235322797968
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_140235435449424('path', u'widget/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((u' for="%s"' % __attr_for))
                __append(u' class="horizontal">\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322709392
                __attrs_140235322709392 = _static_140235489934800

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322709328
                __default_140235322709328 = _DEFAULT_MARKER

                # <Value u'widget/label' (19:45)> -> __cache_140235322710992
                __token = 1033
                try:
                    __zt_tmp = __attrs_140235322709392
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235322710992 = _static_140235435449424('path', u'widget/label', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'widget/label' (19:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b14985990> -> __condition
                __expression = __cache_140235322710992

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>label</span>')
                else:
                    __content = __cache_140235322710992
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b14985850> name=None at 7f8b14985910> -> __attrs_140235322709264
                __attrs_140235322709264 = _static_140235322710096

                # <Value u"python:widget.required and widget.mode == 'input'" (22:29)> -> __condition
                __token = 1149
                try:
                    __zt_tmp = __attrs_140235322709264
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('python', u"widget.required and widget.mode == 'input'", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="required horizontal"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322709520
                    __default_140235322709520 = _DEFAULT_MARKER

                    # <Translate msgid=u'title_required' node=<_ast.Str object at 0x7f8b149854d0> at 7f8b14985650> -> __attr_title
                    __attr_title = u'Required'
                    __attr_title = translate(u'title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u'>&nbsp;</span>')
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b149853d0> name=None at 7f8b14985e10> -> __attrs_140235322453264
                __attrs_140235322453264 = _static_140235322708944
                __backup_description_140235322665424 = get('description', __marker)

                # <Value u"python: getattr(widget, 'description', widget.field.description)" (26:36)> -> __value
                __token = 1336
                try:
                    __zt_tmp = __attrs_140235322453264
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u" getattr(widget, 'description', widget.field.description)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['description'] = __value

                # <Value u'python:description and not hidden' (29:27)> -> __condition
                __token = 1507
                try:
                    __zt_tmp = __attrs_140235322453264
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('python', u'description and not hidden', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span class="formHelp" >')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322708752
                    __default_140235322708752 = _DEFAULT_MARKER

                    # <Value u'description' (28:35)> -> __cache_140235322708624
                    __token = 1467
                    try:
                        __zt_tmp = __attrs_140235322453264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235322708624 = _static_140235435449424('path', u'description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'description' (28:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b14985d50> -> __condition
                    __expression = __cache_140235322708624

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'field description\n        ')
                    else:
                        __content = __cache_140235322708624
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</span>')
                if (__backup_description_140235322665424 is __marker):
                    del econtext['description']
                else:
                    econtext['description'] = __backup_description_140235322665424
                __append(u'\n    </label>')
            __append(u'\n\n    ')

            # <Static value=<_ast.Dict object at 0x7f8b148e3690> name=None at 7f8b148e36d0> -> __attrs_140235322046288
            __attrs_140235322046288 = _static_140235322046096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="fieldErrorBox">')

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322048080
            __default_140235322048080 = _DEFAULT_MARKER

            # <Value u'error/render|nothing' (35:32)> -> __cache_140235322797264
            __token = 1666
            try:
                __zt_tmp = __attrs_140235322046288
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140235322797264 = _static_140235435449424('path', u'error/render|nothing', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

            # <BinOp left=<Value u'error/render|nothing' (35:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148e3210> -> __condition
            __expression = __cache_140235322797264

            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append(u'\n        Error\n    ')
            else:
                __content = __cache_140235322797264
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append(u'</div>\n\n    ')
            if (__slot_widget is None):

                # <Static value=<_ast.Dict object at 0x7f8b148e3d50> name=None at 7f8b148e3850> -> __attrs_140235322047568
                __attrs_140235322047568 = _static_140235322047824

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322046608
                __default_140235322046608 = _DEFAULT_MARKER

                # <Value u'widget/render' (39:46)> -> __cache_140235322044496
                __token = 1761
                try:
                    __zt_tmp = __attrs_140235322047568
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140235322044496 = _static_140235435449424('path', u'widget/render', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                # <BinOp left=<Value u'widget/render' (39:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148e3d90> -> __condition
                __expression = __cache_140235322044496

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="text" />')
                else:
                    __content = __cache_140235322044496
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            else:
                __slot_widget(__stream, econtext.copy(), rcontext)
            __append(u'\n</div>')
            __i18n_domain = __previous_i18n_domain_140235321890256
            if (__backup_fieldname_class_140235319855632 is __marker):
                del econtext['fieldname_class']
            else:
                econtext['fieldname_class'] = __backup_fieldname_class_140235319855632
            if (__backup_wrapper_css_class_140235319702544 is __marker):
                del econtext['wrapper_css_class']
            else:
                econtext['wrapper_css_class'] = __backup_wrapper_css_class_140235319702544
            if (__backup_empty_class_140235319678096 is __marker):
                del econtext['empty_class']
            else:
                econtext['empty_class'] = __backup_empty_class_140235319678096
            if (__backup_empty_values_140235319853584 is __marker):
                del econtext['empty_values']
            else:
                econtext['empty_values'] = __backup_empty_values_140235319853584
            if (__backup_error_class_140235320935504 is __marker):
                del econtext['error_class']
            else:
                econtext['error_class'] = __backup_error_class_140235320935504
            if (__backup_error_140235321015824 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_140235321015824
            if (__backup_hidden_140235320016848 is __marker):
                del econtext['hidden']
            else:
                econtext['hidden'] = __backup_hidden_140235320016848
            if (__backup_widget_140235322045136 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140235322045136
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
            __token = None
            render_widget_wrapper(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_widget_wrapper': render_widget_wrapper, 'render': render, }
# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.contenttypes-2.2.3-py2.7.egg/plone/app/contenttypes/browser/templates/document.pt'

__tokens = {451: (u'context/table_of_contents|nothing', 12, 36), 543: (u'context/text | nothing', 14, 21), 678: (u"python: toc and 'pat-autotoc' or ''", 16, 28), 596: (u'python:context.text.output_relative_to(view.context)', 15, 29), 251: (u'context/main_template/macros/master', 6, 21), 251: (u'context/main_template/macros/master', 6, 21)}

from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386072522896 = {u'id': u'parent-fieldname-text', u'class': u"python: toc and 'pat-autotoc' or ''", }
_static_140386186297040 = __C2ZContextWrapper
_static_140386073255440 = u'master'
_static_140386186296528 = __compile_zt_expr
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078062032
            __attrs_140386078062032 = _static_140386247937936
            __backup_toc_140386071506768 = get('toc', __marker)

            # <Value u'context/table_of_contents|nothing' (12:36)> -> __value
            __token = 451
            try:
                __zt_tmp = __attrs_140386078062032
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'context/table_of_contents|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['toc'] = __value
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x7fae2dfbf090> name=None at 7fae2dfbfa10> -> __attrs_140386072526160
            __attrs_140386072526160 = _static_140386072522896

            # <Value u'context/text | nothing' (14:21)> -> __condition
            __token = 543
            try:
                __zt_tmp = __attrs_140386072526160
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'context/text | nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="parent-fieldname-text"')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072525840
                __default_140386072525840 = _DEFAULT_MARKER

                # <Substitution u"python: toc and 'pat-autotoc' or ''" (16:28)> -> __attr_class
                __token = 678
                try:
                    __zt_tmp = __attrs_140386072526160
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140386186296528('python', u" toc and 'pat-autotoc' or ''", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((u' class="%s"' % __attr_class))
                __append(u'>')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072524496
                __default_140386072524496 = _DEFAULT_MARKER

                # <Value u'python:context.text.output_relative_to(view.context)' (15:29)> -> __cache_140386072525008
                __token = 596
                try:
                    __zt_tmp = __attrs_140386072526160
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140386072525008 = _static_140386186296528('python', u'context.text.output_relative_to(view.context)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                # <BinOp left=<Value u'python:context.text.output_relative_to(view.context)' (15:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e507c10> -> __condition
                __expression = __cache_140386072525008

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140386072525008
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append(u'</div>')
            __append(u'\n')
            if (__backup_toc_140386071506768 is __marker):
                del econtext['toc']
            else:
                econtext['toc'] = __backup_toc_140386071506768
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386073253456
            __attrs_140386073253456 = _static_140386247937936
            __previous_i18n_domain_140386073252880 = __i18n_domain
            __i18n_domain = u'plone'
            __backup_macroname_140386071998944 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fae2e071e10> name=None at 7fae2e071890> -> __value
            __value = _static_140386073255440
            econtext['macroname'] = __value

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078064272
                __attrs_140386078064272 = _static_140386247937936
                __append(u'\n')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append(u'\n')
            _slots = econtext[u'__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value u'context/main_template/macros/master' (6:21)> -> __macro
            __token = 251
            try:
                __zt_tmp = __attrs_140386073253456
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140386186296528('path', u'context/main_template/macros/master', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __token = 251
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140386071998944 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140386071998944
            __i18n_domain = __previous_i18n_domain_140386073252880
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_content_core': render_content_core, 'render': render, }
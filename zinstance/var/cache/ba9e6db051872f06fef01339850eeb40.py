# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/plone.app.i18n-3.0.6-py2.7.egg/plone/app/i18n/locales/browser/languageselector.pt'

__tokens = {29: (u'view/available', 1, 29), 105: (u'view/showFlags', 3, 26), 146: (u' view/language', 4, 25), 186: (u'l context/@@plone_context_state/view_u', 5, 23), 252: (u'rl view/portal_', 6, 24), 305: (u'languages', 7, 31), 342: (u'lang/code', 8, 25), 381: (u' lang/selecte', 9, 28), 425: (u's string:language-${cod', 10, 28), 477: (u"nt python: selected and 'currentLanguage ' or", 11, 25), 558: (u'string:${current}${codeclass}', 12, 30), 637: (u'lang/flag|nothing', 14, 28), 683: (u' lang/native|lang/nam', 15, 27), 737: (u'g python:showFlags and fl', 16, 30), 799: (u'string:${here_url}?set_language=${code}', 17, 32), 872: (u' nam', 18, 32), 913: (u'showflag', 19, 34), 1127: (u' nam', 24, 40), 1058: (u'string:${portal_url}${flag}', 23, 41), 1175: (u'e na', 25, 41), 1247: (u'not: showflag', 27, 37), 1297: (u'name', 28, 35)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386069898640 = {u'id': u'portal-languageselector', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386079221712 = {u'class': u'string:${current}${codeclass}', }
_static_140386186296528 = __compile_zt_expr
_static_140386071167632 = {u'href': u'', u'title': u'name', }
_static_140386071754896 = {u'width': u'14', u'alt': u'', u'src': u'string:${portal_url}${flag}', u'title': u'name', u'height': u'11', }
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069899536
            __attrs_140386069899536 = _static_140386247937936

            # <Value u'view/available' (1:29)> -> __condition
            __token = 29
            try:
                __zt_tmp = __attrs_140386069899536
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'view/available', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __append(u'\n')

                # <Static value=<_ast.Dict object at 0x7fae2dd3e590> name=None at 7fae2dd3e5d0> -> __attrs_140386069898576
                __attrs_140386069898576 = _static_140386069898640
                __backup_showFlags_140386070708752 = get('showFlags', __marker)

                # <Value u'view/showFlags' (3:26)> -> __value
                __token = 105
                try:
                    __zt_tmp = __attrs_140386069898576
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/showFlags', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['showFlags'] = __value
                __backup_languages_140386078098256 = get('languages', __marker)

                # <Value u'view/languages' (4:25)> -> __value
                __token = 146
                try:
                    __zt_tmp = __attrs_140386069898576
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/languages', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['languages'] = __value
                __backup_here_url_140386078077200 = get('here_url', __marker)

                # <Value u'context/@@plone_context_state/view_url' (5:23)> -> __value
                __token = 186
                try:
                    __zt_tmp = __attrs_140386069898576
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'context/@@plone_context_state/view_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['here_url'] = __value
                __backup_portal_url_140386079147152 = get('portal_url', __marker)

                # <Value u'view/portal_url' (6:24)> -> __value
                __token = 252
                try:
                    __zt_tmp = __attrs_140386069898576
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/portal_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['portal_url'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul id="portal-languageselector">\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079223568
                __attrs_140386079223568 = _static_140386247937936
                __backup_lang_140386078077968 = get('lang', __marker)

                # <Value u'languages' (7:31)> -> __iterator
                __token = 305
                try:
                    __zt_tmp = __attrs_140386079223568
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'languages', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386079219792, ) = getitem('repeat')(u'lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item
                    __append(u'\n    ')

                    # <Static value=<_ast.Dict object at 0x7fae2e6227d0> name=None at 7fae2e622d10> -> __attrs_140386079222160
                    __attrs_140386079222160 = _static_140386079221712
                    __backup_code_140386072526736 = get('code', __marker)

                    # <Value u'lang/code' (8:25)> -> __value
                    __token = 342
                    try:
                        __zt_tmp = __attrs_140386079222160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'lang/code', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['code'] = __value
                    __backup_selected_140386078152912 = get('selected', __marker)

                    # <Value u'lang/selected' (9:28)> -> __value
                    __token = 381
                    try:
                        __zt_tmp = __attrs_140386079222160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'lang/selected', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __backup_codeclass_140386079219920 = get('codeclass', __marker)

                    # <Value u'string:language-${code}' (10:28)> -> __value
                    __token = 425
                    try:
                        __zt_tmp = __attrs_140386079222160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('string', u'language-${code}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['codeclass'] = __value
                    __backup_current_140386079220752 = get('current', __marker)

                    # <Value u"python: selected and 'currentLanguage ' or ''" (11:25)> -> __value
                    __token = 477
                    try:
                        __zt_tmp = __attrs_140386079222160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u" selected and 'currentLanguage ' or ''", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['current'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079220624
                    __default_140386079220624 = _DEFAULT_MARKER

                    # <Substitution u'string:${current}${codeclass}' (12:30)> -> __attr_class
                    __token = 558
                    try:
                        __zt_tmp = __attrs_140386079222160
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140386186296528('string', u'${current}${codeclass}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((u' class="%s"' % __attr_class))
                    __append(u'>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2de74290> name=None at 7fae2de74950> -> __attrs_140386071169296
                    __attrs_140386071169296 = _static_140386071167632
                    __backup_flag_140386079220368 = get('flag', __marker)

                    # <Value u'lang/flag|nothing' (14:28)> -> __value
                    __token = 637
                    try:
                        __zt_tmp = __attrs_140386071169296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'lang/flag|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['flag'] = __value
                    __backup_name_140386135460880 = get('name', __marker)

                    # <Value u'lang/native|lang/name' (15:27)> -> __value
                    __token = 683
                    try:
                        __zt_tmp = __attrs_140386071169296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'lang/native|lang/name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['name'] = __value
                    __backup_showflag_140386071169680 = get('showflag', __marker)

                    # <Value u'python:showFlags and flag' (16:30)> -> __value
                    __token = 737
                    try:
                        __zt_tmp = __attrs_140386071169296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u'showFlags and flag', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['showflag'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<a')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071168528
                    __default_140386071168528 = _DEFAULT_MARKER

                    # <Substitution u'string:${here_url}?set_language=${code}' (17:32)> -> __attr_href
                    __token = 799
                    try:
                        __zt_tmp = __attrs_140386071169296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('string', u'${here_url}?set_language=${code}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071170576
                    __default_140386071170576 = _DEFAULT_MARKER

                    # <Substitution u'name' (18:32)> -> __attr_title
                    __token = 872
                    try:
                        __zt_tmp = __attrs_140386071169296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140386186296528('path', u'name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((u' title="%s"' % __attr_title))
                    __append(u' >')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071756368
                    __attrs_140386071756368 = _static_140386247937936

                    # <Value u'showflag' (19:34)> -> __condition
                    __token = 913
                    try:
                        __zt_tmp = __attrs_140386071756368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'showflag', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n                ')

                        # <Static value=<_ast.Dict object at 0x7fae2df03890> name=None at 7fae2df03ad0> -> __attrs_140386072523664
                        __attrs_140386072523664 = _static_140386071754896

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<img width="14" height="11"')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071755024
                        __default_140386071755024 = _DEFAULT_MARKER

                        # <Substitution u'name' (24:40)> -> __attr_alt
                        __token = 1127
                        try:
                            __zt_tmp = __attrs_140386072523664
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_140386186296528('path', u'name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((u' alt="%s"' % __attr_alt))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071756432
                        __default_140386071756432 = _DEFAULT_MARKER

                        # <Substitution u'string:${portal_url}${flag}' (23:41)> -> __attr_src
                        __token = 1058
                        try:
                            __zt_tmp = __attrs_140386072523664
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_140386186296528('string', u'${portal_url}${flag}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((u' src="%s"' % __attr_src))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071754832
                        __default_140386071754832 = _DEFAULT_MARKER

                        # <Substitution u'name' (25:41)> -> __attr_title
                        __token = 1175
                        try:
                            __zt_tmp = __attrs_140386072523664
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140386186296528('path', u'name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((u' title="%s"' % __attr_title))
                        __append(u' />\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072525712
                    __attrs_140386072525712 = _static_140386247937936

                    # <Value u'not: showflag' (27:37)> -> __condition
                    __token = 1247
                    try:
                        __zt_tmp = __attrs_140386072525712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('not', u' showflag', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072526288
                        __default_140386072526288 = _DEFAULT_MARKER

                        # <Value u'name' (28:35)> -> __cache_140386072525328
                        __token = 1297
                        try:
                            __zt_tmp = __attrs_140386072525712
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386072525328 = _static_140386186296528('path', u'name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'name' (28:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dfbfd90> -> __condition
                        __expression = __cache_140386072525328

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'language name')
                        else:
                            __content = __cache_140386072525328
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append(u'</a>')
                    if (__backup_showflag_140386071169680 is __marker):
                        del econtext['showflag']
                    else:
                        econtext['showflag'] = __backup_showflag_140386071169680
                    if (__backup_name_140386135460880 is __marker):
                        del econtext['name']
                    else:
                        econtext['name'] = __backup_name_140386135460880
                    if (__backup_flag_140386079220368 is __marker):
                        del econtext['flag']
                    else:
                        econtext['flag'] = __backup_flag_140386079220368
                    __append(u'\n    </li>')
                    if (__backup_current_140386079220752 is __marker):
                        del econtext['current']
                    else:
                        econtext['current'] = __backup_current_140386079220752
                    if (__backup_codeclass_140386079219920 is __marker):
                        del econtext['codeclass']
                    else:
                        econtext['codeclass'] = __backup_codeclass_140386079219920
                    if (__backup_selected_140386078152912 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140386078152912
                    if (__backup_code_140386072526736 is __marker):
                        del econtext['code']
                    else:
                        econtext['code'] = __backup_code_140386072526736
                    __append(u'\n    ')
                    ____index_140386079219792 -= 1
                    if (____index_140386079219792 > 0):
                        __append('')
                if (__backup_lang_140386078077968 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_140386078077968
                __append(u'\n</ul>')
                if (__backup_portal_url_140386079147152 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_140386079147152
                if (__backup_here_url_140386078077200 is __marker):
                    del econtext['here_url']
                else:
                    econtext['here_url'] = __backup_here_url_140386078077200
                if (__backup_languages_140386078098256 is __marker):
                    del econtext['languages']
                else:
                    econtext['languages'] = __backup_languages_140386078098256
                if (__backup_showFlags_140386070708752 is __marker):
                    del econtext['showFlags']
                else:
                    econtext['showFlags'] = __backup_showFlags_140386070708752
                __append(u'\n')
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
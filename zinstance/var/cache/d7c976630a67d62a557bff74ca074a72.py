# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/resources/browser/scripts.pt'

__tokens = {21: (u"string:PORTAL_URL = '${view/site_url}';", 1, 21), 101: (u'view/scripts', 3, 28), 149: (u'script/conditionalcomment', 4, 33), 184: (u' script/resetrjs|nothin', 4, 68), 235: (u'resetrjs', 6, 23), 286: (u'string:&lt;scri', 7, 40), 359: (u'nothing', 9, 32), 660: (u'string:&lt;/scri', 17, 39), 738: (u'condcomment', 20, 23), 793: (u'string:&lt;!--[if ${condcomment', 21, 41), 916: (u'script/src', 24, 55), 939: (u' script/bundl', 24, 78), 959: (u'c script/async|nothi', 24, 98), 986: (u'er script/defer|noth', 24, 125), 1045: (u'condcomment', 26, 23), 1093: (u'condcomment', 27, 34), 1129: (u'string:&lt;![endif]', 27, 70), 1209: (u'resetrjs', 30, 23), 1263: (u'string:&lt;scri', 31, 43), 1406: (u'string:&lt;/scri', 34, 42)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386186297040 = __C2ZContextWrapper
_static_140386186296528 = __compile_zt_expr
_static_140386079112144 = {u'defer': u'script/defer|nothing', u'src': u'script/src', u'type': u'text/javascript', u'data-bundle': u'script/bundle', u'async': u'script/async|nothing', }
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386073255504
            __attrs_140386073255504 = _static_140386247937936

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script>')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386073252944
            __default_140386073252944 = _DEFAULT_MARKER

            # <Value u"string:PORTAL_URL = '${view/site_url}';" (1:21)> -> __cache_140386073253456
            __token = 21
            try:
                __zt_tmp = __attrs_140386073255504
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140386073253456 = _static_140386186296528('string', u"PORTAL_URL = '${view/site_url}';", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

            # <BinOp left=<Value u"string:PORTAL_URL = '${view/site_url}';" (1:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e071490> -> __condition
            __expression = __cache_140386073253456

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140386073253456
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append(u'</script>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386073197264
            __attrs_140386073197264 = _static_140386247937936
            __backup_script_140386072587024 = get('script', __marker)

            # <Value u'view/scripts' (3:28)> -> __iterator
            __token = 101
            try:
                __zt_tmp = __attrs_140386073197264
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140386186296528('path', u'view/scripts', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            (__iterator, ____index_140386073197200, ) = getitem('repeat')(u'script', __iterator)
            econtext['script'] = None
            for __item in __iterator:
                econtext['script'] = __item
                __append(u'\n  ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386073196944
                __attrs_140386073196944 = _static_140386247937936
                __backup_condcomment_140386071505808 = get('condcomment', __marker)

                # <Value u'script/conditionalcomment' (4:33)> -> __value
                __token = 149
                try:
                    __zt_tmp = __attrs_140386073196944
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'script/conditionalcomment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['condcomment'] = __value
                __backup_resetrjs_140386072329872 = get('resetrjs', __marker)

                # <Value u'script/resetrjs|nothing' (4:68)> -> __value
                __token = 184
                try:
                    __zt_tmp = __attrs_140386073196944
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'script/resetrjs|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['resetrjs'] = __value
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071210448
                __attrs_140386071210448 = _static_140386247937936

                # <Value u'resetrjs' (6:23)> -> __condition
                __token = 235
                try:
                    __zt_tmp = __attrs_140386071210448
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'resetrjs', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078062992
                    __attrs_140386078062992 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071210000
                    __default_140386071210000 = _DEFAULT_MARKER

                    # <Value u'string:<script>' (7:40)> -> __cache_140386071208784
                    __token = 286
                    try:
                        __zt_tmp = __attrs_140386078062992
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386071208784 = _static_140386186296528('string', u'<script>', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'string:<script>' (7:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de7e5d0> -> __condition
                    __expression = __cache_140386071208784

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386071208784
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079184464
                    __attrs_140386079184464 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079184784
                    __default_140386079184784 = _DEFAULT_MARKER

                    # <Value u'nothing' (9:32)> -> __cache_140386071210768
                    __token = 359
                    try:
                        __zt_tmp = __attrs_140386079184464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386071210768 = _static_140386186296528('path', u'nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'nothing' (9:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de7e790> -> __condition
                    __expression = __cache_140386071210768

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n        Reset RequireJS definitions so that people who put RequireJS in a legacy compilation do not get errors\n      ')
                    else:
                        __content = __cache_140386071210768
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n\n      var _old_define = define;\n      var _old_require = require;\n      define = undefined;\n      require = undefined;\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079110544
                    __attrs_140386079110544 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079112464
                    __default_140386079112464 = _DEFAULT_MARKER

                    # <Value u'string:</script>' (17:39)> -> __cache_140386073196176
                    __token = 660
                    try:
                        __zt_tmp = __attrs_140386079110544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386073196176 = _static_140386186296528('string', u'</script>', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'string:</script>' (17:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e6194d0> -> __condition
                    __expression = __cache_140386073196176

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386073196176
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n    ')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078062736
                __attrs_140386078062736 = _static_140386247937936

                # <Value u'condcomment' (20:23)> -> __condition
                __token = 738
                try:
                    __zt_tmp = __attrs_140386078062736
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'condcomment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386079109712
                    __attrs_140386079109712 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079110160
                    __default_140386079110160 = _DEFAULT_MARKER

                    # <Value u'string:<!--[if ${condcomment}]>' (21:41)> -> __cache_140386079110864
                    __token = 793
                    try:
                        __zt_tmp = __attrs_140386079109712
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386079110864 = _static_140386186296528('string', u'<!--[if ${condcomment}]>', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'string:<!--[if ${condcomment}]>' (21:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e607e50> -> __condition
                    __expression = __cache_140386079110864

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386079110864
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n    ')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e607bd0> name=None at 7fae2e607290> -> __attrs_140386071623824
                __attrs_140386071623824 = _static_140386079112144

                # <script ... (0:0)
                # --------------------------------------------------------
                __append(u'<script type="text/javascript"')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071247824
                __default_140386071247824 = _DEFAULT_MARKER

                # <Substitution u'script/src' (24:55)> -> __attr_src
                __token = 916
                try:
                    __zt_tmp = __attrs_140386071623824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_src = _static_140386186296528('path', u'script/src', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_src is not None):
                    __append((u' src="%s"' % __attr_src))

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071247056
                __default_140386071247056 = _DEFAULT_MARKER

                # <Substitution u'script/bundle' (24:78)> -> __attr_data_bundle
                __token = 939
                try:
                    __zt_tmp = __attrs_140386071623824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_bundle = _static_140386186296528('path', u'script/bundle', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_data_bundle = __quote(__attr_data_bundle, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_bundle is not None):
                    __append((u' data-bundle="%s"' % __attr_data_bundle))

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071247120
                __default_140386071247120 = _DEFAULT_MARKER

                # <Substitution u'script/async|nothing' (24:98)> -> __attr_async
                __token = 959
                try:
                    __zt_tmp = __attrs_140386071623824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_async = _static_140386186296528('path', u'script/async|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_async = __quote(__attr_async, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_async is not None):
                    __append((u' async="%s"' % __attr_async))

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386071247312
                __default_140386071247312 = _DEFAULT_MARKER

                # <Boolean u'script/defer|nothing' (24:125)> -> __attr_defer
                __token = 986
                try:
                    __zt_tmp = __attrs_140386071623824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_defer = _static_140386186296528('path', u'script/defer|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if (__attr_defer is _DEFAULT_MARKER):
                    __attr_defer = None
                else:
                    if __attr_defer:
                        __attr_defer = u'defer'
                    else:
                        __attr_defer = None
                if (__attr_defer is not None):
                    __append((u' defer="%s"' % __attr_defer))
                __append(u'></script>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071625232
                __attrs_140386071625232 = _static_140386247937936

                # <Value u'condcomment' (26:23)> -> __condition
                __token = 1045
                try:
                    __zt_tmp = __attrs_140386071625232
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'condcomment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072526672
                    __attrs_140386072526672 = _static_140386247937936

                    # <Value u'condcomment' (27:34)> -> __condition
                    __token = 1093
                    try:
                        __zt_tmp = __attrs_140386072526672
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'condcomment', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072526288
                        __default_140386072526288 = _DEFAULT_MARKER

                        # <Value u'string:<![endif]-->' (27:70)> -> __cache_140386071624144
                        __token = 1129
                        try:
                            __zt_tmp = __attrs_140386072526672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386071624144 = _static_140386186296528('string', u'<![endif]-->', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'string:<![endif]-->' (27:70)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dfbfe50> -> __condition
                        __expression = __cache_140386071624144

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140386071624144
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                    __append(u'\n    ')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071624592
                __attrs_140386071624592 = _static_140386247937936

                # <Value u'resetrjs' (30:23)> -> __condition
                __token = 1209
                try:
                    __zt_tmp = __attrs_140386071624592
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'resetrjs', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072526800
                    __attrs_140386072526800 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072526032
                    __default_140386072526032 = _DEFAULT_MARKER

                    # <Value u'string:<script>' (31:43)> -> __cache_140386072526352
                    __token = 1263
                    try:
                        __zt_tmp = __attrs_140386072526800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386072526352 = _static_140386186296528('string', u'<script>', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'string:<script>' (31:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dfbfd50> -> __condition
                    __expression = __cache_140386072526352

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386072526352
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n      define = _old_define;\n      require = _old_require;\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078136912
                    __attrs_140386078136912 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078137040
                    __default_140386078137040 = _DEFAULT_MARKER

                    # <Value u'string:</script>' (34:42)> -> __cache_140386072525712
                    __token = 1406
                    try:
                        __zt_tmp = __attrs_140386078136912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386072525712 = _static_140386186296528('string', u'</script>', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'string:</script>' (34:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dfbf050> -> __condition
                    __expression = __cache_140386072525712

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140386072525712
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n    ')
                __append(u'\n\n  ')
                if (__backup_resetrjs_140386072329872 is __marker):
                    del econtext['resetrjs']
                else:
                    econtext['resetrjs'] = __backup_resetrjs_140386072329872
                if (__backup_condcomment_140386071505808 is __marker):
                    del econtext['condcomment']
                else:
                    econtext['condcomment'] = __backup_condcomment_140386071505808
                __append(u'\n')
                ____index_140386073197200 -= 1
                if (____index_140386073197200 > 0):
                    __append('')
            if (__backup_script_140386072587024 is __marker):
                del econtext['script']
            else:
                econtext['script'] = __backup_script_140386072587024
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
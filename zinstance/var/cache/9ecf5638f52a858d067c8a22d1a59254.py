# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/browser/templates/basic_error_message.pt'

__tokens = {293: (u'python:view.is_manager()', 8, 27), 352: (u'not:isManager', 11, 24), 423: (u'isManager', 12, 24), 434: (u'${options/error_type}', 12, 35), 436: (u'options/error_type', 12, 37), 694: (u'isManager', 23, 21), 705: (u'${options/error_type}', 23, 32), 707: (u'options/error_type', 23, 34), 755: (u'isManager', 25, 22), 786: (u'options/error_tb', 26, 20), 834: (u'not:isManager', 28, 26)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386186297040 = __C2ZContextWrapper
_static_140386204876304 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }
_static_140386186296528 = __compile_zt_expr
_static_140386204895632 = {u'class': u'documentFirstHeading', }
_static_140386204893904 = {u'class': u'documentFirstHeading', }
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

            # <Static value=<_ast.Dict object at 0x7fae35df7e10> name=None at 7fae35df7f50> -> __attrs_140386204877328
            __attrs_140386204877328 = _static_140386204876304
            __previous_i18n_domain_140386204879120 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204877136
            __attrs_140386204877136 = _static_140386247937936
            __backup_isManager_140386133933200 = get('isManager', __marker)

            # <Value u'python:view.is_manager()' (8:27)> -> __value
            __token = 293
            try:
                __zt_tmp = __attrs_140386204877136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u'view.is_manager()', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['isManager'] = __value
            __append(u'\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204878288
            __attrs_140386204878288 = _static_140386247937936

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204880208
            __attrs_140386204880208 = _static_140386247937936

            # <Value u'not:isManager' (11:24)> -> __condition
            __token = 352
            try:
                __zt_tmp = __attrs_140386204880208
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('not', u'isManager', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <title ... (0:0)
                # --------------------------------------------------------
                __append(u'<title>')
                __stream_140386204879184 = []
                __append_140386204879184 = __stream_140386204879184.append
                __append_140386204879184(u'Error')
                __msgid_140386204879184 = __re_whitespace(''.join(__stream_140386204879184)).strip()
                if __msgid_140386204879184:
                    __append(translate(__msgid_140386204879184, mapping=None, default=__msgid_140386204879184, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</title>')
            __append(u'\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204880464
            __attrs_140386204880464 = _static_140386247937936

            # <Value u'isManager' (12:24)> -> __condition
            __token = 423
            try:
                __zt_tmp = __attrs_140386204880464
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'isManager', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <title ... (0:0)
                # --------------------------------------------------------
                __append(u'<title>')

                # <Interpolation value=<Substitution u'${options/error_type}' (12:35)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fae35dfc5d0> -> __content_140386296014144
                __token = 434
                __token = 436
                try:
                    __zt_tmp = __attrs_140386204880464
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140386296014144 = _static_140386186296528('path', u'options/error_type', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __content_140386296014144 = __quote(__content_140386296014144, '\x00', '&#0;', None, None)
                __content_140386296014144 = __content_140386296014144
                if (__content_140386296014144 is None):
                    pass
                else:
                    if (__content_140386296014144 is None):
                        __content_140386296014144 = None
                    else:
                        __tt = type(__content_140386296014144)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __content_140386296014144 = unicode(__content_140386296014144)
                        else:
                            if (__tt is str):
                                __content_140386296014144 = decode(__content_140386296014144)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __content_140386296014144 = __content_140386296014144.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140386296014144)
                                        __content_140386296014144 = (unicode(__content_140386296014144) if (__content_140386296014144 is __converted) else __converted)
                                    else:
                                        __content_140386296014144 = __content_140386296014144()
                if (__content_140386296014144 is not None):
                    __append(__content_140386296014144)
                __append(u'</title>')
            __append(u'\n</head>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204893392
            __attrs_140386204893392 = _static_140386247937936

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae35dfc990> name=None at 7fae35dfca10> -> __attrs_140386204894800
            __attrs_140386204894800 = _static_140386204895632

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h1 class="documentFirstHeading">')
            __stream_140386204896016 = []
            __append_140386204896016 = __stream_140386204896016.append
            __append_140386204896016(u'\n      We&#8217;re sorry, but there seems to be an error&hellip;\n  ')
            __msgid_140386204896016 = __re_whitespace(''.join(__stream_140386204896016)).strip()
            if u'heading_site_error_sorry':
                __append(translate(u'heading_site_error_sorry', mapping=None, default=__msgid_140386204896016, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</h1>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae35dfc2d0> name=None at 7fae35dfcad0> -> __attrs_140386204894416
            __attrs_140386204894416 = _static_140386204893904

            # <Value u'isManager' (23:21)> -> __condition
            __token = 694
            try:
                __zt_tmp = __attrs_140386204894416
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'isManager', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h2 class="documentFirstHeading">')

                # <Interpolation value=<Substitution u'${options/error_type}' (23:32)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fae35dfcd50> -> __content_140386296014144
                __token = 705
                __token = 707
                try:
                    __zt_tmp = __attrs_140386204894416
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140386296014144 = _static_140386186296528('path', u'options/error_type', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __content_140386296014144 = __quote(__content_140386296014144, '\x00', '&#0;', None, None)
                __content_140386296014144 = __content_140386296014144
                if (__content_140386296014144 is None):
                    pass
                else:
                    if (__content_140386296014144 is None):
                        __content_140386296014144 = None
                    else:
                        __tt = type(__content_140386296014144)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __content_140386296014144 = unicode(__content_140386296014144)
                        else:
                            if (__tt is str):
                                __content_140386296014144 = decode(__content_140386296014144)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __content_140386296014144 = __content_140386296014144.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140386296014144)
                                        __content_140386296014144 = (unicode(__content_140386296014144) if (__content_140386296014144 is __converted) else __converted)
                                    else:
                                        __content_140386296014144 = __content_140386296014144()
                if (__content_140386296014144 is not None):
                    __append(__content_140386296014144)
                __append(u'</h2>')
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175264464
            __attrs_140386175264464 = _static_140386247937936

            # <Value u'isManager' (25:22)> -> __condition
            __token = 755
            try:
                __zt_tmp = __attrs_140386175264464
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'isManager', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <pre ... (0:0)
                # --------------------------------------------------------
                __append(u'<pre>')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204895248
                __default_140386204895248 = _DEFAULT_MARKER

                # <Value u'options/error_tb' (26:20)> -> __cache_140386204893328
                __token = 786
                try:
                    __zt_tmp = __attrs_140386175264464
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140386204893328 = _static_140386186296528('path', u'options/error_tb', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                # <BinOp left=<Value u'options/error_tb' (26:20)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae35dfcc90> -> __condition
                __expression = __cache_140386204893328

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140386204893328
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append(u'</pre>')
            __append(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175263056
            __attrs_140386175263056 = _static_140386247937936

            # <Value u'not:isManager' (28:26)> -> __condition
            __token = 834
            try:
                __zt_tmp = __attrs_140386175263056
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('not', u'isManager', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386175266128
                __attrs_140386175266128 = _static_140386247937936

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p>')
                __stream_140386178894256_site_admin = ''
                __stream_140386175266640 = []
                __append_140386175266640 = __stream_140386175266640.append
                __append_140386175266640(u'\n      If you are certain you have the correct web address but are encountering an error, please\n      contact the ')
                __stream_140386178894256_site_admin = []
                __append_140386178894256_site_admin = __stream_140386178894256_site_admin.append

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127697872
                __attrs_140386127697872 = _static_140386247937936

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_140386178894256_site_admin(u'<span>')
                __stream_140386127698384 = []
                __append_140386127698384 = __stream_140386127698384.append
                __append_140386127698384(u'site administration')
                __msgid_140386127698384 = __re_whitespace(''.join(__stream_140386127698384)).strip()
                if u'label_site_admin':
                    __append_140386178894256_site_admin(translate(u'label_site_admin', mapping=None, default=__msgid_140386127698384, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append_140386178894256_site_admin(u'</span>')
                __append_140386175266640(u'${site_admin}')
                __stream_140386178894256_site_admin = ''.join(__stream_140386178894256_site_admin)
                __append_140386175266640(u'.\n      ')
                __msgid_140386175266640 = __re_whitespace(''.join(__stream_140386175266640)).strip()
                if u'description_site_error_mail_site_admin':
                    __append(translate(u'description_site_error_mail_site_admin', mapping={u'site_admin': __stream_140386178894256_site_admin, }, default=__msgid_140386175266640, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</p>\n  ')
            __append(u'\n\n</body>\n')
            if (__backup_isManager_140386133933200 is __marker):
                del econtext['isManager']
            else:
                econtext['isManager'] = __backup_isManager_140386133933200
            __append(u'\n</html>')
            __i18n_domain = __previous_i18n_domain_140386204879120
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
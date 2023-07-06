# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/browser/templates/plone-addsite.pt'

__tokens = {620: (u'string:${context/absolute_url}/++resource++plone-admin-ui.css', 15, 29), 786: (u'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js', 17, 53), 911: (u'string:${context/absolute_url}/++resource++plone-admin-ui.js', 18, 53), 1123: (u'string:${context/absolute_url}/++resource++plone-logo.png', 25, 29), 5050: (u'view/profiles', 37, 29), 5098: (u' profiles/bas', 38, 33), 5148: (u'e profiles/defau', 39, 34), 5204: (u'es profiles/extensi', 40, 36), 5253: (u'ced request/advanced|not', 41, 25), 4973: (u'string:${context/absolute_url}/@@plone-addsite', 36, 31), 5695: (u'request/site_id|nothing', 54, 37), 6450: (u'view/browser_language', 77, 45), 6518: (u' python:view.grouped_languages(browser_language', 78, 45), 6609: (u'grouped_languages', 79, 40), 6650: (u'group/label', 79, 81), 6737: (u'group/languages', 82, 39), 6798: (u"python:lang['langcode']", 83, 44), 6869: (u" python:lang['langcode'] == browser_languag", 84, 46), 6950: (u"python: lang['label']", 85, 35), 7559: (u'view/timezones', 106, 30), 7614: (u'tz_list', 107, 38), 7645: (u'group', 107, 69), 7716: (u'python:tz_list[group]', 109, 33), 7779: (u'tz/value', 110, 40), 7820: (u'tz/label', 111, 31), 7963: (u'advanced', 118, 40), 8308: (u'not:advanced', 125, 34), 8455: (u'python: len(base_profiles) > 1', 131, 34), 8863: (u'base_profiles', 142, 40), 9121: (u' info/i', 148, 44), 9068: (u'info/id', 147, 42), 9176: (u"d python: default_profile==info['id'] and 'checked' or nothi", 149, 45), 9309: (u'info/id', 151, 43), 9354: (u'info/title', 152, 36), 9460: (u'info/description', 154, 49), 9642: (u'python: extension_profiles', 161, 40), 9720: (u'python: not advanced', 162, 49), 9794: (u'python: advanced', 163, 51), 9919: (u'python: advanced', 167, 65), 10185: (u'extension_profiles', 173, 39), 10290: (u'info/selected|nothing', 175, 45), 10357: (u'python: not selected or advanced', 176, 43), 10430: (u'python: advanced', 177, 38), 10608: (u'info/id', 180, 49), 10662: (u' info/i', 181, 45), 10721: (u'd info/selected|nothi', 182, 49), 10826: (u'info/id', 184, 46), 10874: (u'info/title', 185, 39), 11045: (u'python: advanced', 188, 84), 11012: (u'info/description', 188, 51), 11200: (u'python: selected and not advanced', 192, 43), 11357: (u'info/id', 194, 47), 11414: (u' info/selected|nothin', 195, 48)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386127926864 = {u'class': u'field', }
_static_140386125454800 = {u'value': u'UTC', }
_static_140386180401040 = {u'for': u'default_language', }
_static_140386204888400 = {u'type': u'submit', u'name': u'submit', u'value': u'Create Plone Site', }
_static_140386247937936 = {}
_static_140386179460432 = {u'for': u'info/id', }
_static_140386195054736 = {u'id': u'portal_timezone', u'name': u'portal_timezone', }
_static_140386204879248 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }
_static_140386192670160 = {u'for': u'info/id', }
_static_140386177529104 = {u'class': u'formHelp', }
_static_140386135459984 = {u'for': u'title', }
_static_140386179447568 = {u'class': u'formHelp', }
_static_140386135565264 = {u'class': u'field', }
_static_140386179410768 = {u'class': u'addons-group', }
_static_140386135566864 = {u'id': u'site_id', u'type': u'text', u'name': u'site_id', u'value': u'request/site_id|nothing', u'size': u'20', }
_static_140386177529936 = {u'id': u'add-on-list', }
_static_140386204876560 = {u'class': u'field', }
_static_140386125455632 = {u'type': u'hidden', u'name': u'setup_content:boolean', u'value': u'true', }
_static_140386127926160 = {u'selected': u"python:lang['langcode'] == browser_language", u'value': u'en', }
_static_140386204897232 = {u'src': u'string:${context/absolute_url}/++resource++plone-admin-ui.js', u'type': u'text/javascript', }
_static_140386178043472 = {u'src': u'/++resource++plone-logo.png', u'alt': u'Plone logo', u'height': u'28', u'width': u'108', }
_static_140386127635664 = {u'content': u'width=device-width, initial-scale=1', u'name': u'viewport', }
_static_140386125456528 = {u'for': u'profile_id', }
_static_140386204858640 = {u'checked': u'checked', u'type': u'checkbox', u'name': u'setup_content:boolean', }
_static_140386204860880 = {u'for': u'portal_timezone', }
_static_140386127926224 = {u'label': u'group/label', }
_static_140386204859344 = {u'class': u'formHelp', }
_static_140386127635088 = {u'charset': u'utf-8', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386204894992 = {u'href': u'/++resource++plone-admin-ui.css', u'type': u'text/css', u'rel': u'stylesheet', }
_static_140386179457872 = {u'checked': u"python: default_profile==info['id'] and 'checked' or nothing", u'type': u'radio', u'name': u'profile_id:string', u'value': u'profile', u'id': u'info/id', }
_static_140386127913680 = {u'src': u'data:image/png;base64,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', u'alt': u'', }
_static_140386135458512 = {u'class': u'formHelp', }
_static_140386174004304 = {u'id': u'box', }
_static_140386135564496 = {u'class': u'formHelp', }
_static_140386195055312 = {u'label': u'group', }
_static_140386127895632 = {u'class': u'field', }
_static_140386204886224 = {u'checked': u'info/selected|nothing', u'type': u'hidden', u'name': u'extension_ids:list', u'value': u'', }
_static_140386125458960 = {u'class': u'field', }
_static_140386178041040 = {u'class': u'circle running', }
_static_140386127915344 = {u'action': u'#', u'method': u'post', }
_static_140386180401744 = {u'class': u'formHelp', }
_static_140386192669584 = {u'class': u'formHelp', }
_static_140386204863440 = {u'class': u'formHelp', }
_static_140386178005904 = {u'class': u'formControls', }
_static_140386204895952 = {u'src': u'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js', u'type': u'text/javascript', }
_static_140386186296528 = __compile_zt_expr
_static_140386127895952 = {u'for': u'site_id', }
_static_140386135461456 = {u'type': u'text', u'name': u'title', u'value': u'Site', u'size': u'30', }
_static_140386180402704 = {u'name': u'default_language', }
_static_140386178005840 = {u'class': u'formHelp', }
_static_140386125449296 = {u'checked': u'info/selected|nothing', u'type': u'checkbox', u'name': u'extension_ids:list', u'value': u'', u'id': u'info/id', }
_static_140386204863632 = {u'class': u'field', }
_static_140386179410384 = {u'type': u'hidden', u'name': u'form.submitted:boolean', u'value': u'True', }

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
            __append(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')

            # <Static value=<_ast.Dict object at 0x7fae35df8990> name=None at 7fae35df8750> -> __attrs_140386204877072
            __attrs_140386204877072 = _static_140386204879248
            __previous_i18n_domain_140386204878416 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204880656
            __attrs_140386204880656 = _static_140386247937936

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae3144e290> name=None at 7fae3144e750> -> __attrs_140386127634960
            __attrs_140386127634960 = _static_140386127635088

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta charset="utf-8"/>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae3144e4d0> name=None at 7fae3144eed0> -> __attrs_140386127635024
            __attrs_140386127635024 = _static_140386127635664

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append(u'<meta name="viewport" content="width=device-width, initial-scale=1"/>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127634704
            __attrs_140386127634704 = _static_140386247937936

            # <title ... (0:0)
            # --------------------------------------------------------
            __append(u'<title>')
            __stream_140386127635280 = []
            __append_140386127635280 = __stream_140386127635280.append
            __append_140386127635280(u'Create a Plone site')
            __msgid_140386127635280 = __re_whitespace(''.join(__stream_140386127635280)).strip()
            if __msgid_140386127635280:
                __append(translate(__msgid_140386127635280, mapping=None, default=__msgid_140386127635280, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</title>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae35dfc710> name=None at 7fae3144ee10> -> __attrs_140386204896976
            __attrs_140386204896976 = _static_140386204894992

            # <link ... (0:0)
            # --------------------------------------------------------
            __append(u'<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204896336
            __default_140386204896336 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/++resource++plone-admin-ui.css' (15:29)> -> __attr_href
            __token = 620
            try:
                __zt_tmp = __attrs_140386204896976
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140386186296528('string', u'${context/absolute_url}/++resource++plone-admin-ui.css', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', u'/++resource++plone-admin-ui.css', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((u' href="%s"' % __attr_href))
            __append(u' />\n  ')

            # <Static value=<_ast.Dict object at 0x7fae35dfcad0> name=None at 7fae35dfc4d0> -> __attrs_140386204896720
            __attrs_140386204896720 = _static_140386204895952

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script type="text/javascript"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204896656
            __default_140386204896656 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js' (17:53)> -> __attr_src
            __token = 786
            try:
                __zt_tmp = __attrs_140386204896720
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140386186296528('string', u'${context/absolute_url}/++resource++jstz-1.0.4.min.js', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae35dfcfd0> name=None at 7fae35dfcc90> -> __attrs_140386174004048
            __attrs_140386174004048 = _static_140386204897232

            # <script ... (0:0)
            # --------------------------------------------------------
            __append(u'<script type="text/javascript"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386174004240
            __default_140386174004240 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/++resource++plone-admin-ui.js' (18:53)> -> __attr_src
            __token = 911
            try:
                __zt_tmp = __attrs_140386174004048
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140386186296528('string', u'${context/absolute_url}/++resource++plone-admin-ui.js', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u'></script>\n</head>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386174002064
            __attrs_140386174002064 = _static_140386247937936

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae34086c50> name=None at 7fae34086610> -> __attrs_140386174003920
            __attrs_140386174003920 = _static_140386174004304

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div id="box">\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386174001616
            __attrs_140386174001616 = _static_140386247937936

            # <header ... (0:0)
            # --------------------------------------------------------
            __append(u'<header>')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386174001360
            __attrs_140386174001360 = _static_140386247937936

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h1>')

            # <Static value=<_ast.Dict object at 0x7fae34460e50> name=None at 7fae34460c90> -> __attrs_140386178041232
            __attrs_140386178041232 = _static_140386178043472

            # <img ... (0:0)
            # --------------------------------------------------------
            __append(u'<img')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386178042000
            __default_140386178042000 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/++resource++plone-logo.png' (25:29)> -> __attr_src
            __token = 1123
            try:
                __zt_tmp = __attrs_140386178041232
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140386186296528('string', u'${context/absolute_url}/++resource++plone-logo.png', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', u'/++resource++plone-logo.png', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((u' src="%s"' % __attr_src))
            __append(u' width="108" height="28"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386178040080
            __default_140386178040080 = _DEFAULT_MARKER

            # <Translate msgid=None node=<_ast.Str object at 0x7fae34460d50> at 7fae34460450> -> __attr_alt
            __attr_alt = u'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_alt is not None):
                __append((u' alt="%s"' % __attr_alt))
            __append(u'/></h1>\n    </header>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386178041744
            __attrs_140386178041744 = _static_140386247937936

            # <article ... (0:0)
            # --------------------------------------------------------
            __append(u'<article>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae344604d0> name=None at 7fae34460390> -> __attrs_140386178043536
            __attrs_140386178043536 = _static_140386178041040

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="circle running">\n            ')

            # <Static value=<_ast.Dict object at 0x7fae314922d0> name=None at 7fae31492810> -> __attrs_140386127913552
            __attrs_140386127913552 = _static_140386127913680

            # <img ... (0:0)
            # --------------------------------------------------------
            __append(u'<img alt="" src="data:image/png;base64,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" />\n        </div>\n  ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386127914000
            __attrs_140386127914000 = _static_140386247937936

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append(u'<h1>')
            __stream_140386127916752 = []
            __append_140386127916752 = __stream_140386127916752.append
            __append_140386127916752(u'Create a Plone site')
            __msgid_140386127916752 = __re_whitespace(''.join(__stream_140386127916752)).strip()
            if __msgid_140386127916752:
                __append(translate(__msgid_140386127916752, mapping=None, default=__msgid_140386127916752, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</h1>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae31492950> name=None at 7fae31492a10> -> __attrs_140386127914640
            __attrs_140386127914640 = _static_140386127915344
            __backup_profiles_140386127690128 = get('profiles', __marker)

            # <Value u'view/profiles' (37:29)> -> __value
            __token = 5050
            try:
                __zt_tmp = __attrs_140386127914640
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/profiles', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['profiles'] = __value
            __backup_base_profiles_140386126059728 = get('base_profiles', __marker)

            # <Value u'profiles/base' (38:33)> -> __value
            __token = 5098
            try:
                __zt_tmp = __attrs_140386127914640
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'profiles/base', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['base_profiles'] = __value
            __backup_default_profile_140386126060048 = get('default_profile', __marker)

            # <Value u'profiles/default' (39:34)> -> __value
            __token = 5148
            try:
                __zt_tmp = __attrs_140386127914640
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'profiles/default', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['default_profile'] = __value
            __backup_extension_profiles_140386126059472 = get('extension_profiles', __marker)

            # <Value u'profiles/extensions' (40:36)> -> __value
            __token = 5204
            try:
                __zt_tmp = __attrs_140386127914640
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'profiles/extensions', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['extension_profiles'] = __value
            __backup_advanced_140386126059280 = get('advanced', __marker)

            # <Value u'request/advanced|nothing' (41:25)> -> __value
            __token = 5253
            try:
                __zt_tmp = __attrs_140386127914640
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'request/advanced|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['advanced'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append(u'<form')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127916944
            __default_140386127916944 = _DEFAULT_MARKER

            # <Substitution u'string:${context/absolute_url}/@@plone-addsite' (36:31)> -> __attr_action
            __token = 4973
            try:
                __zt_tmp = __attrs_140386127914640
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140386186296528('string', u'${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', u'#', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((u' action="%s"' % __attr_action))
            __append(u' method="post">\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae3148dc50> name=None at 7fae3148d790> -> __attrs_140386127893008
            __attrs_140386127893008 = _static_140386127895632

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="field">\n        ')

            # <Static value=<_ast.Dict object at 0x7fae3148dd90> name=None at 7fae3148db90> -> __attrs_140386127895120
            __attrs_140386127895120 = _static_140386127895952

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label for="site_id">')
            __stream_140386127895184 = []
            __append_140386127895184 = __stream_140386127895184.append
            __append_140386127895184(u'\n          Path identifier\n        ')
            __msgid_140386127895184 = __re_whitespace(''.join(__stream_140386127895184)).strip()
            if __msgid_140386127895184:
                __append(translate(__msgid_140386127895184, mapping=None, default=__msgid_140386127895184, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae31bde0d0> name=None at 7fae31bdef10> -> __attrs_140386135566544
            __attrs_140386135566544 = _static_140386135564496

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="formHelp">')
            __stream_140386127893456 = []
            __append_140386127893456 = __stream_140386127893456.append
            __append_140386127893456(u'\n          The ID of the site. This ends up as part of the URL.')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386135567440
            __attrs_140386135567440 = _static_140386247937936

            # <br ... (0:0)
            # --------------------------------------------------------
            __append_140386127893456(u'<br />\n          No special characters or spaces are allowed.\n        ')
            __msgid_140386127893456 = __re_whitespace(''.join(__stream_140386127893456)).strip()
            if __msgid_140386127893456:
                __append(translate(__msgid_140386127893456, mapping=None, default=__msgid_140386127893456, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</div>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae31bdea10> name=None at 7fae31bded90> -> __attrs_140386135565008
            __attrs_140386135565008 = _static_140386135566864

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="text" name="site_id" size="20" id="site_id"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386135567888
            __default_140386135567888 = _DEFAULT_MARKER

            # <Substitution u'request/site_id|nothing' (54:37)> -> __attr_value
            __token = 5695
            try:
                __zt_tmp = __attrs_140386135565008
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140386186296528('path', u'request/site_id|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />\n      </div>\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae31bde3d0> name=None at 7fae31bdef90> -> __attrs_140386135458576
            __attrs_140386135458576 = _static_140386135565264

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="field">\n        ')

            # <Static value=<_ast.Dict object at 0x7fae31bc4890> name=None at 7fae31bc4510> -> __attrs_140386135460304
            __attrs_140386135460304 = _static_140386135459984

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label for="title">')
            __stream_140386135461648 = []
            __append_140386135461648 = __stream_140386135461648.append
            __append_140386135461648(u'Title')
            __msgid_140386135461648 = __re_whitespace(''.join(__stream_140386135461648)).strip()
            if u'label_title':
                __append(translate(u'label_title', mapping=None, default=__msgid_140386135461648, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae31bc42d0> name=None at 7fae31bc4550> -> __attrs_140386135458320
            __attrs_140386135458320 = _static_140386135458512

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="formHelp">')
            __stream_140386135459536 = []
            __append_140386135459536 = __stream_140386135459536.append
            __append_140386135459536(u'\n          A short title for the site. This will be shown in the title of the\n          browser window on each page.\n        ')
            __msgid_140386135459536 = __re_whitespace(''.join(__stream_140386135459536)).strip()
            if __msgid_140386135459536:
                __append(translate(__msgid_140386135459536, mapping=None, default=__msgid_140386135459536, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</div>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae31bc4e50> name=None at 7fae31bc4410> -> __attrs_140386204873360
            __attrs_140386204873360 = _static_140386135461456

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="text" name="title" size="30"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204876688
            __default_140386204876688 = _DEFAULT_MARKER

            # <Translate msgid=u'text_default_site_title' node=<_ast.Str object at 0x7fae35df7ad0> at 7fae35df7890> -> __attr_value
            __attr_value = u'Site'
            __attr_value = translate(u'text_default_site_title', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />\n      </div>\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae35df7f10> name=None at 7fae31bc4e10> -> __attrs_140386180400720
            __attrs_140386180400720 = _static_140386204876560

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="field">\n        ')

            # <Static value=<_ast.Dict object at 0x7fae346a0790> name=None at 7fae346a0090> -> __attrs_140386180400912
            __attrs_140386180400912 = _static_140386180401040

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label for="default_language">')
            __stream_140386180400464 = []
            __append_140386180400464 = __stream_140386180400464.append
            __append_140386180400464(u'Language')
            __msgid_140386180400464 = __re_whitespace(''.join(__stream_140386180400464)).strip()
            if __msgid_140386180400464:
                __append(translate(__msgid_140386180400464, mapping=None, default=__msgid_140386180400464, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae346a0a50> name=None at 7fae346a0b10> -> __attrs_140386180403088
            __attrs_140386180403088 = _static_140386180401744

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="formHelp">')
            __stream_140386180399952 = []
            __append_140386180399952 = __stream_140386180399952.append
            __append_140386180399952(u'\n          The main language of the site.\n        ')
            __msgid_140386180399952 = __re_whitespace(''.join(__stream_140386180399952)).strip()
            if __msgid_140386180399952:
                __append(translate(__msgid_140386180399952, mapping=None, default=__msgid_140386180399952, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</div>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae346a0e10> name=None at 7fae346a0e50> -> __attrs_140386180400080
            __attrs_140386180400080 = _static_140386180402704
            __backup_browser_language_140386125765584 = get('browser_language', __marker)

            # <Value u'view/browser_language' (77:45)> -> __value
            __token = 6450
            try:
                __zt_tmp = __attrs_140386180400080
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/browser_language', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['browser_language'] = __value
            __backup_grouped_languages_140386125765328 = get('grouped_languages', __marker)

            # <Value u'python:view.grouped_languages(browser_language)' (78:45)> -> __value
            __token = 6518
            try:
                __zt_tmp = __attrs_140386180400080
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u'view.grouped_languages(browser_language)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['grouped_languages'] = __value

            # <select ... (0:0)
            # --------------------------------------------------------
            __append(u'<select name="default_language">\n            ')

            # <Static value=<_ast.Dict object at 0x7fae314953d0> name=None at 7fae314959d0> -> __attrs_140386127928464
            __attrs_140386127928464 = _static_140386127926224
            __backup_group_140386125765840 = get('group', __marker)

            # <Value u'grouped_languages' (79:40)> -> __iterator
            __token = 6609
            try:
                __zt_tmp = __attrs_140386127928464
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140386186296528('path', u'grouped_languages', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            (__iterator, ____index_140386127928272, ) = getitem('repeat')(u'group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <optgroup ... (0:0)
                # --------------------------------------------------------
                __append(u'<optgroup')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127929104
                __default_140386127929104 = _DEFAULT_MARKER

                # <Substitution u'group/label' (79:81)> -> __attr_label
                __token = 6650
                try:
                    __zt_tmp = __attrs_140386127928464
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_label = _static_140386186296528('path', u'group/label', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_label is not None):
                    __append((u' label="%s"' % __attr_label))
                __append(u'>\n\n              ')

                # <Static value=<_ast.Dict object at 0x7fae31495390> name=None at 7fae31495510> -> __attrs_140386204863696
                __attrs_140386204863696 = _static_140386127926160
                __backup_lang_140386125764880 = get('lang', __marker)

                # <Value u'group/languages' (82:39)> -> __iterator
                __token = 6737
                try:
                    __zt_tmp = __attrs_140386204863696
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'group/languages', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386204863504, ) = getitem('repeat')(u'lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127928848
                    __default_140386127928848 = _DEFAULT_MARKER

                    # <Substitution u"python:lang['langcode']" (83:44)> -> __attr_value
                    __token = 6798
                    try:
                        __zt_tmp = __attrs_140386204863696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140386186296528('python', u"lang['langcode']", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', u'en', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127927888
                    __default_140386127927888 = _DEFAULT_MARKER

                    # <Boolean u"python:lang['langcode'] == browser_language" (84:46)> -> __attr_selected
                    __token = 6869
                    try:
                        __zt_tmp = __attrs_140386204863696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_140386186296528('python', u"lang['langcode'] == browser_language", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = u'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((u' selected="%s"' % __attr_selected))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386127926352
                    __default_140386127926352 = _DEFAULT_MARKER

                    # <Value u"python: lang['label']" (85:35)> -> __cache_140386127925712
                    __token = 6950
                    try:
                        __zt_tmp = __attrs_140386204863696
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386127925712 = _static_140386186296528('python', u" lang['label']", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u"python: lang['label']" (85:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae31495b50> -> __condition
                    __expression = __cache_140386127925712

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                  English\n              ')
                    else:
                        __content = __cache_140386127925712
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</option>')
                    ____index_140386204863504 -= 1
                    if (____index_140386204863504 > 0):
                        __append('\n              ')
                if (__backup_lang_140386125764880 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_140386125764880
                __append(u'\n\n            </optgroup>')
                ____index_140386127928272 -= 1
                if (____index_140386127928272 > 0):
                    __append('\n            ')
            if (__backup_group_140386125765840 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_140386125765840
            __append(u'\n        </select>')
            if (__backup_grouped_languages_140386125765328 is __marker):
                del econtext['grouped_languages']
            else:
                econtext['grouped_languages'] = __backup_grouped_languages_140386125765328
            if (__backup_browser_language_140386125765584 is __marker):
                del econtext['browser_language']
            else:
                econtext['browser_language'] = __backup_browser_language_140386125765584
            __append(u'\n      </div>\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae31495650> name=None at 7fae346a0490> -> __attrs_140386204861072
            __attrs_140386204861072 = _static_140386127926864

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="field">\n        ')

            # <Static value=<_ast.Dict object at 0x7fae35df41d0> name=None at 7fae35df46d0> -> __attrs_140386204863056
            __attrs_140386204863056 = _static_140386204860880

            # <label ... (0:0)
            # --------------------------------------------------------
            __append(u'<label for="portal_timezone">')
            __stream_140386204861840 = []
            __append_140386204861840 = __stream_140386204861840.append
            __append_140386204861840(u'\n          Default timezone\n        ')
            __msgid_140386204861840 = __re_whitespace(''.join(__stream_140386204861840)).strip()
            if __msgid_140386204861840:
                __append(translate(__msgid_140386204861840, mapping=None, default=__msgid_140386204861840, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</label>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae35df4bd0> name=None at 7fae35df4d90> -> __attrs_140386204863248
            __attrs_140386204863248 = _static_140386204863440

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="formHelp">')
            __stream_140386204863952 = []
            __append_140386204863952 = __stream_140386204863952.append
            __append_140386204863952(u'\n          The default timezone setting of the portal. Users will be able to set\n          their own timezone, if available timezones are defined in the date and\n          time settings.\n        ')
            __msgid_140386204863952 = __re_whitespace(''.join(__stream_140386204863952)).strip()
            if __msgid_140386204863952:
                __append(translate(__msgid_140386204863952, mapping=None, default=__msgid_140386204863952, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</div>\n\n        ')

            # <Static value=<_ast.Dict object at 0x7fae3549a090> name=None at 7fae3549a690> -> __attrs_140386195055056
            __attrs_140386195055056 = _static_140386195054736
            __backup_tz_list_140386125765456 = get('tz_list', __marker)

            # <Value u'view/timezones' (106:30)> -> __value
            __token = 7559
            try:
                __zt_tmp = __attrs_140386195055056
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'view/timezones', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['tz_list'] = __value

            # <select ... (0:0)
            # --------------------------------------------------------
            __append(u'<select id="portal_timezone" name="portal_timezone">\n          ')

            # <Static value=<_ast.Dict object at 0x7fae3549a2d0> name=None at 7fae3549a310> -> __attrs_140386125453072
            __attrs_140386125453072 = _static_140386195055312
            __backup_group_140386125765200 = get('group', __marker)

            # <Value u'tz_list' (107:38)> -> __iterator
            __token = 7614
            try:
                __zt_tmp = __attrs_140386125453072
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140386186296528('path', u'tz_list', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            (__iterator, ____index_140386125451792, ) = getitem('repeat')(u'group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <optgroup ... (0:0)
                # --------------------------------------------------------
                __append(u'<optgroup')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386195054800
                __default_140386195054800 = _DEFAULT_MARKER

                # <Substitution u'group' (107:69)> -> __attr_label
                __token = 7645
                try:
                    __zt_tmp = __attrs_140386125453072
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_label = _static_140386186296528('path', u'group', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_label is not None):
                    __append((u' label="%s"' % __attr_label))
                __append(u'>\n          ')

                # <Static value=<_ast.Dict object at 0x7fae31239dd0> name=None at 7fae31239250> -> __attrs_140386125453008
                __attrs_140386125453008 = _static_140386125454800
                __backup_tz_140386128255952 = get('tz', __marker)

                # <Value u'python:tz_list[group]' (109:33)> -> __iterator
                __token = 7716
                try:
                    __zt_tmp = __attrs_140386125453008
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('python', u'tz_list[group]', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386125452944, ) = getitem('repeat')(u'tz', __iterator)
                econtext['tz'] = None
                for __item in __iterator:
                    econtext['tz'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<option')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386125451984
                    __default_140386125451984 = _DEFAULT_MARKER

                    # <Substitution u'tz/value' (110:40)> -> __attr_value
                    __token = 7779
                    try:
                        __zt_tmp = __attrs_140386125453008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140386186296528('path', u'tz/value', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', u'UTC', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386125454928
                    __default_140386125454928 = _DEFAULT_MARKER

                    # <Value u'tz/label' (111:31)> -> __cache_140386125454992
                    __token = 7820
                    try:
                        __zt_tmp = __attrs_140386125453008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386125454992 = _static_140386186296528('path', u'tz/label', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'tz/label' (111:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae31239ed0> -> __condition
                    __expression = __cache_140386125454992

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n              UTC\n          ')
                    else:
                        __content = __cache_140386125454992
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</option>')
                    ____index_140386125452944 -= 1
                    if (____index_140386125452944 > 0):
                        __append('\n          ')
                if (__backup_tz_140386128255952 is __marker):
                    del econtext['tz']
                else:
                    econtext['tz'] = __backup_tz_140386128255952
                __append(u'\n          </optgroup>')
                ____index_140386125451792 -= 1
                if (____index_140386125451792 > 0):
                    __append('\n          ')
            if (__backup_group_140386125765200 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_140386125765200
            __append(u'\n        </select>')
            if (__backup_tz_list_140386125765456 is __marker):
                del econtext['tz_list']
            else:
                econtext['tz_list'] = __backup_tz_list_140386125765456
            __append(u'\n      </div>\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae35df4c90> name=None at 7fae35df43d0> -> __attrs_140386125452048
            __attrs_140386125452048 = _static_140386204863632

            # <Value u'advanced' (118:40)> -> __condition
            __token = 7963
            try:
                __zt_tmp = __attrs_140386125452048
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'advanced', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="field">\n        ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386125453712
                __attrs_140386125453712 = _static_140386247937936

                # <label ... (0:0)
                # --------------------------------------------------------
                __append(u'<label>')

                # <Static value=<_ast.Dict object at 0x7fae35df3910> name=None at 7fae35df39d0> -> __attrs_140386204860112
                __attrs_140386204860112 = _static_140386204858640

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="checkbox" name="setup_content:boolean" checked="checked" /> ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204857360
                __attrs_140386204857360 = _static_140386247937936
                __stream_140386204859216 = []
                __append_140386204859216 = __stream_140386204859216.append
                __append_140386204859216(u'Example content')
                __msgid_140386204859216 = __re_whitespace(''.join(__stream_140386204859216)).strip()
                if __msgid_140386204859216:
                    __append(translate(__msgid_140386204859216, mapping=None, default=__msgid_140386204859216, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</label>\n        ')

                # <Static value=<_ast.Dict object at 0x7fae35df3bd0> name=None at 7fae35df3e90> -> __attrs_140386204859024
                __attrs_140386204859024 = _static_140386204859344

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="formHelp">')
                __stream_140386204857168 = []
                __append_140386204857168 = __stream_140386204857168.append
                __append_140386204857168(u'\n            Should the default example content be added to the site?\n        ')
                __msgid_140386204857168 = __re_whitespace(''.join(__stream_140386204857168)).strip()
                if __msgid_140386204857168:
                    __append(translate(__msgid_140386204857168, mapping=None, default=__msgid_140386204857168, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</div>\n      </div>')
            __append(u'\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386204859152
            __attrs_140386204859152 = _static_140386247937936

            # <Value u'not:advanced' (125:34)> -> __condition
            __token = 8308
            try:
                __zt_tmp = __attrs_140386204859152
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('not', u'advanced', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7fae3123a110> name=None at 7fae35df3650> -> __attrs_140386125457168
                __attrs_140386125457168 = _static_140386125455632

                # <input ... (0:0)
                # --------------------------------------------------------
                __append(u'<input type="hidden" name="setup_content:boolean" value="true" />\n      ')
            __append(u'\n\n\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386195055568
            __attrs_140386195055568 = _static_140386247937936

            # <Value u'python: len(base_profiles) > 1' (131:34)> -> __condition
            __token = 8455
            try:
                __zt_tmp = __attrs_140386195055568
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('python', u' len(base_profiles) > 1', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7fae3123ae10> name=None at 7fae3123a810> -> __attrs_140386125456720
                __attrs_140386125456720 = _static_140386125458960

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="field">\n          ')

                # <Static value=<_ast.Dict object at 0x7fae3123a490> name=None at 7fae3123a210> -> __attrs_140386179446672
                __attrs_140386179446672 = _static_140386125456528

                # <label ... (0:0)
                # --------------------------------------------------------
                __append(u'<label for="profile_id">')
                __stream_140386125457552 = []
                __append_140386125457552 = __stream_140386125457552.append
                __append_140386125457552(u'\n            Base configuration\n          ')
                __msgid_140386125457552 = __re_whitespace(''.join(__stream_140386125457552)).strip()
                if __msgid_140386125457552:
                    __append(translate(__msgid_140386125457552, mapping=None, default=__msgid_140386125457552, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</label>\n\n          ')

                # <Static value=<_ast.Dict object at 0x7fae345b7b10> name=None at 7fae345b7d90> -> __attrs_140386179446160
                __attrs_140386179446160 = _static_140386179447568

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="formHelp">')
                __stream_140386179446288 = []
                __append_140386179446288 = __stream_140386179446288.append
                __append_140386179446288(u"\n            You normally don't need to change anything here unless you have\n            specific reasons and know what you are doing.\n          ")
                __msgid_140386179446288 = __re_whitespace(''.join(__stream_140386179446288)).strip()
                if __msgid_140386179446288:
                    __append(translate(__msgid_140386179446288, mapping=None, default=__msgid_140386179446288, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</div>\n\n            ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386179446736
                __attrs_140386179446736 = _static_140386247937936
                __backup_info_140386125765712 = get('info', __marker)

                # <Value u'base_profiles' (142:40)> -> __iterator
                __token = 8863
                try:
                    __zt_tmp = __attrs_140386179446736
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'base_profiles', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386179445776, ) = getitem('repeat')(u'info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item
                    __append(u'\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386179445200
                    __attrs_140386179445200 = _static_140386247937936

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<label>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fae345ba350> name=None at 7fae345ba090> -> __attrs_140386179457552
                    __attrs_140386179457552 = _static_140386179457872

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="radio" name="profile_id:string"')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179458640
                    __default_140386179458640 = _DEFAULT_MARKER

                    # <Substitution u'info/id' (148:44)> -> __attr_value
                    __token = 9121
                    try:
                        __zt_tmp = __attrs_140386179457552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140386186296528('path', u'info/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', u'profile', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179458000
                    __default_140386179458000 = _DEFAULT_MARKER

                    # <Substitution u'info/id' (147:42)> -> __attr_id
                    __token = 9068
                    try:
                        __zt_tmp = __attrs_140386179457552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140386186296528('path', u'info/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((u' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179458384
                    __default_140386179458384 = _DEFAULT_MARKER

                    # <Boolean u"python: default_profile==info['id'] and 'checked' or nothing" (149:45)> -> __attr_checked
                    __token = 9176
                    try:
                        __zt_tmp = __attrs_140386179457552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_140386186296528('python', u" default_profile==info['id'] and 'checked' or nothing", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = u'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((u' checked="%s"' % __attr_checked))
                    __append(u' />\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fae345bad50> name=None at 7fae345bab90> -> __attrs_140386177530064
                    __attrs_140386177530064 = _static_140386179460432

                    # <tal ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<tal')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179459408
                    __default_140386179459408 = _DEFAULT_MARKER

                    # <Substitution u'info/id' (151:43)> -> __attr_for
                    __token = 9309
                    try:
                        __zt_tmp = __attrs_140386177530064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_140386186296528('path', u'info/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((u' for="%s"' % __attr_for))
                    __append(u'>')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179458128
                    __default_140386179458128 = _DEFAULT_MARKER

                    # <Value u'info/title' (152:36)> -> __cache_140386179458576
                    __token = 9354
                    try:
                        __zt_tmp = __attrs_140386177530064
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386179458576 = _static_140386186296528('path', u'info/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'info/title' (152:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae345ba710> -> __condition
                    __expression = __cache_140386179458576

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u' Profile title ')
                    else:
                        __content = __cache_140386179458576
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</tal>\n              </label>\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae343e3510> name=None at 7fae343e3b10> -> __attrs_140386177528912
                    __attrs_140386177528912 = _static_140386177529104

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="formHelp">')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386177528080
                    __default_140386177528080 = _DEFAULT_MARKER

                    # <Value u'info/description' (154:49)> -> __cache_140386179446480
                    __token = 9460
                    try:
                        __zt_tmp = __attrs_140386177528912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386179446480 = _static_140386186296528('path', u'info/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'info/description' (154:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae343e3ed0> -> __condition
                    __expression = __cache_140386179446480

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'\n                Profile description\n              ')
                    else:
                        __content = __cache_140386179446480
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</div>\n            ')
                    ____index_140386179445776 -= 1
                    if (____index_140386179445776 > 0):
                        __append('')
                if (__backup_info_140386125765712 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_140386125765712
                __append(u'\n        </div>\n      ')
            __append(u'\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386125455568
            __attrs_140386125455568 = _static_140386247937936

            # <Value u'python: extension_profiles' (161:40)> -> __condition
            __token = 9642
            try:
                __zt_tmp = __attrs_140386125455568
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('python', u' extension_profiles', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:
                __append(u'\n        ')

                # <Static value=<_ast.Dict object at 0x7fae343e3850> name=None at 7fae343e3310> -> __attrs_140386178003664
                __attrs_140386178003664 = _static_140386177529936

                # <Negate value=<Value u'python: not advanced' (162:49)> at 7fae343e34d0> -> __cache_140386177529040

                # <Value u'python: not advanced' (162:49)> -> __cache_140386177529040
                __token = 9720
                try:
                    __zt_tmp = __attrs_140386178003664
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140386177529040 = _static_140386186296528('python', u' not advanced', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __cache_140386177529040 = not __cache_140386177529040
                __condition = __cache_140386177529040
                if __condition:

                    # <fieldset ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<fieldset id="add-on-list">')
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386178006736
                __attrs_140386178006736 = _static_140386247937936

                # <Value u'python: advanced' (163:51)> -> __condition
                __token = 9794
                try:
                    __zt_tmp = __attrs_140386178006736
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('python', u' advanced', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <legend ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<legend>')
                    __stream_140386178003216 = []
                    __append_140386178003216 = __stream_140386178003216.append
                    __append_140386178003216(u'\n            Add-ons\n          ')
                    __msgid_140386178003216 = __re_whitespace(''.join(__stream_140386178003216)).strip()
                    if __msgid_140386178003216:
                        __append(translate(__msgid_140386178003216, mapping=None, default=__msgid_140386178003216, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</legend>')
                __append(u'\n\n          ')

                # <Static value=<_ast.Dict object at 0x7fae34457b50> name=None at 7fae344575d0> -> __attrs_140386178005328
                __attrs_140386178005328 = _static_140386178005840

                # <Value u'python: advanced' (167:65)> -> __condition
                __token = 9919
                try:
                    __zt_tmp = __attrs_140386178005328
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('python', u' advanced', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="formHelp">')
                    __stream_140386178004368 = []
                    __append_140386178004368 = __stream_140386178004368.append
                    __append_140386178004368(u'\n              Select any add-ons you want to activate immediately. You can\n              also activate add-ons after the site has been created using the\n              Add-ons control panel.\n          ')
                    __msgid_140386178004368 = __re_whitespace(''.join(__stream_140386178004368)).strip()
                    if __msgid_140386178004368:
                        __append(translate(__msgid_140386178004368, mapping=None, default=__msgid_140386178004368, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</div>')
                __append(u'\n\n          ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386178003728
                __attrs_140386178003728 = _static_140386247937936
                __backup_info_140386128255888 = get('info', __marker)

                # <Value u'extension_profiles' (173:39)> -> __iterator
                __token = 10185
                try:
                    __zt_tmp = __attrs_140386178003728
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'extension_profiles', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386178004624, ) = getitem('repeat')(u'info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item
                    __append(u'\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae345aeb50> name=None at 7fae345ae2d0> -> __attrs_140386179407952
                    __attrs_140386179407952 = _static_140386179410768

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="addons-group">\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386179410640
                    __attrs_140386179410640 = _static_140386247937936
                    __backup_selected_140386126123792 = get('selected', __marker)

                    # <Value u'info/selected|nothing' (175:45)> -> __value
                    __token = 10290
                    try:
                        __zt_tmp = __attrs_140386179410640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'info/selected|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386179409552
                    __attrs_140386179409552 = _static_140386247937936

                    # <Value u'python: not selected or advanced' (176:43)> -> __condition
                    __token = 10357
                    try:
                        __zt_tmp = __attrs_140386179409552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('python', u' not selected or advanced', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386125449424
                        __attrs_140386125449424 = _static_140386247937936

                        # <Value u'python: advanced' (177:38)> -> __condition
                        __token = 10430
                        try:
                            __zt_tmp = __attrs_140386125449424
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('python', u' advanced', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div>\n                    ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386125447440
                            __attrs_140386125447440 = _static_140386247937936

                            # <label ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<label>\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae31238850> name=None at 7fae31238810> -> __attrs_140386192670096
                            __attrs_140386192670096 = _static_140386125449296

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input type="checkbox" name="extension_ids:list"')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386125447696
                            __default_140386125447696 = _DEFAULT_MARKER

                            # <Substitution u'info/id' (180:49)> -> __attr_value
                            __token = 10608
                            try:
                                __zt_tmp = __attrs_140386192670096
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140386186296528('path', u'info/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386125450000
                            __default_140386125450000 = _DEFAULT_MARKER

                            # <Substitution u'info/id' (181:45)> -> __attr_id
                            __token = 10662
                            try:
                                __zt_tmp = __attrs_140386192670096
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_140386186296528('path', u'info/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_id is not None):
                                __append((u' id="%s"' % __attr_id))

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386192670672
                            __default_140386192670672 = _DEFAULT_MARKER

                            # <Boolean u'info/selected|nothing' (182:49)> -> __attr_checked
                            __token = 10721
                            try:
                                __zt_tmp = __attrs_140386192670096
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_checked = _static_140386186296528('path', u'info/selected|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if (__attr_checked is _DEFAULT_MARKER):
                                __attr_checked = None
                            else:
                                if __attr_checked:
                                    __attr_checked = u'checked'
                                else:
                                    __attr_checked = None
                            if (__attr_checked is not None):
                                __append((u' checked="%s"' % __attr_checked))
                            __append(u' />\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae35253dd0> name=None at 7fae35253750> -> __attrs_140386192669712
                            __attrs_140386192669712 = _static_140386192670160

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386192667792
                            __default_140386192667792 = _DEFAULT_MARKER

                            # <Substitution u'info/id' (184:46)> -> __attr_for
                            __token = 10826
                            try:
                                __zt_tmp = __attrs_140386192669712
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_for = _static_140386186296528('path', u'info/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_for is not None):
                                __append((u' for="%s"' % __attr_for))
                            __append(u'>')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386192669520
                            __default_140386192669520 = _DEFAULT_MARKER

                            # <Value u'info/title' (185:39)> -> __cache_140386192670544
                            __token = 10874
                            try:
                                __zt_tmp = __attrs_140386192669712
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140386192670544 = _static_140386186296528('path', u'info/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                            # <BinOp left=<Value u'info/title' (185:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae35253310> -> __condition
                            __expression = __cache_140386192670544

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'profile title')
                            else:
                                __content = __cache_140386192670544
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</span>\n                    </label>\n                  </div>')
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae35253b90> name=None at 7fae352536d0> -> __attrs_140386192668880
                        __attrs_140386192668880 = _static_140386192669584

                        # <Value u'python: advanced' (188:84)> -> __condition
                        __token = 11045
                        try:
                            __zt_tmp = __attrs_140386192668880
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('python', u' advanced', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<p class="formHelp">')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386192666896
                            __default_140386192666896 = _DEFAULT_MARKER

                            # <Value u'info/description' (188:51)> -> __cache_140386125450192
                            __token = 11012
                            try:
                                __zt_tmp = __attrs_140386192668880
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140386125450192 = _static_140386186296528('path', u'info/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                            # <BinOp left=<Value u'info/description' (188:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae31238690> -> __condition
                            __expression = __cache_140386125450192

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'\n                    profile description\n                  ')
                            else:
                                __content = __cache_140386125450192
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(u'</p>')
                        __append(u'\n                ')
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386179411728
                    __attrs_140386179411728 = _static_140386247937936

                    # <Value u'python: selected and not advanced' (192:43)> -> __condition
                    __token = 11200
                    try:
                        __zt_tmp = __attrs_140386179411728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('python', u' selected and not advanced', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae35dfa4d0> name=None at 7fae35dfac10> -> __attrs_140386204885648
                        __attrs_140386204885648 = _static_140386204886224

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="hidden" name="extension_ids:list"')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204887056
                        __default_140386204887056 = _DEFAULT_MARKER

                        # <Substitution u'info/id' (194:47)> -> __attr_value
                        __token = 11357
                        try:
                            __zt_tmp = __attrs_140386204885648
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140386186296528('path', u'info/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', u'', _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386204888848
                        __default_140386204888848 = _DEFAULT_MARKER

                        # <Boolean u'info/selected|nothing' (195:48)> -> __attr_checked
                        __token = 11414
                        try:
                            __zt_tmp = __attrs_140386204885648
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_checked = _static_140386186296528('path', u'info/selected|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if (__attr_checked is _DEFAULT_MARKER):
                            __attr_checked = None
                        else:
                            if __attr_checked:
                                __attr_checked = u'checked'
                            else:
                                __attr_checked = None
                        if (__attr_checked is not None):
                            __append((u' checked="%s"' % __attr_checked))
                        __append(u' />\n                ')
                    __append(u'\n              ')
                    if (__backup_selected_140386126123792 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140386126123792
                    __append(u'\n            </div>\n          ')
                    ____index_140386178004624 -= 1
                    if (____index_140386178004624 > 0):
                        __append('')
                if (__backup_info_140386128255888 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_140386128255888
                __append(u'\n\n        ')
                __condition = __cache_140386177529040
                if __condition:
                    __append(u'</fieldset>')
                __append(u'\n      ')
            __append(u'\n\n      ')

            # <Static value=<_ast.Dict object at 0x7fae34457b90> name=None at 7fae35df3e50> -> __attrs_140386179410960
            __attrs_140386179410960 = _static_140386178005904

            # <div ... (0:0)
            # --------------------------------------------------------
            __append(u'<div class="formControls">\n        ')

            # <Static value=<_ast.Dict object at 0x7fae345ae9d0> name=None at 7fae345ae650> -> __attrs_140386204886480
            __attrs_140386204886480 = _static_140386179410384

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="hidden" name="form.submitted:boolean" value="True" />\n        ')

            # <Static value=<_ast.Dict object at 0x7fae35dfad50> name=None at 7fae35dfad90> -> __attrs_140386179474448
            __attrs_140386179474448 = _static_140386204888400

            # <input ... (0:0)
            # --------------------------------------------------------
            __append(u'<input type="submit" name="submit"')

            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386179476432
            __default_140386179476432 = _DEFAULT_MARKER

            # <Translate msgid=None node=<_ast.Str object at 0x7fae345bec50> at 7fae345be9d0> -> __attr_value
            __attr_value = u'Create Plone Site'
            __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
            if (__attr_value is not None):
                __append((u' value="%s"' % __attr_value))
            __append(u' />\n      </div>\n\n  </form>')
            if (__backup_advanced_140386126059280 is __marker):
                del econtext['advanced']
            else:
                econtext['advanced'] = __backup_advanced_140386126059280
            if (__backup_extension_profiles_140386126059472 is __marker):
                del econtext['extension_profiles']
            else:
                econtext['extension_profiles'] = __backup_extension_profiles_140386126059472
            if (__backup_default_profile_140386126060048 is __marker):
                del econtext['default_profile']
            else:
                econtext['default_profile'] = __backup_default_profile_140386126060048
            if (__backup_base_profiles_140386126059728 is __marker):
                del econtext['base_profiles']
            else:
                econtext['base_profiles'] = __backup_base_profiles_140386126059728
            if (__backup_profiles_140386127690128 is __marker):
                del econtext['profiles']
            else:
                econtext['profiles'] = __backup_profiles_140386127690128
            __append(u'\n</article>\n</div>\n  </body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140386204878416
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
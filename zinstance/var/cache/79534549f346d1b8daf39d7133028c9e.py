# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/skins/plone_prefs/portlet_prefs.pt'

__tokens = {322: (u"python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", 8, 28), 428: (u" python:controlPanel.getGroups('site'", 9, 21), 490: (u'l controlPanel/site_u', 10, 22), 638: (u'controlPanel/maySeeSomeConfiglets', 14, 19), 758: (u'string:${site_url}/@@overview-controlpanel', 17, 32), 967: (u'groups', 24, 28), 1021: (u"python:controlPanel.enumConfiglets(group=group['id'])", 26, 44), 1112: (u'configlets', 27, 36), 1160: (u'group/title', 28, 35), 1344: (u'configlets', 31, 56), 1394: (u'configlet/visible', 32, 37), 1489: (u'configlet/icon|nothing', 34, 42), 1559: (u'configlet/url', 35, 46), 1629: (u'configlet/title', 36, 54)}

from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386070706320 = {u'href': u'', }
_static_140386076992464 = {u'class': u'configlets', }
_static_140386069282640 = {u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386076994768 = {u'href': u'', }
_static_140386186296528 = __compile_zt_expr
_static_140386070728464 = {u'class': u'portletHeader', }
_static_140386077039824 = {u'class': u'configlets', }
_static_140386070113424 = {u'class': u'portletContent', }
_static_140386070725328 = {u'role': u'section', u'class': u'portlet portletNavigationTree portletSiteSetup', u'id': u'portlet-prefs', }
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

    def render_portlet(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069357200
            __attrs_140386069357200 = _static_140386247937936
            __backup_controlPanel_140386069379408 = get('controlPanel', __marker)

            # <Value u"python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (8:28)> -> __value
            __token = 322
            try:
                __zt_tmp = __attrs_140386069357200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['controlPanel'] = __value
            __backup_groups_140386080021392 = get('groups', __marker)

            # <Value u"python:controlPanel.getGroups('site')" (9:21)> -> __value
            __token = 428
            try:
                __zt_tmp = __attrs_140386069357200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('python', u"controlPanel.getGroups('site')", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['groups'] = __value
            __backup_site_url_140386076812688 = get('site_url', __marker)

            # <Value u'controlPanel/site_url' (10:22)> -> __value
            __token = 490
            try:
                __zt_tmp = __attrs_140386069357200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140386186296528('path', u'controlPanel/site_url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            econtext['site_url'] = __value
            __append(u'\n\n')

            # <Static value=<_ast.Dict object at 0x7fae2de082d0> name=None at 7fae2dca71d0> -> __attrs_140386070728592
            __attrs_140386070728592 = _static_140386070725328

            # <Value u'controlPanel/maySeeSomeConfiglets' (14:19)> -> __condition
            __token = 638
            try:
                __zt_tmp = __attrs_140386070728592
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140386186296528('path', u'controlPanel/maySeeSomeConfiglets', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            if __condition:

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section class="portlet portletNavigationTree portletSiteSetup" role="section" id="portlet-prefs">\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2de08f10> name=None at 7fae2de08950> -> __attrs_140386070727952
                __attrs_140386070727952 = _static_140386070728464

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header class="portletHeader">\n        ')

                # <Static value=<_ast.Dict object at 0x7fae2de03890> name=None at 7fae2de03c10> -> __attrs_140386070112528
                __attrs_140386070112528 = _static_140386070706320

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070112208
                __default_140386070112208 = _DEFAULT_MARKER

                # <Substitution u'string:${site_url}/@@overview-controlpanel' (17:32)> -> __attr_href
                __token = 758
                try:
                    __zt_tmp = __attrs_140386070112528
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140386186296528('string', u'${site_url}/@@overview-controlpanel', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>')
                __stream_140386070706832 = []
                __append_140386070706832 = __stream_140386070706832.append
                __append_140386070706832(u'Site Setup')
                __msgid_140386070706832 = __re_whitespace(''.join(__stream_140386070706832)).strip()
                if __msgid_140386070706832:
                    __append(translate(__msgid_140386070706832, mapping=None, default=__msgid_140386070706832, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</a>\n  </header>\n\n  ')

                # <Static value=<_ast.Dict object at 0x7fae2dd72c90> name=None at 7fae2dd72690> -> __attrs_140386077037328
                __attrs_140386077037328 = _static_140386070113424

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append(u'<nav class="portletContent">\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e40dcd0> name=None at 7fae2e40d450> -> __attrs_140386077038416
                __attrs_140386077038416 = _static_140386077039824

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="configlets">\n      ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077242192
                __attrs_140386077242192 = _static_140386247937936

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li>')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077244176
                __attrs_140386077244176 = _static_140386247937936
                __backup_group_140386080020560 = get('group', __marker)

                # <Value u'groups' (24:28)> -> __iterator
                __token = 967
                try:
                    __zt_tmp = __attrs_140386077244176
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'groups', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386077243920, ) = getitem('repeat')(u'group', __iterator)
                econtext['group'] = None
                for __item in __iterator:
                    econtext['group'] = __item
                    __append(u'\n\n          ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077243728
                    __attrs_140386077243728 = _static_140386247937936
                    __backup_configlets_140386077082128 = get('configlets', __marker)

                    # <Value u"python:controlPanel.enumConfiglets(group=group['id'])" (26:44)> -> __value
                    __token = 1021
                    try:
                        __zt_tmp = __attrs_140386077243728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u"controlPanel.enumConfiglets(group=group['id'])", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['configlets'] = __value

                    # <Value u'configlets' (27:36)> -> __condition
                    __token = 1112
                    try:
                        __zt_tmp = __attrs_140386077243728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'configlets', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077245328
                        __attrs_140386077245328 = _static_140386247937936

                        # <strong ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<strong>')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077245136
                        __default_140386077245136 = _DEFAULT_MARKER

                        # <Value u'group/title' (28:35)> -> __cache_140386077242960
                        __token = 1160
                        try:
                            __zt_tmp = __attrs_140386077245328
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386077242960 = _static_140386186296528('path', u'group/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'group/title' (28:35)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e43f5d0> -> __condition
                        __expression = __cache_140386077242960

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Plone Configlet Group Title')
                        else:
                            __content = __cache_140386077242960
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</strong>\n              ')

                        # <Static value=<_ast.Dict object at 0x7fae2e4023d0> name=None at 7fae2e402d50> -> __attrs_140386076991824
                        __attrs_140386076991824 = _static_140386076992464

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<ul class="configlets">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076994832
                        __attrs_140386076994832 = _static_140386247937936
                        __backup_configlet_140386080111184 = get('configlet', __marker)

                        # <Value u'configlets' (31:56)> -> __iterator
                        __token = 1344
                        try:
                            __zt_tmp = __attrs_140386076994832
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140386186296528('path', u'configlets', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        (__iterator, ____index_140386076994256, ) = getitem('repeat')(u'configlet', __iterator)
                        econtext['configlet'] = None
                        for __item in __iterator:
                            econtext['configlet'] = __item
                            __append(u'\n                  ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076995088
                            __attrs_140386076995088 = _static_140386247937936

                            # <Value u'configlet/visible' (32:37)> -> __condition
                            __token = 1394
                            try:
                                __zt_tmp = __attrs_140386076995088
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('path', u'configlet/visible', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <li ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<li>\n                      ')

                                # <Static value=<_ast.Dict object at 0x7fae2e402cd0> name=None at 7fae2e402d90> -> __attrs_140386080028688
                                __attrs_140386080028688 = _static_140386076994768
                                __backup_icon_140386080021584 = get('icon', __marker)

                                # <Value u'configlet/icon|nothing' (34:42)> -> __value
                                __token = 1489
                                try:
                                    __zt_tmp = __attrs_140386080028688
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140386186296528('path', u'configlet/icon|nothing', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                econtext['icon'] = __value

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<a')

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386080029136
                                __default_140386080029136 = _DEFAULT_MARKER

                                # <Substitution u'configlet/url' (35:46)> -> __attr_href
                                __token = 1559
                                try:
                                    __zt_tmp = __attrs_140386080028688
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140386186296528('path', u'configlet/url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((u' href="%s"' % __attr_href))
                                __append(u'>\n                      ')

                                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080027792
                                __attrs_140386080027792 = _static_140386247937936

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386080030160
                                __default_140386080030160 = _DEFAULT_MARKER

                                # <Value u'configlet/title' (36:54)> -> __cache_140386080028176
                                __token = 1629
                                try:
                                    __zt_tmp = __attrs_140386080027792
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140386080028176 = _static_140386186296528('path', u'configlet/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                                # <BinOp left=<Value u'configlet/title' (36:54)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e6e7710> -> __condition
                                __expression = __cache_140386080028176

                                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140386080028176
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                                __append(u'\n                      </a>')
                                if (__backup_icon_140386080021584 is __marker):
                                    del econtext['icon']
                                else:
                                    econtext['icon'] = __backup_icon_140386080021584
                                __append(u'\n                  </li>')
                            __append(u'\n                  ')
                            ____index_140386076994256 -= 1
                            if (____index_140386076994256 > 0):
                                __append('')
                        if (__backup_configlet_140386080111184 is __marker):
                            del econtext['configlet']
                        else:
                            econtext['configlet'] = __backup_configlet_140386080111184
                        __append(u'\n              </ul>\n          ')
                    if (__backup_configlets_140386077082128 is __marker):
                        del econtext['configlets']
                    else:
                        econtext['configlets'] = __backup_configlets_140386077082128
                    __append(u'\n      ')
                    ____index_140386077243920 -= 1
                    if (____index_140386077243920 > 0):
                        __append('')
                if (__backup_group_140386080020560 is __marker):
                    del econtext['group']
                else:
                    econtext['group'] = __backup_group_140386080020560
                __append(u'</li>\n    </ul>\n  </nav>\n\n</section>')
            __append(u'\n\n')
            if (__backup_site_url_140386076812688 is __marker):
                del econtext['site_url']
            else:
                econtext['site_url'] = __backup_site_url_140386076812688
            if (__backup_groups_140386080021392 is __marker):
                del econtext['groups']
            else:
                econtext['groups'] = __backup_groups_140386080021392
            if (__backup_controlPanel_140386069379408 is __marker):
                del econtext['controlPanel']
            else:
                econtext['controlPanel'] = __backup_controlPanel_140386069379408
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

            # <Static value=<_ast.Dict object at 0x7fae2dca7f50> name=None at 7fae2dca7110> -> __attrs_140386069280528
            __attrs_140386069280528 = _static_140386069282640
            __previous_i18n_domain_140386077015248 = __i18n_domain
            __i18n_domain = u'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077012240
            __attrs_140386077012240 = _static_140386247937936

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>\n')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append(u'\n</body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140386077015248
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {u'render_portlet': render_portlet, 'render': render, }
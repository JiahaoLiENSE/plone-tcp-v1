# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/controlpanel/browser/quickinstaller.pt'

__tokens = {459: (u'string:$portal_url/@@overview-controlpanel', 14, 28), 1362: (u'view/get_upgrades', 41, 38), 1418: (u' python:len(products', 42, 37), 1603: (u'not:products', 45, 34), 1981: (u'products', 51, 57), 2077: (u'products', 53, 49), 2122: (u'product/id', 54, 34), 2389: (u'pid', 58, 59), 2672: (u'string:Upgrade ${pid}', 64, 47), 2780: (u'product/title', 67, 37), 2995: (u'product/description', 72, 43), 3029: (u'product/description', 72, 77), 3160: (u'pid', 73, 62), 3207: (u'product/version', 73, 109), 3355: (u'product/upgrade_info', 76, 47), 3552: (u'not:upgrade_info/hasProfile', 80, 43), 3742: (u'upgrade_info/installedVersion', 82, 81), 3864: (u'upgrade_info/hasProfile', 84, 43), 4075: (u'upgrade_info/installedVersion', 86, 91), 4344: (u'upgrade_info/newVersion', 89, 90), 4496: (u'not:upgrade_info/available', 93, 42), 5024: (u'python:num_products > 1', 104, 33), 5167: (u'products', 106, 54), 5344: (u'product/id', 109, 48), 5972: (u'view/get_available', 125, 38), 6029: (u' python:len(products', 126, 37), 6306: (u'products', 131, 38), 6356: (u'product/id', 132, 39), 6590: (u'pid', 136, 49), 6910: (u'product/title', 145, 37), 7125: (u'product/description', 150, 43), 7217: (u'product/description', 152, 33), 7330: (u'pid', 153, 62), 7377: (u'product/version', 153, 109), 7551: (u'not:product/uninstall_profile', 157, 35), 7885: (u'view/get_installed', 167, 38), 7942: (u' python:len(products', 168, 37), 8223: (u'products', 173, 40), 8275: (u'product/id', 174, 41), 8514: (u'pid', 178, 48), 8747: (u'product/uninstall_profile', 183, 42), 8919: (u'product/title', 187, 41), 9154: (u'product/description', 192, 47), 9254: (u'product/description', 194, 37), 9371: (u'pid', 195, 66), 9418: (u'product/version', 195, 113), 9605: (u'not:product/uninstall_profile', 199, 39), 9954: (u'view/get_broken', 209, 38), 10012: (u' python:len(products', 210, 41), 10068: (u'num_products', 211, 32), 10336: (u'products', 216, 38), 10405: (u'product/product_id', 218, 37), 10619: (u'product/type', 223, 37), 10734: (u'product/value', 224, 65), 261: (u'context/prefs_main_template/macros/master', 6, 23), 261: (u'context/prefs_main_template/macros/master', 6, 23)}

from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386069308304 = {u'id': u'install-products', u'class': u'portlet', }
_static_140386080006416 = {u'role': u'status', u'class': u'portalMessage info', }
_static_140386070113616 = {u'id': u'broken-products', u'class': u'portlet', }
_static_140386069309712 = {u'class': u'configlets', }
_static_140386077072592 = {u'class': u'portletHeader', }
_static_140386069308176 = {u'class': u'portletContent', }
_static_140386076992080 = {u'class': u'discreet', }
_static_140386077070160 = {u'class': u'configlets', }
_static_140386069282256 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140386080083536 = {u'action': u'uninstall_products', u'method': u'post', u'class': u'pull-right', }
_static_140386247937936 = {}
_static_140386070744336 = {u'type': u'hidden', u'name': u'prefs_reinstallProducts:list', u'value': u'product', }
_static_140386080045008 = {u'id': u'content-core', }
_static_140386070514960 = {u'class': u'portletHeader', }
_static_140386080090704 = {u'class': u'configletDescription discreet', }
_static_140386069243984 = {u'class': u'discreet', }
_static_140386077081360 = {u'type': u'submit', u'class': u'context', u'value': u'Upgrade them ALL!', u'name': u'form.submitted', }
_static_140386069274832 = {u'class': u'configletDescription discreet', }
_static_140386080046352 = {u'class': u'documentFirstHeading', }
_static_140386069215248 = {u'type': u'hidden', u'name': u'prefs_reinstallProducts:list', u'value': u'pid', }
_static_140386077070800 = {u'id': u'activated-products', u'class': u'portlet', }
_static_140386069245456 = {u'class': u'configletDetails', }
_static_140386070512208 = {u'class': u'portletContent', }
_static_140386069185104 = u'master'
_static_140386077014352 = {u'class': u'portletContent', }
_static_140386077072336 = {u'class': u'portletContent', }
_static_140386080104016 = {u'id': u'upgrade-products', u'class': u'portlet', }
_static_140386072421648 = {u'href': u'string:$portal_url/@@overview-controlpanel', u'id': u'setup-link', u'class': u'link-parent', }
_static_140386080027984 = {u'class': u'configlets', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386080101968 = {u'class': u'discreet', }
_static_140386080028880 = {u'class': u'portletContent', }
_static_140386080037520 = {u'action': u'install_products', u'method': u'post', u'class': u'pull-right', }
_static_140386070727696 = {u'role': u'status', u'id': u'up-to-date-message', u'class': u'portalMessage info', }
_static_140386077022032 = {u'action': u'upgrade_products', u'method': u'post', }
_static_140386079999568 = {u'class': u'configletDescription discreet', }
_static_140386077015760 = {u'class': u'portletHeader', }
_static_140386080022800 = {u'type': u'submit', u'class': u'context', u'value': u'Install', u'name': u'form.submitted', }
_static_140386076992784 = {u'class': u'configletDescription discreet', }
_static_140386069110736 = {u'class': u'discreet', }
_static_140386080101136 = {u'href': u'http://docs.plone.org/manage/installing/installing_addons.html', }
_static_140386080082704 = {u'type': u'hidden', u'name': u'uninstall_product', u'value': u'pid', }
_static_140386076986704 = {u'type': u'submit', u'class': u'destructive', u'value': u'Uninstall', u'name': u'form.submitted', }
_static_140386069278864 = {u'class': u'discreet', }
_static_140386080044496 = {u'class': u'documentDescription', }
_static_140386186296528 = __compile_zt_expr
_static_140386070128208 = {u'class': u'portletHeader', }
_static_140386069216528 = {u'type': u'submit', u'class': u'standalone', u'value': u'Upgrade ${pid}', u'name': u'form.submitted', }
_static_140386070110864 = {u'class': u'configlets', }
_static_140386077041232 = {u'action': u'upgrade_products', u'method': u'post', u'class': u'pull-right', }
_static_140386080024208 = {u'type': u'hidden', u'name': u'install_product', u'value': u'pid', }

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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069185680
            __attrs_140386069185680 = _static_140386247937936
            __backup_macroname_140386117433216 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fae2dc90250> name=None at 7fae2dc90590> -> __value
            __value = _static_140386069185104
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069186640
                __attrs_140386069186640 = _static_140386247937936
                __previous_i18n_domain_140386072421904 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2dfa6510> name=None at 7fae2dfa6f10> -> __attrs_140386080046864
                __attrs_140386080046864 = _static_140386072421648

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a id="setup-link" class="link-parent"')

                # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386072420496
                __default_140386072420496 = _DEFAULT_MARKER

                # <Substitution u'string:$portal_url/@@overview-controlpanel' (14:28)> -> __attr_href
                __token = 459
                try:
                    __zt_tmp = __attrs_140386080046864
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140386186296528('string', u'$portal_url/@@overview-controlpanel', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>')
                __stream_140386072421776 = []
                __append_140386072421776 = __stream_140386072421776.append
                __append_140386072421776(u'\n        Site Setup\n    ')
                __msgid_140386072421776 = __re_whitespace(''.join(__stream_140386072421776)).strip()
                if __msgid_140386072421776:
                    __append(translate(__msgid_140386072421776, mapping=None, default=__msgid_140386072421776, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</a>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e6ebd10> name=None at 7fae2e6ebbd0> -> __attrs_140386080044816
                __attrs_140386080044816 = _static_140386080046352

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1 class="documentFirstHeading">')
                __stream_140386080044240 = []
                __append_140386080044240 = __stream_140386080044240.append
                __append_140386080044240(u'Add-ons')
                __msgid_140386080044240 = __re_whitespace(''.join(__stream_140386080044240)).strip()
                if __msgid_140386080044240:
                    __append(translate(__msgid_140386080044240, mapping=None, default=__msgid_140386080044240, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</h1>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e6eb5d0> name=None at 7fae2e6eb250> -> __attrs_140386080045520
                __attrs_140386080045520 = _static_140386080044496

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="documentDescription">')
                __stream_140386080045712 = []
                __append_140386080045712 = __stream_140386080045712.append
                __append_140386080045712(u'\n      This is the Add-on configuration section, you can activate and deactivate\n      add-ons in the lists below.\n    ')
                __msgid_140386080045712 = __re_whitespace(''.join(__stream_140386080045712)).strip()
                if __msgid_140386080045712:
                    __append(translate(__msgid_140386080045712, mapping=None, default=__msgid_140386080045712, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</div>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e6eb7d0> name=None at 7fae2e6eb450> -> __attrs_140386080103632
                __attrs_140386080103632 = _static_140386080045008

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="content-core">\n\n        ')

                # <Static value=<_ast.Dict object at 0x7fae2e6f9650> name=None at 7fae2e6f9d10> -> __attrs_140386080100880
                __attrs_140386080100880 = _static_140386080101968

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="discreet">')
                __stream_140386072383808_third_party_product = ''
                __stream_140386080102096 = []
                __append_140386080102096 = __stream_140386080102096.append
                __append_140386080102096(u'\n          To make new add-ons show up here, add them to your buildout\n          configuration, run buildout, and restart the server process.\n          For detailed instructions see\n          ')
                __stream_140386072383808_third_party_product = []
                __append_140386072383808_third_party_product = __stream_140386072383808_third_party_product.append

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080101456
                __attrs_140386080101456 = _static_140386247937936

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_140386072383808_third_party_product(u'<span>\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2e6f9310> name=None at 7fae2e6f9610> -> __attrs_140386077013456
                __attrs_140386077013456 = _static_140386080101136

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_140386072383808_third_party_product(u'<a href="http://docs.plone.org/manage/installing/installing_addons.html">')
                __stream_140386080104080 = []
                __append_140386080104080 = __stream_140386080104080.append
                __append_140386080104080(u'\n            Installing a third party add-on\n          ')
                __msgid_140386080104080 = __re_whitespace(''.join(__stream_140386080104080)).strip()
                if __msgid_140386080104080:
                    __append_140386072383808_third_party_product(translate(__msgid_140386080104080, mapping=None, default=__msgid_140386080104080, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append_140386072383808_third_party_product(u'</a>\n          </span>')
                __append_140386080102096(u'${third_party_product}')
                __stream_140386072383808_third_party_product = ''.join(__stream_140386072383808_third_party_product)
                __append_140386080102096(u'.\n        ')
                __msgid_140386080102096 = __re_whitespace(''.join(__stream_140386080102096)).strip()
                if __msgid_140386080102096:
                    __append(translate(__msgid_140386080102096, mapping={u'third_party_product': __stream_140386072383808_third_party_product, }, default=__msgid_140386080102096, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</p>\n\n        ')

                # <Static value=<_ast.Dict object at 0x7fae2e6f9e50> name=None at 7fae2e6f9850> -> __attrs_140386077012432
                __attrs_140386077012432 = _static_140386080104016
                __backup_products_140386069186320 = get('products', __marker)

                # <Value u'view/get_upgrades' (41:38)> -> __value
                __token = 1362
                try:
                    __zt_tmp = __attrs_140386077012432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/get_upgrades', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140386080044560 = get('num_products', __marker)

                # <Value u'python:len(products)' (42:37)> -> __value
                __token = 1418
                try:
                    __zt_tmp = __attrs_140386077012432
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('python', u'len(products)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="upgrade-products" class="portlet">\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2e407ed0> name=None at 7fae2e407790> -> __attrs_140386077013328
                __attrs_140386077013328 = _static_140386077015760

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header class="portletHeader">')
                __stream_140386077015888 = []
                __append_140386077015888 = __stream_140386077015888.append
                __append_140386077015888(u'Upgrades')
                __msgid_140386077015888 = __re_whitespace(''.join(__stream_140386077015888)).strip()
                if __msgid_140386077015888:
                    __append(translate(__msgid_140386077015888, mapping=None, default=__msgid_140386077015888, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2e407950> name=None at 7fae2e407dd0> -> __attrs_140386070728144
                __attrs_140386070728144 = _static_140386077014352

                # <Value u'not:products' (45:34)> -> __condition
                __token = 1603
                try:
                    __zt_tmp = __attrs_140386070728144
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('not', u'products', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section class="portletContent">\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae2de08c10> name=None at 7fae2de08f50> -> __attrs_140386070725072
                    __attrs_140386070725072 = _static_140386070727696

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="up-to-date-message" class="portalMessage info" role="status">\n                 ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069311440
                    __attrs_140386069311440 = _static_140386247937936

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140386069311376 = []
                    __append_140386069311376 = __stream_140386069311376.append
                    __append_140386069311376(u'No upgrades in this corner')
                    __msgid_140386069311376 = __re_whitespace(''.join(__stream_140386069311376)).strip()
                    if __msgid_140386069311376:
                        __append(translate(__msgid_140386069311376, mapping=None, default=__msgid_140386069311376, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n                 ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069308752
                    __attrs_140386069308752 = _static_140386247937936

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140386069307664 = []
                    __append_140386069307664 = __stream_140386069307664.append
                    __append_140386069307664(u'You are up to date. High fives.')
                    __msgid_140386069307664 = __re_whitespace(''.join(__stream_140386069307664)).strip()
                    if __msgid_140386069307664:
                        __append(translate(__msgid_140386069307664, mapping=None, default=__msgid_140386069307664, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n             </div>\n          </section>')
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2dcae310> name=None at 7fae2de08fd0> -> __attrs_140386069309648
                __attrs_140386069309648 = _static_140386069308176

                # <Value u'products' (51:57)> -> __condition
                __token = 1981
                try:
                    __zt_tmp = __attrs_140386069309648
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'products', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section class="portletContent">\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae2dcae910> name=None at 7fae2dcaedd0> -> __attrs_140386077043472
                    __attrs_140386077043472 = _static_140386069309712

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul class="configlets">\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077041360
                    __attrs_140386077041360 = _static_140386247937936
                    __backup_product_140386077014608 = get('product', __marker)

                    # <Value u'products' (53:49)> -> __iterator
                    __token = 2077
                    try:
                        __zt_tmp = __attrs_140386077041360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140386186296528('path', u'products', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    (__iterator, ____index_140386077043024, ) = getitem('repeat')(u'product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077043216
                        __attrs_140386077043216 = _static_140386247937936
                        __backup_pid_140386069307792 = get('pid', __marker)

                        # <Value u'product/id' (54:34)> -> __value
                        __token = 2122
                        try:
                            __zt_tmp = __attrs_140386077043216
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('path', u'product/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['pid'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fae2e40e250> name=None at 7fae2e40e890> -> __attrs_140386069216656
                        __attrs_140386069216656 = _static_140386077041232

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<form action="upgrade_products" method="post" class="pull-right">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae2dc97810> name=None at 7fae2dc97ad0> -> __attrs_140386069216976
                        __attrs_140386069216976 = _static_140386069215248

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="hidden" name="prefs_reinstallProducts:list"')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069217168
                        __default_140386069217168 = _DEFAULT_MARKER

                        # <Substitution u'pid' (58:59)> -> __attr_value
                        __token = 2389
                        try:
                            __zt_tmp = __attrs_140386069216976
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140386186296528('path', u'pid', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' />\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae2dc97d10> name=None at 7fae2dc976d0> -> __attrs_140386080092112
                        __attrs_140386080092112 = _static_140386069216528

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="standalone" type="submit"')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386080091408
                        __default_140386080091408 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<Substitution u'string:Upgrade ${pid}' (64:47)> at 7fae2e6f6910> -> __attr_value

                        # <Substitution u'string:Upgrade ${pid}' (64:47)> -> __attr_value
                        __token = 2672
                        try:
                            __zt_tmp = __attrs_140386080092112
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140386186296528('string', u'Upgrade ${pid}', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', u'Upgrade ${pid}', _DEFAULT_MARKER)
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' name="form.submitted"/>\n                </form>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080088336
                        __attrs_140386080088336 = _static_140386247937936

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h3>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080090832
                        __attrs_140386080090832 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386080088144
                        __default_140386080088144 = _DEFAULT_MARKER

                        # <Value u'product/title' (67:37)> -> __cache_140386080089168
                        __token = 2780
                        try:
                            __zt_tmp = __attrs_140386080090832
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386080089168 = _static_140386186296528('path', u'product/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/title' (67:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e6f6650> -> __condition
                        __expression = __cache_140386080089168

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>\n                    Add-on Name\n                  </span>')
                        else:
                            __content = __cache_140386080089168
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                </h3>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fae2e6f6a50> name=None at 7fae2e6f6e50> -> __attrs_140386080091280
                        __attrs_140386080091280 = _static_140386080090704

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p class="configletDescription discreet">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069245520
                        __attrs_140386069245520 = _static_140386247937936

                        # <Value u'product/description' (72:43)> -> __condition
                        __token = 2995
                        try:
                            __zt_tmp = __attrs_140386069245520
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('path', u'product/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069245200
                            __default_140386069245200 = _DEFAULT_MARKER

                            # <Value u'product/description' (72:77)> -> __cache_140386069243152
                            __token = 3029
                            try:
                                __zt_tmp = __attrs_140386069245520
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140386069243152 = _static_140386186296528('path', u'product/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                            # <BinOp left=<Value u'product/description' (72:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dc9e2d0> -> __condition
                            __expression = __cache_140386069243152

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'add-on description')
                            else:
                                __content = __cache_140386069243152
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae2dc9e850> name=None at 7fae2dc9e750> -> __attrs_140386069242000
                        __attrs_140386069242000 = _static_140386069243984

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<em class="discreet"> \u2013 (')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069241936
                        __attrs_140386069241936 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069243024
                        __default_140386069243024 = _DEFAULT_MARKER

                        # <Value u'pid' (73:62)> -> __cache_140386069242256
                        __token = 3160
                        try:
                            __zt_tmp = __attrs_140386069241936
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386069242256 = _static_140386186296528('path', u'pid', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'pid' (73:62)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dc9e290> -> __condition
                        __expression = __cache_140386069242256

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>plugin.app.name</span>')
                        else:
                            __content = __cache_140386069242256
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u' ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069300496
                        __attrs_140386069300496 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069300240
                        __default_140386069300240 = _DEFAULT_MARKER

                        # <Value u'product/version' (73:109)> -> __cache_140386069299600
                        __token = 3207
                        try:
                            __zt_tmp = __attrs_140386069300496
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386069299600 = _static_140386186296528('path', u'product/version', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/version' (73:109)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dcac050> -> __condition
                        __expression = __cache_140386069299600

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>1.0</span>')
                        else:
                            __content = __cache_140386069299600
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u')</em>\n                </p>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fae2dc9ee10> name=None at 7fae2dc9e3d0> -> __attrs_140386069300432
                        __attrs_140386069300432 = _static_140386069245456

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<ul class="configletDetails">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069299792
                        __attrs_140386069299792 = _static_140386247937936
                        __backup_upgrade_info_140386069216336 = get('upgrade_info', __marker)

                        # <Value u'product/upgrade_info' (76:47)> -> __value
                        __token = 3355
                        try:
                            __zt_tmp = __attrs_140386069299792
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140386186296528('path', u'product/upgrade_info', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        econtext['upgrade_info'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                      ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069302352
                        __attrs_140386069302352 = _static_140386247937936

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140386069303184 = []
                        __append_140386069303184 = __stream_140386069303184.append
                        __append_140386069303184(u'\n                        This addon has been upgraded.\n                      ')
                        __msgid_140386069303184 = __re_whitespace(''.join(__stream_140386069303184)).strip()
                        if __msgid_140386069303184:
                            __append(translate(__msgid_140386069303184, mapping=None, default=__msgid_140386069303184, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n                      ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077016272
                        __attrs_140386077016272 = _static_140386247937936

                        # <Value u'not:upgrade_info/hasProfile' (80:43)> -> __condition
                        __token = 3552
                        try:
                            __zt_tmp = __attrs_140386077016272
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('not', u'upgrade_info/hasProfile', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140386072231520_version = ''
                            __stream_140386069299984 = []
                            __append_140386069299984 = __stream_140386069299984.append
                            __append_140386069299984(u'\n                        Old version was ')
                            __stream_140386072231520_version = []
                            __append_140386072231520_version = __stream_140386072231520_version.append

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078080592
                            __attrs_140386078080592 = _static_140386247937936

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_140386072231520_version(u'<strong>')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386078077456
                            __default_140386078077456 = _DEFAULT_MARKER

                            # <Value u'upgrade_info/installedVersion' (82:81)> -> __cache_140386070542608
                            __token = 3742
                            try:
                                __zt_tmp = __attrs_140386078080592
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140386070542608 = _static_140386186296528('path', u'upgrade_info/installedVersion', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                            # <BinOp left=<Value u'upgrade_info/installedVersion' (82:81)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dddb650> -> __condition
                            __expression = __cache_140386070542608

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_140386072231520_version(u'version')
                            else:
                                __content = __cache_140386070542608
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_140386072231520_version(__content)
                            __append_140386072231520_version(u'</strong>')
                            __append_140386069299984(u'${version}')
                            __stream_140386072231520_version = ''.join(__stream_140386072231520_version)
                            __append_140386069299984(u'.\n                      ')
                            __msgid_140386069299984 = __re_whitespace(''.join(__stream_140386069299984)).strip()
                            if u'label_product_upgrade_old_version':
                                __append(translate(u'label_product_upgrade_old_version', mapping={u'version': __stream_140386072231520_version, }, default=__msgid_140386069299984, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>')
                        __append(u'\n                      ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070156112
                        __attrs_140386070156112 = _static_140386247937936

                        # <Value u'upgrade_info/hasProfile' (84:43)> -> __condition
                        __token = 3864
                        try:
                            __zt_tmp = __attrs_140386070156112
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('path', u'upgrade_info/hasProfile', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386078153168
                            __attrs_140386078153168 = _static_140386247937936
                            __stream_140386070857920_version = ''
                            __stream_140386078151824 = []
                            __append_140386078151824 = __stream_140386078151824.append
                            __append_140386078151824(u'\n                          Old profile version was ')
                            __stream_140386070857920_version = []
                            __append_140386070857920_version = __stream_140386070857920_version.append

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069972880
                            __attrs_140386069972880 = _static_140386247937936

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_140386070857920_version(u'<strong>')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070735696
                            __default_140386070735696 = _DEFAULT_MARKER

                            # <Value u'upgrade_info/installedVersion' (86:91)> -> __cache_140386071777552
                            __token = 4075
                            try:
                                __zt_tmp = __attrs_140386069972880
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140386071777552 = _static_140386186296528('path', u'upgrade_info/installedVersion', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                            # <BinOp left=<Value u'upgrade_info/installedVersion' (86:91)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2de0a790> -> __condition
                            __expression = __cache_140386071777552

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_140386070857920_version(u'version')
                            else:
                                __content = __cache_140386071777552
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_140386070857920_version(__content)
                            __append_140386070857920_version(u'</strong>')
                            __append_140386078151824(u'${version}')
                            __stream_140386070857920_version = ''.join(__stream_140386070857920_version)
                            __append_140386078151824(u'.\n                        ')
                            __msgid_140386078151824 = __re_whitespace(''.join(__stream_140386078151824)).strip()
                            if u'label_product_upgrade_old_profile_version':
                                __append(translate(u'label_product_upgrade_old_profile_version', mapping={u'version': __stream_140386070857920_version, }, default=__msgid_140386078151824, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069971280
                            __attrs_140386069971280 = _static_140386247937936
                            __stream_140386070857920_version = ''
                            __stream_140386078150864 = []
                            __append_140386078150864 = __stream_140386078150864.append
                            __append_140386078150864(u'\n                          New profile version is ')
                            __stream_140386070857920_version = []
                            __append_140386070857920_version = __stream_140386070857920_version.append

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077022928
                            __attrs_140386077022928 = _static_140386247937936

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_140386070857920_version(u'<strong>')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077022672
                            __default_140386077022672 = _DEFAULT_MARKER

                            # <Value u'upgrade_info/newVersion' (89:90)> -> __cache_140386071743824
                            __token = 4344
                            try:
                                __zt_tmp = __attrs_140386077022928
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140386071743824 = _static_140386186296528('path', u'upgrade_info/newVersion', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                            # <BinOp left=<Value u'upgrade_info/newVersion' (89:90)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e0711d0> -> __condition
                            __expression = __cache_140386071743824

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_140386070857920_version(u'version')
                            else:
                                __content = __cache_140386071743824
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_140386070857920_version(__content)
                            __append_140386070857920_version(u'</strong>')
                            __append_140386078150864(u'${version}')
                            __stream_140386070857920_version = ''.join(__stream_140386070857920_version)
                            __append_140386078150864(u'.\n                        ')
                            __msgid_140386078150864 = __re_whitespace(''.join(__stream_140386078150864)).strip()
                            if u'label_product_upgrade_new_profile_version':
                                __append(translate(u'label_product_upgrade_new_profile_version', mapping={u'version': __stream_140386070857920_version, }, default=__msgid_140386078150864, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'\n                      </span>')
                        __append(u'\n\n                      ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071741968
                        __attrs_140386071741968 = _static_140386247937936

                        # <Value u'not:upgrade_info/available' (93:42)> -> __condition
                        __token = 4496
                        try:
                            __zt_tmp = __attrs_140386071741968
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('not', u'upgrade_info/available', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div>\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077021072
                            __attrs_140386077021072 = _static_140386247937936

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<strong>')
                            __stream_140386077022480 = []
                            __append_140386077022480 = __stream_140386077022480.append
                            __append_140386077022480(u'Warning')
                            __msgid_140386077022480 = __re_whitespace(''.join(__stream_140386077022480)).strip()
                            if __msgid_140386077022480:
                                __append(translate(__msgid_140386077022480, mapping=None, default=__msgid_140386077022480, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</strong>\n                        ')

                            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077022224
                            __attrs_140386077022224 = _static_140386247937936

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140386077020752 = []
                            __append_140386077020752 = __stream_140386077020752.append
                            __append_140386077020752(u'There is no upgrade procedure defined for this\n                        addon. Please consult the addon documentation\n                        for upgrade information, or contact the addon\n                        author.')
                            __msgid_140386077020752 = __re_whitespace(''.join(__stream_140386077020752)).strip()
                            if __msgid_140386077020752:
                                __append(translate(__msgid_140386077020752, mapping=None, default=__msgid_140386077020752, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>\n                      </div>')
                        __append(u'\n                  </li>')
                        if (__backup_upgrade_info_140386069216336 is __marker):
                            del econtext['upgrade_info']
                        else:
                            econtext['upgrade_info'] = __backup_upgrade_info_140386069216336
                        __append(u'\n                </ul>\n              </li>')
                        if (__backup_pid_140386069307792 is __marker):
                            del econtext['pid']
                        else:
                            econtext['pid'] = __backup_pid_140386069307792
                        __append(u'\n              ')
                        ____index_140386077043024 -= 1
                        if (____index_140386077043024 > 0):
                            __append('')
                    if (__backup_product_140386077014608 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_140386077014608
                    __append(u'\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069299856
                    __attrs_140386069299856 = _static_140386247937936

                    # <Value u'python:num_products > 1' (104:33)> -> __condition
                    __token = 5024
                    try:
                        __zt_tmp = __attrs_140386069299856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('python', u'num_products > 1', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fae2e409750> name=None at 7fae2e4097d0> -> __attrs_140386077023888
                        __attrs_140386077023888 = _static_140386077022032

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<form action="upgrade_products" method="post">\n                   ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070485072
                        __attrs_140386070485072 = _static_140386247937936
                        __backup_product_140386077042896 = get('product', __marker)

                        # <Value u'products' (106:54)> -> __iterator
                        __token = 5167
                        try:
                            __zt_tmp = __attrs_140386070485072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140386186296528('path', u'products', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        (__iterator, ____index_140386182019920, ) = getitem('repeat')(u'product', __iterator)
                        econtext['product'] = None
                        for __item in __iterator:
                            econtext['product'] = __item
                            __append(u'\n                   ')

                            # <Static value=<_ast.Dict object at 0x7fae2de0cd10> name=None at 7fae2de0c850> -> __attrs_140386077080080
                            __attrs_140386077080080 = _static_140386070744336

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input type="hidden"')

                            # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069981392
                            __default_140386069981392 = _DEFAULT_MARKER

                            # <Substitution u'product/id' (109:48)> -> __attr_value
                            __token = 5344
                            try:
                                __zt_tmp = __attrs_140386077080080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140386186296528('path', u'product/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', u'product', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))
                            __append(u' name="prefs_reinstallProducts:list" />\n                   ')
                            ____index_140386182019920 -= 1
                            if (____index_140386182019920 > 0):
                                __append('')
                        if (__backup_product_140386077042896 is __marker):
                            del econtext['product']
                        else:
                            econtext['product'] = __backup_product_140386077042896
                        __append(u'\n                   ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077080272
                        __attrs_140386077080272 = _static_140386247937936

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n                     ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077077968
                        __attrs_140386077077968 = _static_140386247937936

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div>')
                        __stream_140386077079632 = []
                        __append_140386077079632 = __stream_140386077079632.append
                        __append_140386077079632(u'This can be risky, are you sure you want to do this?')
                        __msgid_140386077079632 = __re_whitespace(''.join(__stream_140386077079632)).strip()
                        if u'label_product_upgrade_all_action':
                            __append(translate(u'label_product_upgrade_all_action', mapping=None, default=__msgid_140386077079632, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</div>\n                     ')

                        # <Static value=<_ast.Dict object at 0x7fae2e417f10> name=None at 7fae2e4177d0> -> __attrs_140386070705424
                        __attrs_140386070705424 = _static_140386077081360

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="context" type="submit"')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077080912
                        __default_140386077080912 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<_ast.Str object at 0x7fae2e417410> at 7fae2e417f90> -> __attr_value
                        __attr_value = u'Upgrade them ALL!'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' name="form.submitted" />\n                   </span>\n                </form>\n               </li>')
                    __append(u'\n              </ul>\n          </section>')
                __append(u'\n        </section>')
                if (__backup_num_products_140386080044560 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140386080044560
                if (__backup_products_140386069186320 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140386069186320
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7fae2dcae390> name=None at 7fae2dcae690> -> __attrs_140386077081296
                __attrs_140386077081296 = _static_140386069308304
                __backup_products_140386080104144 = get('products', __marker)

                # <Value u'view/get_available' (125:38)> -> __value
                __token = 5972
                try:
                    __zt_tmp = __attrs_140386077081296
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/get_available', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140386080102992 = get('num_products', __marker)

                # <Value u'python:len(products)' (126:37)> -> __value
                __token = 6029
                try:
                    __zt_tmp = __attrs_140386077081296
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('python', u'len(products)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="install-products" class="portlet">\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2e415cd0> name=None at 7fae2e415050> -> __attrs_140386077069776
                __attrs_140386077069776 = _static_140386077072592

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header class="portletHeader">')
                __stream_140386077071056 = []
                __append_140386077071056 = __stream_140386077071056.append
                __append_140386077071056(u'Available add-ons')
                __msgid_140386077071056 = __re_whitespace(''.join(__stream_140386077071056)).strip()
                if __msgid_140386077071056:
                    __append(translate(__msgid_140386077071056, mapping=None, default=__msgid_140386077071056, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2e415bd0> name=None at 7fae2e415410> -> __attrs_140386077072976
                __attrs_140386077072976 = _static_140386077072336

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section class="portletContent">\n            ')

                # <Static value=<_ast.Dict object at 0x7fae2e415350> name=None at 7fae2e415550> -> __attrs_140386077070544
                __attrs_140386077070544 = _static_140386077070160

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="configlets">\n              ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080036688
                __attrs_140386080036688 = _static_140386247937936
                __backup_product_140386069309264 = get('product', __marker)

                # <Value u'products' (131:38)> -> __iterator
                __token = 6306
                try:
                    __zt_tmp = __attrs_140386080036688
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'products', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386080036304, ) = getitem('repeat')(u'product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080037456
                    __attrs_140386080037456 = _static_140386247937936
                    __backup_pid_140386070728400 = get('pid', __marker)

                    # <Value u'product/id' (132:39)> -> __value
                    __token = 6356
                    try:
                        __zt_tmp = __attrs_140386080037456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'product/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae2e6e9a90> name=None at 7fae2e6e9e10> -> __attrs_140386080025040
                    __attrs_140386080025040 = _static_140386080037520

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form action="install_products" method="post" class="pull-right">\n                   ')

                    # <Static value=<_ast.Dict object at 0x7fae2e6e6690> name=None at 7fae2e6e6d10> -> __attrs_140386080025744
                    __attrs_140386080025744 = _static_140386080024208

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden" name="install_product"')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386080026320
                    __default_140386080026320 = _DEFAULT_MARKER

                    # <Substitution u'pid' (136:49)> -> __attr_value
                    __token = 6590
                    try:
                        __zt_tmp = __attrs_140386080025744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140386186296528('path', u'pid', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n                   ')

                    # <Static value=<_ast.Dict object at 0x7fae2e6e6110> name=None at 7fae2e6e6050> -> __attrs_140386069275536
                    __attrs_140386069275536 = _static_140386080022800

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="context" type="submit"')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069278160
                    __default_140386069278160 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7fae2dca6050> at 7fae2dca6990> -> __attr_value
                    __attr_value = u'Install'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' name="form.submitted"/>\n                </form>\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069278672
                    __attrs_140386069278672 = _static_140386247937936

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h3>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069276624
                    __attrs_140386069276624 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069277968
                    __default_140386069277968 = _DEFAULT_MARKER

                    # <Value u'product/title' (145:37)> -> __cache_140386069276944
                    __token = 6910
                    try:
                        __zt_tmp = __attrs_140386069276624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386069276944 = _static_140386186296528('path', u'product/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'product/title' (145:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dca6a10> -> __condition
                    __expression = __cache_140386069276944

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n                    Add-on Name\n                  </span>')
                    else:
                        __content = __cache_140386069276944
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                </h3>\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae2dca60d0> name=None at 7fae2dca6ad0> -> __attrs_140386069282192
                    __attrs_140386069282192 = _static_140386069274832

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="configletDescription discreet">\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069282128
                    __attrs_140386069282128 = _static_140386247937936

                    # <Value u'product/description' (150:43)> -> __condition
                    __token = 7125
                    try:
                        __zt_tmp = __attrs_140386069282128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'product/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069281040
                        __default_140386069281040 = _DEFAULT_MARKER

                        # <Value u'product/description' (152:33)> -> __cache_140386069281872
                        __token = 7217
                        try:
                            __zt_tmp = __attrs_140386069282128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386069281872 = _static_140386186296528('path', u'product/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/description' (152:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dca7610> -> __condition
                        __expression = __cache_140386069281872

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'add-on description')
                        else:
                            __content = __cache_140386069281872
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fae2dca7090> name=None at 7fae2dca7490> -> __attrs_140386069282448
                    __attrs_140386069282448 = _static_140386069278864

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<em class="discreet"> \u2013 (')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069360592
                    __attrs_140386069360592 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069359952
                    __default_140386069359952 = _DEFAULT_MARKER

                    # <Value u'pid' (153:62)> -> __cache_140386069359376
                    __token = 7330
                    try:
                        __zt_tmp = __attrs_140386069360592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386069359376 = _static_140386186296528('path', u'pid', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'pid' (153:62)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dcbadd0> -> __condition
                    __expression = __cache_140386069359376

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>plugin.app.name</span>')
                    else:
                        __content = __cache_140386069359376
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u' ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069357008
                    __attrs_140386069357008 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069358288
                    __default_140386069358288 = _DEFAULT_MARKER

                    # <Value u'product/version' (153:109)> -> __cache_140386069360464
                    __token = 7377
                    try:
                        __zt_tmp = __attrs_140386069357008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386069360464 = _static_140386186296528('path', u'product/version', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'product/version' (153:109)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dcbac50> -> __condition
                    __expression = __cache_140386069360464

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>1.0</span>')
                    else:
                        __content = __cache_140386069360464
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u')</em>\n                </p>\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae2dca7dd0> name=None at 7fae2dca7050> -> __attrs_140386069357968
                    __attrs_140386069357968 = _static_140386069282256

                    # <Value u'not:product/uninstall_profile' (157:35)> -> __condition
                    __token = 7551
                    try:
                        __zt_tmp = __attrs_140386069357968
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('not', u'product/uninstall_profile', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <dl ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dl class="portalMessage warning" role="status">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070515600
                        __attrs_140386070515600 = _static_140386247937936

                        # <dt ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dt>')
                        __stream_140386070512464 = []
                        __append_140386070512464 = __stream_140386070512464.append
                        __append_140386070512464(u'Warning')
                        __msgid_140386070512464 = __re_whitespace(''.join(__stream_140386070512464)).strip()
                        if __msgid_140386070512464:
                            __append(translate(__msgid_140386070512464, mapping=None, default=__msgid_140386070512464, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</dt>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070514000
                        __attrs_140386070514000 = _static_140386247937936

                        # <dd ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dd>')
                        __stream_140386070513232 = []
                        __append_140386070513232 = __stream_140386070513232.append
                        __append_140386070513232(u'This product cannot be uninstalled!')
                        __msgid_140386070513232 = __re_whitespace(''.join(__stream_140386070513232)).strip()
                        if __msgid_140386070513232:
                            __append(translate(__msgid_140386070513232, mapping=None, default=__msgid_140386070513232, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</dd>\n                </dl>')
                    __append(u'\n              ')
                    if (__backup_pid_140386070728400 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_140386070728400
                    __append(u'\n              </li>')
                    ____index_140386080036304 -= 1
                    if (____index_140386080036304 > 0):
                        __append('\n              ')
                if (__backup_product_140386069309264 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_140386069309264
                __append(u'\n            </ul>\n          </section>\n        </section>')
                if (__backup_num_products_140386080102992 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140386080102992
                if (__backup_products_140386080104144 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140386080104144
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7fae2e4155d0> name=None at 7fae2e415810> -> __attrs_140386069356752
                __attrs_140386069356752 = _static_140386077070800
                __backup_products_140386080103248 = get('products', __marker)

                # <Value u'view/get_installed' (167:38)> -> __value
                __token = 7885
                try:
                    __zt_tmp = __attrs_140386069356752
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/get_installed', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140386080101200 = get('num_products', __marker)

                # <Value u'python:len(products)' (168:37)> -> __value
                __token = 7942
                try:
                    __zt_tmp = __attrs_140386069356752
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('python', u'len(products)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="activated-products" class="portlet">\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2ddd4d10> name=None at 7fae2ddd4e50> -> __attrs_140386070511888
                __attrs_140386070511888 = _static_140386070514960

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header class="portletHeader">')
                __stream_140386070513168 = []
                __append_140386070513168 = __stream_140386070513168.append
                __append_140386070513168(u'Activated add-ons')
                __msgid_140386070513168 = __re_whitespace(''.join(__stream_140386070513168)).strip()
                if __msgid_140386070513168:
                    __append(translate(__msgid_140386070513168, mapping=None, default=__msgid_140386070513168, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n          ')

                # <Static value=<_ast.Dict object at 0x7fae2ddd4250> name=None at 7fae2ddd4b10> -> __attrs_140386070515088
                __attrs_140386070515088 = _static_140386070512208

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section class="portletContent">\n            ')

                # <Static value=<_ast.Dict object at 0x7fae2dd72290> name=None at 7fae2dd72350> -> __attrs_140386077037776
                __attrs_140386077037776 = _static_140386070110864

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="configlets">\n                ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077040528
                __attrs_140386077040528 = _static_140386247937936
                __backup_product_140386069214672 = get('product', __marker)

                # <Value u'products' (173:40)> -> __iterator
                __token = 8223
                try:
                    __zt_tmp = __attrs_140386077040528
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'products', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386077038928, ) = getitem('repeat')(u'product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080080464
                    __attrs_140386080080464 = _static_140386247937936
                    __backup_pid_140386077041808 = get('pid', __marker)

                    # <Value u'product/id' (174:41)> -> __value
                    __token = 8275
                    try:
                        __zt_tmp = __attrs_140386080080464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('path', u'product/id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7fae2e6f4e50> name=None at 7fae2e6f4750> -> __attrs_140386080082000
                    __attrs_140386080082000 = _static_140386080083536

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form action="uninstall_products" method="post" class="pull-right">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae2e6f4b10> name=None at 7fae2e6f4c90> -> __attrs_140386076984272
                    __attrs_140386076984272 = _static_140386080082704

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden" name="uninstall_product"')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386076984656
                    __default_140386076984656 = _DEFAULT_MARKER

                    # <Substitution u'pid' (178:48)> -> __attr_value
                    __token = 8514
                    try:
                        __zt_tmp = __attrs_140386076984272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140386186296528('path', u'pid', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae2e400d50> name=None at 7fae2e400b90> -> __attrs_140386076986896
                    __attrs_140386076986896 = _static_140386076986704

                    # <Value u'product/uninstall_profile' (183:42)> -> __condition
                    __token = 8747
                    try:
                        __zt_tmp = __attrs_140386076986896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'product/uninstall_profile', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="destructive" type="submit"')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386076985296
                        __default_140386076985296 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<_ast.Str object at 0x7fae2e400e90> at 7fae2e400710> -> __attr_value
                        __attr_value = u'Uninstall'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' name="form.submitted"/>')
                    __append(u'\n                  </form>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076983504
                    __attrs_140386076983504 = _static_140386247937936

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h3>\n                      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076992336
                    __attrs_140386076992336 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386076992720
                    __default_140386076992720 = _DEFAULT_MARKER

                    # <Value u'product/title' (187:41)> -> __cache_140386076993552
                    __token = 8919
                    try:
                        __zt_tmp = __attrs_140386076992336
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386076993552 = _static_140386186296528('path', u'product/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'product/title' (187:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e402710> -> __condition
                    __expression = __cache_140386076993552

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n                        Add-on Name\n                      </span>')
                    else:
                        __content = __cache_140386076993552
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                    </h3>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae2e402510> name=None at 7fae2e4020d0> -> __attrs_140386076991824
                    __attrs_140386076991824 = _static_140386076992784

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="configletDescription discreet">\n                      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386076994256
                    __attrs_140386076994256 = _static_140386247937936

                    # <Value u'product/description' (192:47)> -> __condition
                    __token = 9154
                    try:
                        __zt_tmp = __attrs_140386076994256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'product/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386076994576
                        __default_140386076994576 = _DEFAULT_MARKER

                        # <Value u'product/description' (194:37)> -> __cache_140386076992272
                        __token = 9254
                        try:
                            __zt_tmp = __attrs_140386076994256
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386076992272 = _static_140386186296528('path', u'product/description', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/description' (194:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e402850> -> __condition
                        __expression = __cache_140386076992272

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'add-on description')
                        else:
                            __content = __cache_140386076992272
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append(u'\n                      ')

                    # <Static value=<_ast.Dict object at 0x7fae2e402250> name=None at 7fae2e402e10> -> __attrs_140386080009104
                    __attrs_140386080009104 = _static_140386076992080

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<em class="discreet"> \u2013 (')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080009040
                    __attrs_140386080009040 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386080008656
                    __default_140386080008656 = _DEFAULT_MARKER

                    # <Value u'pid' (195:66)> -> __cache_140386080009488
                    __token = 9371
                    try:
                        __zt_tmp = __attrs_140386080009040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386080009488 = _static_140386186296528('path', u'pid', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'pid' (195:66)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e6e2ed0> -> __condition
                    __expression = __cache_140386080009488

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>plugin.app.name</span>')
                    else:
                        __content = __cache_140386080009488
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u' ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080009296
                    __attrs_140386080009296 = _static_140386247937936

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386080009872
                    __default_140386080009872 = _DEFAULT_MARKER

                    # <Value u'product/version' (195:113)> -> __cache_140386080008016
                    __token = 9418
                    try:
                        __zt_tmp = __attrs_140386080009296
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386080008016 = _static_140386186296528('path', u'product/version', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'product/version' (195:113)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e6e28d0> -> __condition
                    __expression = __cache_140386080008016

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>1.0</span>')
                    else:
                        __content = __cache_140386080008016
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u')</em>\n                    </p>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7fae2e6e2110> name=None at 7fae2e402190> -> __attrs_140386070128080
                    __attrs_140386070128080 = _static_140386080006416

                    # <Value u'not:product/uninstall_profile' (199:39)> -> __condition
                    __token = 9605
                    try:
                        __zt_tmp = __attrs_140386070128080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('not', u'product/uninstall_profile', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <dl ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dl class="portalMessage info" role="status">\n                      ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070127184
                        __attrs_140386070127184 = _static_140386247937936

                        # <dt ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dt>')
                        __stream_140386070128784 = []
                        __append_140386070128784 = __stream_140386070128784.append
                        __append_140386070128784(u'Info')
                        __msgid_140386070128784 = __re_whitespace(''.join(__stream_140386070128784)).strip()
                        if __msgid_140386070128784:
                            __append(translate(__msgid_140386070128784, mapping=None, default=__msgid_140386070128784, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</dt>\n                      ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070128720
                        __attrs_140386070128720 = _static_140386247937936

                        # <dd ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dd>')
                        __stream_140386070128400 = []
                        __append_140386070128400 = __stream_140386070128400.append
                        __append_140386070128400(u'This product cannot be uninstalled!')
                        __msgid_140386070128400 = __re_whitespace(''.join(__stream_140386070128400)).strip()
                        if __msgid_140386070128400:
                            __append(translate(__msgid_140386070128400, mapping=None, default=__msgid_140386070128400, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</dd>\n                    </dl>')
                    __append(u'\n                ')
                    if (__backup_pid_140386077041808 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_140386077041808
                    __append(u'\n                </li>')
                    ____index_140386077038928 -= 1
                    if (____index_140386077038928 > 0):
                        __append('\n                ')
                if (__backup_product_140386069214672 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_140386069214672
                __append(u'\n              </ul>\n          </section>\n        </section>')
                if (__backup_num_products_140386080101200 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140386080101200
                if (__backup_products_140386080103248 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140386080103248
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7fae2dd72d50> name=None at 7fae2dd72750> -> __attrs_140386070129616
                __attrs_140386070129616 = _static_140386070113616
                __backup_products_140386077044304 = get('products', __marker)

                # <Value u'view/get_broken' (209:38)> -> __value
                __token = 9954
                try:
                    __zt_tmp = __attrs_140386070129616
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/get_broken', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140386080100816 = get('num_products', __marker)

                # <Value u'python:len(products)' (210:41)> -> __value
                __token = 10012
                try:
                    __zt_tmp = __attrs_140386070129616
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('python', u'len(products)', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <Value u'num_products' (211:32)> -> __condition
                __token = 10068
                try:
                    __zt_tmp = __attrs_140386070129616
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'num_products', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section id="broken-products" class="portlet">\n          ')

                    # <Static value=<_ast.Dict object at 0x7fae2dd76650> name=None at 7fae2dd763d0> -> __attrs_140386080030288
                    __attrs_140386080030288 = _static_140386070128208

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<header class="portletHeader">')
                    __stream_140386070130384 = []
                    __append_140386070130384 = __stream_140386070130384.append
                    __append_140386070130384(u'Broken add-ons')
                    __msgid_140386070130384 = __re_whitespace(''.join(__stream_140386070130384)).strip()
                    if __msgid_140386070130384:
                        __append(translate(__msgid_140386070130384, mapping=None, default=__msgid_140386070130384, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</header>\n          ')

                    # <Static value=<_ast.Dict object at 0x7fae2e6e78d0> name=None at 7fae2e6e7410> -> __attrs_140386080027792
                    __attrs_140386080027792 = _static_140386080028880

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section class="portletContent">\n            ')

                    # <Static value=<_ast.Dict object at 0x7fae2e6e7550> name=None at 7fae2e6e7910> -> __attrs_140386080027280
                    __attrs_140386080027280 = _static_140386080027984

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul class="configlets">\n              ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080028240
                    __attrs_140386080028240 = _static_140386247937936
                    __backup_product_140386077017168 = get('product', __marker)

                    # <Value u'products' (216:38)> -> __iterator
                    __token = 10336
                    try:
                        __zt_tmp = __attrs_140386080028240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140386186296528('path', u'products', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    (__iterator, ____index_140386069212944, ) = getitem('repeat')(u'product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071752912
                        __attrs_140386071752912 = _static_140386247937936

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h3>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080001296
                        __attrs_140386080001296 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386080001040
                        __default_140386080001040 = _DEFAULT_MARKER

                        # <Value u'product/product_id' (218:37)> -> __cache_140386079998160
                        __token = 10405
                        try:
                            __zt_tmp = __attrs_140386080001296
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386079998160 = _static_140386186296528('path', u'product/product_id', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/product_id' (218:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e6e04d0> -> __condition
                        __expression = __cache_140386079998160

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>\n                    Add-on Name\n                  </span>')
                        else:
                            __content = __cache_140386079998160
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                </h3>\n                ')

                        # <Static value=<_ast.Dict object at 0x7fae2e6e0650> name=None at 7fae2e6e0b50> -> __attrs_140386079998544
                        __attrs_140386079998544 = _static_140386079999568

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p class="configletDescription discreet">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386080000656
                        __attrs_140386080000656 = _static_140386247937936

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386079998608
                        __default_140386079998608 = _DEFAULT_MARKER

                        # <Value u'product/type' (223:37)> -> __cache_140386080001616
                        __token = 10619
                        try:
                            __zt_tmp = __attrs_140386080000656
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386080001616 = _static_140386186296528('path', u'product/type', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/type' (223:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e6e0390> -> __condition
                        __expression = __cache_140386080001616

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Error Type')
                        else:
                            __content = __cache_140386080001616
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7fae2dc7dfd0> name=None at 7fae2e6e0890> -> __attrs_140386069110288
                        __attrs_140386069110288 = _static_140386069110736

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<em class="discreet"> - ')

                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069109072
                        __attrs_140386069109072 = _static_140386247937936

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069110352
                        __default_140386069110352 = _DEFAULT_MARKER

                        # <Value u'product/value' (224:65)> -> __cache_140386069107920
                        __token = 10734
                        try:
                            __zt_tmp = __attrs_140386069109072
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386069107920 = _static_140386186296528('path', u'product/value', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/value' (224:65)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dc7d690> -> __condition
                        __expression = __cache_140386069107920

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Error Reason')
                        else:
                            __content = __cache_140386069107920
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</em>\n                </p>\n              </li>')
                        ____index_140386069212944 -= 1
                        if (____index_140386069212944 > 0):
                            __append('\n              ')
                    if (__backup_product_140386077017168 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_140386077017168
                    __append(u'\n            </ul>\n          </section>\n        </section>')
                if (__backup_num_products_140386080100816 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140386080100816
                if (__backup_products_140386077044304 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140386077044304
                __append(u'\n\n    </div>\n')
                __i18n_domain = __previous_i18n_domain_140386072421904
            _slots = econtext[u'__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value u'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140386069185680
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140386186296528('path', u'context/prefs_main_template/macros/master', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140386117433216 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140386117433216
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
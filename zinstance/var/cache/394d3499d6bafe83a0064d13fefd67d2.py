# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/controlpanel/browser/quickinstaller.pt'

__tokens = {459: (u'string:$portal_url/@@overview-controlpanel', 14, 28), 1362: (u'view/get_upgrades', 41, 38), 1418: (u' python:len(products', 42, 37), 1603: (u'not:products', 45, 34), 1981: (u'products', 51, 57), 2077: (u'products', 53, 49), 2122: (u'product/id', 54, 34), 2389: (u'pid', 58, 59), 2672: (u'string:Upgrade ${pid}', 64, 47), 2780: (u'product/title', 67, 37), 2995: (u'product/description', 72, 43), 3029: (u'product/description', 72, 77), 3160: (u'pid', 73, 62), 3207: (u'product/version', 73, 109), 3355: (u'product/upgrade_info', 76, 47), 3552: (u'not:upgrade_info/hasProfile', 80, 43), 3742: (u'upgrade_info/installedVersion', 82, 81), 3864: (u'upgrade_info/hasProfile', 84, 43), 4075: (u'upgrade_info/installedVersion', 86, 91), 4344: (u'upgrade_info/newVersion', 89, 90), 4496: (u'not:upgrade_info/available', 93, 42), 5024: (u'python:num_products > 1', 104, 33), 5167: (u'products', 106, 54), 5344: (u'product/id', 109, 48), 5972: (u'view/get_available', 125, 38), 6029: (u' python:len(products', 126, 37), 6306: (u'products', 131, 38), 6356: (u'product/id', 132, 39), 6590: (u'pid', 136, 49), 6910: (u'product/title', 145, 37), 7125: (u'product/description', 150, 43), 7217: (u'product/description', 152, 33), 7330: (u'pid', 153, 62), 7377: (u'product/version', 153, 109), 7551: (u'not:product/uninstall_profile', 157, 35), 7885: (u'view/get_installed', 167, 38), 7942: (u' python:len(products', 168, 37), 8223: (u'products', 173, 40), 8275: (u'product/id', 174, 41), 8514: (u'pid', 178, 48), 8747: (u'product/uninstall_profile', 183, 42), 8919: (u'product/title', 187, 41), 9154: (u'product/description', 192, 47), 9254: (u'product/description', 194, 37), 9371: (u'pid', 195, 66), 9418: (u'product/version', 195, 113), 9605: (u'not:product/uninstall_profile', 199, 39), 9954: (u'view/get_broken', 209, 38), 10012: (u' python:len(products', 210, 41), 10068: (u'num_products', 211, 32), 10336: (u'products', 216, 38), 10405: (u'product/product_id', 218, 37), 10619: (u'product/type', 223, 37), 10734: (u'product/value', 224, 65), 261: (u'context/prefs_main_template/macros/master', 6, 23), 261: (u'context/prefs_main_template/macros/master', 6, 23)}

from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper

_static_140235432292240 = {u'class': u'portletContent', }
_static_140235322019280 = {u'class': u'configlets', }
_static_140235431285200 = {u'class': u'configletDescription discreet', }
_static_140235423522256 = {u'class': u'portletContent', }
_static_140235423486096 = {u'class': u'configlets', }
_static_140235424482256 = {u'action': u'upgrade_products', u'method': u'post', }
_static_140235451450192 = {u'class': u'portletHeader', }
_static_140235374093008 = {u'type': u'submit', u'class': u'standalone', u'value': u'Upgrade ${pid}', u'name': u'form.submitted', }
_static_140235374256912 = {u'type': u'hidden', u'name': u'prefs_reinstallProducts:list', u'value': u'pid', }
_static_140235321931280 = {u'type': u'submit', u'class': u'destructive', u'value': u'Uninstall', u'name': u'form.submitted', }
_static_140235322082832 = {u'type': u'submit', u'class': u'context', u'value': u'Upgrade them ALL!', u'name': u'form.submitted', }
_static_140235424626704 = {u'action': u'uninstall_products', u'method': u'post', u'class': u'pull-right', }
_static_140235368758224 = {u'href': u'http://docs.plone.org/manage/installing/installing_addons.html', }
_static_140235322059920 = {u'class': u'discreet', }
_static_140235432291088 = {u'role': u'status', u'id': u'up-to-date-message', u'class': u'portalMessage info', }
_static_140235321932240 = {u'type': u'hidden', u'name': u'uninstall_product', u'value': u'pid', }
_static_140235322019792 = {u'id': u'activated-products', u'class': u'portlet', }
_static_140235322096656 = u'master'
_static_140235322040016 = {u'class': u'portletContent', }
_static_140235322516560 = {u'class': u'portletContent', }
_static_140235321952464 = {u'role': u'status', u'class': u'portalMessage info', }
_static_140235322037584 = {u'class': u'portletHeader', }
_static_140235322506000 = {u'class': u'discreet', }
_static_140235431246288 = {u'type': u'hidden', u'name': u'install_product', u'value': u'pid', }
_static_140235431246160 = {u'type': u'submit', u'class': u'context', u'value': u'Install', u'name': u'form.submitted', }
_static_140235374256784 = {u'action': u'upgrade_products', u'method': u'post', u'class': u'pull-right', }
_static_140235322077776 = {u'class': u'documentFirstHeading', }
_static_140235322077968 = {u'href': u'string:$portal_url/@@overview-controlpanel', u'id': u'setup-link', u'class': u'link-parent', }
_static_140235424283280 = {u'class': u'configletDescription discreet', }
_static_140235423490000 = {u'id': u'install-products', u'class': u'portlet', }
_static_140235321942864 = {u'id': u'upgrade-products', u'class': u'portlet', }
_static_140235322135184 = {u'class': u'configletDescription discreet', }
_static_140235321945936 = {u'id': u'content-core', }
_static_140235322750672 = {u'type': u'hidden', u'name': u'prefs_reinstallProducts:list', u'value': u'product', }
_static_140235322481488 = {u'class': u'discreet', }
_static_140235322421968 = {u'id': u'broken-products', u'class': u'portlet', }
_static_140235322089040 = {u'class': u'discreet', }
_static_140235368765904 = {u'action': u'install_products', u'method': u'post', u'class': u'pull-right', }
_static_140235322453264 = {u'class': u'configlets', }
_static_140235322424080 = {u'class': u'configlets', }
_static_140235489934800 = {}
_static_140235435449424 = __compile_zt_expr
_static_140235322422736 = {u'class': u'portletContent', }
_static_140235374162000 = {u'class': u'configletDescription discreet', }
_static_140235322422864 = {u'class': u'portletHeader', }
_static_140235322057104 = {u'class': u'configletDetails', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235321944208 = {u'class': u'discreet', }
_static_140235368752016 = {u'class': u'portletHeader', }
_static_140235322078160 = {u'class': u'documentDescription', }
_static_140235322480848 = {u'role': u'status', u'class': u'portalMessage warning', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322094864
            __attrs_140235322094864 = _static_140235489934800
            __backup_macroname_140235373760992 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8b148efc10> name=None at 7f8b148ef0d0> -> __value
            __value = _static_140235322096656
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322096912
                __attrs_140235322096912 = _static_140235489934800
                __previous_i18n_domain_140235322094224 = __i18n_domain
                __i18n_domain = u'plone'
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b148eb310> name=None at 7f8b148ebe90> -> __attrs_140235322079824
                __attrs_140235322079824 = _static_140235322077968

                # <a ... (0:0)
                # --------------------------------------------------------
                __append(u'<a id="setup-link" class="link-parent"')

                # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322081040
                __default_140235322081040 = _DEFAULT_MARKER

                # <Substitution u'string:$portal_url/@@overview-controlpanel' (14:28)> -> __attr_href
                __token = 459
                try:
                    __zt_tmp = __attrs_140235322079824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140235435449424('string', u'$portal_url/@@overview-controlpanel', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((u' href="%s"' % __attr_href))
                __append(u'>')
                __stream_140235322079376 = []
                __append_140235322079376 = __stream_140235322079376.append
                __append_140235322079376(u'\n        Site Setup\n    ')
                __msgid_140235322079376 = __re_whitespace(''.join(__stream_140235322079376)).strip()
                if __msgid_140235322079376:
                    __append(translate(__msgid_140235322079376, mapping=None, default=__msgid_140235322079376, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</a>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b148eb250> name=None at 7f8b148ebc90> -> __attrs_140235322077840
                __attrs_140235322077840 = _static_140235322077776

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1 class="documentFirstHeading">')
                __stream_140235322078224 = []
                __append_140235322078224 = __stream_140235322078224.append
                __append_140235322078224(u'Add-ons')
                __msgid_140235322078224 = __re_whitespace(''.join(__stream_140235322078224)).strip()
                if __msgid_140235322078224:
                    __append(translate(__msgid_140235322078224, mapping=None, default=__msgid_140235322078224, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</h1>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b148eb3d0> name=None at 7f8b148ebc50> -> __attrs_140235374137936
                __attrs_140235374137936 = _static_140235322078160

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="documentDescription">')
                __stream_140235322080080 = []
                __append_140235322080080 = __stream_140235322080080.append
                __append_140235322080080(u'\n      This is the Add-on configuration section, you can activate and deactivate\n      add-ons in the lists below.\n    ')
                __msgid_140235322080080 = __re_whitespace(''.join(__stream_140235322080080)).strip()
                if __msgid_140235322080080:
                    __append(translate(__msgid_140235322080080, mapping=None, default=__msgid_140235322080080, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</div>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b148caf50> name=None at 7f8b148caa10> -> __attrs_140235321944336
                __attrs_140235321944336 = _static_140235321945936

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div id="content-core">\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b148ca890> name=None at 7f8b148ca9d0> -> __attrs_140235321946000
                __attrs_140235321946000 = _static_140235321944208

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="discreet">')
                __stream_140235428633728_third_party_product = ''
                __stream_140235321943888 = []
                __append_140235321943888 = __stream_140235321943888.append
                __append_140235321943888(u'\n          To make new add-ons show up here, add them to your buildout\n          configuration, run buildout, and restart the server process.\n          For detailed instructions see\n          ')
                __stream_140235428633728_third_party_product = []
                __append_140235428633728_third_party_product = __stream_140235428633728_third_party_product.append

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321942416
                __attrs_140235321942416 = _static_140235489934800

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_140235428633728_third_party_product(u'<span>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1756fbd0> name=None at 7f8b1756fb50> -> __attrs_140235368758672
                __attrs_140235368758672 = _static_140235368758224

                # <a ... (0:0)
                # --------------------------------------------------------
                __append_140235428633728_third_party_product(u'<a href="http://docs.plone.org/manage/installing/installing_addons.html">')
                __stream_140235368759056 = []
                __append_140235368759056 = __stream_140235368759056.append
                __append_140235368759056(u'\n            Installing a third party add-on\n          ')
                __msgid_140235368759056 = __re_whitespace(''.join(__stream_140235368759056)).strip()
                if __msgid_140235368759056:
                    __append_140235428633728_third_party_product(translate(__msgid_140235368759056, mapping=None, default=__msgid_140235368759056, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append_140235428633728_third_party_product(u'</a>\n          </span>')
                __append_140235321943888(u'${third_party_product}')
                __stream_140235428633728_third_party_product = ''.join(__stream_140235428633728_third_party_product)
                __append_140235321943888(u'.\n        ')
                __msgid_140235321943888 = __re_whitespace(''.join(__stream_140235321943888)).strip()
                if __msgid_140235321943888:
                    __append(translate(__msgid_140235321943888, mapping={u'third_party_product': __stream_140235428633728_third_party_product, }, default=__msgid_140235321943888, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</p>\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b148ca350> name=None at 7f8b148ca250> -> __attrs_140235368753488
                __attrs_140235368753488 = _static_140235321942864
                __backup_products_140235322097104 = get('products', __marker)

                # <Value u'view/get_upgrades' (41:38)> -> __value
                __token = 1362
                try:
                    __zt_tmp = __attrs_140235368753488
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/get_upgrades', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140235322077648 = get('num_products', __marker)

                # <Value u'python:len(products)' (42:37)> -> __value
                __token = 1418
                try:
                    __zt_tmp = __attrs_140235368753488
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u'len(products)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="upgrade-products" class="portlet">\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1756e390> name=None at 7f8b1756e190> -> __attrs_140235368753808
                __attrs_140235368753808 = _static_140235368752016

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header class="portletHeader">')
                __stream_140235368753616 = []
                __append_140235368753616 = __stream_140235368753616.append
                __append_140235368753616(u'Upgrades')
                __msgid_140235368753616 = __re_whitespace(''.join(__stream_140235368753616)).strip()
                if __msgid_140235368753616:
                    __append(translate(__msgid_140235368753616, mapping=None, default=__msgid_140235368753616, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1a9a9dd0> name=None at 7f8b1756ef90> -> __attrs_140235423520400
                __attrs_140235423520400 = _static_140235423522256

                # <Value u'not:products' (45:34)> -> __condition
                __token = 1603
                try:
                    __zt_tmp = __attrs_140235423520400
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('not', u'products', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section class="portletContent">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1b206b10> name=None at 7f8b1b206750> -> __attrs_140235432291856
                    __attrs_140235432291856 = _static_140235432291088

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div id="up-to-date-message" class="portalMessage info" role="status">\n                 ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322052560
                    __attrs_140235322052560 = _static_140235489934800

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140235322049360 = []
                    __append_140235322049360 = __stream_140235322049360.append
                    __append_140235322049360(u'No upgrades in this corner')
                    __msgid_140235322049360 = __re_whitespace(''.join(__stream_140235322049360)).strip()
                    if __msgid_140235322049360:
                        __append(translate(__msgid_140235322049360, mapping=None, default=__msgid_140235322049360, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n                 ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322051088
                    __attrs_140235322051088 = _static_140235489934800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140235322049936 = []
                    __append_140235322049936 = __stream_140235322049936.append
                    __append_140235322049936(u'You are up to date. High fives.')
                    __msgid_140235322049936 = __re_whitespace(''.join(__stream_140235322049936)).strip()
                    if __msgid_140235322049936:
                        __append(translate(__msgid_140235322049936, mapping=None, default=__msgid_140235322049936, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>\n             </div>\n          </section>')
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1b206f90> name=None at 7f8b1b206250> -> __attrs_140235322050896
                __attrs_140235322050896 = _static_140235432292240

                # <Value u'products' (51:57)> -> __condition
                __token = 1981
                try:
                    __zt_tmp = __attrs_140235322050896
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'products', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section class="portletContent">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b1a9a1090> name=None at 7f8b1a9a1990> -> __attrs_140235423489168
                    __attrs_140235423489168 = _static_140235423486096

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul class="configlets">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235423489552
                    __attrs_140235423489552 = _static_140235489934800
                    __backup_product_140235368756688 = get('product', __marker)

                    # <Value u'products' (53:49)> -> __iterator
                    __token = 2077
                    try:
                        __zt_tmp = __attrs_140235423489552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140235435449424('path', u'products', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    (__iterator, ____index_140235374164432, ) = getitem('repeat')(u'product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item
                        __append(u'\n              ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374163408
                        __attrs_140235374163408 = _static_140235489934800
                        __backup_pid_140235322050320 = get('pid', __marker)

                        # <Value u'product/id' (54:34)> -> __value
                        __token = 2122
                        try:
                            __zt_tmp = __attrs_140235374163408
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('path', u'product/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['pid'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8b17aae290> name=None at 7f8b17aaeb10> -> __attrs_140235374259280
                        __attrs_140235374259280 = _static_140235374256784

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<form action="upgrade_products" method="post" class="pull-right">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b17aae310> name=None at 7f8b17aae890> -> __attrs_140235374095120
                        __attrs_140235374095120 = _static_140235374256912

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input type="hidden" name="prefs_reinstallProducts:list"')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235374093648
                        __default_140235374093648 = _DEFAULT_MARKER

                        # <Substitution u'pid' (58:59)> -> __attr_value
                        __token = 2389
                        try:
                            __zt_tmp = __attrs_140235374095120
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140235435449424('path', u'pid', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' />\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b17a862d0> name=None at 7f8b17a864d0> -> __attrs_140235321907792
                        __attrs_140235321907792 = _static_140235374093008

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="standalone" type="submit"')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321906064
                        __default_140235321906064 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<Substitution u'string:Upgrade ${pid}' (64:47)> at 7f8b148c15d0> -> __attr_value

                        # <Substitution u'string:Upgrade ${pid}' (64:47)> -> __attr_value
                        __token = 2672
                        try:
                            __zt_tmp = __attrs_140235321907792
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140235435449424('string', u'Upgrade ${pid}', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', u'Upgrade ${pid}', _DEFAULT_MARKER)
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' name="form.submitted"/>\n                </form>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321908880
                        __attrs_140235321908880 = _static_140235489934800

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h3>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235442513872
                        __attrs_140235442513872 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235442511952
                        __default_140235442511952 = _DEFAULT_MARKER

                        # <Value u'product/title' (67:37)> -> __cache_140235442512336
                        __token = 2780
                        try:
                            __zt_tmp = __attrs_140235442513872
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235442512336 = _static_140235435449424('path', u'product/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/title' (67:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1bbc6dd0> -> __condition
                        __expression = __cache_140235442512336

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>\n                    Add-on Name\n                  </span>')
                        else:
                            __content = __cache_140235442512336
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                </h3>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8b17a97050> name=None at 7f8b17a97890> -> __attrs_140235442514512
                        __attrs_140235442514512 = _static_140235374162000

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p class="configletDescription discreet">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322058832
                        __attrs_140235322058832 = _static_140235489934800

                        # <Value u'product/description' (72:43)> -> __condition
                        __token = 2995
                        try:
                            __zt_tmp = __attrs_140235322058832
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140235435449424('path', u'product/description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235442512080
                            __default_140235442512080 = _DEFAULT_MARKER

                            # <Value u'product/description' (72:77)> -> __cache_140235442515536
                            __token = 3029
                            try:
                                __zt_tmp = __attrs_140235322058832
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140235442515536 = _static_140235435449424('path', u'product/description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                            # <BinOp left=<Value u'product/description' (72:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1bbc6c50> -> __condition
                            __expression = __cache_140235442515536

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append(u'add-on description')
                            else:
                                __content = __cache_140235442515536
                                __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                        __append(u'\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b148e6c90> name=None at 7f8b148e6c10> -> __attrs_140235322059664
                        __attrs_140235322059664 = _static_140235322059920

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<em class="discreet"> \u2013 (')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322059600
                        __attrs_140235322059600 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322057872
                        __default_140235322057872 = _DEFAULT_MARKER

                        # <Value u'pid' (73:62)> -> __cache_140235322059152
                        __token = 3160
                        try:
                            __zt_tmp = __attrs_140235322059600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235322059152 = _static_140235435449424('path', u'pid', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'pid' (73:62)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148e6a10> -> __condition
                        __expression = __cache_140235322059152

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>plugin.app.name</span>')
                        else:
                            __content = __cache_140235322059152
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u' ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321985616
                        __attrs_140235321985616 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322060496
                        __default_140235322060496 = _DEFAULT_MARKER

                        # <Value u'product/version' (73:109)> -> __cache_140235322059472
                        __token = 3207
                        try:
                            __zt_tmp = __attrs_140235321985616
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235322059472 = _static_140235435449424('path', u'product/version', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/version' (73:109)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148e69d0> -> __condition
                        __expression = __cache_140235322059472

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>1.0</span>')
                        else:
                            __content = __cache_140235322059472
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u')</em>\n                </p>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8b148e6190> name=None at 7f8b148e6350> -> __attrs_140235321985360
                        __attrs_140235321985360 = _static_140235322057104

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<ul class="configletDetails">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321986320
                        __attrs_140235321986320 = _static_140235489934800
                        __backup_upgrade_info_140235374257040 = get('upgrade_info', __marker)

                        # <Value u'product/upgrade_info' (76:47)> -> __value
                        __token = 3355
                        try:
                            __zt_tmp = __attrs_140235321986320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140235435449424('path', u'product/upgrade_info', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        econtext['upgrade_info'] = __value

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                      ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321985680
                        __attrs_140235321985680 = _static_140235489934800

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')
                        __stream_140235321983760 = []
                        __append_140235321983760 = __stream_140235321983760.append
                        __append_140235321983760(u'\n                        This addon has been upgraded.\n                      ')
                        __msgid_140235321983760 = __re_whitespace(''.join(__stream_140235321983760)).strip()
                        if __msgid_140235321983760:
                            __append(translate(__msgid_140235321983760, mapping=None, default=__msgid_140235321983760, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</span>\n                      ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321986448
                        __attrs_140235321986448 = _static_140235489934800

                        # <Value u'not:upgrade_info/hasProfile' (80:43)> -> __condition
                        __token = 3552
                        try:
                            __zt_tmp = __attrs_140235321986448
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140235435449424('not', u'upgrade_info/hasProfile', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140235322620576_version = ''
                            __stream_140235321984784 = []
                            __append_140235321984784 = __stream_140235321984784.append
                            __append_140235321984784(u'\n                        Old version was ')
                            __stream_140235322620576_version = []
                            __append_140235322620576_version = __stream_140235322620576_version.append

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322010896
                            __attrs_140235322010896 = _static_140235489934800

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_140235322620576_version(u'<strong>')

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322011472
                            __default_140235322011472 = _DEFAULT_MARKER

                            # <Value u'upgrade_info/installedVersion' (82:81)> -> __cache_140235322009232
                            __token = 3742
                            try:
                                __zt_tmp = __attrs_140235322010896
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140235322009232 = _static_140235435449424('path', u'upgrade_info/installedVersion', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                            # <BinOp left=<Value u'upgrade_info/installedVersion' (82:81)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148dab10> -> __condition
                            __expression = __cache_140235322009232

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_140235322620576_version(u'version')
                            else:
                                __content = __cache_140235322009232
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_140235322620576_version(__content)
                            __append_140235322620576_version(u'</strong>')
                            __append_140235321984784(u'${version}')
                            __stream_140235322620576_version = ''.join(__stream_140235322620576_version)
                            __append_140235321984784(u'.\n                      ')
                            __msgid_140235321984784 = __re_whitespace(''.join(__stream_140235321984784)).strip()
                            if u'label_product_upgrade_old_version':
                                __append(translate(u'label_product_upgrade_old_version', mapping={u'version': __stream_140235322620576_version, }, default=__msgid_140235321984784, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>')
                        __append(u'\n                      ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322008848
                        __attrs_140235322008848 = _static_140235489934800

                        # <Value u'upgrade_info/hasProfile' (84:43)> -> __condition
                        __token = 3864
                        try:
                            __zt_tmp = __attrs_140235322008848
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140235435449424('path', u'upgrade_info/hasProfile', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322011024
                            __attrs_140235322011024 = _static_140235489934800
                            __stream_140235322621296_version = ''
                            __stream_140235322010640 = []
                            __append_140235322010640 = __stream_140235322010640.append
                            __append_140235322010640(u'\n                          Old profile version was ')
                            __stream_140235322621296_version = []
                            __append_140235322621296_version = __stream_140235322621296_version.append

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235424485136
                            __attrs_140235424485136 = _static_140235489934800

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_140235322621296_version(u'<strong>')

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322008528
                            __default_140235322008528 = _DEFAULT_MARKER

                            # <Value u'upgrade_info/installedVersion' (86:91)> -> __cache_140235322009488
                            __token = 4075
                            try:
                                __zt_tmp = __attrs_140235424485136
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140235322009488 = _static_140235435449424('path', u'upgrade_info/installedVersion', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                            # <BinOp left=<Value u'upgrade_info/installedVersion' (86:91)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148da290> -> __condition
                            __expression = __cache_140235322009488

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_140235322621296_version(u'version')
                            else:
                                __content = __cache_140235322009488
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_140235322621296_version(__content)
                            __append_140235322621296_version(u'</strong>')
                            __append_140235322010640(u'${version}')
                            __stream_140235322621296_version = ''.join(__stream_140235322621296_version)
                            __append_140235322010640(u'.\n                        ')
                            __msgid_140235322010640 = __re_whitespace(''.join(__stream_140235322010640)).strip()
                            if u'label_product_upgrade_old_profile_version':
                                __append(translate(u'label_product_upgrade_old_profile_version', mapping={u'version': __stream_140235322621296_version, }, default=__msgid_140235322010640, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235424482448
                            __attrs_140235424482448 = _static_140235489934800
                            __stream_140235322621296_version = ''
                            __stream_140235322008720 = []
                            __append_140235322008720 = __stream_140235322008720.append
                            __append_140235322008720(u'\n                          New profile version is ')
                            __stream_140235322621296_version = []
                            __append_140235322621296_version = __stream_140235322621296_version.append

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235424482960
                            __attrs_140235424482960 = _static_140235489934800

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append_140235322621296_version(u'<strong>')

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424481680
                            __default_140235424481680 = _DEFAULT_MARKER

                            # <Value u'upgrade_info/newVersion' (89:90)> -> __cache_140235424483344
                            __token = 4344
                            try:
                                __zt_tmp = __attrs_140235424482960
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140235424483344 = _static_140235435449424('path', u'upgrade_info/newVersion', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                            # <BinOp left=<Value u'upgrade_info/newVersion' (89:90)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1aa94790> -> __condition
                            __expression = __cache_140235424483344

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                __append_140235322621296_version(u'version')
                            else:
                                __content = __cache_140235424483344
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append_140235322621296_version(__content)
                            __append_140235322621296_version(u'</strong>')
                            __append_140235322008720(u'${version}')
                            __stream_140235322621296_version = ''.join(__stream_140235322621296_version)
                            __append_140235322008720(u'.\n                        ')
                            __msgid_140235322008720 = __re_whitespace(''.join(__stream_140235322008720)).strip()
                            if u'label_product_upgrade_new_profile_version':
                                __append(translate(u'label_product_upgrade_new_profile_version', mapping={u'version': __stream_140235322621296_version, }, default=__msgid_140235322008720, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'\n                      </span>')
                        __append(u'\n\n                      ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235424482768
                        __attrs_140235424482768 = _static_140235489934800

                        # <Value u'not:upgrade_info/available' (93:42)> -> __condition
                        __token = 4496
                        try:
                            __zt_tmp = __attrs_140235424482768
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140235435449424('not', u'upgrade_info/available', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div>\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235424483088
                            __attrs_140235424483088 = _static_140235489934800

                            # <strong ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<strong>')
                            __stream_140235424482704 = []
                            __append_140235424482704 = __stream_140235424482704.append
                            __append_140235424482704(u'Warning')
                            __msgid_140235424482704 = __re_whitespace(''.join(__stream_140235424482704)).strip()
                            if __msgid_140235424482704:
                                __append(translate(__msgid_140235424482704, mapping=None, default=__msgid_140235424482704, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</strong>\n                        ')

                            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322749264
                            __attrs_140235322749264 = _static_140235489934800

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>')
                            __stream_140235424483664 = []
                            __append_140235424483664 = __stream_140235424483664.append
                            __append_140235424483664(u'There is no upgrade procedure defined for this\n                        addon. Please consult the addon documentation\n                        for upgrade information, or contact the addon\n                        author.')
                            __msgid_140235424483664 = __re_whitespace(''.join(__stream_140235424483664)).strip()
                            if __msgid_140235424483664:
                                __append(translate(__msgid_140235424483664, mapping=None, default=__msgid_140235424483664, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</span>\n                      </div>')
                        __append(u'\n                  </li>')
                        if (__backup_upgrade_info_140235374257040 is __marker):
                            del econtext['upgrade_info']
                        else:
                            econtext['upgrade_info'] = __backup_upgrade_info_140235374257040
                        __append(u'\n                </ul>\n              </li>')
                        if (__backup_pid_140235322050320 is __marker):
                            del econtext['pid']
                        else:
                            econtext['pid'] = __backup_pid_140235322050320
                        __append(u'\n              ')
                        ____index_140235374164432 -= 1
                        if (____index_140235374164432 > 0):
                            __append('')
                    if (__backup_product_140235368756688 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_140235368756688
                    __append(u'\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321984080
                    __attrs_140235321984080 = _static_140235489934800

                    # <Value u'python:num_products > 1' (104:33)> -> __condition
                    __token = 5024
                    try:
                        __zt_tmp = __attrs_140235321984080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('python', u'num_products > 1', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8b1aa943d0> name=None at 7f8b1aa941d0> -> __attrs_140235322750544
                        __attrs_140235322750544 = _static_140235424482256

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<form action="upgrade_products" method="post">\n                   ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322752272
                        __attrs_140235322752272 = _static_140235489934800
                        __backup_product_140235374164752 = get('product', __marker)

                        # <Value u'products' (106:54)> -> __iterator
                        __token = 5167
                        try:
                            __zt_tmp = __attrs_140235322752272
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140235435449424('path', u'products', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        (__iterator, ____index_140235322751440, ) = getitem('repeat')(u'product', __iterator)
                        econtext['product'] = None
                        for __item in __iterator:
                            econtext['product'] = __item
                            __append(u'\n                   ')

                            # <Static value=<_ast.Dict object at 0x7f8b1498f6d0> name=None at 7f8b1498f750> -> __attrs_140235322082640
                            __attrs_140235322082640 = _static_140235322750672

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<input type="hidden"')

                            # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322084944
                            __default_140235322084944 = _DEFAULT_MARKER

                            # <Substitution u'product/id' (109:48)> -> __attr_value
                            __token = 5344
                            try:
                                __zt_tmp = __attrs_140235322082640
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140235435449424('path', u'product/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', u'product', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((u' value="%s"' % __attr_value))
                            __append(u' name="prefs_reinstallProducts:list" />\n                   ')
                            ____index_140235322751440 -= 1
                            if (____index_140235322751440 > 0):
                                __append('')
                        if (__backup_product_140235374164752 is __marker):
                            del econtext['product']
                        else:
                            econtext['product'] = __backup_product_140235374164752
                        __append(u'\n                   ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322081744
                        __attrs_140235322081744 = _static_140235489934800

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n                     ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322083280
                        __attrs_140235322083280 = _static_140235489934800

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<div>')
                        __stream_140235322082256 = []
                        __append_140235322082256 = __stream_140235322082256.append
                        __append_140235322082256(u'This can be risky, are you sure you want to do this?')
                        __msgid_140235322082256 = __re_whitespace(''.join(__stream_140235322082256)).strip()
                        if u'label_product_upgrade_all_action':
                            __append(translate(u'label_product_upgrade_all_action', mapping=None, default=__msgid_140235322082256, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</div>\n                     ')

                        # <Static value=<_ast.Dict object at 0x7f8b148ec610> name=None at 7f8b148ecdd0> -> __attrs_140235451451728
                        __attrs_140235451451728 = _static_140235322082832

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="context" type="submit"')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235451449424
                        __default_140235451449424 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<_ast.Str object at 0x7f8b1c44cb90> at 7f8b1c44ce10> -> __attr_value
                        __attr_value = u'Upgrade them ALL!'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' name="form.submitted" />\n                   </span>\n                </form>\n               </li>')
                    __append(u'\n              </ul>\n          </section>')
                __append(u'\n        </section>')
                if (__backup_num_products_140235322077648 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140235322077648
                if (__backup_products_140235322097104 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140235322097104
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1a9a1fd0> name=None at 7f8b148e4c50> -> __attrs_140235322085328
                __attrs_140235322085328 = _static_140235423490000
                __backup_products_140235321942480 = get('products', __marker)

                # <Value u'view/get_available' (125:38)> -> __value
                __token = 5972
                try:
                    __zt_tmp = __attrs_140235322085328
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/get_available', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140235321944080 = get('num_products', __marker)

                # <Value u'python:len(products)' (126:37)> -> __value
                __token = 6029
                try:
                    __zt_tmp = __attrs_140235322085328
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u'len(products)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="install-products" class="portlet">\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1c44c350> name=None at 7f8b1c44c550> -> __attrs_140235322515792
                __attrs_140235322515792 = _static_140235451450192

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header class="portletHeader">')
                __stream_140235451452880 = []
                __append_140235451452880 = __stream_140235451452880.append
                __append_140235451452880(u'Available add-ons')
                __msgid_140235451452880 = __re_whitespace(''.join(__stream_140235451452880)).strip()
                if __msgid_140235451452880:
                    __append(translate(__msgid_140235451452880, mapping=None, default=__msgid_140235451452880, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b14956450> name=None at 7f8b14956dd0> -> __attrs_140235322015888
                __attrs_140235322015888 = _static_140235322516560

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section class="portletContent">\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b148dcdd0> name=None at 7f8b148dcbd0> -> __attrs_140235322018000
                __attrs_140235322018000 = _static_140235322019280

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="configlets">\n              ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322017424
                __attrs_140235322017424 = _static_140235489934800
                __backup_product_140235322049488 = get('product', __marker)

                # <Value u'products' (131:38)> -> __iterator
                __token = 6306
                try:
                    __zt_tmp = __attrs_140235322017424
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140235435449424('path', u'products', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                (__iterator, ____index_140235322019600, ) = getitem('repeat')(u'product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322018192
                    __attrs_140235322018192 = _static_140235489934800
                    __backup_pid_140235432290192 = get('pid', __marker)

                    # <Value u'product/id' (132:39)> -> __value
                    __token = 6356
                    try:
                        __zt_tmp = __attrs_140235322018192
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'product/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8b175719d0> name=None at 7f8b17571690> -> __attrs_140235368766288
                    __attrs_140235368766288 = _static_140235368765904

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form action="install_products" method="post" class="pull-right">\n                   ')

                    # <Static value=<_ast.Dict object at 0x7f8b1b1079d0> name=None at 7f8b1b107e90> -> __attrs_140235431244496
                    __attrs_140235431244496 = _static_140235431246288

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden" name="install_product"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431246096
                    __default_140235431246096 = _DEFAULT_MARKER

                    # <Substitution u'pid' (136:49)> -> __attr_value
                    __token = 6590
                    try:
                        __zt_tmp = __attrs_140235431244496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140235435449424('path', u'pid', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n                   ')

                    # <Static value=<_ast.Dict object at 0x7f8b1b107950> name=None at 7f8b1b107f50> -> __attrs_140235431285776
                    __attrs_140235431285776 = _static_140235431246160

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input class="context" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431245712
                    __default_140235431245712 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7f8b1b107a90> at 7f8b1b107390> -> __attr_value
                    __attr_value = u'Install'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' name="form.submitted"/>\n                </form>\n\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431286800
                    __attrs_140235431286800 = _static_140235489934800

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h3>\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431288144
                    __attrs_140235431288144 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431286928
                    __default_140235431286928 = _DEFAULT_MARKER

                    # <Value u'product/title' (145:37)> -> __cache_140235431287696
                    __token = 6910
                    try:
                        __zt_tmp = __attrs_140235431288144
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235431287696 = _static_140235435449424('path', u'product/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'product/title' (145:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b111250> -> __condition
                    __expression = __cache_140235431287696

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n                    Add-on Name\n                  </span>')
                    else:
                        __content = __cache_140235431287696
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                </h3>\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8b1b1111d0> name=None at 7f8b1b111610> -> __attrs_140235322481360
                    __attrs_140235322481360 = _static_140235431285200

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="configletDescription discreet">\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322482256
                    __attrs_140235322482256 = _static_140235489934800

                    # <Value u'product/description' (150:43)> -> __condition
                    __token = 7125
                    try:
                        __zt_tmp = __attrs_140235322482256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'product/description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322481168
                        __default_140235322481168 = _DEFAULT_MARKER

                        # <Value u'product/description' (152:33)> -> __cache_140235322479376
                        __token = 7217
                        try:
                            __zt_tmp = __attrs_140235322482256
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235322479376 = _static_140235435449424('path', u'product/description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/description' (152:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1494d850> -> __condition
                        __expression = __cache_140235322479376

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'add-on description')
                        else:
                            __content = __cache_140235322479376
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f8b1494db50> name=None at 7f8b1494d510> -> __attrs_140235373402832
                    __attrs_140235373402832 = _static_140235322481488

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<em class="discreet"> \u2013 (')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322479120
                    __attrs_140235322479120 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322480592
                    __default_140235322480592 = _DEFAULT_MARKER

                    # <Value u'pid' (153:62)> -> __cache_140235322479440
                    __token = 7330
                    try:
                        __zt_tmp = __attrs_140235322479120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235322479440 = _static_140235435449424('path', u'pid', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'pid' (153:62)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1494d050> -> __condition
                    __expression = __cache_140235322479440

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>plugin.app.name</span>')
                    else:
                        __content = __cache_140235322479440
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u' ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321997776
                    __attrs_140235321997776 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321997008
                    __default_140235321997008 = _DEFAULT_MARKER

                    # <Value u'product/version' (153:109)> -> __cache_140235322482512
                    __token = 7377
                    try:
                        __zt_tmp = __attrs_140235321997776
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235322482512 = _static_140235435449424('path', u'product/version', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'product/version' (153:109)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148d77d0> -> __condition
                    __expression = __cache_140235322482512

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>1.0</span>')
                    else:
                        __content = __cache_140235322482512
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u')</em>\n                </p>\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8b1494d8d0> name=None at 7f8b1494df90> -> __attrs_140235321995984
                    __attrs_140235321995984 = _static_140235322480848

                    # <Value u'not:product/uninstall_profile' (157:35)> -> __condition
                    __token = 7551
                    try:
                        __zt_tmp = __attrs_140235321995984
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('not', u'product/uninstall_profile', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <dl ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dl class="portalMessage warning" role="status">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321996880
                        __attrs_140235321996880 = _static_140235489934800

                        # <dt ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dt>')
                        __stream_140235321998224 = []
                        __append_140235321998224 = __stream_140235321998224.append
                        __append_140235321998224(u'Warning')
                        __msgid_140235321998224 = __re_whitespace(''.join(__stream_140235321998224)).strip()
                        if __msgid_140235321998224:
                            __append(translate(__msgid_140235321998224, mapping=None, default=__msgid_140235321998224, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</dt>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321995920
                        __attrs_140235321995920 = _static_140235489934800

                        # <dd ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dd>')
                        __stream_140235321996624 = []
                        __append_140235321996624 = __stream_140235321996624.append
                        __append_140235321996624(u'This product cannot be uninstalled!')
                        __msgid_140235321996624 = __re_whitespace(''.join(__stream_140235321996624)).strip()
                        if __msgid_140235321996624:
                            __append(translate(__msgid_140235321996624, mapping=None, default=__msgid_140235321996624, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</dd>\n                </dl>')
                    __append(u'\n              ')
                    if (__backup_pid_140235432290192 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_140235432290192
                    __append(u'\n              </li>')
                    ____index_140235322019600 -= 1
                    if (____index_140235322019600 > 0):
                        __append('\n              ')
                if (__backup_product_140235322049488 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_140235322049488
                __append(u'\n            </ul>\n          </section>\n        </section>')
                if (__backup_num_products_140235321944080 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140235321944080
                if (__backup_products_140235321942480 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140235321942480
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b148dcfd0> name=None at 7f8b148dc710> -> __attrs_140235321999120
                __attrs_140235321999120 = _static_140235322019792
                __backup_products_140235321942992 = get('products', __marker)

                # <Value u'view/get_installed' (167:38)> -> __value
                __token = 7885
                try:
                    __zt_tmp = __attrs_140235321999120
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/get_installed', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140235321944144 = get('num_products', __marker)

                # <Value u'python:len(products)' (168:37)> -> __value
                __token = 7942
                try:
                    __zt_tmp = __attrs_140235321999120
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u'len(products)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section id="activated-products" class="portlet">\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1493f650> name=None at 7f8b1493f4d0> -> __attrs_140235322424912
                __attrs_140235322424912 = _static_140235322422864

                # <header ... (0:0)
                # --------------------------------------------------------
                __append(u'<header class="portletHeader">')
                __stream_140235321999184 = []
                __append_140235321999184 = __stream_140235321999184.append
                __append_140235321999184(u'Activated add-ons')
                __msgid_140235321999184 = __re_whitespace(''.join(__stream_140235321999184)).strip()
                if __msgid_140235321999184:
                    __append(translate(__msgid_140235321999184, mapping=None, default=__msgid_140235321999184, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</header>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1493f5d0> name=None at 7f8b1493fc10> -> __attrs_140235322421648
                __attrs_140235322421648 = _static_140235322422736

                # <section ... (0:0)
                # --------------------------------------------------------
                __append(u'<section class="portletContent">\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b1493fb10> name=None at 7f8b1493f810> -> __attrs_140235322424144
                __attrs_140235322424144 = _static_140235322424080

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul class="configlets">\n                ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235424628624
                __attrs_140235424628624 = _static_140235489934800
                __backup_product_140235374259920 = get('product', __marker)

                # <Value u'products' (173:40)> -> __iterator
                __token = 8223
                try:
                    __zt_tmp = __attrs_140235424628624
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140235435449424('path', u'products', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                (__iterator, ____index_140235424628240, ) = getitem('repeat')(u'product', __iterator)
                econtext['product'] = None
                for __item in __iterator:
                    econtext['product'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235424627792
                    __attrs_140235424627792 = _static_140235489934800
                    __backup_pid_140235374164048 = get('pid', __marker)

                    # <Value u'product/id' (174:41)> -> __value
                    __token = 8275
                    try:
                        __zt_tmp = __attrs_140235424627792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('path', u'product/id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['pid'] = __value
                    __append(u'\n                  ')

                    # <Static value=<_ast.Dict object at 0x7f8b1aab7810> name=None at 7f8b1aab7d90> -> __attrs_140235321932880
                    __attrs_140235321932880 = _static_140235424626704

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<form action="uninstall_products" method="post" class="pull-right">\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f8b148c79d0> name=None at 7f8b148c7750> -> __attrs_140235321932496
                    __attrs_140235321932496 = _static_140235321932240

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<input type="hidden" name="uninstall_product"')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321933264
                    __default_140235321933264 = _DEFAULT_MARKER

                    # <Substitution u'pid' (178:48)> -> __attr_value
                    __token = 8514
                    try:
                        __zt_tmp = __attrs_140235321932496
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140235435449424('path', u'pid', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((u' value="%s"' % __attr_value))
                    __append(u' />\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f8b148c7610> name=None at 7f8b148c7310> -> __attrs_140235424282512
                    __attrs_140235424282512 = _static_140235321931280

                    # <Value u'product/uninstall_profile' (183:42)> -> __condition
                    __token = 8747
                    try:
                        __zt_tmp = __attrs_140235424282512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'product/uninstall_profile', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<input class="destructive" type="submit"')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424282320
                        __default_140235424282320 = _DEFAULT_MARKER

                        # <Translate msgid=None node=<_ast.Str object at 0x7f8b148c72d0> at 7f8b148c7e90> -> __attr_value
                        __attr_value = u'Uninstall'
                        __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        if (__attr_value is not None):
                            __append((u' value="%s"' % __attr_value))
                        __append(u' name="form.submitted"/>')
                    __append(u'\n                  </form>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235424283536
                    __attrs_140235424283536 = _static_140235489934800

                    # <h3 ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<h3>\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235424282832
                    __attrs_140235424282832 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235424284112
                    __default_140235424284112 = _DEFAULT_MARKER

                    # <Value u'product/title' (187:41)> -> __cache_140235424284048
                    __token = 8919
                    try:
                        __zt_tmp = __attrs_140235424282832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235424284048 = _static_140235435449424('path', u'product/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'product/title' (187:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1aa63510> -> __condition
                    __expression = __cache_140235424284048

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>\n                        Add-on Name\n                      </span>')
                    else:
                        __content = __cache_140235424284048
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'\n                    </h3>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f8b1aa63a90> name=None at 7f8b1aa63c10> -> __attrs_140235322507024
                    __attrs_140235322507024 = _static_140235424283280

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="configletDescription discreet">\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322504016
                    __attrs_140235322504016 = _static_140235489934800

                    # <Value u'product/description' (192:47)> -> __condition
                    __token = 9154
                    try:
                        __zt_tmp = __attrs_140235322504016
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'product/description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322507152
                        __default_140235322507152 = _DEFAULT_MARKER

                        # <Value u'product/description' (194:37)> -> __cache_140235322503824
                        __token = 9254
                        try:
                            __zt_tmp = __attrs_140235322504016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235322503824 = _static_140235435449424('path', u'product/description', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/description' (194:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b14953790> -> __condition
                        __expression = __cache_140235322503824

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'add-on description')
                        else:
                            __content = __cache_140235322503824
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append(u'\n                      ')

                    # <Static value=<_ast.Dict object at 0x7f8b14953b10> name=None at 7f8b14953a50> -> __attrs_140235321951888
                    __attrs_140235321951888 = _static_140235322506000

                    # <em ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<em class="discreet"> \u2013 (')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321952528
                    __attrs_140235321952528 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321952080
                    __default_140235321952080 = _DEFAULT_MARKER

                    # <Value u'pid' (195:66)> -> __cache_140235321951760
                    __token = 9371
                    try:
                        __zt_tmp = __attrs_140235321952528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235321951760 = _static_140235435449424('path', u'pid', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'pid' (195:66)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148cc6d0> -> __condition
                    __expression = __cache_140235321951760

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>plugin.app.name</span>')
                    else:
                        __content = __cache_140235321951760
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u' ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321951824
                    __attrs_140235321951824 = _static_140235489934800

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321954256
                    __default_140235321954256 = _DEFAULT_MARKER

                    # <Value u'product/version' (195:113)> -> __cache_140235321952720
                    __token = 9418
                    try:
                        __zt_tmp = __attrs_140235321951824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235321952720 = _static_140235435449424('path', u'product/version', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'product/version' (195:113)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148cce90> -> __condition
                    __expression = __cache_140235321952720

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>1.0</span>')
                    else:
                        __content = __cache_140235321952720
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u')</em>\n                    </p>\n                    ')

                    # <Static value=<_ast.Dict object at 0x7f8b148cc8d0> name=None at 7f8b14953b50> -> __attrs_140235321952784
                    __attrs_140235321952784 = _static_140235321952464

                    # <Value u'not:product/uninstall_profile' (199:39)> -> __condition
                    __token = 9605
                    try:
                        __zt_tmp = __attrs_140235321952784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('not', u'product/uninstall_profile', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <dl ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dl class="portalMessage info" role="status">\n                      ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322036368
                        __attrs_140235322036368 = _static_140235489934800

                        # <dt ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dt>')
                        __stream_140235322038160 = []
                        __append_140235322038160 = __stream_140235322038160.append
                        __append_140235322038160(u'Info')
                        __msgid_140235322038160 = __re_whitespace(''.join(__stream_140235322038160)).strip()
                        if __msgid_140235322038160:
                            __append(translate(__msgid_140235322038160, mapping=None, default=__msgid_140235322038160, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</dt>\n                      ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322038352
                        __attrs_140235322038352 = _static_140235489934800

                        # <dd ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<dd>')
                        __stream_140235322038736 = []
                        __append_140235322038736 = __stream_140235322038736.append
                        __append_140235322038736(u'This product cannot be uninstalled!')
                        __msgid_140235322038736 = __re_whitespace(''.join(__stream_140235322038736)).strip()
                        if __msgid_140235322038736:
                            __append(translate(__msgid_140235322038736, mapping=None, default=__msgid_140235322038736, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                        __append(u'</dd>\n                    </dl>')
                    __append(u'\n                ')
                    if (__backup_pid_140235374164048 is __marker):
                        del econtext['pid']
                    else:
                        econtext['pid'] = __backup_pid_140235374164048
                    __append(u'\n                </li>')
                    ____index_140235424628240 -= 1
                    if (____index_140235424628240 > 0):
                        __append('\n                ')
                if (__backup_product_140235374259920 is __marker):
                    del econtext['product']
                else:
                    econtext['product'] = __backup_product_140235374259920
                __append(u'\n              </ul>\n          </section>\n        </section>')
                if (__backup_num_products_140235321944144 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140235321944144
                if (__backup_products_140235321942992 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140235321942992
                __append(u'\n\n        ')

                # <Static value=<_ast.Dict object at 0x7f8b1493f2d0> name=None at 7f8b1493fed0> -> __attrs_140235321950864
                __attrs_140235321950864 = _static_140235322421968
                __backup_products_140235374165520 = get('products', __marker)

                # <Value u'view/get_broken' (209:38)> -> __value
                __token = 9954
                try:
                    __zt_tmp = __attrs_140235321950864
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/get_broken', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['products'] = __value
                __backup_num_products_140235321943632 = get('num_products', __marker)

                # <Value u'python:len(products)' (210:41)> -> __value
                __token = 10012
                try:
                    __zt_tmp = __attrs_140235321950864
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u'len(products)', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['num_products'] = __value

                # <Value u'num_products' (211:32)> -> __condition
                __token = 10068
                try:
                    __zt_tmp = __attrs_140235321950864
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'num_products', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section id="broken-products" class="portlet">\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8b148e1550> name=None at 7f8b148e1590> -> __attrs_140235322038608
                    __attrs_140235322038608 = _static_140235322037584

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<header class="portletHeader">')
                    __stream_140235322040080 = []
                    __append_140235322040080 = __stream_140235322040080.append
                    __append_140235322040080(u'Broken add-ons')
                    __msgid_140235322040080 = __re_whitespace(''.join(__stream_140235322040080)).strip()
                    if __msgid_140235322040080:
                        __append(translate(__msgid_140235322040080, mapping=None, default=__msgid_140235322040080, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</header>\n          ')

                    # <Static value=<_ast.Dict object at 0x7f8b148e1ed0> name=None at 7f8b148e13d0> -> __attrs_140235322451472
                    __attrs_140235322451472 = _static_140235322040016

                    # <section ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<section class="portletContent">\n            ')

                    # <Static value=<_ast.Dict object at 0x7f8b14946d10> name=None at 7f8b149468d0> -> __attrs_140235322453200
                    __attrs_140235322453200 = _static_140235322453264

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<ul class="configlets">\n              ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322452304
                    __attrs_140235322452304 = _static_140235489934800
                    __backup_product_140235322010192 = get('product', __marker)

                    # <Value u'products' (216:38)> -> __iterator
                    __token = 10336
                    try:
                        __zt_tmp = __attrs_140235322452304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140235435449424('path', u'products', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    (__iterator, ____index_140235322452432, ) = getitem('repeat')(u'product', __iterator)
                    econtext['product'] = None
                    for __item in __iterator:
                        econtext['product'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<li>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322137488
                        __attrs_140235322137488 = _static_140235489934800

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<h3>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322138512
                        __attrs_140235322138512 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322138384
                        __default_140235322138384 = _DEFAULT_MARKER

                        # <Value u'product/product_id' (218:37)> -> __cache_140235322136784
                        __token = 10405
                        try:
                            __zt_tmp = __attrs_140235322138512
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235322136784 = _static_140235435449424('path', u'product/product_id', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/product_id' (218:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148f9dd0> -> __condition
                        __expression = __cache_140235322136784

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<span>\n                    Add-on Name\n                  </span>')
                        else:
                            __content = __cache_140235322136784
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'\n                </h3>\n                ')

                        # <Static value=<_ast.Dict object at 0x7f8b148f9290> name=None at 7f8b148f9350> -> __attrs_140235322136144
                        __attrs_140235322136144 = _static_140235322135184

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<p class="configletDescription discreet">\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322135440
                        __attrs_140235322135440 = _static_140235489934800

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<span>')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322134864
                        __default_140235322134864 = _DEFAULT_MARKER

                        # <Value u'product/type' (223:37)> -> __cache_140235322135824
                        __token = 10619
                        try:
                            __zt_tmp = __attrs_140235322135440
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235322135824 = _static_140235435449424('path', u'product/type', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/type' (223:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148f9a90> -> __condition
                        __expression = __cache_140235322135824

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Error Type')
                        else:
                            __content = __cache_140235322135824
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</span>\n                  ')

                        # <Static value=<_ast.Dict object at 0x7f8b148ede50> name=None at 7f8b148f9550> -> __attrs_140235322087120
                        __attrs_140235322087120 = _static_140235322089040

                        # <em ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<em class="discreet"> - ')

                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322088784
                        __attrs_140235322088784 = _static_140235489934800

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235322085584
                        __default_140235322085584 = _DEFAULT_MARKER

                        # <Value u'product/value' (224:65)> -> __cache_140235322087440
                        __token = 10734
                        try:
                            __zt_tmp = __attrs_140235322088784
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235322087440 = _static_140235435449424('path', u'product/value', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'product/value' (224:65)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148ed9d0> -> __condition
                        __expression = __cache_140235322087440

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Error Reason')
                        else:
                            __content = __cache_140235322087440
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</em>\n                </p>\n              </li>')
                        ____index_140235322452432 -= 1
                        if (____index_140235322452432 > 0):
                            __append('\n              ')
                    if (__backup_product_140235322010192 is __marker):
                        del econtext['product']
                    else:
                        econtext['product'] = __backup_product_140235322010192
                    __append(u'\n            </ul>\n          </section>\n        </section>')
                if (__backup_num_products_140235321943632 is __marker):
                    del econtext['num_products']
                else:
                    econtext['num_products'] = __backup_num_products_140235321943632
                if (__backup_products_140235374165520 is __marker):
                    del econtext['products']
                else:
                    econtext['products'] = __backup_products_140235374165520
                __append(u'\n\n    </div>\n')
                __i18n_domain = __previous_i18n_domain_140235322094224
            _slots = econtext[u'__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value u'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140235322094864
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140235435449424('path', u'context/prefs_main_template/macros/master', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140235373760992 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140235373760992
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
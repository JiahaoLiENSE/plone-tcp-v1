# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/controlpanel/browser/overview.pt'

__tokens = {421: (u"python:request.set('disable_plone.leftcolumn',1)", 12, 47), 517: (u" python:request.set('disable_plone.rightcolumn',1", 13, 46), 932: (u'view/python2_warning', 26, 24), 1336: (u'view/python_warning', 38, 24), 1679: (u'view/plone_maintenance_warning', 49, 24), 2056: (u'view/plone_security_warning', 60, 24), 2424: (u'view/version_warning', 71, 24), 3038: (u'view/upgrade_warning', 89, 24), 3335: (u'string:${context/portal_url}/@@plone-upgrade', 97, 36), 3731: (u'view/mailhost_warning', 109, 24), 4322: (u'string:${portal_url}/@@mail-controlpanel', 120, 40), 4567: (u'view/timezone_warning', 129, 24), 5120: (u'string:${portal_url}/@@dateandtime-controlpanel', 141, 40), 5390: (u'not:view/pil', 150, 24), 5687: (u'view/categories', 159, 39), 5741: (u"python:view.sublists(category.get('id'))", 160, 36), 5871: (u'sublist', 161, 87), 5934: (u'category/title', 162, 53), 6052: (u'sublist', 165, 53), 6133: (u'sublist', 168, 31), 6189: (u'sublist', 169, 46), 6275: (u'action/visible', 170, 76), 6429: (u'action/icon', 173, 46), 6492: (u'action/url', 174, 50), 6562: (u"python:'icon-controlpanel-' + action['id'].replace('.', '_')", 175, 57), 6686: (u'action/title', 176, 54), 7074: (u'not:sublist', 188, 32), 7447: (u'view/version_overview', 201, 41), 7496: (u'version', 202, 25), 7587: (u'view/server_info', 204, 42), 7643: (u' server_info/wsg', 205, 38), 7787: (u'has_wsgi', 208, 51), 7858: (u'not:has_wsgi', 209, 51), 7991: (u'${server_info/server_name}', 213, 18), 7993: (u'server_info/server_name', 213, 20), 8043: (u'${server_info/version}', 214, 18), 8045: (u'server_info/version', 214, 20), 8143: (u'not:view/is_dev_mode', 220, 22), 8721: (u'view/is_dev_mode', 232, 22), 261: (u'here/prefs_main_template/macros/master', 6, 23), 261: (u'here/prefs_main_template/macros/master', 6, 23)}

from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140235424628624 = {u'class': u'discreet', }
_static_140235374256336 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140235357421712 = {u'class': u'discreet', }
_static_140235322041808 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140235368757904 = {u'href': u'https://plone.org/download/release-schedule', }
_static_140235321930192 = {u'class': u'portletHeader', }
_static_140235431247824 = {u'href': u'', }
_static_140235428392592 = {u'href': u'#', u'title': u'Go to the upgrade page', }
_static_140235423487248 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140235321943056 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140235322043920 = {u'href': u'', }
_static_140235428389136 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140235431247312 = {u'class': u"python:'icon-controlpanel-' + action['id'].replace('.', '_')", }
_static_140235368765072 = {u'class': u'inner-configlet', }
_static_140235368752016 = {u'class': u'documentDescription', }
_static_140235435450064 = __C2ZContextWrapper
_static_140235431257680 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140235377022352 = {u'class': u'discreet', }
_static_140235368765584 = {u'class': u'row configlets', }
_static_140235489934800 = {}
_static_140235321945040 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140235435449424 = __compile_zt_expr
_static_140235321933200 = {u'class': u'portlet portletNavigationTree portletSiteSetup', }
_static_140235321999312 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140235426049744 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140235357425168 = {u'href': u'', }
_static_140235428378960 = {u'class': u'portletContent', }
_static_140235321985104 = u'master'
_static_140235321933584 = {u'class': u'visualClear', }
_static_140235368764752 = {u'class': u'col-xs-4 col-sm-3 col-md-2', }
_static_140235368751184 = {u'class': u'documentFirstHeading', }

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

            # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374096336
            __attrs_140235374096336 = _static_140235489934800
            __previous_i18n_domain_140235321985488 = __i18n_domain
            __i18n_domain = u'plone'
            __backup_macroname_140235437953584 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f8b148d4850> name=None at 7f8b148d4490> -> __value
            __value = _static_140235321985104
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321984400
                __attrs_140235321984400 = _static_140235489934800
                __backup_disable_column_one_140235321984272 = get('disable_column_one', __marker)

                # <Value u"python:request.set('disable_plone.leftcolumn',1)" (12:47)> -> __value
                __token = 421
                try:
                    __zt_tmp = __attrs_140235321984400
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u"request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_140235321986512 = get('disable_column_two', __marker)

                # <Value u"python:request.set('disable_plone.rightcolumn',1)" (13:46)> -> __value
                __token = 517
                try:
                    __zt_tmp = __attrs_140235321984400
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('python', u"request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_140235321986512 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_140235321986512
                if (__backup_disable_column_one_140235321984272 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_140235321984272
            _slots = econtext[u'__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321983120
                __attrs_140235321983120 = _static_140235489934800

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1756e050> name=None at 7f8b1756e4d0> -> __attrs_140235368751632
                __attrs_140235368751632 = _static_140235368751184

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1 class="documentFirstHeading">')
                __stream_140235368753680 = []
                __append_140235368753680 = __stream_140235368753680.append
                __append_140235368753680(u'Site Setup')
                __msgid_140235368753680 = __re_whitespace(''.join(__stream_140235368753680)).strip()
                if __msgid_140235368753680:
                    __append(translate(__msgid_140235368753680, mapping=None, default=__msgid_140235368753680, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</h1>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1756e390> name=None at 7f8b1756e7d0> -> __attrs_140235321945296
                __attrs_140235321945296 = _static_140235368752016

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="documentDescription">')
                __stream_140235368752720 = []
                __append_140235368752720 = __stream_140235368752720.append
                __append_140235368752720(u'\n        Configuration area for Plone and add-on Products.\n    ')
                __msgid_140235368752720 = __re_whitespace(''.join(__stream_140235368752720)).strip()
                if u'description_control_panel':
                    __append(translate(u'description_control_panel', mapping=None, default=__msgid_140235368752720, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</p>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b148ca410> name=None at 7f8b148ca3d0> -> __attrs_140235321943120
                __attrs_140235321943120 = _static_140235321943056

                # <Value u'view/python2_warning' (26:24)> -> __condition
                __token = 932
                try:
                    __zt_tmp = __attrs_140235321943120
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/python2_warning', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321942672
                    __attrs_140235321942672 = _static_140235489934800

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140235321945168 = []
                    __append_140235321945168 = __stream_140235321945168.append
                    __append_140235321945168(u'\n            Warning\n        ')
                    __msgid_140235321945168 = __re_whitespace(''.join(__stream_140235321945168)).strip()
                    if __msgid_140235321945168:
                        __append(translate(__msgid_140235321945168, mapping=None, default=__msgid_140235321945168, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321942224
                    __attrs_140235321942224 = _static_140235489934800
                    __stream_140235321943760 = []
                    __append_140235321943760 = __stream_140235321943760.append
                    __append_140235321943760(u'\n            You are using Python 2.\n            This should only be used temporarily while preparing to migrate to Python 3.\n        ')
                    __msgid_140235321943760 = __re_whitespace(''.join(__stream_140235321943760)).strip()
                    if u'text_python2_warning':
                        __append(translate(u'text_python2_warning', mapping=None, default=__msgid_140235321943760, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b148cabd0> name=None at 7f8b148ca1d0> -> __attrs_140235374258384
                __attrs_140235374258384 = _static_140235321945040

                # <Value u'view/python_warning' (38:24)> -> __condition
                __token = 1336
                try:
                    __zt_tmp = __attrs_140235374258384
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/python_warning', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374259920
                    __attrs_140235374259920 = _static_140235489934800

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140235374259344 = []
                    __append_140235374259344 = __stream_140235374259344.append
                    __append_140235374259344(u'\n            Warning\n        ')
                    __msgid_140235374259344 = __re_whitespace(''.join(__stream_140235374259344)).strip()
                    if __msgid_140235374259344:
                        __append(translate(__msgid_140235374259344, mapping=None, default=__msgid_140235374259344, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235374257296
                    __attrs_140235374257296 = _static_140235489934800
                    __stream_140235374258768 = []
                    __append_140235374258768 = __stream_140235374258768.append
                    __append_140235374258768(u'\n            You are using a Python version that is not supported.\n        ')
                    __msgid_140235374258768 = __re_whitespace(''.join(__stream_140235374258768)).strip()
                    if u'text_python_warning':
                        __append(translate(u'text_python_warning', mapping=None, default=__msgid_140235374258768, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b17aae0d0> name=None at 7f8b17aae250> -> __attrs_140235321998160
                __attrs_140235321998160 = _static_140235374256336

                # <Value u'view/plone_maintenance_warning' (49:24)> -> __condition
                __token = 1679
                try:
                    __zt_tmp = __attrs_140235321998160
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/plone_maintenance_warning', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321995664
                    __attrs_140235321995664 = _static_140235489934800

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140235321997008 = []
                    __append_140235321997008 = __stream_140235321997008.append
                    __append_140235321997008(u'\n            Warning\n        ')
                    __msgid_140235321997008 = __re_whitespace(''.join(__stream_140235321997008)).strip()
                    if __msgid_140235321997008:
                        __append(translate(__msgid_140235321997008, mapping=None, default=__msgid_140235321997008, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321996112
                    __attrs_140235321996112 = _static_140235489934800
                    __stream_140235321995792 = []
                    __append_140235321995792 = __stream_140235321995792.append
                    __append_140235321995792(u'\n            You are using a Plone version that is out of maintenance support.\n        ')
                    __msgid_140235321995792 = __re_whitespace(''.join(__stream_140235321995792)).strip()
                    if u'text_plone_maintenance_warning':
                        __append(translate(u'text_plone_maintenance_warning', mapping=None, default=__msgid_140235321995792, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b148d7fd0> name=None at 7f8b148d7e50> -> __attrs_140235321996368
                __attrs_140235321996368 = _static_140235321999312

                # <Value u'view/plone_security_warning' (60:24)> -> __condition
                __token = 2056
                try:
                    __zt_tmp = __attrs_140235321996368
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/plone_security_warning', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321998864
                    __attrs_140235321998864 = _static_140235489934800

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140235321998352 = []
                    __append_140235321998352 = __stream_140235321998352.append
                    __append_140235321998352(u'\n            Warning\n        ')
                    __msgid_140235321998352 = __re_whitespace(''.join(__stream_140235321998352)).strip()
                    if __msgid_140235321998352:
                        __append(translate(__msgid_140235321998352, mapping=None, default=__msgid_140235321998352, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431257552
                    __attrs_140235431257552 = _static_140235489934800
                    __stream_140235431259472 = []
                    __append_140235431259472 = __stream_140235431259472.append
                    __append_140235431259472(u'\n            You are using a Plone version that is out of security support.\n        ')
                    __msgid_140235431259472 = __re_whitespace(''.join(__stream_140235431259472)).strip()
                    if u'text_plone_security_warning':
                        __append(translate(u'text_plone_security_warning', mapping=None, default=__msgid_140235431259472, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1b10a650> name=None at 7f8b1b10a150> -> __attrs_140235431257040
                __attrs_140235431257040 = _static_140235431257680

                # <Value u'view/version_warning' (71:24)> -> __condition
                __token = 2424
                try:
                    __zt_tmp = __attrs_140235431257040
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/version_warning', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431258384
                    __attrs_140235431258384 = _static_140235489934800

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140235431259600 = []
                    __append_140235431259600 = __stream_140235431259600.append
                    __append_140235431259600(u'\n            Warning\n        ')
                    __msgid_140235431259600 = __re_whitespace(''.join(__stream_140235431259600)).strip()
                    if __msgid_140235431259600:
                        __append(translate(__msgid_140235431259600, mapping=None, default=__msgid_140235431259600, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235423489360
                    __attrs_140235423489360 = _static_140235489934800
                    __stream_140235322618656_plone_release_schedule_link = ''
                    __stream_140235423488912 = []
                    __append_140235423488912 = __stream_140235423488912.append
                    __append_140235423488912(u'\n            Go to the\n            ')
                    __stream_140235322618656_plone_release_schedule_link = []
                    __append_140235322618656_plone_release_schedule_link = __stream_140235322618656_plone_release_schedule_link.append

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235423486352
                    __attrs_140235423486352 = _static_140235489934800
                    __append_140235322618656_plone_release_schedule_link(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8b1756fa90> name=None at 7f8b1756f390> -> __attrs_140235368756624
                    __attrs_140235368756624 = _static_140235368757904

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140235322618656_plone_release_schedule_link(u'<a href="https://plone.org/download/release-schedule" >')
                    __stream_140235368755344 = []
                    __append_140235368755344 = __stream_140235368755344.append
                    __append_140235368755344(u'Plone release schedule')
                    __msgid_140235368755344 = __re_whitespace(''.join(__stream_140235368755344)).strip()
                    if u'text_plone_release_schedule_link':
                        __append_140235322618656_plone_release_schedule_link(translate(u'text_plone_release_schedule_link', mapping=None, default=__msgid_140235368755344, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140235322618656_plone_release_schedule_link(u'</a>\n            ')
                    __append_140235423488912(u'${plone_release_schedule_link}')
                    __stream_140235322618656_plone_release_schedule_link = ''.join(__stream_140235322618656_plone_release_schedule_link)
                    __append_140235423488912(u'\n            for more information.\n        ')
                    __msgid_140235423488912 = __re_whitespace(''.join(__stream_140235423488912)).strip()
                    if u'text_plone_release_schedule':
                        __append(translate(u'text_plone_release_schedule', mapping={u'plone_release_schedule_link': __stream_140235322618656_plone_release_schedule_link, }, default=__msgid_140235423488912, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1a9a1510> name=None at 7f8b1a9a1910> -> __attrs_140235368758672
                __attrs_140235368758672 = _static_140235423487248

                # <Value u'view/upgrade_warning' (89:24)> -> __condition
                __token = 3038
                try:
                    __zt_tmp = __attrs_140235368758672
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/upgrade_warning', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235428392208
                    __attrs_140235428392208 = _static_140235489934800

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140235428390992 = []
                    __append_140235428390992 = __stream_140235428390992.append
                    __append_140235428390992(u'\n            Warning\n        ')
                    __msgid_140235428390992 = __re_whitespace(''.join(__stream_140235428390992)).strip()
                    if __msgid_140235428390992:
                        __append(translate(__msgid_140235428390992, mapping=None, default=__msgid_140235428390992, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235428389392
                    __attrs_140235428389392 = _static_140235489934800
                    __stream_140235322618656_link_continue_with_the_upgrade = ''
                    __stream_140235428390864 = []
                    __append_140235428390864 = __stream_140235428390864.append
                    __append_140235428390864(u'\n            The site configuration is outdated and needs to be\n            upgraded. Please\n            ')
                    __stream_140235322618656_link_continue_with_the_upgrade = []
                    __append_140235322618656_link_continue_with_the_upgrade = __stream_140235322618656_link_continue_with_the_upgrade.append

                    # <Static value=<_ast.Dict object at 0x7f8b1ae4ee90> name=None at 7f8b1ae4e750> -> __attrs_140235377127952
                    __attrs_140235377127952 = _static_140235428392592

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140235322618656_link_continue_with_the_upgrade(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235377131472
                    __default_140235377131472 = _DEFAULT_MARKER

                    # <Substitution u'string:${context/portal_url}/@@plone-upgrade' (97:36)> -> __attr_href
                    __token = 3335
                    try:
                        __zt_tmp = __attrs_140235377127952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140235435449424('string', u'${context/portal_url}/@@plone-upgrade', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140235322618656_link_continue_with_the_upgrade((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235377129808
                    __default_140235377129808 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7f8b17d6be90> at 7f8b17d6b650> -> __attr_title
                    __attr_title = u'Go to the upgrade page'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append_140235322618656_link_continue_with_the_upgrade((u' title="%s"' % __attr_title))
                    __append_140235322618656_link_continue_with_the_upgrade(u'>')
                    __stream_140235428390032 = []
                    __append_140235428390032 = __stream_140235428390032.append
                    __append_140235428390032(u'\n              continue with the upgrade\n            ')
                    __msgid_140235428390032 = __re_whitespace(''.join(__stream_140235428390032)).strip()
                    if __msgid_140235428390032:
                        __append_140235322618656_link_continue_with_the_upgrade(translate(__msgid_140235428390032, mapping=None, default=__msgid_140235428390032, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140235322618656_link_continue_with_the_upgrade(u'</a>')
                    __append_140235428390864(u'${link_continue_with_the_upgrade}')
                    __stream_140235322618656_link_continue_with_the_upgrade = ''.join(__stream_140235322618656_link_continue_with_the_upgrade)
                    __append_140235428390864(u'.\n        ')
                    __msgid_140235428390864 = __re_whitespace(''.join(__stream_140235428390864)).strip()
                    if __msgid_140235428390864:
                        __append(translate(__msgid_140235428390864, mapping={u'link_continue_with_the_upgrade': __stream_140235322618656_link_continue_with_the_upgrade, }, default=__msgid_140235428390864, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1ae4e110> name=None at 7f8b1ae4e2d0> -> __attrs_140235377128464
                __attrs_140235377128464 = _static_140235428389136

                # <Value u'view/mailhost_warning' (109:24)> -> __condition
                __token = 3731
                try:
                    __zt_tmp = __attrs_140235377128464
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/mailhost_warning', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426047888
                    __attrs_140235426047888 = _static_140235489934800

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140235426047504 = []
                    __append_140235426047504 = __stream_140235426047504.append
                    __append_140235426047504(u'\n            Warning\n        ')
                    __msgid_140235426047504 = __re_whitespace(''.join(__stream_140235426047504)).strip()
                    if __msgid_140235426047504:
                        __append(translate(__msgid_140235426047504, mapping=None, default=__msgid_140235426047504, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235426047312
                    __attrs_140235426047312 = _static_140235489934800
                    __stream_140235322618656_label_mail_control_panel_link = ''
                    __stream_140235426046928 = []
                    __append_140235426046928 = __stream_140235426046928.append
                    __append_140235426046928(u"\n            You have not configured a mail host or a site 'From'\n            address, various features including contact forms, email\n            notification and password reset will not work. Go to the\n            ")
                    __stream_140235322618656_label_mail_control_panel_link = []
                    __append_140235322618656_label_mail_control_panel_link = __stream_140235322618656_label_mail_control_panel_link.append

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235357422352
                    __attrs_140235357422352 = _static_140235489934800
                    __append_140235322618656_label_mail_control_panel_link(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8b16aa0e10> name=None at 7f8b16aa03d0> -> __attrs_140235357424528
                    __attrs_140235357424528 = _static_140235357425168

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140235322618656_label_mail_control_panel_link(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235357422608
                    __default_140235357422608 = _DEFAULT_MARKER

                    # <Substitution u'string:${portal_url}/@@mail-controlpanel' (120:40)> -> __attr_href
                    __token = 4322
                    try:
                        __zt_tmp = __attrs_140235357424528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140235435449424('string', u'${portal_url}/@@mail-controlpanel', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140235322618656_label_mail_control_panel_link((u' href="%s"' % __attr_href))
                    __append_140235322618656_label_mail_control_panel_link(u' >')
                    __stream_140235357422992 = []
                    __append_140235357422992 = __stream_140235357422992.append
                    __append_140235357422992(u'Mail control panel')
                    __msgid_140235357422992 = __re_whitespace(''.join(__stream_140235357422992)).strip()
                    if u'text_no_mailhost_configured_control_panel_link':
                        __append_140235322618656_label_mail_control_panel_link(translate(u'text_no_mailhost_configured_control_panel_link', mapping=None, default=__msgid_140235357422992, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140235322618656_label_mail_control_panel_link(u'</a>\n            ')
                    __append_140235426046928(u'${label_mail_control_panel_link}')
                    __stream_140235322618656_label_mail_control_panel_link = ''.join(__stream_140235322618656_label_mail_control_panel_link)
                    __append_140235426046928(u'\n            to fix this.\n        ')
                    __msgid_140235426046928 = __re_whitespace(''.join(__stream_140235426046928)).strip()
                    if u'text_no_mailhost_configured':
                        __append(translate(u'text_no_mailhost_configured', mapping={u'label_mail_control_panel_link': __stream_140235322618656_label_mail_control_panel_link, }, default=__msgid_140235426046928, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1ac12ed0> name=None at 7f8b1ac12b10> -> __attrs_140235357424272
                __attrs_140235357424272 = _static_140235426049744

                # <Value u'view/timezone_warning' (129:24)> -> __condition
                __token = 4567
                try:
                    __zt_tmp = __attrs_140235357424272
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/timezone_warning', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322042768
                    __attrs_140235322042768 = _static_140235489934800

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140235322042384 = []
                    __append_140235322042384 = __stream_140235322042384.append
                    __append_140235322042384(u'\n            Warning\n        ')
                    __msgid_140235322042384 = __re_whitespace(''.join(__stream_140235322042384)).strip()
                    if __msgid_140235322042384:
                        __append(translate(__msgid_140235322042384, mapping=None, default=__msgid_140235322042384, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322042320
                    __attrs_140235322042320 = _static_140235489934800
                    __stream_140235322618656_label_mail_event_settings_link = ''
                    __stream_140235322043472 = []
                    __append_140235322043472 = __stream_140235322043472.append
                    __append_140235322043472(u'\n\n            You have not set the portal timezone. Date/Time handling will not\n            work properly for timezone aware date/time values.\n            Go to the\n            ')
                    __stream_140235322618656_label_mail_event_settings_link = []
                    __append_140235322618656_label_mail_event_settings_link = __stream_140235322618656_label_mail_event_settings_link.append

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235322042960
                    __attrs_140235322042960 = _static_140235489934800
                    __append_140235322618656_label_mail_event_settings_link(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7f8b148e2e10> name=None at 7f8b148e2850> -> __attrs_140235431286864
                    __attrs_140235431286864 = _static_140235322043920

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140235322618656_label_mail_event_settings_link(u'<a')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431288720
                    __default_140235431288720 = _DEFAULT_MARKER

                    # <Substitution u'string:${portal_url}/@@dateandtime-controlpanel' (141:40)> -> __attr_href
                    __token = 5120
                    try:
                        __zt_tmp = __attrs_140235431286864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140235435449424('string', u'${portal_url}/@@dateandtime-controlpanel', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140235322618656_label_mail_event_settings_link((u' href="%s"' % __attr_href))
                    __append_140235322618656_label_mail_event_settings_link(u' >')
                    __stream_140235322040976 = []
                    __append_140235322040976 = __stream_140235322040976.append
                    __append_140235322040976(u'Date and Time Settings control panel')
                    __msgid_140235322040976 = __re_whitespace(''.join(__stream_140235322040976)).strip()
                    if u'text_no_timezone_configured_control_panel_link':
                        __append_140235322618656_label_mail_event_settings_link(translate(u'text_no_timezone_configured_control_panel_link', mapping=None, default=__msgid_140235322040976, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140235322618656_label_mail_event_settings_link(u'</a>\n            ')
                    __append_140235322043472(u'${label_mail_event_settings_link}')
                    __stream_140235322618656_label_mail_event_settings_link = ''.join(__stream_140235322618656_label_mail_event_settings_link)
                    __append_140235322043472(u'\n            to fix this.\n        ')
                    __msgid_140235322043472 = __re_whitespace(''.join(__stream_140235322043472)).strip()
                    if u'text_no_timezone_configured':
                        __append(translate(u'text_no_timezone_configured', mapping={u'label_mail_event_settings_link': __stream_140235322618656_label_mail_event_settings_link, }, default=__msgid_140235322043472, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b148e25d0> name=None at 7f8b148e2d50> -> __attrs_140235431287184
                __attrs_140235431287184 = _static_140235322041808

                # <Value u'not:view/pil' (150:24)> -> __condition
                __token = 5390
                try:
                    __zt_tmp = __attrs_140235431287184
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('not', u'view/pil', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431285456
                    __attrs_140235431285456 = _static_140235489934800

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140235431287568 = []
                    __append_140235431287568 = __stream_140235431287568.append
                    __append_140235431287568(u'\n            Warning\n        ')
                    __msgid_140235431287568 = __re_whitespace(''.join(__stream_140235431287568)).strip()
                    if __msgid_140235431287568:
                        __append(translate(__msgid_140235431287568, mapping=None, default=__msgid_140235431287568, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431285840
                    __attrs_140235431285840 = _static_140235489934800
                    __stream_140235431285136 = []
                    __append_140235431285136 = __stream_140235431285136.append
                    __append_140235431285136(u'\n            PIL is not installed properly, image scaling will not work.\n        ')
                    __msgid_140235431285136 = __re_whitespace(''.join(__stream_140235431285136)).strip()
                    if u'text_no_pil_installed':
                        __append(translate(u'text_no_pil_installed', mapping=None, default=__msgid_140235431285136, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235431287376
                __attrs_140235431287376 = _static_140235489934800
                __backup_category_140235368754704 = get('category', __marker)

                # <Value u'view/categories' (159:39)> -> __iterator
                __token = 5687
                try:
                    __zt_tmp = __attrs_140235431287376
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140235435449424('path', u'view/categories', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                (__iterator, ____index_140235321931024, ) = getitem('repeat')(u'category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321930320
                    __attrs_140235321930320 = _static_140235489934800
                    __backup_sublist_140235368751312 = get('sublist', __marker)

                    # <Value u"python:view.sublists(category.get('id'))" (160:36)> -> __value
                    __token = 5741
                    try:
                        __zt_tmp = __attrs_140235321930320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140235435449424('python', u"view.sublists(category.get('id'))", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    econtext['sublist'] = __value
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b148c7d90> name=None at 7f8b148c7290> -> __attrs_140235321931600
                    __attrs_140235321931600 = _static_140235321933200

                    # <Value u'sublist' (161:87)> -> __condition
                    __token = 5871
                    try:
                        __zt_tmp = __attrs_140235321931600
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140235435449424('path', u'sublist', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                    if __condition:

                        # <section ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<section class="portlet portletNavigationTree portletSiteSetup">\n          ')

                        # <Static value=<_ast.Dict object at 0x7f8b148c71d0> name=None at 7f8b148c7690> -> __attrs_140235428378704
                        __attrs_140235428378704 = _static_140235321930192

                        # <header ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<header class="portletHeader">')

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235321931984
                        __default_140235321931984 = _DEFAULT_MARKER

                        # <Value u'category/title' (162:53)> -> __cache_140235321930704
                        __token = 5934
                        try:
                            __zt_tmp = __attrs_140235428378704
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140235321930704 = _static_140235435449424('path', u'category/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                        # <BinOp left=<Value u'category/title' (162:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b148c7710> -> __condition
                        __expression = __cache_140235321930704

                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Category')
                        else:
                            __content = __cache_140235321930704
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</header>\n\n          ')

                        # <Static value=<_ast.Dict object at 0x7f8b1ae4b950> name=None at 7f8b1ae4be90> -> __attrs_140235428378064
                        __attrs_140235428378064 = _static_140235428378960

                        # <Value u'sublist' (165:53)> -> __condition
                        __token = 6052
                        try:
                            __zt_tmp = __attrs_140235428378064
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140235435449424('path', u'sublist', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        if __condition:

                            # <nav ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<nav class="portletContent">\n\n            ')

                            # <Static value=<_ast.Dict object at 0x7f8b17571890> name=None at 7f8b17571190> -> __attrs_140235368765328
                            __attrs_140235368765328 = _static_140235368765584

                            # <Value u'sublist' (168:31)> -> __condition
                            __token = 6133
                            try:
                                __zt_tmp = __attrs_140235368765328
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140235435449424('path', u'sublist', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                            if __condition:

                                # <ul ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<ul class="row configlets">\n              ')

                                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235377129616
                                __attrs_140235377129616 = _static_140235489934800
                                __backup_action_140235428380368 = get('action', __marker)

                                # <Value u'sublist' (169:46)> -> __iterator
                                __token = 6189
                                try:
                                    __zt_tmp = __attrs_140235377129616
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_140235435449424('path', u'sublist', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                (__iterator, ____index_140235377130320, ) = getitem('repeat')(u'action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item
                                    __append(u'\n                      ')

                                    # <Static value=<_ast.Dict object at 0x7f8b17571550> name=None at 7f8b16aa0bd0> -> __attrs_140235368763984
                                    __attrs_140235368763984 = _static_140235368764752

                                    # <Value u'action/visible' (170:76)> -> __condition
                                    __token = 6275
                                    try:
                                        __zt_tmp = __attrs_140235368763984
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_140235435449424('path', u'action/visible', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                    if __condition:

                                        # <li ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<li class="col-xs-4 col-sm-3 col-md-2">\n                        ')

                                        # <Static value=<_ast.Dict object at 0x7f8b17571690> name=None at 7f8b17571b10> -> __attrs_140235431244048
                                        __attrs_140235431244048 = _static_140235368765072

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<div class="inner-configlet">\n                          ')

                                        # <Static value=<_ast.Dict object at 0x7f8b1b107fd0> name=None at 7f8b1b107f50> -> __attrs_140235431243984
                                        __attrs_140235431243984 = _static_140235431247824
                                        __backup_icon_140235424482832 = get('icon', __marker)

                                        # <Value u'action/icon' (173:46)> -> __value
                                        __token = 6429
                                        try:
                                            __zt_tmp = __attrs_140235431243984
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_140235435449424('path', u'action/icon', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                        econtext['icon'] = __value

                                        # <a ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<a')

                                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431245392
                                        __default_140235431245392 = _DEFAULT_MARKER

                                        # <Substitution u'action/url' (174:50)> -> __attr_href
                                        __token = 6492
                                        try:
                                            __zt_tmp = __attrs_140235431243984
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_href = _static_140235435449424('path', u'action/url', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                        __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                                        if (__attr_href is not None):
                                            __append((u' href="%s"' % __attr_href))
                                        __append(u'>\n                             ')

                                        # <Static value=<_ast.Dict object at 0x7f8b1b107dd0> name=None at 7f8b1b107d10> -> __attrs_140235431245264
                                        __attrs_140235431245264 = _static_140235431247312

                                        # <span ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<span')

                                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235431244752
                                        __default_140235431244752 = _DEFAULT_MARKER

                                        # <Substitution u"python:'icon-controlpanel-' + action['id'].replace('.', '_')" (175:57)> -> __attr_class
                                        __token = 6562
                                        try:
                                            __zt_tmp = __attrs_140235431245264
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_class = _static_140235435449424('python', u"'icon-controlpanel-' + action['id'].replace('.', '_')", econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_class is not None):
                                            __append((u' class="%s"' % __attr_class))
                                        __append(u'></span>\n                              ')

                                        # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432291728
                                        __attrs_140235432291728 = _static_140235489934800

                                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235432289360
                                        __default_140235432289360 = _DEFAULT_MARKER

                                        # <Value u'action/title' (176:54)> -> __cache_140235432290128
                                        __token = 6686
                                        try:
                                            __zt_tmp = __attrs_140235432291728
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_140235432290128 = _static_140235435449424('path', u'action/title', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                                        # <BinOp left=<Value u'action/title' (176:54)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b1b2063d0> -> __condition
                                        __expression = __cache_140235432290128

                                        # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            __append(u'\n                                  Title\n                              ')
                                        else:
                                            __content = __cache_140235432290128
                                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                            __content = __quote(__content, None, '\xad', None, None)
                                            if (__content is not None):
                                                __append(__content)
                                        __append(u'\n                          </a>')
                                        if (__backup_icon_140235424482832 is __marker):
                                            del econtext['icon']
                                        else:
                                            econtext['icon'] = __backup_icon_140235424482832
                                        __append(u'\n                        </div>\n                      </li>')
                                    __append(u'\n                  ')
                                    ____index_140235377130320 -= 1
                                    if (____index_140235377130320 > 0):
                                        __append('')
                                if (__backup_action_140235428380368 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_140235428380368
                                __append(u'\n                </ul>')
                            __append(u'\n            </nav>')
                        __append(u'\n\n            ')

                        # <Static value=<_ast.Dict object at 0x7f8b16aa0090> name=None at 7f8b16aa0b50> -> __attrs_140235431245200
                        __attrs_140235431245200 = _static_140235357421712

                        # <Value u'not:sublist' (188:32)> -> __condition
                        __token = 7074
                        try:
                            __zt_tmp = __attrs_140235431245200
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140235435449424('not', u'sublist', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="discreet">')
                            __stream_140235374096144 = []
                            __append_140235374096144 = __stream_140235374096144.append
                            __append_140235374096144(u'\n                No preference panels available.\n            ')
                            __msgid_140235374096144 = __re_whitespace(''.join(__stream_140235374096144)).strip()
                            if u'label_no_prefs_panels_available':
                                __append(translate(u'label_no_prefs_panels_available', mapping=None, default=__msgid_140235374096144, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</div>')
                        __append(u'\n\n        </section>')
                    __append(u'\n      ')
                    if (__backup_sublist_140235368751312 is __marker):
                        del econtext['sublist']
                    else:
                        econtext['sublist'] = __backup_sublist_140235368751312
                    __append(u'\n    ')
                    ____index_140235321931024 -= 1
                    if (____index_140235321931024 > 0):
                        __append('')
                if (__backup_category_140235368754704 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_140235368754704
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b148c7f10> name=None at 7f8b1b111090> -> __attrs_140235321933136
                __attrs_140235321933136 = _static_140235321933584

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear"><!-- --></div>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432290768
                __attrs_140235432290768 = _static_140235489934800

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h2>')
                __stream_140235432288656 = []
                __append_140235432288656 = __stream_140235432288656.append
                __append_140235432288656(u'Version Overview')
                __msgid_140235432288656 = __re_whitespace(''.join(__stream_140235432288656)).strip()
                if u'heading_version_overview':
                    __append(translate(u'heading_version_overview', mapping=None, default=__msgid_140235432288656, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</h2>\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235432290832
                __attrs_140235432290832 = _static_140235489934800

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul>\n      ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235377024528
                __attrs_140235377024528 = _static_140235489934800
                __backup_version_140235321985232 = get('version', __marker)

                # <Value u'view/version_overview' (201:41)> -> __iterator
                __token = 7447
                try:
                    __zt_tmp = __attrs_140235377024528
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140235435449424('path', u'view/version_overview', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                (__iterator, ____index_140235377023312, ) = getitem('repeat')(u'version', __iterator)
                econtext['version'] = None
                for __item in __iterator:
                    econtext['version'] = __item
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235377023440
                    __attrs_140235377023440 = _static_140235489934800

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>')

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __default_140235377022096
                    __default_140235377022096 = _DEFAULT_MARKER

                    # <Value u'version' (202:25)> -> __cache_140235377022032
                    __token = 7496
                    try:
                        __zt_tmp = __attrs_140235377023440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140235377022032 = _static_140235435449424('path', u'version', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))

                    # <BinOp left=<Value u'version' (202:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f8b1e8fff10> at 7f8b17d512d0> -> __condition
                    __expression = __cache_140235377022032

                    # <Symbol value=<DEFAULT> at 7f8b1e8fff10> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'Version')
                    else:
                        __content = __cache_140235377022032
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</li>\n      ')
                    ____index_140235377023312 -= 1
                    if (____index_140235377023312 > 0):
                        __append('')
                if (__backup_version_140235321985232 is __marker):
                    del econtext['version']
                else:
                    econtext['version'] = __backup_version_140235321985232
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235377022928
                __attrs_140235377022928 = _static_140235489934800
                __backup_server_info_140235423486160 = get('server_info', __marker)

                # <Value u'view/server_info' (204:42)> -> __value
                __token = 7587
                try:
                    __zt_tmp = __attrs_140235377022928
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'view/server_info', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['server_info'] = __value
                __backup_has_wsgi_140235423489040 = get('has_wsgi', __marker)

                # <Value u'server_info/wsgi' (205:38)> -> __value
                __token = 7643
                try:
                    __zt_tmp = __attrs_140235377022928
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140235435449424('path', u'server_info/wsgi', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                econtext['has_wsgi'] = __value
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373782032
                __attrs_140235373782032 = _static_140235489934800

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li>\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373783248
                __attrs_140235373783248 = _static_140235489934800
                __stream_140235373781456 = []
                __append_140235373781456 = __stream_140235373781456.append
                __append_140235373781456(u'WSGI:')
                __msgid_140235373781456 = __re_whitespace(''.join(__stream_140235373781456)).strip()
                if __msgid_140235373781456:
                    __append(translate(__msgid_140235373781456, mapping=None, default=__msgid_140235373781456, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235373781904
                __attrs_140235373781904 = _static_140235489934800

                # <Value u'has_wsgi' (208:51)> -> __condition
                __token = 7787
                try:
                    __zt_tmp = __attrs_140235373781904
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'has_wsgi', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140235373784592 = []
                    __append_140235373784592 = __stream_140235373784592.append
                    __append_140235373784592(u'On')
                    __msgid_140235373784592 = __re_whitespace(''.join(__stream_140235373784592)).strip()
                    if __msgid_140235373784592:
                        __append(translate(__msgid_140235373784592, mapping=None, default=__msgid_140235373784592, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321994896
                __attrs_140235321994896 = _static_140235489934800

                # <Value u'not:has_wsgi' (209:51)> -> __condition
                __token = 7858
                try:
                    __zt_tmp = __attrs_140235321994896
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('not', u'has_wsgi', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140235321993936 = []
                    __append_140235321993936 = __stream_140235321993936.append
                    __append_140235321993936(u'Off')
                    __msgid_140235321993936 = __re_whitespace(''.join(__stream_140235321993936)).strip()
                    if __msgid_140235321993936:
                        __append(translate(__msgid_140235321993936, mapping=None, default=__msgid_140235321993936, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>')
                __append(u'\n          </li>\n          ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321992912
                __attrs_140235321992912 = _static_140235489934800

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li>\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321992080
                __attrs_140235321992080 = _static_140235489934800
                __stream_140235321994640 = []
                __append_140235321994640 = __stream_140235321994640.append
                __append_140235321994640(u'Server:')
                __msgid_140235321994640 = __re_whitespace(''.join(__stream_140235321994640)).strip()
                if __msgid_140235321994640:
                    __append(translate(__msgid_140235321994640, mapping=None, default=__msgid_140235321994640, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321993424
                __attrs_140235321993424 = _static_140235489934800

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Interpolation value=<Substitution u'${server_info/server_name}' (213:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8b148d6f10> -> __content_140235542500720
                __token = 7991
                __token = 7993
                try:
                    __zt_tmp = __attrs_140235321993424
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140235542500720 = _static_140235435449424('path', u'server_info/server_name', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __content_140235542500720 = __quote(__content_140235542500720, '\x00', '&#0;', None, None)
                __content_140235542500720 = __content_140235542500720
                if (__content_140235542500720 is None):
                    pass
                else:
                    if (__content_140235542500720 is None):
                        __content_140235542500720 = None
                    else:
                        __tt = type(__content_140235542500720)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __content_140235542500720 = unicode(__content_140235542500720)
                        else:
                            if (__tt is str):
                                __content_140235542500720 = decode(__content_140235542500720)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __content_140235542500720 = __content_140235542500720.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140235542500720)
                                        __content_140235542500720 = (unicode(__content_140235542500720) if (__content_140235542500720 is __converted) else __converted)
                                    else:
                                        __content_140235542500720 = __content_140235542500720()
                if (__content_140235542500720 is not None):
                    __append(__content_140235542500720)
                __append(u'</span>\n            ')

                # <Static value=<_ast.Dict object at 0x7f8b1e8ffdd0> name=None at 7f8b1e8ffcd0> -> __attrs_140235321993808
                __attrs_140235321993808 = _static_140235489934800

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Interpolation value=<Substitution u'${server_info/version}' (214:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f8b148d6350> -> __content_140235542500720
                __token = 8043
                __token = 8045
                try:
                    __zt_tmp = __attrs_140235321993808
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140235542500720 = _static_140235435449424('path', u'server_info/version', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                __content_140235542500720 = __quote(__content_140235542500720, '\x00', '&#0;', None, None)
                __content_140235542500720 = __content_140235542500720
                if (__content_140235542500720 is None):
                    pass
                else:
                    if (__content_140235542500720 is None):
                        __content_140235542500720 = None
                    else:
                        __tt = type(__content_140235542500720)
                        if ((__tt is int) or (__tt is float) or (__tt is long)):
                            __content_140235542500720 = unicode(__content_140235542500720)
                        else:
                            if (__tt is str):
                                __content_140235542500720 = decode(__content_140235542500720)
                            else:
                                if (__tt is not unicode):
                                    try:
                                        __content_140235542500720 = __content_140235542500720.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140235542500720)
                                        __content_140235542500720 = (unicode(__content_140235542500720) if (__content_140235542500720 is __converted) else __converted)
                                    else:
                                        __content_140235542500720 = __content_140235542500720()
                if (__content_140235542500720 is not None):
                    __append(__content_140235542500720)
                __append(u'</span>\n          </li>\n      ')
                if (__backup_has_wsgi_140235423489040 is __marker):
                    del econtext['has_wsgi']
                else:
                    econtext['has_wsgi'] = __backup_has_wsgi_140235423489040
                if (__backup_server_info_140235423486160 is __marker):
                    del econtext['server_info']
                else:
                    econtext['server_info'] = __backup_server_info_140235423486160
                __append(u'\n    </ul>\n\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b17d51590> name=None at 7f8b17d51810> -> __attrs_140235321994832
                __attrs_140235321994832 = _static_140235377022352

                # <Value u'not:view/is_dev_mode' (220:22)> -> __condition
                __token = 8143
                try:
                    __zt_tmp = __attrs_140235321994832
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('not', u'view/is_dev_mode', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="discreet">')
                    __stream_140235377024656 = []
                    __append_140235377024656 = __stream_140235377024656.append
                    __append_140235377024656(u'\n      You are running in "production mode". This is the preferred mode of\n      operation for a live Plone site, but means that some\n      configuration changes will not take effect until your server is\n      restarted or a product refreshed. If this is a development instance,\n      and you want to enable debug mode, stop the server, set \'debug-mode=on\'\n      in your buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_140235377024656 = __re_whitespace(''.join(__stream_140235377024656)).strip()
                    if u'description_production_mode':
                        __append(translate(u'description_production_mode', mapping=None, default=__msgid_140235377024656, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7f8b1aab7f90> name=None at 7f8b1aab7c90> -> __attrs_140235424627600
                __attrs_140235424627600 = _static_140235424628624

                # <Value u'view/is_dev_mode' (232:22)> -> __condition
                __token = 8721
                try:
                    __zt_tmp = __attrs_140235424627600
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140235435449424('path', u'view/is_dev_mode', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="discreet">')
                    __stream_140235424625552 = []
                    __append_140235424625552 = __stream_140235424625552.append
                    __append_140235424625552(u'\n      You are running in "debug mode". This mode is intended for sites that\n      are under development. This allows many configuration changes to be\n      immediately visible, but will make your site run more slowly. To turn\n      off debug mode, stop the server, set \'debug-mode=off\' in your\n      buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_140235424625552 = __re_whitespace(''.join(__stream_140235424625552)).strip()
                    if u'description_debug_mode':
                        __append(translate(u'description_debug_mode', mapping=None, default=__msgid_140235424625552, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>')
                __append(u'\n\n</div>')
            _slots = econtext[u'__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value u'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140235374096336
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140235435449424('path', u'here/prefs_main_template/macros/master', econtext=econtext)(_static_140235435450064(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140235437953584 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140235437953584
            __i18n_domain = __previous_i18n_domain_140235321985488
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
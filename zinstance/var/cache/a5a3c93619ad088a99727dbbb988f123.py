# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/controlpanel/browser/overview.pt'

__tokens = {421: (u"python:request.set('disable_plone.leftcolumn',1)", 12, 47), 517: (u" python:request.set('disable_plone.rightcolumn',1", 13, 46), 932: (u'view/python2_warning', 26, 24), 1336: (u'view/python_warning', 38, 24), 1679: (u'view/plone_maintenance_warning', 49, 24), 2056: (u'view/plone_security_warning', 60, 24), 2424: (u'view/version_warning', 71, 24), 3038: (u'view/upgrade_warning', 89, 24), 3335: (u'string:${context/portal_url}/@@plone-upgrade', 97, 36), 3731: (u'view/mailhost_warning', 109, 24), 4322: (u'string:${portal_url}/@@mail-controlpanel', 120, 40), 4567: (u'view/timezone_warning', 129, 24), 5120: (u'string:${portal_url}/@@dateandtime-controlpanel', 141, 40), 5390: (u'not:view/pil', 150, 24), 5687: (u'view/categories', 159, 39), 5741: (u"python:view.sublists(category.get('id'))", 160, 36), 5871: (u'sublist', 161, 87), 5934: (u'category/title', 162, 53), 6052: (u'sublist', 165, 53), 6133: (u'sublist', 168, 31), 6189: (u'sublist', 169, 46), 6275: (u'action/visible', 170, 76), 6429: (u'action/icon', 173, 46), 6492: (u'action/url', 174, 50), 6562: (u"python:'icon-controlpanel-' + action['id'].replace('.', '_')", 175, 57), 6686: (u'action/title', 176, 54), 7074: (u'not:sublist', 188, 32), 7447: (u'view/version_overview', 201, 41), 7496: (u'version', 202, 25), 7587: (u'view/server_info', 204, 42), 7643: (u' server_info/wsg', 205, 38), 7787: (u'has_wsgi', 208, 51), 7858: (u'not:has_wsgi', 209, 51), 7991: (u'${server_info/server_name}', 213, 18), 7993: (u'server_info/server_name', 213, 20), 8043: (u'${server_info/version}', 214, 18), 8045: (u'server_info/version', 214, 20), 8143: (u'not:view/is_dev_mode', 220, 22), 8721: (u'view/is_dev_mode', 232, 22), 261: (u'here/prefs_main_template/macros/master', 6, 23), 261: (u'here/prefs_main_template/macros/master', 6, 23)}

from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from sys import exc_info as _exc_info
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr

_static_140386069152656 = {u'class': u'discreet', }
_static_140386077036176 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140386077001104 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140386247937936 = {}
_static_140386077044560 = {u'class': u"python:'icon-controlpanel-' + action['id'].replace('.', '_')", }
_static_140386077038864 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140386077092432 = {u'class': u'documentDescription', }
_static_140386069155792 = {u'class': u'col-xs-4 col-sm-3 col-md-2', }
_static_140386069172048 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140386070040656 = {u'href': u'', }
_static_140386077089936 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140386077014352 = u'master'
_static_140386069309648 = {u'class': u'portletContent', }
_static_140386077061776 = {u'class': u'discreet', }
_static_140386186297040 = __C2ZContextWrapper
_static_140386077067728 = {u'class': u'portletHeader', }
_static_140386077090320 = {u'class': u'documentFirstHeading', }
_static_140386070127888 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140386077079760 = {u'href': u'https://plone.org/download/release-schedule', }
_static_140386070747920 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140386077003536 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140386077066896 = {u'class': u'portlet portletNavigationTree portletSiteSetup', }
_static_140386069152976 = {u'class': u'inner-configlet', }
_static_140386077042960 = {u'href': u'', }
_static_140386069309968 = {u'class': u'row configlets', }
_static_140386077080144 = {u'role': u'status', u'class': u'portalMessage warning', }
_static_140386186296528 = __compile_zt_expr
_static_140386077050704 = {u'class': u'discreet', }
_static_140386077033872 = {u'href': u'#', u'title': u'Go to the upgrade page', }
_static_140386077067024 = {u'class': u'visualClear', }
_static_140386070746000 = {u'href': u'', }

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

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077012240
            __attrs_140386077012240 = _static_140386247937936
            __previous_i18n_domain_140386077012688 = __i18n_domain
            __i18n_domain = u'plone'
            __backup_macroname_140386115401280 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7fae2e407950> name=None at 7fae2e407690> -> __value
            __value = _static_140386077014352
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077015056
                __attrs_140386077015056 = _static_140386247937936
                __backup_disable_column_one_140386070661136 = get('disable_column_one', __marker)

                # <Value u"python:request.set('disable_plone.leftcolumn',1)" (12:47)> -> __value
                __token = 421
                try:
                    __zt_tmp = __attrs_140386077015056
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('python', u"request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_140386069901520 = get('disable_column_two', __marker)

                # <Value u"python:request.set('disable_plone.rightcolumn',1)" (13:46)> -> __value
                __token = 517
                try:
                    __zt_tmp = __attrs_140386077015056
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('python', u"request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_140386069901520 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_140386069901520
                if (__backup_disable_column_one_140386070661136 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_140386070661136
            _slots = econtext[u'__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getitem = econtext.__getitem__
                get = econtext.get

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077012496
                __attrs_140386077012496 = _static_140386247937936

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e41a210> name=None at 7fae2e4079d0> -> __attrs_140386077092752
                __attrs_140386077092752 = _static_140386077090320

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h1 class="documentFirstHeading">')
                __stream_140386077014928 = []
                __append_140386077014928 = __stream_140386077014928.append
                __append_140386077014928(u'Site Setup')
                __msgid_140386077014928 = __re_whitespace(''.join(__stream_140386077014928)).strip()
                if __msgid_140386077014928:
                    __append(translate(__msgid_140386077014928, mapping=None, default=__msgid_140386077014928, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</h1>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e41aa50> name=None at 7fae2e41af50> -> __attrs_140386077091856
                __attrs_140386077091856 = _static_140386077092432

                # <p ... (0:0)
                # --------------------------------------------------------
                __append(u'<p class="documentDescription">')
                __stream_140386077093648 = []
                __append_140386077093648 = __stream_140386077093648.append
                __append_140386077093648(u'\n        Configuration area for Plone and add-on Products.\n    ')
                __msgid_140386077093648 = __re_whitespace(''.join(__stream_140386077093648)).strip()
                if u'description_control_panel':
                    __append(translate(u'description_control_panel', mapping=None, default=__msgid_140386077093648, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</p>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e41a090> name=None at 7fae2e41a610> -> __attrs_140386077091472
                __attrs_140386077091472 = _static_140386077089936

                # <Value u'view/python2_warning' (26:24)> -> __condition
                __token = 932
                try:
                    __zt_tmp = __attrs_140386077091472
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/python2_warning', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077002704
                    __attrs_140386077002704 = _static_140386247937936

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140386077001296 = []
                    __append_140386077001296 = __stream_140386077001296.append
                    __append_140386077001296(u'\n            Warning\n        ')
                    __msgid_140386077001296 = __re_whitespace(''.join(__stream_140386077001296)).strip()
                    if __msgid_140386077001296:
                        __append(translate(__msgid_140386077001296, mapping=None, default=__msgid_140386077001296, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077000656
                    __attrs_140386077000656 = _static_140386247937936
                    __stream_140386076999952 = []
                    __append_140386076999952 = __stream_140386076999952.append
                    __append_140386076999952(u'\n            You are using Python 2.\n            This should only be used temporarily while preparing to migrate to Python 3.\n        ')
                    __msgid_140386076999952 = __re_whitespace(''.join(__stream_140386076999952)).strip()
                    if u'text_python2_warning':
                        __append(translate(u'text_python2_warning', mapping=None, default=__msgid_140386076999952, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e404590> name=None at 7fae2e404710> -> __attrs_140386077003664
                __attrs_140386077003664 = _static_140386077001104

                # <Value u'view/python_warning' (38:24)> -> __condition
                __token = 1336
                try:
                    __zt_tmp = __attrs_140386077003664
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/python_warning', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077003280
                    __attrs_140386077003280 = _static_140386247937936

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140386077000208 = []
                    __append_140386077000208 = __stream_140386077000208.append
                    __append_140386077000208(u'\n            Warning\n        ')
                    __msgid_140386077000208 = __re_whitespace(''.join(__stream_140386077000208)).strip()
                    if __msgid_140386077000208:
                        __append(translate(__msgid_140386077000208, mapping=None, default=__msgid_140386077000208, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077001936
                    __attrs_140386077001936 = _static_140386247937936
                    __stream_140386077001808 = []
                    __append_140386077001808 = __stream_140386077001808.append
                    __append_140386077001808(u'\n            You are using a Python version that is not supported.\n        ')
                    __msgid_140386077001808 = __re_whitespace(''.join(__stream_140386077001808)).strip()
                    if u'text_python_warning':
                        __append(translate(u'text_python_warning', mapping=None, default=__msgid_140386077001808, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e404f10> name=None at 7fae2e4049d0> -> __attrs_140386077039248
                __attrs_140386077039248 = _static_140386077003536

                # <Value u'view/plone_maintenance_warning' (49:24)> -> __condition
                __token = 1679
                try:
                    __zt_tmp = __attrs_140386077039248
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/plone_maintenance_warning', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077040400
                    __attrs_140386077040400 = _static_140386247937936

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140386077039504 = []
                    __append_140386077039504 = __stream_140386077039504.append
                    __append_140386077039504(u'\n            Warning\n        ')
                    __msgid_140386077039504 = __re_whitespace(''.join(__stream_140386077039504)).strip()
                    if __msgid_140386077039504:
                        __append(translate(__msgid_140386077039504, mapping=None, default=__msgid_140386077039504, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077040592
                    __attrs_140386077040592 = _static_140386247937936
                    __stream_140386077040080 = []
                    __append_140386077040080 = __stream_140386077040080.append
                    __append_140386077040080(u'\n            You are using a Plone version that is out of maintenance support.\n        ')
                    __msgid_140386077040080 = __re_whitespace(''.join(__stream_140386077040080)).strip()
                    if u'text_plone_maintenance_warning':
                        __append(translate(u'text_plone_maintenance_warning', mapping=None, default=__msgid_140386077040080, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e40d910> name=None at 7fae2e40da10> -> __attrs_140386077037712
                __attrs_140386077037712 = _static_140386077038864

                # <Value u'view/plone_security_warning' (60:24)> -> __condition
                __token = 2056
                try:
                    __zt_tmp = __attrs_140386077037712
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/plone_security_warning', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069170704
                    __attrs_140386069170704 = _static_140386247937936

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140386069171536 = []
                    __append_140386069171536 = __stream_140386069171536.append
                    __append_140386069171536(u'\n            Warning\n        ')
                    __msgid_140386069171536 = __re_whitespace(''.join(__stream_140386069171536)).strip()
                    if __msgid_140386069171536:
                        __append(translate(__msgid_140386069171536, mapping=None, default=__msgid_140386069171536, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069170768
                    __attrs_140386069170768 = _static_140386247937936
                    __stream_140386069168784 = []
                    __append_140386069168784 = __stream_140386069168784.append
                    __append_140386069168784(u'\n            You are using a Plone version that is out of security support.\n        ')
                    __msgid_140386069168784 = __re_whitespace(''.join(__stream_140386069168784)).strip()
                    if u'text_plone_security_warning':
                        __append(translate(u'text_plone_security_warning', mapping=None, default=__msgid_140386069168784, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2dc8cf50> name=None at 7fae2dc8ce10> -> __attrs_140386069171344
                __attrs_140386069171344 = _static_140386069172048

                # <Value u'view/version_warning' (71:24)> -> __condition
                __token = 2424
                try:
                    __zt_tmp = __attrs_140386069171344
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/version_warning', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077080784
                    __attrs_140386077080784 = _static_140386247937936

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140386077077648 = []
                    __append_140386077077648 = __stream_140386077077648.append
                    __append_140386077077648(u'\n            Warning\n        ')
                    __msgid_140386077077648 = __re_whitespace(''.join(__stream_140386077077648)).strip()
                    if __msgid_140386077077648:
                        __append(translate(__msgid_140386077077648, mapping=None, default=__msgid_140386077077648, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077079504
                    __attrs_140386077079504 = _static_140386247937936
                    __stream_140386079966704_plone_release_schedule_link = ''
                    __stream_140386077079440 = []
                    __append_140386077079440 = __stream_140386077079440.append
                    __append_140386077079440(u'\n            Go to the\n            ')
                    __stream_140386079966704_plone_release_schedule_link = []
                    __append_140386079966704_plone_release_schedule_link = __stream_140386079966704_plone_release_schedule_link.append

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077081296
                    __attrs_140386077081296 = _static_140386247937936
                    __append_140386079966704_plone_release_schedule_link(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae2e4178d0> name=None at 7fae2e417ad0> -> __attrs_140386077077968
                    __attrs_140386077077968 = _static_140386077079760

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140386079966704_plone_release_schedule_link(u'<a href="https://plone.org/download/release-schedule" >')
                    __stream_140386077078992 = []
                    __append_140386077078992 = __stream_140386077078992.append
                    __append_140386077078992(u'Plone release schedule')
                    __msgid_140386077078992 = __re_whitespace(''.join(__stream_140386077078992)).strip()
                    if u'text_plone_release_schedule_link':
                        __append_140386079966704_plone_release_schedule_link(translate(u'text_plone_release_schedule_link', mapping=None, default=__msgid_140386077078992, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140386079966704_plone_release_schedule_link(u'</a>\n            ')
                    __append_140386077079440(u'${plone_release_schedule_link}')
                    __stream_140386079966704_plone_release_schedule_link = ''.join(__stream_140386079966704_plone_release_schedule_link)
                    __append_140386077079440(u'\n            for more information.\n        ')
                    __msgid_140386077079440 = __re_whitespace(''.join(__stream_140386077079440)).strip()
                    if u'text_plone_release_schedule':
                        __append(translate(u'text_plone_release_schedule', mapping={u'plone_release_schedule_link': __stream_140386079966704_plone_release_schedule_link, }, default=__msgid_140386077079440, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e417a50> name=None at 7fae2e417b50> -> __attrs_140386077078160
                __attrs_140386077078160 = _static_140386077080144

                # <Value u'view/upgrade_warning' (89:24)> -> __condition
                __token = 3038
                try:
                    __zt_tmp = __attrs_140386077078160
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/upgrade_warning', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077032976
                    __attrs_140386077032976 = _static_140386247937936

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140386077033360 = []
                    __append_140386077033360 = __stream_140386077033360.append
                    __append_140386077033360(u'\n            Warning\n        ')
                    __msgid_140386077033360 = __re_whitespace(''.join(__stream_140386077033360)).strip()
                    if __msgid_140386077033360:
                        __append(translate(__msgid_140386077033360, mapping=None, default=__msgid_140386077033360, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077033040
                    __attrs_140386077033040 = _static_140386247937936
                    __stream_140386079966704_link_continue_with_the_upgrade = ''
                    __stream_140386077033296 = []
                    __append_140386077033296 = __stream_140386077033296.append
                    __append_140386077033296(u'\n            The site configuration is outdated and needs to be\n            upgraded. Please\n            ')
                    __stream_140386079966704_link_continue_with_the_upgrade = []
                    __append_140386079966704_link_continue_with_the_upgrade = __stream_140386079966704_link_continue_with_the_upgrade.append

                    # <Static value=<_ast.Dict object at 0x7fae2e40c590> name=None at 7fae2e40cb10> -> __attrs_140386077033168
                    __attrs_140386077033168 = _static_140386077033872

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140386079966704_link_continue_with_the_upgrade(u'<a')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386069151376
                    __default_140386069151376 = _DEFAULT_MARKER

                    # <Substitution u'string:${context/portal_url}/@@plone-upgrade' (97:36)> -> __attr_href
                    __token = 3335
                    try:
                        __zt_tmp = __attrs_140386077033168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('string', u'${context/portal_url}/@@plone-upgrade', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140386079966704_link_continue_with_the_upgrade((u' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077035856
                    __default_140386077035856 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<_ast.Str object at 0x7fae2e40c750> at 7fae2e40c150> -> __attr_title
                    __attr_title = u'Go to the upgrade page'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                    if (__attr_title is not None):
                        __append_140386079966704_link_continue_with_the_upgrade((u' title="%s"' % __attr_title))
                    __append_140386079966704_link_continue_with_the_upgrade(u'>')
                    __stream_140386077035408 = []
                    __append_140386077035408 = __stream_140386077035408.append
                    __append_140386077035408(u'\n              continue with the upgrade\n            ')
                    __msgid_140386077035408 = __re_whitespace(''.join(__stream_140386077035408)).strip()
                    if __msgid_140386077035408:
                        __append_140386079966704_link_continue_with_the_upgrade(translate(__msgid_140386077035408, mapping=None, default=__msgid_140386077035408, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140386079966704_link_continue_with_the_upgrade(u'</a>')
                    __append_140386077033296(u'${link_continue_with_the_upgrade}')
                    __stream_140386079966704_link_continue_with_the_upgrade = ''.join(__stream_140386079966704_link_continue_with_the_upgrade)
                    __append_140386077033296(u'.\n        ')
                    __msgid_140386077033296 = __re_whitespace(''.join(__stream_140386077033296)).strip()
                    if __msgid_140386077033296:
                        __append(translate(__msgid_140386077033296, mapping={u'link_continue_with_the_upgrade': __stream_140386079966704_link_continue_with_the_upgrade, }, default=__msgid_140386077033296, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e40ce90> name=None at 7fae2e40c090> -> __attrs_140386070129296
                __attrs_140386070129296 = _static_140386077036176

                # <Value u'view/mailhost_warning' (109:24)> -> __condition
                __token = 3731
                try:
                    __zt_tmp = __attrs_140386070129296
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/mailhost_warning', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070129488
                    __attrs_140386070129488 = _static_140386247937936

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140386070126800 = []
                    __append_140386070126800 = __stream_140386070126800.append
                    __append_140386070126800(u'\n            Warning\n        ')
                    __msgid_140386070126800 = __re_whitespace(''.join(__stream_140386070126800)).strip()
                    if __msgid_140386070126800:
                        __append(translate(__msgid_140386070126800, mapping=None, default=__msgid_140386070126800, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070128720
                    __attrs_140386070128720 = _static_140386247937936
                    __stream_140386079966704_label_mail_control_panel_link = ''
                    __stream_140386070130512 = []
                    __append_140386070130512 = __stream_140386070130512.append
                    __append_140386070130512(u"\n            You have not configured a mail host or a site 'From'\n            address, various features including contact forms, email\n            notification and password reset will not work. Go to the\n            ")
                    __stream_140386079966704_label_mail_control_panel_link = []
                    __append_140386079966704_label_mail_control_panel_link = __stream_140386079966704_label_mail_control_panel_link.append

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070128848
                    __attrs_140386070128848 = _static_140386247937936
                    __append_140386079966704_label_mail_control_panel_link(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae2de0d390> name=None at 7fae2de0dc50> -> __attrs_140386070748624
                    __attrs_140386070748624 = _static_140386070746000

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140386079966704_label_mail_control_panel_link(u'<a')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386070749136
                    __default_140386070749136 = _DEFAULT_MARKER

                    # <Substitution u'string:${portal_url}/@@mail-controlpanel' (120:40)> -> __attr_href
                    __token = 4322
                    try:
                        __zt_tmp = __attrs_140386070748624
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('string', u'${portal_url}/@@mail-controlpanel', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140386079966704_label_mail_control_panel_link((u' href="%s"' % __attr_href))
                    __append_140386079966704_label_mail_control_panel_link(u' >')
                    __stream_140386070745616 = []
                    __append_140386070745616 = __stream_140386070745616.append
                    __append_140386070745616(u'Mail control panel')
                    __msgid_140386070745616 = __re_whitespace(''.join(__stream_140386070745616)).strip()
                    if u'text_no_mailhost_configured_control_panel_link':
                        __append_140386079966704_label_mail_control_panel_link(translate(u'text_no_mailhost_configured_control_panel_link', mapping=None, default=__msgid_140386070745616, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140386079966704_label_mail_control_panel_link(u'</a>\n            ')
                    __append_140386070130512(u'${label_mail_control_panel_link}')
                    __stream_140386079966704_label_mail_control_panel_link = ''.join(__stream_140386079966704_label_mail_control_panel_link)
                    __append_140386070130512(u'\n            to fix this.\n        ')
                    __msgid_140386070130512 = __re_whitespace(''.join(__stream_140386070130512)).strip()
                    if u'text_no_mailhost_configured':
                        __append(translate(u'text_no_mailhost_configured', mapping={u'label_mail_control_panel_link': __stream_140386079966704_label_mail_control_panel_link, }, default=__msgid_140386070130512, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2dd76510> name=None at 7fae2dd76d50> -> __attrs_140386070746320
                __attrs_140386070746320 = _static_140386070127888

                # <Value u'view/timezone_warning' (129:24)> -> __condition
                __token = 4567
                try:
                    __zt_tmp = __attrs_140386070746320
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/timezone_warning', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070746256
                    __attrs_140386070746256 = _static_140386247937936

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140386070747344 = []
                    __append_140386070747344 = __stream_140386070747344.append
                    __append_140386070747344(u'\n            Warning\n        ')
                    __msgid_140386070747344 = __re_whitespace(''.join(__stream_140386070747344)).strip()
                    if __msgid_140386070747344:
                        __append(translate(__msgid_140386070747344, mapping=None, default=__msgid_140386070747344, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070746640
                    __attrs_140386070746640 = _static_140386247937936
                    __stream_140386079966704_label_mail_event_settings_link = ''
                    __stream_140386070747600 = []
                    __append_140386070747600 = __stream_140386070747600.append
                    __append_140386070747600(u'\n\n            You have not set the portal timezone. Date/Time handling will not\n            work properly for timezone aware date/time values.\n            Go to the\n            ')
                    __stream_140386079966704_label_mail_event_settings_link = []
                    __append_140386079966704_label_mail_event_settings_link = __stream_140386079966704_label_mail_event_settings_link.append

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069942800
                    __attrs_140386069942800 = _static_140386247937936
                    __append_140386079966704_label_mail_event_settings_link(u'\n                ')

                    # <Static value=<_ast.Dict object at 0x7fae2dd61050> name=None at 7fae2de03310> -> __attrs_140386069974736
                    __attrs_140386069974736 = _static_140386070040656

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140386079966704_label_mail_event_settings_link(u'<a')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077025680
                    __default_140386077025680 = _DEFAULT_MARKER

                    # <Substitution u'string:${portal_url}/@@dateandtime-controlpanel' (141:40)> -> __attr_href
                    __token = 5120
                    try:
                        __zt_tmp = __attrs_140386069974736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140386186296528('string', u'${portal_url}/@@dateandtime-controlpanel', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140386079966704_label_mail_event_settings_link((u' href="%s"' % __attr_href))
                    __append_140386079966704_label_mail_event_settings_link(u' >')
                    __stream_140386069942864 = []
                    __append_140386069942864 = __stream_140386069942864.append
                    __append_140386069942864(u'Date and Time Settings control panel')
                    __msgid_140386069942864 = __re_whitespace(''.join(__stream_140386069942864)).strip()
                    if u'text_no_timezone_configured_control_panel_link':
                        __append_140386079966704_label_mail_event_settings_link(translate(u'text_no_timezone_configured_control_panel_link', mapping=None, default=__msgid_140386069942864, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append_140386079966704_label_mail_event_settings_link(u'</a>\n            ')
                    __append_140386070747600(u'${label_mail_event_settings_link}')
                    __stream_140386079966704_label_mail_event_settings_link = ''.join(__stream_140386079966704_label_mail_event_settings_link)
                    __append_140386070747600(u'\n            to fix this.\n        ')
                    __msgid_140386070747600 = __re_whitespace(''.join(__stream_140386070747600)).strip()
                    if u'text_no_timezone_configured':
                        __append(translate(u'text_no_timezone_configured', mapping={u'label_mail_event_settings_link': __stream_140386079966704_label_mail_event_settings_link, }, default=__msgid_140386070747600, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2de0db10> name=None at 7fae2de0d990> -> __attrs_140386069944528
                __attrs_140386069944528 = _static_140386070747920

                # <Value u'not:view/pil' (150:24)> -> __condition
                __token = 5390
                try:
                    __zt_tmp = __attrs_140386069944528
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('not', u'view/pil', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<div class="portalMessage warning" role="status">\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069944144
                    __attrs_140386069944144 = _static_140386247937936

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<strong>')
                    __stream_140386069943760 = []
                    __append_140386069943760 = __stream_140386069943760.append
                    __append_140386069943760(u'\n            Warning\n        ')
                    __msgid_140386069943760 = __re_whitespace(''.join(__stream_140386069943760)).strip()
                    if __msgid_140386069943760:
                        __append(translate(__msgid_140386069943760, mapping=None, default=__msgid_140386069943760, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</strong>\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069942352
                    __attrs_140386069942352 = _static_140386247937936
                    __stream_140386069945360 = []
                    __append_140386069945360 = __stream_140386069945360.append
                    __append_140386069945360(u'\n            PIL is not installed properly, image scaling will not work.\n        ')
                    __msgid_140386069945360 = __re_whitespace(''.join(__stream_140386069945360)).strip()
                    if u'text_no_pil_installed':
                        __append(translate(u'text_no_pil_installed', mapping=None, default=__msgid_140386069945360, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'\n    </div>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069945168
                __attrs_140386069945168 = _static_140386247937936
                __backup_category_140386077014800 = get('category', __marker)

                # <Value u'view/categories' (159:39)> -> __iterator
                __token = 5687
                try:
                    __zt_tmp = __attrs_140386069945168
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'view/categories', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386077065744, ) = getitem('repeat')(u'category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append(u'\n      ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077067920
                    __attrs_140386077067920 = _static_140386247937936
                    __backup_sublist_140386077092688 = get('sublist', __marker)

                    # <Value u"python:view.sublists(category.get('id'))" (160:36)> -> __value
                    __token = 5741
                    try:
                        __zt_tmp = __attrs_140386077067920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140386186296528('python', u"view.sublists(category.get('id'))", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    econtext['sublist'] = __value
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae2e414690> name=None at 7fae2e414450> -> __attrs_140386077067280
                    __attrs_140386077067280 = _static_140386077066896

                    # <Value u'sublist' (161:87)> -> __condition
                    __token = 5871
                    try:
                        __zt_tmp = __attrs_140386077067280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140386186296528('path', u'sublist', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                    if __condition:

                        # <section ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<section class="portlet portletNavigationTree portletSiteSetup">\n          ')

                        # <Static value=<_ast.Dict object at 0x7fae2e4149d0> name=None at 7fae2e414110> -> __attrs_140386069307472
                        __attrs_140386069307472 = _static_140386077067728

                        # <header ... (0:0)
                        # --------------------------------------------------------
                        __append(u'<header class="portletHeader">')

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077066384
                        __default_140386077066384 = _DEFAULT_MARKER

                        # <Value u'category/title' (162:53)> -> __cache_140386077066192
                        __token = 5934
                        try:
                            __zt_tmp = __attrs_140386069307472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140386077066192 = _static_140386186296528('path', u'category/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                        # <BinOp left=<Value u'category/title' (162:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2dc93910> -> __condition
                        __expression = __cache_140386077066192

                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append(u'Category')
                        else:
                            __content = __cache_140386077066192
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append(u'</header>\n\n          ')

                        # <Static value=<_ast.Dict object at 0x7fae2dcae8d0> name=None at 7fae2dcae610> -> __attrs_140386069310800
                        __attrs_140386069310800 = _static_140386069309648

                        # <Value u'sublist' (165:53)> -> __condition
                        __token = 6052
                        try:
                            __zt_tmp = __attrs_140386069310800
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('path', u'sublist', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <nav ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<nav class="portletContent">\n\n            ')

                            # <Static value=<_ast.Dict object at 0x7fae2dcaea10> name=None at 7fae2dcaed10> -> __attrs_140386069310928
                            __attrs_140386069310928 = _static_140386069309968

                            # <Value u'sublist' (168:31)> -> __condition
                            __token = 6133
                            try:
                                __zt_tmp = __attrs_140386069310928
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140386186296528('path', u'sublist', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                            if __condition:

                                # <ul ... (0:0)
                                # --------------------------------------------------------
                                __append(u'<ul class="row configlets">\n              ')

                                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386069151824
                                __attrs_140386069151824 = _static_140386247937936
                                __backup_action_140386077082640 = get('action', __marker)

                                # <Value u'sublist' (169:46)> -> __iterator
                                __token = 6189
                                try:
                                    __zt_tmp = __attrs_140386069151824
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_140386186296528('path', u'sublist', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                (__iterator, ____index_140386069155280, ) = getitem('repeat')(u'action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item
                                    __append(u'\n                      ')

                                    # <Static value=<_ast.Dict object at 0x7fae2dc88fd0> name=None at 7fae2dc88f90> -> __attrs_140386069153040
                                    __attrs_140386069153040 = _static_140386069155792

                                    # <Value u'action/visible' (170:76)> -> __condition
                                    __token = 6275
                                    try:
                                        __zt_tmp = __attrs_140386069153040
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_140386186296528('path', u'action/visible', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                    if __condition:

                                        # <li ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<li class="col-xs-4 col-sm-3 col-md-2">\n                        ')

                                        # <Static value=<_ast.Dict object at 0x7fae2dc884d0> name=None at 7fae2dc889d0> -> __attrs_140386077042192
                                        __attrs_140386077042192 = _static_140386069152976

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<div class="inner-configlet">\n                          ')

                                        # <Static value=<_ast.Dict object at 0x7fae2e40e910> name=None at 7fae2e40e750> -> __attrs_140386077043152
                                        __attrs_140386077043152 = _static_140386077042960
                                        __backup_icon_140386069154704 = get('icon', __marker)

                                        # <Value u'action/icon' (173:46)> -> __value
                                        __token = 6429
                                        try:
                                            __zt_tmp = __attrs_140386077043152
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_140386186296528('path', u'action/icon', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                        econtext['icon'] = __value

                                        # <a ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<a')

                                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077043280
                                        __default_140386077043280 = _DEFAULT_MARKER

                                        # <Substitution u'action/url' (174:50)> -> __attr_href
                                        __token = 6492
                                        try:
                                            __zt_tmp = __attrs_140386077043152
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_href = _static_140386186296528('path', u'action/url', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                        __attr_href = __quote(__attr_href, '"', '&quot;', u'', _DEFAULT_MARKER)
                                        if (__attr_href is not None):
                                            __append((u' href="%s"' % __attr_href))
                                        __append(u'>\n                             ')

                                        # <Static value=<_ast.Dict object at 0x7fae2e40ef50> name=None at 7fae2e40e090> -> __attrs_140386077042320
                                        __attrs_140386077042320 = _static_140386077044560

                                        # <span ... (0:0)
                                        # --------------------------------------------------------
                                        __append(u'<span')

                                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077043024
                                        __default_140386077043024 = _DEFAULT_MARKER

                                        # <Substitution u"python:'icon-controlpanel-' + action['id'].replace('.', '_')" (175:57)> -> __attr_class
                                        __token = 6562
                                        try:
                                            __zt_tmp = __attrs_140386077042320
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_class = _static_140386186296528('python', u"'icon-controlpanel-' + action['id'].replace('.', '_')", econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                                        __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                        if (__attr_class is not None):
                                            __append((u' class="%s"' % __attr_class))
                                        __append(u'></span>\n                              ')

                                        # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077070160
                                        __attrs_140386077070160 = _static_140386247937936

                                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077072016
                                        __default_140386077072016 = _DEFAULT_MARKER

                                        # <Value u'action/title' (176:54)> -> __cache_140386077041872
                                        __token = 6686
                                        try:
                                            __zt_tmp = __attrs_140386077070160
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_140386077041872 = _static_140386186296528('path', u'action/title', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                                        # <BinOp left=<Value u'action/title' (176:54)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e4150d0> -> __condition
                                        __expression = __cache_140386077041872

                                        # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            __append(u'\n                                  Title\n                              ')
                                        else:
                                            __content = __cache_140386077041872
                                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language'))
                                            __content = __quote(__content, None, '\xad', None, None)
                                            if (__content is not None):
                                                __append(__content)
                                        __append(u'\n                          </a>')
                                        if (__backup_icon_140386069154704 is __marker):
                                            del econtext['icon']
                                        else:
                                            econtext['icon'] = __backup_icon_140386069154704
                                        __append(u'\n                        </div>\n                      </li>')
                                    __append(u'\n                  ')
                                    ____index_140386069155280 -= 1
                                    if (____index_140386069155280 > 0):
                                        __append('')
                                if (__backup_action_140386077082640 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_140386077082640
                                __append(u'\n                </ul>')
                            __append(u'\n            </nav>')
                        __append(u'\n\n            ')

                        # <Static value=<_ast.Dict object at 0x7fae2dc88390> name=None at 7fae2dc885d0> -> __attrs_140386077044304
                        __attrs_140386077044304 = _static_140386069152656

                        # <Value u'not:sublist' (188:32)> -> __condition
                        __token = 7074
                        try:
                            __zt_tmp = __attrs_140386077044304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140386186296528('not', u'sublist', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append(u'<div class="discreet">')
                            __stream_140386069310608 = []
                            __append_140386069310608 = __stream_140386069310608.append
                            __append_140386069310608(u'\n                No preference panels available.\n            ')
                            __msgid_140386069310608 = __re_whitespace(''.join(__stream_140386069310608)).strip()
                            if u'label_no_prefs_panels_available':
                                __append(translate(u'label_no_prefs_panels_available', mapping=None, default=__msgid_140386069310608, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                            __append(u'</div>')
                        __append(u'\n\n        </section>')
                    __append(u'\n      ')
                    if (__backup_sublist_140386077092688 is __marker):
                        del econtext['sublist']
                    else:
                        econtext['sublist'] = __backup_sublist_140386077092688
                    __append(u'\n    ')
                    ____index_140386077065744 -= 1
                    if (____index_140386077065744 > 0):
                        __append('')
                if (__backup_category_140386077014800 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_140386077014800
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e414710> name=None at 7fae2e4141d0> -> __attrs_140386069307664
                __attrs_140386069307664 = _static_140386077067024

                # <div ... (0:0)
                # --------------------------------------------------------
                __append(u'<div class="visualClear"><!-- --></div>\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077070736
                __attrs_140386077070736 = _static_140386247937936

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append(u'<h2>')
                __stream_140386077072592 = []
                __append_140386077072592 = __stream_140386077072592.append
                __append_140386077072592(u'Version Overview')
                __msgid_140386077072592 = __re_whitespace(''.join(__stream_140386077072592)).strip()
                if u'heading_version_overview':
                    __append(translate(u'heading_version_overview', mapping=None, default=__msgid_140386077072592, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'</h2>\n    ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077071312
                __attrs_140386077071312 = _static_140386247937936

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append(u'<ul>\n      ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077072976
                __attrs_140386077072976 = _static_140386247937936
                __backup_version_140386077013392 = get('version', __marker)

                # <Value u'view/version_overview' (201:41)> -> __iterator
                __token = 7447
                try:
                    __zt_tmp = __attrs_140386077072976
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140386186296528('path', u'view/version_overview', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                (__iterator, ____index_140386077072720, ) = getitem('repeat')(u'version', __iterator)
                econtext['version'] = None
                for __item in __iterator:
                    econtext['version'] = __item
                    __append(u'\n        ')

                    # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077072784
                    __attrs_140386077072784 = _static_140386247937936

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<li>')

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __default_140386077072464
                    __default_140386077072464 = _DEFAULT_MARKER

                    # <Value u'version' (202:25)> -> __cache_140386077070416
                    __token = 7496
                    try:
                        __zt_tmp = __attrs_140386077072784
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140386077070416 = _static_140386186296528('path', u'version', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))

                    # <BinOp left=<Value u'version' (202:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fae38708d50> at 7fae2e415c90> -> __condition
                    __expression = __cache_140386077070416

                    # <Symbol value=<DEFAULT> at 7fae38708d50> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append(u'Version')
                    else:
                        __content = __cache_140386077070416
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(u'</li>\n      ')
                    ____index_140386077072720 -= 1
                    if (____index_140386077072720 > 0):
                        __append('')
                if (__backup_version_140386077013392 is __marker):
                    del econtext['version']
                else:
                    econtext['version'] = __backup_version_140386077013392
                __append(u'\n      ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077069840
                __attrs_140386077069840 = _static_140386247937936
                __backup_server_info_140386077079568 = get('server_info', __marker)

                # <Value u'view/server_info' (204:42)> -> __value
                __token = 7587
                try:
                    __zt_tmp = __attrs_140386077069840
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'view/server_info', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['server_info'] = __value
                __backup_has_wsgi_140386077081168 = get('has_wsgi', __marker)

                # <Value u'server_info/wsgi' (205:38)> -> __value
                __token = 7643
                try:
                    __zt_tmp = __attrs_140386077069840
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140386186296528('path', u'server_info/wsgi', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                econtext['has_wsgi'] = __value
                __append(u'\n          ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077064016
                __attrs_140386077064016 = _static_140386247937936

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li>\n            ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077063824
                __attrs_140386077063824 = _static_140386247937936
                __stream_140386077063376 = []
                __append_140386077063376 = __stream_140386077063376.append
                __append_140386077063376(u'WSGI:')
                __msgid_140386077063376 = __re_whitespace(''.join(__stream_140386077063376)).strip()
                if __msgid_140386077063376:
                    __append(translate(__msgid_140386077063376, mapping=None, default=__msgid_140386077063376, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077063184
                __attrs_140386077063184 = _static_140386247937936

                # <Value u'has_wsgi' (208:51)> -> __condition
                __token = 7787
                try:
                    __zt_tmp = __attrs_140386077063184
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'has_wsgi', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140386077064272 = []
                    __append_140386077064272 = __stream_140386077064272.append
                    __append_140386077064272(u'On')
                    __msgid_140386077064272 = __re_whitespace(''.join(__stream_140386077064272)).strip()
                    if __msgid_140386077064272:
                        __append(translate(__msgid_140386077064272, mapping=None, default=__msgid_140386077064272, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>')
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077062160
                __attrs_140386077062160 = _static_140386247937936

                # <Value u'not:has_wsgi' (209:51)> -> __condition
                __token = 7858
                try:
                    __zt_tmp = __attrs_140386077062160
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('not', u'has_wsgi', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<span>')
                    __stream_140386077062736 = []
                    __append_140386077062736 = __stream_140386077062736.append
                    __append_140386077062736(u'Off')
                    __msgid_140386077062736 = __re_whitespace(''.join(__stream_140386077062736)).strip()
                    if __msgid_140386077062736:
                        __append(translate(__msgid_140386077062736, mapping=None, default=__msgid_140386077062736, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</span>')
                __append(u'\n          </li>\n          ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077062608
                __attrs_140386077062608 = _static_140386247937936

                # <li ... (0:0)
                # --------------------------------------------------------
                __append(u'<li>\n            ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077051024
                __attrs_140386077051024 = _static_140386247937936
                __stream_140386077050448 = []
                __append_140386077050448 = __stream_140386077050448.append
                __append_140386077050448(u'Server:')
                __msgid_140386077050448 = __re_whitespace(''.join(__stream_140386077050448)).strip()
                if __msgid_140386077050448:
                    __append(translate(__msgid_140386077050448, mapping=None, default=__msgid_140386077050448, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                __append(u'\n            ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077050640
                __attrs_140386077050640 = _static_140386247937936

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Interpolation value=<Substitution u'${server_info/server_name}' (213:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fae2e410e50> -> __content_140386296014144
                __token = 7991
                __token = 7993
                try:
                    __zt_tmp = __attrs_140386077050640
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140386296014144 = _static_140386186296528('path', u'server_info/server_name', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
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
                __append(u'</span>\n            ')

                # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386077052432
                __attrs_140386077052432 = _static_140386247937936

                # <span ... (0:0)
                # --------------------------------------------------------
                __append(u'<span>')

                # <Interpolation value=<Substitution u'${server_info/version}' (214:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fae2e410210> -> __content_140386296014144
                __token = 8043
                __token = 8045
                try:
                    __zt_tmp = __attrs_140386077052432
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140386296014144 = _static_140386186296528('path', u'server_info/version', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
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
                __append(u'</span>\n          </li>\n      ')
                if (__backup_has_wsgi_140386077081168 is __marker):
                    del econtext['has_wsgi']
                else:
                    econtext['has_wsgi'] = __backup_has_wsgi_140386077081168
                if (__backup_server_info_140386077079568 is __marker):
                    del econtext['server_info']
                else:
                    econtext['server_info'] = __backup_server_info_140386077079568
                __append(u'\n    </ul>\n\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e413290> name=None at 7fae2e415890> -> __attrs_140386077051216
                __attrs_140386077051216 = _static_140386077061776

                # <Value u'not:view/is_dev_mode' (220:22)> -> __condition
                __token = 8143
                try:
                    __zt_tmp = __attrs_140386077051216
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('not', u'view/is_dev_mode', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="discreet">')
                    __stream_140386077071696 = []
                    __append_140386077071696 = __stream_140386077071696.append
                    __append_140386077071696(u'\n      You are running in "production mode". This is the preferred mode of\n      operation for a live Plone site, but means that some\n      configuration changes will not take effect until your server is\n      restarted or a product refreshed. If this is a development instance,\n      and you want to enable debug mode, stop the server, set \'debug-mode=on\'\n      in your buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_140386077071696 = __re_whitespace(''.join(__stream_140386077071696)).strip()
                    if u'description_production_mode':
                        __append(translate(u'description_production_mode', mapping=None, default=__msgid_140386077071696, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>')
                __append(u'\n\n    ')

                # <Static value=<_ast.Dict object at 0x7fae2e410750> name=None at 7fae2e410810> -> __attrs_140386069357008
                __attrs_140386069357008 = _static_140386077050704

                # <Value u'view/is_dev_mode' (232:22)> -> __condition
                __token = 8721
                try:
                    __zt_tmp = __attrs_140386069357008
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140386186296528('path', u'view/is_dev_mode', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append(u'<p class="discreet">')
                    __stream_140386077050768 = []
                    __append_140386077050768 = __stream_140386077050768.append
                    __append_140386077050768(u'\n      You are running in "debug mode". This mode is intended for sites that\n      are under development. This allows many configuration changes to be\n      immediately visible, but will make your site run more slowly. To turn\n      off debug mode, stop the server, set \'debug-mode=off\' in your\n      buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_140386077050768 = __re_whitespace(''.join(__stream_140386077050768)).strip()
                    if u'description_debug_mode':
                        __append(translate(u'description_debug_mode', mapping=None, default=__msgid_140386077050768, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
                    __append(u'</p>')
                __append(u'\n\n</div>')
            _slots = econtext[u'__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value u'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140386077012240
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140386186296528('path', u'here/prefs_main_template/macros/master', econtext=econtext)(_static_140386186297040(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140386115401280 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140386115401280
            __i18n_domain = __previous_i18n_domain_140386077012688
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
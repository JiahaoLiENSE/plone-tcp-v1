# -*- coding: utf-8 -*-
__filename = '/home/kali/plone5_12_env/buildout-cache/eggs/cp27mu/Products.CMFPlone-5.2.12-py2.7.egg/Products/CMFPlone/browser/templates/plone-frontpage.pt'

__tokens = {}

from sys import exc_info as _exc_info

_static_140386072662096 = {u'href': u'https://docs.plone.org', u'class': u'link-plain', u'target': u'_blank', }
_static_140386071907728 = {u'href': u'https://plone.org/sponsors/be-a-hero', u'target': u'_blank', }
_static_140386072246672 = {u'href': u'https://plone.org/download/add-ons', u'class': u'link-plain', u'target': u'_blank', }
_static_140386072131088 = {u'href': u'@@content-controlpanel', u'target': u'_blank', }
_static_140386071161424 = {u'class': u'discreet', }
_static_140386072180432 = {u'href': u'@@markup-controlpanel', u'target': u'_blank', }
_static_140386072179280 = {u'class': u'discreet', }
_static_140386072640400 = {u'href': u'https://plone.org/support', u'class': u'link-plain', u'target': u'_blank', }
_static_140386071157072 = {u'href': u'@@mail-controlpanel', u'target': u'_blank', }
_static_140386072245200 = {u'href': u'@@theming-controlpanel', u'target': u'_blank', }
_static_140386247937936 = {}
_static_140386070990544 = {u'class': u'discreet', }
_static_140386072172048 = {u'href': u'https://plone.com/success-stories/', u'class': u'link-plain', u'target': u'_blank', }
_static_140386071158544 = {u'class': u'discreet', }
_static_140386070987792 = {u'class': u'hero', }
_static_140386072691856 = {u'href': u'https://plone.com/success-stories/', u'class': u'link-plain', u'target': u'_blank', }
_static_140386072132560 = {u'class': u'discreet', }
_static_140386072029136 = {u'href': u'https://www.python.org', u'class': u'link-plain', u'target': u'_blank', }
_static_140386071159952 = {u'href': u'@@security-controlpanel', u'target': u'_blank', }
_static_140386072327440 = {u'lang': u'en', u'xmlns': u'http://www.w3.org/1999/xhtml', u'xml:lang': u'en', }
_static_140386070990800 = {u'href': u'https://plone.com', u'class': u'context', u'target': u'_blank', }
_static_140386072182224 = {u'href': u'@@overview-controlpanel', u'target': u'_blank', }
_static_140386072664464 = {u'href': u'https://training.plone.org', u'class': u'link-plain', u'target': u'_blank', }
_static_140386072100112 = {u'href': u'https://plone.com/providers/', u'class': u'link-plain', u'target': u'_blank', }
_static_140386072638224 = {u'href': u'https://plone.org/download/add-ons', u'class': u'link-plain', u'target': u'_blank', }
_static_140386071189392 = {u'href': u'https://plone.com/features/', u'class': u'link-plain', u'target': u'_blank', }
_static_140386072049168 = {u'href': u'https://plone.com', u'class': u'link-plain', u'target': u'_blank', }
_static_140386072051408 = {u'href': u'https://plone.org', u'class': u'link-plain', u'target': u'_blank', }
_static_140386072129616 = {u'class': u'discreet', }
_static_140386071155728 = {u'class': u'discreet', }

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

            # <Static value=<_ast.Dict object at 0x7fae2df8f510> name=None at 7fae2df8f690> -> __attrs_140386071401424
            __attrs_140386071401424 = _static_140386072327440
            __previous_i18n_domain_140386071401808 = __i18n_domain
            __i18n_domain = u'plonefrontpage'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append(u'<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071402896
            __attrs_140386071402896 = _static_140386247937936

            # <head ... (0:0)
            # --------------------------------------------------------
            __append(u'<head></head>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072339152
            __attrs_140386072339152 = _static_140386247937936

            # <body ... (0:0)
            # --------------------------------------------------------
            __append(u'<body>')
            __stream_140386072339792 = []
            __append_140386072339792 = __stream_140386072339792.append
            __append_140386072339792(u'\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae2de48410> name=None at 7fae2de48390> -> __attrs_140386070988304
            __attrs_140386070988304 = _static_140386070987792

            # <div ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<div class="hero">\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070989584
            __attrs_140386070989584 = _static_140386247937936

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<h1>Welcome!</h1>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386070990224
            __attrs_140386070990224 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<p>')

            # <Static value=<_ast.Dict object at 0x7fae2de48fd0> name=None at 7fae2de48f90> -> __attrs_140386072253712
            __attrs_140386072253712 = _static_140386070990800

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="context" href="https://plone.com" target="_blank">Learn more about Plone</a></p>\n  </div>\n\n  ')

            # <Static value=<_ast.Dict object at 0x7fae2de48ed0> name=None at 7fae2de48dd0> -> __attrs_140386072254352
            __attrs_140386072254352 = _static_140386070990544

            # <p ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<p class="discreet">\nIf you\'re seeing this instead of the web site you were expecting, the owner of\nthis web site has just installed Plone. Do not contact the Plone Team or the\nPlone support channels about this.\n</p>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072254928
            __attrs_140386072254928 = _static_140386247937936

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<h2>Get started</h2>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072255504
            __attrs_140386072255504 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<p>\nBefore you start exploring your newly created Plone site, please do the following:\n</p>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072256080
            __attrs_140386072256080 = _static_140386247937936

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<ol>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071155088
            __attrs_140386071155088 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>Make sure you are logged in as an admin/manager user.\n        ')

            # <Static value=<_ast.Dict object at 0x7fae2de71410> name=None at 7fae2de713d0> -> __attrs_140386071156304
            __attrs_140386071156304 = _static_140386071155728

            # <span ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<span class="discreet">(You should have a Site Setup entry in the user menu)</span></li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071156624
            __attrs_140386071156624 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>')

            # <Static value=<_ast.Dict object at 0x7fae2de71950> name=None at 7fae2de71990> -> __attrs_140386071158096
            __attrs_140386071158096 = _static_140386071157072

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a href="@@mail-controlpanel" target="_blank">Set up your mail server</a>. ')

            # <Static value=<_ast.Dict object at 0x7fae2de71f10> name=None at 7fae2de71ed0> -> __attrs_140386071159184
            __attrs_140386071159184 = _static_140386071158544

            # <span ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<span class="discreet">(Plone needs a valid SMTP server to verify users and send out password reminders)</span></li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071159504
            __attrs_140386071159504 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>')

            # <Static value=<_ast.Dict object at 0x7fae2de72490> name=None at 7fae2de724d0> -> __attrs_140386071160976
            __attrs_140386071160976 = _static_140386071159952

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a href="@@security-controlpanel" target="_blank">Decide what security level you want on your site</a>. ')

            # <Static value=<_ast.Dict object at 0x7fae2de72a50> name=None at 7fae2de72a10> -> __attrs_140386071162000
            __attrs_140386071162000 = _static_140386071161424

            # <span ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<span class="discreet">(Allow self registration, password policies, etc)</span></li>\n</ol>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071159696
            __attrs_140386071159696 = _static_140386247937936

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<h2>Get comfortable</h2>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071162768
            __attrs_140386071162768 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<p>After that, we suggest you do one or more of the following:</p>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071187984
            __attrs_140386071187984 = _static_140386247937936

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<ul>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071188752
            __attrs_140386071188752 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>Find out ')

            # <Static value=<_ast.Dict object at 0x7fae2de79790> name=None at 7fae2de79750> -> __attrs_140386071190608
            __attrs_140386071190608 = _static_140386071189392

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://plone.com/features/" target="_blank">What\'s new in Plone</a>.</li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071190992
            __attrs_140386071190992 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>Read the ')

            # <Static value=<_ast.Dict object at 0x7fae2dfe1050> name=None at 7fae2de79fd0> -> __attrs_140386072663376
            __attrs_140386072663376 = _static_140386072662096

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://docs.plone.org" target="_blank">documentation</a>.</li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072663824
            __attrs_140386072663824 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>Follow a ')

            # <Static value=<_ast.Dict object at 0x7fae2dfe1990> name=None at 7fae2dfe1950> -> __attrs_140386072665680
            __attrs_140386072665680 = _static_140386072664464

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://training.plone.org" target="_blank">training</a>.</li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072666064
            __attrs_140386072666064 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>Explore the ')

            # <Static value=<_ast.Dict object at 0x7fae2dfdb310> name=None at 7fae2dfdb2d0> -> __attrs_140386072639440
            __attrs_140386072639440 = _static_140386072638224

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://plone.org/download/add-ons" target="_blank">available add-ons</a> for Plone.</li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072639760
            __attrs_140386072639760 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>Read and/or subscribe to the ')

            # <Static value=<_ast.Dict object at 0x7fae2dfdbb90> name=None at 7fae2dfdbb50> -> __attrs_140386072690832
            __attrs_140386072690832 = _static_140386072640400

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://plone.org/support" target="_blank">support channels</a>.</li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072691216
            __attrs_140386072691216 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>Find out ')

            # <Static value=<_ast.Dict object at 0x7fae2dfe8490> name=None at 7fae2dfe8450> -> __attrs_140386072693072
            __attrs_140386072693072 = _static_140386072691856

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://plone.com/success-stories/" target="_blank">how others are using Plone</a>.</li>\n</ul>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072693136
            __attrs_140386072693136 = _static_140386247937936

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<h2>Make it your own</h2>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072693840
            __attrs_140386072693840 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<p>Plone has a lot of different settings that can be used to make it do what you want it to. Some examples:</p>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072694416
            __attrs_140386072694416 = _static_140386247937936

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<ul>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072244688
            __attrs_140386072244688 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>\n    Try out a different theme, either pick from\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2df7b3d0> name=None at 7fae2df7b410> -> __attrs_140386072246224
            __attrs_140386072246224 = _static_140386072245200

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a href="@@theming-controlpanel" target="_blank">the included ones</a>, or one of the\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2df7b990> name=None at 7fae2df7b950> -> __attrs_140386072247888
            __attrs_140386072247888 = _static_140386072246672

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://plone.org/download/add-ons" target="_blank">available themes\n       from plone.org</a>. ')

            # <Static value=<_ast.Dict object at 0x7fae2df5f050> name=None at 7fae2df7bfd0> -> __attrs_140386072130192
            __attrs_140386072130192 = _static_140386072129616

            # <span ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<span class="discreet">(Make sure the theme is\n       compatible with the version of Plone you are currently using)</span>\n    </li>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072130576
            __attrs_140386072130576 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2df5f610> name=None at 7fae2df5f650> -> __attrs_140386072132112
            __attrs_140386072132112 = _static_140386072131088

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a href="@@content-controlpanel" target="_blank">\n    Decide what kind of workflow you want in your site.</a>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2df5fbd0> name=None at 7fae2df5fb90> -> __attrs_140386072133136
            __attrs_140386072133136 = _static_140386072132560

            # <span ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<span class="discreet">(The default is typical for a\n    public web site; if you want to use Plone as a closed intranet or extranet,\n    you can choose a different workflow.)</span>\n    </li>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072133520
            __attrs_140386072133520 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>\n    By default, Plone uses a visual editor for content.\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2df6b250> name=None at 7fae2df6b210> -> __attrs_140386072179856
            __attrs_140386072179856 = _static_140386072179280

            # <span ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<span class="discreet">(If you prefer text-based syntax and/or wiki\n        syntax, you can change this in the\n    ')

            # <Static value=<_ast.Dict object at 0x7fae2df6b6d0> name=None at 7fae2df6b710> -> __attrs_140386072181456
            __attrs_140386072181456 = _static_140386072180432

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a href="@@markup-controlpanel" target="_blank">markup control panel</a>)</span>\n    </li>\n\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072181520
            __attrs_140386072181520 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>\u2026and many more settings are available in the\n        ')

            # <Static value=<_ast.Dict object at 0x7fae2df6bdd0> name=None at 7fae2df6be10> -> __attrs_140386072097296
            __attrs_140386072097296 = _static_140386072182224

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a href="@@overview-controlpanel" target="_blank">Site Setup</a>.\n    </li>\n\n</ul>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072097360
            __attrs_140386072097360 = _static_140386247937936

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<h2>Tell us how you use it</h2>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072098064
            __attrs_140386072098064 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<p>\nAre you doing something interesting with Plone? Big site deployments,\ninteresting use cases? Do you have a company that delivers Plone-based\nsolutions?\n</p>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072098640
            __attrs_140386072098640 = _static_140386247937936

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<ul>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072099408
            __attrs_140386072099408 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>Add your company as a ')

            # <Static value=<_ast.Dict object at 0x7fae2df57d10> name=None at 7fae2df57cd0> -> __attrs_140386072171024
            __attrs_140386072171024 = _static_140386072100112

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://plone.com/providers/" target="_blank">Plone provider</a>.</li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072171408
            __attrs_140386072171408 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>Add a ')

            # <Static value=<_ast.Dict object at 0x7fae2df69610> name=None at 7fae2df695d0> -> __attrs_140386072173264
            __attrs_140386072173264 = _static_140386072172048

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://plone.com/success-stories/" target="_blank">success story</a> describing your\n        deployed project and customer.</li>\n</ul>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072173328
            __attrs_140386072173328 = _static_140386247937936

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<h2>Find out more about Plone</h2>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072174096
            __attrs_140386072174096 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<p>\nPlone is a powerful content management system built on a rock-solid application stack written using the Python programming\nlanguage. More about these technologies:\n</p>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072047760
            __attrs_140386072047760 = _static_140386247937936

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<ul>\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072048528
            __attrs_140386072048528 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>The ')

            # <Static value=<_ast.Dict object at 0x7fae2df4b610> name=None at 7fae2df4b5d0> -> __attrs_140386072050384
            __attrs_140386072050384 = _static_140386072049168

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://plone.com" target="_blank">Plone open source\n    Content Management System</a> web site for evaluators and decision makers.</li>\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072050768
            __attrs_140386072050768 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>The ')

            # <Static value=<_ast.Dict object at 0x7fae2df4bed0> name=None at 7fae2df4be90> -> __attrs_140386072028112
            __attrs_140386072028112 = _static_140386072051408

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://plone.org" target="_blank">Plone community\n    </a> web site for developers.</li>\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072028496
            __attrs_140386072028496 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>The ')

            # <Static value=<_ast.Dict object at 0x7fae2df467d0> name=None at 7fae2df46790> -> __attrs_140386072030352
            __attrs_140386072030352 = _static_140386072029136

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a class="link-plain" href="https://www.python.org" target="_blank">Python\n    programming language</a> web site.</li>\n</ul>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072030416
            __attrs_140386072030416 = _static_140386247937936

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<h2>Support the Plone Foundation</h2>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386072031120
            __attrs_140386072031120 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<p>\nPlone is made possible only through the efforts of thousands of dedicated\nindividuals and hundreds of companies. The Plone Foundation:\n</p>\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071904784
            __attrs_140386071904784 = _static_140386247937936

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<ul>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071905552
            __attrs_140386071905552 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>\u2026protects and promotes Plone.</li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071906128
            __attrs_140386071906128 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>\u2026is a registered 501(c)(3) charitable organization.</li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071906704
            __attrs_140386071906704 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>\u2026donations are tax-deductible.</li>\n    ')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071907280
            __attrs_140386071907280 = _static_140386247937936

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<li>')

            # <Static value=<_ast.Dict object at 0x7fae2df28d90> name=None at 7fae2df28dd0> -> __attrs_140386071929296
            __attrs_140386071929296 = _static_140386071907728

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<a href="https://plone.org/sponsors/be-a-hero" target="_blank">Support the Foundation and help make Plone better!</a></li>\n</ul>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071905040
            __attrs_140386071905040 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<p>Thanks for using our product; we hope you like it!</p>\n\n')

            # <Static value=<_ast.Dict object at 0x7fae38708f90> name=None at 7fae38708a50> -> __attrs_140386071930000
            __attrs_140386071930000 = _static_140386247937936

            # <p ... (0:0)
            # --------------------------------------------------------
            __append_140386072339792(u'<p>\u2014The Plone Team</p>\n')
            __msgid_140386072339792 = __re_whitespace(''.join(__stream_140386072339792)).strip()
            if u'front-text':
                __append(translate(u'front-text', mapping=None, default=__msgid_140386072339792, domain=__i18n_domain, context=__i18n_context, target_language=getitem('target_language')))
            __append(u'</body>\n</html>')
            __i18n_domain = __previous_i18n_domain_140386071401808
            __append(u'\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }
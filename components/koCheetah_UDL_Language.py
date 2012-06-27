# Komodo Cheetah language service.

import logging
from koXMLLanguageBase import koHTMLLanguageBase


log = logging.getLogger("koCheetahLanguage")
#log.setLevel(logging.DEBUG)


def registerLanguage(registry):
    log.debug("Registering language Cheetah")
    registry.registerLanguage(KoCheetahLanguage())


class KoCheetahLanguage(koHTMLLanguageBase):
    name = "Cheetah"
    lexresLangName = "Cheetah"
    _reg_desc_ = "%s Language" % name
    _reg_contractid_ = "@activestate.com/koLanguage?language=%s;1" % name
    _reg_categories_ = [("komodo-language", name)]
    _reg_clsid_ = "a3641181-c337-47f3-aa55-066cdd561ac8"
    defaultExtension = '.tmpl'

    #TODO: Update 'lang_from_udl_family' as appropriate for your
    #      lexer definition. There are four UDL language families:
    #           M (markup), i.e. HTML or XML
    #           CSL (client-side language), e.g. JavaScript
    #           SSL (server-side language), e.g. Perl, PHP, Python
    #           TPL (template language), e.g. RHTML, Django, Smarty
    #      'lang_from_udl_family' maps each UDL family code (M,
    #      CSL, ...) to the sub-language name in your language.
    #      Some examples:
    #        lang_from_udl_family = {   # A PHP file can contain
    #           'M': 'HTML',            #   HTML
    #           'SSL': 'PHP',           #   PHP
    #           'CSL': 'JavaScript',    #   JavaScript
    #        }
    #        lang_from_udl_family = {   # An RHTML file can contain
    #           'M': 'HTML',            #   HTML
    #           'SSL': 'Ruby',          #   Ruby
    #           'CSL': 'JavaScript',    #   JavaScript
    #           'TPL': 'RHTML',         #   RHTML template code
    #        }
    #        lang_from_udl_family = {   # A plain XML can just contain
    #           'M': 'XML',             #   XML
    #        }
    lang_from_udl_family = {
        'M': 'HTML',
        'SSL': 'Python',
        'CSL': 'JavaScript',
        'TPL': 'Cheetah', 
    }

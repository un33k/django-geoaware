
__version__ = '0.5.0'

import defaults

GEOIP_INCLUDE_TEMPLATE_TAGS = getattr(defaults, 'GEOIP_INCLUDE_TEMPLATE_TAGS')
if GEOIP_INCLUDE_TEMPLATE_TAGS:
    from django import template
    application_tags = [
        'geoaware.templatetags.geoaware',
    ]
    for t in application_tags: template.add_to_builtins(t)


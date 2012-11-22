from django.conf import settings

try:
    from django.contrib.gis.geoip import GeoIP
except ImportError:
    from django.contrib.gis.utils import GeoIP

GEOIP_CACHE_METHOD = getattr(settings, 'GEOIP_CACHE_METHOD', GeoIP.GEOIP_STANDARD)
GEOIP_INCLUDE_TEMPLATE_TAGS = getattr(settings, 'GEOIP_INCLUDE_TEMPLATE_TAGS', False)

if getattr(settings, 'GEOIP_DEBUG_DOMAIN_OR_IP', ''):
    GEOIP_DEBUG_DOMAIN_OR_IP = getattr(settings, 'GEOIP_DEBUG_DOMAIN_OR_IP')

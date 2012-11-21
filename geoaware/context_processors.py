from django.conf import settings
from geo import get_geo_info
from geo import get_ip_address

def geoaware(request):
    """ Bring GeoInfo into the context if GeoIP is configured for city or country.
    geo_info = {
        'fqdn_or_ip': '',
        'city': '', 
        'continent_code': '', 
        'region': '',
        'charset': 0,
        'area_code': 0,
        'longitude': 0.0,
        'country_code3': '',
        'latitude': 0.0,
        'postal_code': None,
        'dma_code': 0,
        'country_code': '',
        'country_name': '',
    }
    """
    cxt = {}
    fqdn_or_ip = getattr(settings, 'DEBUG_DOMAIN_OR_IP', get_ip_address(request))
    geo_info = get_geo_info(fqdn_or_ip)
    cxt = {'geo_info': geo_info}
    return cxt

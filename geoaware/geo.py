import re
from django.conf import settings

try:
    from django.contrib.gis.geoip import GeoIP
except ImportError:
    from django.contrib.gis.utils import GeoIP
import defaults

# by no means this is a perfect IP regex
IP_RE = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

def get_ip_address(request):
    """ Make best attempt to get client's real IP or return the loopback IP """
    
    lo = '127.0.0.1'
    get_ip = lambda x,y: request.META.get(x,y)
    ip_addr = get_ip('HTTP_X_FORWARDED_FOR', get_ip('HTTP_X_REAL_IP', get_ip('REMOTE_ADDR', lo)))
    try:
        ip_addr = IP_RE.match(ip_addr).group(0)
    except:
        ip_addr = lo
    return ip_addr


def get_geo_info(request):
    """ Get GeoInfo - Relies on Django to raise exception on improper configuration  """

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
    fqdn_or_ip = getattr(defaults, 'GEOIP_DEBUG_DOMAIN_OR_IP', get_ip_address(request))
    if fqdn_or_ip:
        cache_method = getattr(defaults, 'GEOIP_CACHE_METHOD')
        geo = GeoIP(cache=cache_method)
        try:
            ginfo = geo.city(fqdn_or_ip)
            geo_info.update(ginfo)
        except:
            try:
                ginfo = geo.country(fqdn_or_ip)
                geo_info.update(ginfo)
            except:
                pass
        geo_info['fqdn_or_ip'] = fqdn_or_ip

    return geo_info




from django import template
from django.conf import settings
from ..geo import get_geo_info
from ..geo import get_ip_address

register = template.Library()

def _get_geoip_info(request):
    if 'geo_info' in request.session:
        geo_info = request.session['geo_info']
    else:
        geo_info = get_geo_info(request)
    return geo_info


@register.filter
def geo_country_name(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['country_name'])

@register.filter
def geo_country_code(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['country_code'])

@register.filter
def geo_country_code3(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['country_code3'])

@register.filter
def geo_city(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['city'])

@register.filter
def geo_latitude(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['latitude'])

@register.filter
def geo_longitude(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['longitude'])

@register.filter
def geo_postal_code(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['postal_code'])

@register.filter
def geo_region(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['region'])

@register.filter
def geo_dma_code(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['dma_code'])

@register.filter
def geo_area_code(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['area_code'])

@register.filter
def geo_fqdn_or_ip(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['fqdn_or_ip'])

@register.filter
def geo_charset(request):
    geo_info = _get_geoip_info(request)
    return(geo_info['charset'])



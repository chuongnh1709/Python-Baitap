import json 
import urllib.request

def read_json_from_intenet_unicode(url1):
    DEFAULT_ENCODING = 'utf-8'
    # url = 'https://api.github.com/users?since=100'
    urlResponse =urllib.request.urlopen(url1)
    if hasattr(urlResponse.headers, 'get_content_charset'):
        encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
    else:
        encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
    noi_dung = json.loads(urlResponse.read().decode(encoding))
    return noi_dung

    
if __name__=='__main__':
    chuoiUrl='http://dev-er.com/service_api_ban_sach/api_service_sach.php?task=sac'
    noi_dung=read_json_from_intenet_unicode(chuoiUrl)
    print(noi_dung)
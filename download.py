import ssl
import urllib.request

# 忽略SSL检验
ssl._create_default_https_context = ssl._create_unverified_context


# 下载被加密的ts切片
def ts_download(ts_url):
    path = "temp_e.ts"  # "e" stands for "encrypted"
    urllib.request.urlretrieve(ts_url, path)

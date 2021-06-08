import requests
from api_test.common.getRbjToken import getToken
from api_test.config.rbjConfig import rbj_HOST

token = getToken()


def test_0001():
    """
       测试工号搜索接口，搜索条件为空
    """
    url = f"{rbj_HOST}/workNumber?"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    with requests.request("get", url, headers=headers) as response:
        assert response.json()["code"] == "200"


def test_0002():
    """
        测试工号搜索接口，
        搜索条件：
            工号状态：启用
    """
    url = f"{rbj_HOST}/workNumber?"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    params = {
        "enable": "1"
    }
    with requests.request("get", url, params=params, headers=headers) as response:
        assert response.json()["code"] == "200"


def test_0003():
    """
        测试工号搜索接口，
        搜索条件：
            品牌：安诚
    """
    url = f"{rbj_HOST}/workNumber?"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    params = {
        "insurance_brand": "ACIC"
    }
    with requests.request("get", url, params=params, headers=headers) as response:
        assert response.json()["code"] == "200"


def test_0004():
    """
        测试工号搜索接口，
        搜索条件：
            工号类型：全域出单工号
    """
    url = f"{rbj_HOST}/workNumber?"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    params = {
        "number_type": "full"
    }
    with requests.request("get", url, params=params, headers=headers) as response:
        assert response.json()["code"] == "200"


def test_0005():
    """
        测试工号搜索接口，
        搜索条件：
            工号:传入已存在的工号
    """
    url = f"{rbj_HOST}/workNumber?"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    params = {
        "number": "5101998302"
    }
    with requests.request("get", url, params=params, headers=headers) as response:
        assert response.json()["code"] == "200"


def test_0006():
    """
        测试工号搜索接口，
        搜索条件：
            工号状态:禁用
    """
    url = f"{rbj_HOST}/workNumber?"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    params = {
        "enable": "0"
    }
    with requests.request("get", url, params=params, headers=headers) as response:
        assert response.json()["code"] == "200"


def test_0007():
    """
        测试工号搜索接口，
        搜索条件：
            工号：输入不存在的工号
    """
    url = f"{rbj_HOST}/workNumber?"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    params = {
        "number": "hsdjk132432"
    }
    with requests.request("get", url, params=params, headers=headers) as response:
        assert response.json()["code"] == "200"


def test_0008():
    """
        测试工号搜索接口，
        搜索条件：
            品牌：传入不存在的品牌
    """
    url = f"{rbj_HOST}/workNumber?"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    params = {
        "insurance_brand": "皇城"
    }
    with requests.request("get", url, params=params, headers=headers) as response:
        assert response.json()["code"] == "200"


def test_0009():
    """
        测试工号搜索接口，
        搜索条件：
            工号类型：其他
    """
    url = f"{rbj_HOST}/workNumber?"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    params = {
        "number_type": "other"
    }
    with requests.request("get", url, params=params, headers=headers) as response:
        assert response.json()["code"] == "200"


def test_0010():
    """
        测试工号搜索接口，
        搜索条件：
            工号状态：启用
            品牌：安诚
            工号类型：全域出单工号
            工号：传入已存在的工号
    """
    url = f"{rbj_HOST}/workNumber?"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    params = {
        "enable": "1",
        "insurance_brand": "ACIC",
        "number_type": "full",
        "number": "151016491"
    }
    with requests.request("get", url, params=params, headers=headers) as response:
        assert response.json()["code"] == "200"


def test_0011():
    """
        测试批量启用工号接口：
            不选择工号
    """
    url = f"{rbj_HOST}/workNumber/enable/1"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    with requests.request("put", url, headers=headers) as response:
        assert response.json()["code"] == "506"
        assert response.json()["message"] == "没有数据被操作！"


def test_0012():
    """
        测试批量启用工号接口：
            选择状态为启用的工号
    """
    url = f"{rbj_HOST}/workNumber/enable/1"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    data = {
        "ids[0]": "1084",
        "ids[1]": "1077",
        "ids[2]": "1076",
        "ids[3]": "1075"
    }
    with requests.request("put", url, data=data, headers=headers) as response:
        assert response.json()["status"] == "success"


def test_0013():
    """
        测试批量启用工号接口：
            选择状态为禁用的工号
    """
    url = f"{rbj_HOST}/workNumber/enable/1"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    data = {
        "ids[0]": "843",
        "ids[1]": "842",
        "ids[2]": "838",
        "ids[3]": "831"
    }
    with requests.request("put", url, data=data, headers=headers) as response:
        assert response.json()["status"] == "success"


def test_0014():
    """
        测试批量启用工号接口：
            选择状态为启用和禁用的工号
    """
    url = f"{rbj_HOST}/workNumber/enable/1"
    headers = {
        "Access-Token": token,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36"
    }
    data = {
        "ids[0]": "843",
        "ids[1]": "842",
        "ids[2]": "1075",
        "ids[3]": "1076"
    }
    with requests.request("put", url, data=data, headers=headers) as response:
        assert response.json()["code"] == "506"


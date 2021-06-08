import requests
from api_test.config.rbjConfig import rbj_HOST, passport_HOST


def getTicket():
    userSessionUrl = f"{passport_HOST}/userSession"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36 "
    }
    data = {
        "mobile": "administrator_284",
        "password": "hxy_123456",
        "invitationCode": "",
        "loginType": "PASSWORD"
    }

    response = requests.request("post", userSessionUrl, data=data, headers=headers)
    ticket = response.json()["data"]["ticket"]
    return ticket


def getToken():
    infoUrl = f"{rbj_HOST}/platformAdmins/info"
    ticket = getTicket()
    Cookie = '__jsluid_s=b1ee379f34bde471f423e5727ee89d90; Hm_lvt_d51f7760835a0572a777c119eae5016b=1620616561,' \
             '1621309338,1622537443,1622770211; Hm_lpvt_d51f7760835a0572a777c119eae5016b=1622770211; Access-Ticket=' + ticket + "; Elephant-Ticket=" + ticket
    headers = {
        "Cookie": Cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.128 Safari/537.36 "
    }
    response = requests.request("get", infoUrl, headers=headers)
    return response.json()["data"]["adminInfo"]["accessToken"]

# if __name__ == '__main__':
# getTicket()

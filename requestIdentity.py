# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import settings
from datetime import datetime
from barocert import *

navercertService = NavercertService(settings.LinkID, settings.SecretKey)
navercertService.IPRestrictOnOff = settings.IPRestrictOnOff
navercertService.UseStaticIP = settings.UseStaticIP

"""
네이버 이용자에게 본인인증을 요청합니다.
https://developers.barocert.com/reference/naver/python/identity/api#RequestIdentity
"""

# 이용기관 코드
clientCode = settings.ClientCode

identity = NaverIdentity(        
    receiverHP = navercertService._encrypt('01012341234'),
    receiverName = navercertService._encrypt('홍길동'),
    receiverBirthday = navercertService._encrypt('19700101'),
    callCenterNum = '1588-1600',
    expireIn = 1000,
    # appUseYN = True,
    # returnURL = 'navercert://identity',
    # deviceOSType = 'ANDROID'
)

try:
    obj = navercertService.requestIdentity(clientCode, identity)
    print(obj.receiptID)
    print(obj.scheme)
    print(obj.marketUrl)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)
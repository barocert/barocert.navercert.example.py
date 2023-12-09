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
네이버 이용자에게 복수(최대 50건) 문서의 전자서명을 요청합니다.
https://developers.barocert.com/reference/naver/python/sign/api-multi#RequestMultiSign
"""

# 이용기관 코드
clientCode = settings.ClientCode

multiSignTokens = []
for x in range(0,5):
    multiSignTokens.append(
        NaverMultiSignTokens( 
            tokenType = 'TEXT',
            token = navercertService._encrypt('전자서명(복수) 요청 원문' + str(x)),
            # tokenType = 'HASH',
            # token = navercertService._encrypt(navercertService._sha256('전자서명(복수) 요청 원문' + str(x))),
        )
    )    

multiSign = NaverMultiSign(   
    receiverHP = navercertService._encrypt('01012341243'),
    receiverName = navercertService._encrypt('홍길동'),
    receiverBirthday = navercertService._encrypt('19700101'),
    reqTitle = '전자서명(복수) 요청 메시지 제목',
    reqMessage = navercertService._encrypt('전자서명(복수) 요청 메시지'),
    callCenterNum = '1588-1600',
    expireIn = 1000,
    tokens = multiSignTokens,
    # appUseYN = True,
    # returnURL = 'navercert://sign',
    # deviceOSType = 'ANDROID'
)

try :
    obj = navercertService.requestMultiSign(clientCode, multiSign)
    print(obj.receiptID)
    print(obj.scheme)
    print(obj.marketUrl)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)
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
네이버 이용자에게 단건(1건) 문서의 전자서명을 요청합니다.
https://developers.barocert.com/reference/naver/python/sign/api-single#RequestSign
"""

# 이용기관 코드
clientCode = settings.ClientCode

sign = NaverSign(        
    receiverHP = navercertService._encrypt('01054437896'),
    receiverName = navercertService._encrypt('최상혁'),
    receiverBirthday = navercertService._encrypt('19880301'),
    reqTitle = '전자서명(단건) 메시지 제목',
    reqMessage = navercertService._encrypt('전자서명(단건) 요청 메시지'),
    callCenterNum = '1588-1600',
    expireIn = 1000,
    token = navercertService._encrypt('전자서명(단건) 요청 원문'),
    tokenType = 'TEXT',
    # appUseYN = True,
    # returnURL = 'navercert://sign',
    # deviceOSType = 'ANDROID'
)

try :
    obj = navercertService.requestSign(clientCode, sign)
    print(obj.receiptID)
    print(obj.scheme)
    print(obj.marketUrl)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)
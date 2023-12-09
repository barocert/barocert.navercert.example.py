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
전자서명(단건) 요청 후 반환받은 접수아이디로 인증 진행 상태를 확인합니다.
https://developers.barocert.com/reference/naver/python/sign/api-single#GetSignStatus
"""

# 이용기관 코드
clientCode = settings.ClientCode

try :
    obj = navercertService.getSignStatus(clientCode, '02310310230900000210000000000008')
    print(obj.receiptID)
    print(obj.clientCode)
    print(obj.state)
    print(obj.expireDT)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)
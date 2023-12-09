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
네이버 이용자에게 자동이체 출금동의를 요청합니다.
https://developers.barocert.com/reference/naver/python/cms/api#RequestCMS
"""

# 이용기관 코드
clientCode = settings.ClientCode

cms = NaverCMS(        
    receiverHP = navercertService._encrypt('01012341234'),
    receiverName = navercertService._encrypt('홍길동'),
    receiverBirthday = navercertService._encrypt('19700101'),
    reqTitle = '출금동의 요청 메시지 제목',
    reqMessage = self.navercertService._encrypt('출금동의 요청 메시지'),
    callCenterNum = '1588-1600',
    expireIn = 1000,
    requestCorp = self.navercertService._encrypt('청구기관'),    
    bankName = self.navercertService._encrypt('출금은행'),    
    bankAccountNum = self.navercertService._encrypt('123-456-7890'),    
    bankAccountName = self.navercertService._encrypt('홍길동'),    
    bankAccountBirthday = self.navercertService._encrypt('19700101'),    
    # appUseYN = True,
    # returnURL = 'navercert://cms',
    # deviceOSType = 'ANDROID'
)

try:
    obj = navercertService.requestCMS(clientCode, cms)
    print(obj.receiptID)
    print(obj.scheme)
    print(obj.marketUrl)
except BarocertException as BE :
    print(BE.code)
    print(BE.message)
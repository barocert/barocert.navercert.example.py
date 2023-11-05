# -*- coding: utf-8 -*-

"""
네이버써트 API Python SDK Example

- Python SDK 연동환경 설정방법 안내 : https://developers.barocert.com/guide/naver/identity/python/getting-started/tutorial
- 업데이트 일자 : 2023-11-06
- 연동 기술지원 연락처 : 1600-9854
- 연동 기술지원 이메일 : code@linkhubcorp.com

<테스트 연동개발 준비사항>
1) 17, 20 라인에 선언된 링크아이디(LinkID)와 비밀키(SecretKey)를
    연동신청 후 메일로 발급받은 인증정보를 참조하여 변경합니다.
"""

# 링크아이디
LinkID = "TESTER"

# 비밀키
SecretKey = "SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I="

# 이용기관 코드
ClientCode = "023090000021"

# 인증토큰 IP제한기능 사용여부, True-사용, False-미사용, 기본값(True)
IPRestrictOnOff = True

# 네이버써트 API 서비스 고정 IP 사용여부, True-사용, False-미사용, 기본값(False)
UseStaticIP = False
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=64, verbose_name="사용자 아이디")
    useremail = models.EmailField(max_length=128, verbose_name="사용자 이메일", null=True)
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    regi_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")
    
    def __str__(self) -> str:
        return self.user_id
    
    class Meta:
        db_table = 'tb_user'


# 설계의 순서 #
# 1. 어떤 데이터를 사용할 것인가? -> 머신러닝, 분석 Data가 어떤 것인지?
#   만약 코드 작성부터 한다면 잘못된 것. 비즈니스 로직에 맞게 수정하는게 비용이 큼. 
#   로직 -> 어떤 상황에서 어떻게 프로그램이 동작해야하는가?
# 2. Data IO가 잘되는지 확인, 데이터가 클라이언트와 서버 간에 잘 전송이 가는지 확인한다.
# 3. 재설계, 이 데이터를 이용해서 어떻게 로직을 구현할까? -> 알고리즘
# 4. 코딩 #
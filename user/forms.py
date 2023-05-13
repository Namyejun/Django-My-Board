from django import forms
from .models import User
from django.contrib.auth.hashers import check_password
class LoginForm(forms.Form):
    # 모델 만드는 것과 비슷
    user_id = forms.CharField(max_length=64,\
                            label = "사용자 아이디",\
                            error_messages={"required":"아이디를 입력해 주세요"}\
                            ) # 얘네가 input tag와 일맥상통한다.
    password = forms.CharField(max_length=64,\
                            label="비밀번호",\
                            widget=forms.PasswordInput,\
                            error_messages={"required":"비밀번호를 입력해 주세요"}\
                            ) # 위젯 : input tag의 타입\

    # 유효성 검증에 대한 메소드를 오버라이딩한다.
    def clean(self):
        # cleaned_data : 유효성 검증을 통과한 데이터
        # super().clean() : 부모 클래스에서 유효성 검증이 된 데이터 가져오기
        cleaned_data = super().clean()
        user_id = cleaned_data.get("user_id")
        password = cleaned_data.get("password")

        # "", None 방지 코드
        if user_id and password:
            try:
                user = User.objects.get(user_id = user_id)
            except User.DoesNotExist:
                self.add_error("user_id","아이디가 존재하지 않습니다.")
            else:
                if not check_password(password, user.password):
                    self.add_error("password", "비밀번호가 일치하지 않습니다.")
                else:
                    # 1. 클라이언트가 아이디와 비밀번호를 잘 입력했다. 부모 클래스가 해줌
                    # 2. 클라이언트가 입력한 아이디에 해당하는 유저가 있고 비밀번호도 맞다. 오버라이딩 구현
                    self.uid = user.id # pk를 저장해줌
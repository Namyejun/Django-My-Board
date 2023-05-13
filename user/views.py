from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from .forms import LoginForm
# Create your views here.
def register(request):
    # 사용자의 요청이 GET인 경우
    if request.method == "GET":
        return render(request, 'register.html')
    # 사용자의 요청이 POST인 경우
    elif request.method == "POST":
        user_id = request.POST.get("user_id", None)
        useremail = request.POST.get("useremail", None)
        password = request.POST.get("password", None)

        # 가입시 비밀번호 일치 확인을 위해 받아옵니다.
        # 실제로는 frontend에서 담당, 여기서는 backend에서 담당
        re_password = request.POST.get("re-password", None)

        res_data = {} # attribute = 서버가 클라이언트한테 html에 끼워서 보여줄 데이터

        if not(user_id and useremail and password and re_password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        elif password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."
        else:
            user = User(user_id = user_id, useremail = useremail, password = make_password(password))
            user.save()
            return render(request, 'register.html')

        return render(request, 'register.html', res_data) # view resolver = 템플릿 + 애트리뷰트

def login(request):
    
    if request.method == "GET":
        form = LoginForm()

        # 애트리뷰트로 html에 form을 넘겨준다
    elif request.method == "POST":
        form = LoginForm(request.POST)
        # is_valid : 유효성 검증
        # - 값을 전부 다 제대로 입력했는지 검사
        # + clean 메소드를 오버라이드 하므로 인해서 아이디와 비밀번호까지 검사
        if form.is_valid():
            request.session["user"] = form.uid
            return redirect("/")
        else:
            pass
    return render(request, "login.html", {'form': form})

def logout(request):
    if request.session.get("user"):
        del(request.session["user"]) # 유저 정보 삭제
    
    # 로그아웃 후 리다이렉트로 홈페이지 이동
    return redirect("/")

##############################
# HTML의 폼태그만을 사용한 경우
##############################
# def login(request):
#     # 사용자의 요청이 GET인 경우
#     if request.method == "GET":
#         return render(request, 'login.html')
#     # 사용자의 요청이 POST인 경우
#     elif request.method == "POST":
#         user_id = request.POST.get("user_id", None)
#         password = request.POST.get("password", None)

#         res_data = {}

#         if not(user_id and password):
#             res_data['error'] = "모든 값을 입력해야 합니다."
#         else:
#             try:
#                 user = User.objects.get(user_id = user_id)
#             except:
#                 res_data['error'] = "존재하지 않는 아이디입니다."
#             else:
#                 if check_password(password, user.password):
#                     # 비밀번호 일치시 user의 pk값을 세션에 넣어 보냄, 파이썬 requests 모듈 사용
#                     request.session['user'] = user.id

#                     return redirect("/")
#                 else:
#                     res_data['error'] = "비밀번호가 일치하지 않습니다."            

#         return render(request, 'login.html', res_data)
    
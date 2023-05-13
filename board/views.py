from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from user.models import User
from django.http.response import Http404
from django.core.paginator import Paginator
# Create your views here.

def board_list(request):
    # 모든 게시글 가져오기
    all_boards = Board.objects.all().order_by('-id')
    # GET 방식으로 page를 가져오기, 없으면 기본 1페이지
    # QueryString으로 들어오는 page parameter 받기 - ?page=1
    page = int(request.GET.get("page", 1))
    # 전체 게시글에서 몇 개의 게시글을 쪼개서 가져올지 설정. 여기서는 한 페이지당 3개씩 보여줌
    paginator = Paginator(all_boards, 3)
    # 페이지네이터에서 해당 페이지의 게시글 목록 보여주기
    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})

def board_write(request):
    if not request.session.get('user'):
        return redirect("/user/login")
    if request.method == "GET":
        form = BoardForm()
        return render(request, 'board_write.html', {"form": form})
    elif request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            contents = form.cleaned_data['contents']
            user = User.objects.get(id = request.session.get("user"))

            Board(title = title, contents = contents, writer = user).save()
            return redirect('/board/list')
        return render(request, 'board_write.html', {"form": form})
    
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk = pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {"board":board})
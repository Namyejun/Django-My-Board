from django.shortcuts import render
from user .models import User

import os
def home(request):
   uid = request.session.get('user')
   if uid:
      user = User.objects.get(pk=uid)
      return render(request, "home.html", {"user_model":user})

   return render(request, "home.html")

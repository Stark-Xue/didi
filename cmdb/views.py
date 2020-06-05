from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

from django.shortcuts import HttpResponse

URL_LIST = [
	{"username": 'xue', "email": "1234@qq.com", "gender": "man",}
]

for index in range(20):
	temp = {"username": 'xue'+str(index), "email": "1234@qq.com", "gender": "man",}
	URL_LIST.append(temp)

def home(request):
	if request.method == "POST":
		u = request.POST.get('username', None)
		e = request.POST.get('email', None)
		g = request.POST.get('gender', None)
		temp = {"username": u, "email": e, "gender": g,}
		URL_LIST.append(temp)
	return render(request, 'home.html', {"url_list": URL_LIST})

def login(request):
	# 包含用户所有的提交信息
	# 获取用户的提交方式
	#print(request.method)
	msg_err = ' '
	if request.method == "POST":
		# 获取用户通过POST提交过来的数据
		user = request.POST.get('user', None)
		pwd = request.POST.get('pwd', None)
		if user == "root" and pwd == "123":
			return redirect("/home") # 跳转
		else:
			msg_err = "用户名或密码错误"
		# user = request.POST['user']
		# pwd = request.POST['pwd']
		print(user, pwd)
	# f = open("templates/login.html", 'r', encoding="utf-8")
	# data = f.read()
	# f.close()
	# return HttpResponse(data)
	return render(request, 'login.html', {'msg_err': msg_err}) # 找到模板打开返回给用户
from django.shortcuts import render

# Create your views here.

from .models import Main, CritRats

def index(request):
	return render(request, 'critratmain/index.html')
	
def main(request):
	main = Main.objects.get(id=1)
	context = {'main': main}
	return render(request, 'critratmain/main.html', context)
	
def critRats(request):
	critlist = CritRats.objects.order_by('critrats')
	context ={'critlist' : critlist}
	return render(request, 'critratmain/critrats.html', context)
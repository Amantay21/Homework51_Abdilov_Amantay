from django.shortcuts import render
from django.http import HttpResponseRedirect
from webapp.cat import Cat


def index(request):
    if request.method == 'GET':
        return render(request, 'create_page.html')
    else:
        Cat.name = request.POST.get('cat_name')
        return HttpResponseRedirect('action/')


def action(request):
    if request.method == 'GET':
        context = {
            "name": Cat.name,
            "age": Cat.age,
            "satiety": Cat.satiety,
            "mood": Cat.mood,
            "is_sleep": Cat.is_sleep,
            "avatar": Cat.avatar
        }
        return render(request, 'action_page.html', context)
    else:
        action = request.POST.get("action")
        if action == "play":
            Cat.play()
        elif action == "feed":
            Cat.feed()
        elif action == "put_to_sleep":
            Cat.put_to_sleep()
        else:
            pass
        return HttpResponseRedirect('/action/')

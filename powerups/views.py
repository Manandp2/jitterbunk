from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Powerup, User

# Create your views here.
def index(request):
    return render(request, 'powerups/index.html')

class AllPowerupsView(generic.ListView):

    template_name = 'powerups/all.html'
    context_object_name = 'all_powerups_list'

    def get_queryset(self):
        """
        Return all the powerups (not including those set in the future)
        """
        order = self.kwargs["order"]

        return Powerup.objects.filter(
            date_added__lte=timezone.now()
        ).order_by(order)
        
def sort(request):
    sort_by = request.GET['sort_by']

    return HttpResponseRedirect(reverse('powerups:all', kwargs={'order' : sort_by}))

class AllUsersView(generic.ListView):

    template_name = 'powerups/all_user.html'
    context_object_name = 'all_users_list'

    def get_queryset(self):
        """
        Return all users
        """
        return User.objects.all()

def user_detail(request, pk):
    powerup_list = Powerup.objects.filter(user__pk=pk)
    user = User.objects.filter(id=pk)[0]
    context = {
        'user': user,
        'powerup_list': powerup_list
        }
    return render(request, 'powerups/user_detail.html', context)

class PowerUpDetailView(generic.DetailView):
    model = Powerup
    template_name = 'powerups/powerup_detail.html'

def addPowerup(request):
    user_list = User.objects.all()
    return render(request, 'powerups/add_powerup.html', {'user_list': user_list})

def create(request):
    title = request.POST['title']
    link = request.POST['link']
    description = request.POST['description']
    date_added = timezone.now()
    user = request.POST['user']
    team = request.POST['team']

    try:
        user = User.objects.get(username = user)
    except (KeyError, User.DoesNotExist):
        print('User does not exist')
        user_list = User.objects.all()
        return render(request, 'powerups/add_powerup.html', {
            'user_list': user_list,
            'error_message': "User doesn't exist.",
            'old_form_entries': {
                'title': title,
                'link': link,
                'description': description,
                'team': team
            },
        })
    
    new_powerup = Powerup(title=title, link=link, description=description, date_added=date_added, user=user, team=team)
    new_powerup.save()

    return HttpResponseRedirect(reverse('powerups:index'))


'''
class UserView(generic.ListView):
    model = User
    template_name = 'powerups/user_detail.html'

    def get_queryset(self):
        return User.objects.all()
        
def user_powerups(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    powerup = user.powerup_set.get(pk=request.GET['powerup'])

    return HttpResponseRedirect(reverse('powerups:results', args=(question.id,)))

    try:
        powerup = user.powerup_set.get(pk=request.GET['powerup'])
    except (KeyError, Powerup.DoesNotExist):
        return render(request, 'powerups/user_detail.html', {
            'user': user,
            'error_message': "No powerups.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''
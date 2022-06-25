from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404, redirect
from .models import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    # return HttpResponse("Hello, world. You're at the agency index.")    
    return render(request, 'agency/index.html')
    # username = request.user.username
    # try:
    #     user_logged_in = Client.objects.get(login=username)
    # except(Client.DoesNotExist):
    #     # return HttpResponse("Client does not exist!")
    #     return render(request, 'agency/index.html')
    # else:
    #     mainpage()


# def mainpage(request):
#     return render(request, 'agency/mainpage.html')


def profile(request):
    # return HttpResponse("Your profile is here.")
    # return render(request, 'agency/profile.html')
    username = request.user.username
    try:
        user_logged_in = Client.objects.get(login=username)

    except(Client.DoesNotExist):
        return HttpResponse("Client does not exist!")
    else:
        return render(request, 'agency/profile.html',
                      {'user_client': user_logged_in})


def profile_edit(request):
    username = request.user.username
    try:
        user_logged_in = Client.objects.get(login=username)
        return render(request, 'agency/profile_edit.html', {'user_client': user_logged_in})
    except(Client.DoesNotExist):
        return HttpResponse("Client does not exist!")


def profile_edit_result(request):
    client_list = Client.objects.all()
    new_login = request.POST["F_login"]
    curent_user = request.user
    curent_client = Client.objects.get(login=curent_user.username)

    var = False

    for c in client_list:
        if c.login == new_login and new_login != curent_user.username:
            var = True

    if not var:
        curent_client.name = request.POST['F_name']
        curent_client.surname = request.POST['F_surname']
        curent_client.login = request.POST['F_login']
        curent_client.email = request.POST['F_email']
        curent_client.phone_number = request.POST['F_phone_number']
        curent_client.save()

        curent_user.username = request.POST['F_login']
        curent_user.email = request.POST['F_email']
        curent_user.first_name = request.POST['F_name']
        curent_user.last_name = request.POST['F_surname']
        curent_user.save()

        return redirect(reverse('agency:profile'))
    else:
        return render(request, 'agency/profile_edit_result.html', {
            'error_message': "Login is already in use, try something different!",
            'user_client': curent_client,
        })


def profile_delete(request):
    username = request.user.username
    try:
        user_logged_in = Client.objects.get(login=username)
        return render(request, 'agency/profile_delete.html', {'user_client': user_logged_in})
    except(Client.DoesNotExist):
        return HttpResponse("Unknown error")


def profile_delete_result(request):
    username = request.user.username
    try:
        client_logged_in = Client.objects.get(login=username)
        user_logged_in = User.objects.get(username=username)
        client_logged_in.delete()
        user_logged_in.delete()
        return render(request, "agency/profile_delete_result.html")
    except(Client.DoesNotExist or User.DoesNotExist):
        return HttpResponse("Unknown error")


# def festivals(request):
#     # return HttpResponse("Your festival is here.")
#     return render(request, 'agency/festivals.html')


# def tickets(request):
#     # return HttpResponse("Your tickets are here.")
#     return render(request, 'agency/tickets.html')


# def genres(request):
#     # return HttpResponse("Your genres are here.")
#     return render(request, 'agency/genres.html')


# def instrumets(request):
#     return HttpResponse("Your instruments are here.")


# def concerts(request):
#     return HttpResponse("Your concerts are here.")


# def artists(request):
#     return HttpResponse("Your artists are here.")

def festival_list(request):
    festival_list = Festival.objects.all()
    concert_festival_list = Concert_on_festival.objects.all()
    return render(request, 'agency/festivals.html', {'festival_list': festival_list, 'concert_festival_list': concert_festival_list})


def genre_list(request):
    genre_list = Genre.objects.all()
    instruments_genre_list = Genre_and_intruments.objects.all()
    return render(request, 'agency/genre.html', {'genre_list': genre_list, 'instruments_genre_list': instruments_genre_list})


def ticket_list(request):
    ticket_list = Ticket.objects.all()
    concert_ticket_list = Ticket_for_concert.objects.all()
    return render(request, 'agency/ticket.html', {'ticket_list': ticket_list, 'concert_ticket_list': concert_ticket_list})
    pass

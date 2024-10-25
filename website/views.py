from django.shortcuts import render
from website.models import TeamMember


def page_home(request):
    return render(request, "website/page_home.html")


def page_team(request):
    team_members = TeamMember.load_from_json('website/team.json')
    return render(request, "website/page_team.html", {"members": team_members})

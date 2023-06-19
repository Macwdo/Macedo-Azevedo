from django.http import HttpRequest
from django.shortcuts import render


def lawsuit_board(request: HttpRequest):
    return render(request, "lawsuit_board/lawsuit_board.html")
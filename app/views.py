from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def count_hi(request, str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == "hi":
      count += 1
  return HttpResponse(count)

def string_match(request, a, b):
  count = 0
  short = min(len(a), len(b))
  for i in range(short - 1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return HttpResponse(count)

def round_sum(request, a, b, c):
  def round10(num):
    return (num+5)/10*10
  return HttpResponse(int(round10(a))+int(round10(b))+int(round10(c)))

from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_count = len(word_list)
    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary.keys():
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    word_list = sorted(word_dictionary.items(),
                       key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {"fulltext": fulltext,
                                          "word_count": word_count, "word_list": word_list, "word_dictionary": word_dictionary})

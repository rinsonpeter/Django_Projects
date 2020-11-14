from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1 style="color:red;">This is my first Assignment</h1>''<br>''<iframe width="560" height="315" '
                        'src="https://www.youtube.com/embed/j54R3P76aS4"'
                        ' frameborder="0" allow="accelerometer; autoplay; '
                        'clipboard-write; encrypted-media; gyroscope; picture-in-picture"'
                        ' allowfullscreen></iframe>')


def page2(request):
    return HttpResponse('<h1 style="color:blue;">This is my first Assignment</h1>''<br>'
                        '<iframe width="560" height="315" '
                        'src="https://www.youtube.com/embed/v3m_DlYSJOA" '
                        'frameborder="0" allow="accelerometer; autoplay; '
                        'clipboard-write; encrypted-media; '
                        'gyroscope; picture-in-picture" allowfullscreen></iframe>')

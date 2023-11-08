from .models import Category, HomeContent

def categories(request):
    categories_list = Category.objects.all()
    return {'list':categories_list}


def homecontent(request):
    content = HomeContent.objects.all()
    return {'content': content}
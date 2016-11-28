from django.shortcuts import get_object_or_404, render
from models import Content, Article, Contributor
from pprint import pprint
# Create your views here.

# Returns a webpage showing a list of all Articles in the database
def all_articles(request):
    # Find all blog posts
    data = {'articles': Article.objects.all()}
    pprint (vars(Article.objects.all()[0]))
    return render(request, 'all_articles.html', data)

def article(request, article_id):
	article = get_object_or_404(Article, id=article_id)
	data = {'article': article}
	return render(request, 'article.html', data)
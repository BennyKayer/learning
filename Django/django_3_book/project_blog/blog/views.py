from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from blog.models import Post

# Function way
# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list=object_list, per_page=3)
#     page = request.GET.get("page")
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # Jeżeli dostaliśmy nie-int'a to zwracamy 1-wszą stronę
#         posts = paginator.page(1)
#     except EmptyPage:
#         # Jeżeli dostaliśmy stronę 5
#         # podczas gdy mamy w sumie 3 strony zwrócimy stronę 3
#         posts = paginator.page(paginator.num_pages)
#     return render(
#         request, "blog/post/list.html", {"page": page, "posts": posts}
#     )


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/post/detail.html", {"post": post})

from django.views import generic
from . import models
from .models import Post
from .forms import CommentForm, NewsletterForm
from django.shortcuts import render, get_object_or_404



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 4


# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )





def tampo(request):
    posts = models.Post.objects.filter(status=True).order_by("-created_on")[:3]




    if request.method == "POST":
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            obj = newsletter_form.save(commit=False)
            obj.save()
    else:
        newsletter_form = NewsletterForm()

    return render(request, 'tampo.html', {'posts': posts, 'newsletter_form':newsletter_form})




def product(request):
    product = 'productproductproduct'
    return render(request, 'product.html', {'product': product})




def about(request):
    about = 'aboutaboutaboutaboutabout'
    return render(request, 'about.html', {'about': about})







# End

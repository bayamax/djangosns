from django.shortcuts import render, redirect

from .forms import PostCreateForm

def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:post_list')
    else:
        form = PostCreateForm()
    return render(request, 'post/post_create.html', {'form': form})
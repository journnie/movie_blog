from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewsForm


# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'reviews/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            review = form
            review.save()
            return redirect('reviews:index')

    form = ReviewsForm()
    context = {
        'form': form
    }
    return render(request, 'reviews/create.html', context)

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review': review
    }
    return render(request, 'reviews/detail.html', context)


def edit(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    form = ReviewsForm(request.POST, instance=review)
    context = {
        'form': form,
        'review': review
    }
    return render(request, 'reviews/create.html', context)


def delete(request, review_pk):
    Review.objects.get(pk=review_pk).delete()
    return redirect('reviews:index')

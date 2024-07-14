from datetime import date
# *NOTES*
# This line imports the `date` class from the `datetime` module.
# The `date` class is used to create date objects representing specific dates.
# https://docs.python.org/3/library/datetime.html#datetime.date

from django.shortcuts import render
# *NOTES*
# This line imports the `render` function from `django.shortcuts`.
# The `render` function is used to render a template with a context.
# https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        # *NOTES*
        # This line sets the date for the post using the `date` class.
        # The `date` class is initialized with the year, month, and day.
        # https://docs.python.org/3/library/datetime.html#datetime.date
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
  return post['date']
# *NOTES*
# This function `get_date` takes a post dictionary as an argument and returns the value of the 'date' key.
# This function is used as a key function for sorting posts by date.
# https://docs.python.org/3/howto/sorting.html#key-functions

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    # *NOTES*
    # This line sorts the `all_posts` list by date using the `sorted` function and the `get_date` function as the key.
    # The `sorted` function returns a new sorted list.
    # https://docs.python.org/3/library/functions.html#sorted

    latest_posts = sorted_posts[-3:]
    # *NOTES*
    # This line takes the last three posts from the sorted list, which are the latest posts.
    # List slicing is used to get the last three elements of the list.
    # https://docs.python.org/3/tutorial/introduction.html#lists

    return render(request, "blog/index.html", {
      "posts": latest_posts
    })
    # *NOTES*
    # This line renders the `index.html` template with the `latest_posts` context.
    # The `render` function combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

def posts(request):
    return render(request, "blog/all-posts.html", {
      "all_posts": all_posts
    })
    # *NOTES*
    # This line renders the `all-posts.html` template with the `all_posts` context.
    # The `render` function combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    # *NOTES*
    # This line finds the post with the matching slug using a generator expression and the `next` function.
    # The `next` function returns the first item from the generator that matches the condition.
    # https://docs.python.org/3/library/functions.html#next

    return render(request, "blog/post-detail.html", {
      "post": identified_post
    })
    # *NOTES*
    # This line renders the `post-detail.html` template with the `identified_post` context.
    # The `render` function combines a given template with a given context dictionary and returns an HttpResponse object with that rendered text.
    # https://docs.djangoproject.com/en/5.0/topics/http/shortcuts/#render

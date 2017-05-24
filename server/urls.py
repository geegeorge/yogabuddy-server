# Match url in browser to module in django project
from django.conf.urls import url
# load urls for administration site

# load in functions created in my custom views file
from server.views import splash, get_all_posts, get_posts_by_id,  get_users_by_id, get_all_poses, get_poses_by_id, add_post

# NOT USING GET THESE
# get_users, get_contributors

urlpatterns = [
    url(r'^$', splash ), # Splash page
    url(r'^posts$', get_all_posts), # get all posts (feed)
    url(r'^posts/(\d+)/$', get_posts_by_id), # get individual post (from feed or profile)
    url(r'^users/(\d+)/$', get_users_by_id), # get individual user profile (needs AUTH)
    url(r'^poses$', get_all_poses), # get all poses
    url(r'^poses/(\d+)/$', get_poses_by_id), # get one pose
    # url(r'^create_user$', create_user) # post to  users
    # url(r'^login$', login) # django auth send cookie/token
    # url(r'^logout$', logout) # remove cookie/token
    # url(r'^contributors$', get_contributors) # render contributors page
    url(r'^addpost$', add_post)
]

# The r means we want to treat it as a raw string that will allow us to use backslashes
# The ^ tells us thats the beginning of the string
# The admin part references the administration part of Django
# The $ means end of string
# d means digit or number
# (\d+)/ is allowing us to pass a number in to the url params

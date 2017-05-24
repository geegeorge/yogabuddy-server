from django.db import connection, transaction
from django.http import JsonResponse, HttpResponse

# LETS US DO PSQL STUFF
@transaction.atomic

def splash(request):
    return HttpResponse('SPLISH SPLASH')

# GRABS ALL POSTS
def get_all_posts(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM yoga_posts")
    result = cursor.fetchall() # all results
    return JsonResponse(result, safe=False)
    # result = cursor.fetchmany(10) # limiting search to 10 results

# GRABS A SINGLE POST
def get_posts_by_id(request, posts):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM yoga_posts WHERE id = %s", [posts])
    result = cursor.fetchall() # all results
    return JsonResponse(result, safe=False)

# GRABS ALL USERS (!!!! NOT NEEDED !!!!)
# def get_all_users(request):
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM yoga_users")
#     result = cursor.fetchall() # all results
#     return JsonResponse(result, safe=False)
    # result = cursor.fetchmany(10) # limiting search to 10 results

# GRABS A SINGLE USER
def get_users_by_id(request, users):
    cursor = connection.cursor()
    cursor.execute("SELECT id, username, email, profile_picture_img, bio, admin, moderator, professional, verified_user,  created_at, updated_at  FROM yoga_users WHERE id = %s", [users])
    result = cursor.fetchall() # all results
    return JsonResponse(result, safe=False)

# GRABS ALL POSES
def get_all_poses(request):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM yoga_poses")
    result = cursor.fetchall() # all results
    response = JsonResponse(result)
    return response.result
    # return JsonResponse(result)
    # result = cursor.fetchmany(10) # limiting search to 10 results

# GRABS A SINGLE pose
def get_poses_by_id(request, poses):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM yoga_poses WHERE id = %s", [poses])
    result = cursor.fetchall() # all results
    return JsonResponse(result, safe=False)

# Create a posts
# def create_post(request):
#     # cursor = connection.cursor()
#     # cursor.execute("SELECT * FROM yoga_poses WHERE id = %s", [poses])
#     # result = cursor.fetchall() # all results
#     # return JsonResponse(result, safe=False)
#
# # Create use, check for duplicate username/email,
# def create_user(request):
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM users")
#     # result = cursor.fetchall() # all results
#     # return JsonResponse(result, safe=False)
#
# # Login and send cookie
# def login(request):
#     # cursor = connection.cursor()
#     # cursor.execute("SELECT * FROM yoga_poses WHERE id = %s", [poses])
#     # result = cursor.fetchall() # all results
#     # return JsonResponse(result, safe=False)
#
# # Logout and remove cookie/token

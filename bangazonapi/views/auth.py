from rest_framework.decorators import api_view
from rest_framework.response import Response
from bangazonapi.models.customer import Customer


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    customer = Customer.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if customer is not None:
        data = {
            'id': customer.id,
            'uid': customer.uid,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'bio': customer.bio,
            'profile_image_url': customer.profile_image_url,
            'email': customer.email,
            'username': customer.username,
            'seller': customer.seller
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Now save the user info in the rareapi_user table
    customer = Customer.objects.create(
        uid=request.data['uid'],
        first_name = request.data["firstName"],
        last_name = request.data["lastName"],
        bio = request.data["bio"],
        profile_image_url = request.data["profileImageUrl"],
        email = request.data["email"],
        username = request.data["userName"],
    )

    # Return the user info to the client
    data = {
            'id': customer.id,
            'uid': customer.uid,
            'first_name': customer.first_name,
            'last_name': customer.last_name,
            'bio': customer.bio,
            'profile_image_url': customer.profile_image_url,
            'email': customer.email,
            'username': customer.username,
            'seller': customer.seller
    }
    return Response(data)

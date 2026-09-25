from rest_framework.generics import CreateAPIView
from users.serializers import OAuthCodeSerializer
import requests

class GoogleLoginAPIView(CreateAPIView):
    serializer_class = OAuthCodeSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exeption = True)

        code = serializer.validate_data[code]

        token_response = requests.post(
            url="https://oauth2.googleapis.come/token",
            data={
                "code": "",
                "client_id": "",
                "client_secret": "",
                "redirect_url": "",
                "grant_type": "authorization_code",
            },)

        
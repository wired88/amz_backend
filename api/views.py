from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import *
from .amz_products import Products

# OpenAI
from openai import OpenAI
from admin.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class ContactAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(
            raise_exception=True)  # check if valid. if not, custom made error will be displayed(see serializer class)
        self.perform_create(serializer)  # create isntance in db
        return JsonResponse({"successUrl": "/", "status": status.HTTP_201_CREATED})


class CreateObjectsAPIView(generics.ListCreateAPIView):
    serializer_class = CreateObjectsSerializer
    queryset = AMZProduct.objects.all()
    product = Products
    single_products = product.television_data

    def create_object(self, p, c):
        a = AMZProduct.objects.create(
            title=p["title"],
            url=p["url"],
            image=p["image"],
            price=p["price"],
            category=c,
            rating=p["rating"],
            total_rating=p["total_rating"],
            description=p["description"]
        )
        print(f"Instance created: {a}...")
        a.save()

    def post(self, request, *args, **kwargs):
        for i in self.single_products[:7]:
            self.create_object(i, self.single_products[7])
        return Response({"response": status.HTTP_201_CREATED})






class ComponentCreateTextRequestView(generics.CreateAPIView):
    serializer_class = TextComponentrequestSerializer

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.role = ('You are a helpful assistant designed to output responses in JSON format. '
                    'Responses should include a key "html", a key "css" for the css code, '
                    'a key "js" for the JavaScript code: If not javascript is needed let the js field blank. '
                     'Please do not include any additional text or '
                    'explanations in the "html", "css" and the "js" key-field.')




    def openai_audio_request(self):
        # just upload a audio file -> mobile able to record
        pass



    def save_image_input(self, image):
        created_image = ImageRequest.objects.create(image=image)
        print("created_image", created_image)
        return created_image.image.url

    def openai_image_request(self, role, url, output_format, text):
        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system",
                 "content": role},

                {"role": "user", "content":
                    [
                        {
                            "type": "text",
                            "text": f'Please create the following component in {output_format} '
                                    f'format that you see in the sendet image. But keep the following changes {text}'
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": url
                            }
                        }
                    ]
                 }
            ]
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content


    def openai_text_request(self, text, output_format, role):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system",
                 "content": role},

                {"role": "user", "content":
                    f'Please create me the following component in {output_format} format. {text}'
                 }
            ]
        )

        print(response.choices[0].message.content)
        return response.choices[0].message.content

    def post(self, request, *arg, **kwargs):
        counter = 0

        input_image = request.data.get("image")
        print("input_image", input_image)

        input_type = request.data.get("inputType")
        print("input_type", input_type)

        user_input = request.data.get("userInput")
        print("user_input", user_input)

        output_format = request.data.get("outputFormat")
        print("output_format", output_format)

        if input_type == "image":
            image = self.save_image_input(input_image)
            response = self.openai_image_request(self.role, image, output_format, user_input)
            return JsonResponse({"response": response})

        elif input_type == "text":
            # create here a endless loop till chatGPT answers in the right format.
            # later include a timer
            response = self.openai_text_request(user_input, output_format, self.role)
            while not response[0] and response[1] and response[2]:
                if counter == 3:
                    return JsonResponse({"error": "Error occurred"})
                if response[0] and response[1] and response[2]:
                    break
                else:
                    response = self.openai_text_request(user_input, output_format, self.role)
                counter += 1
            return JsonResponse({"response": response})
        elif input_type == "audio":
            pass


























"""
 print(f'At least one filed does not exist. '
                      f'\n response.html {response.html} '
                      f'\n response.css {response.css}'
                      f'\n response.js {response.js}')
this is i: Apple iPhone 15 (128GB) - Black
        [list(map(lambda i: self.serializer_class.create_object(i, o[10]["category"]), o[:10])) for o in self.objects]

    def post(self):
        map()
        for o in object_list:
            for i in o[:9]:
                self.serializer_class.create_object(i, o[10]["category"])
        return Response({"success"})

data = request.data
        first_name = data.first_name
        last_name = data.last_name
        email = data.email
        options = data.options
        message = data.message
        contact_data = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            options=options,
            message=message
        )
        contact_data.save()
        """

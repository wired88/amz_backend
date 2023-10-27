from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from .serializers import *
from .amz_products import Products



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



"""
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

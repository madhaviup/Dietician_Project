from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app import settings
import os
import boto3

def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['filename']

        cloudFilename = uploaded_file.name
        session = boto3.session.Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
                                        )

        s3 = session.resource('s3',
                              endpoint_url=settings.AWS_S3_ENDPOINT_URL)
        s3.Bucket(settings.AWS_STORAGE_BUCKET_NAME).put_object(Key=cloudFilename, Body=uploaded_file)

        return redirect('registration.html')

    return render(request, 'registration.html')




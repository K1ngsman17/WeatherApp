1. Download the weatherproject.
2. Open the terminal
3. Go to the directory of weatherapp.
3. Make sure python and django is installed. You can use pip for the same.
4. In the terminal, type 'python manage.py runserver'


To host a website on AWS, we can use a free tier account. It requires a credit or a debit card, which I dont possess. 
Hence I have mentioned the steps below:
1. Log in to aws console.
2. From services, choose s3 bucket.
3. Enter the bucket name such as 'WeatherApp'
4. Choose the region in which you wish to host the application.
5. Click create.
6. Upload all the files into the s3 bucket.
7. Click on next and alter the management properties, if needed.
8. Click Upload.
9. Now go to the bucket and choose Properties> Static Website Hosting.
10. Click on use this bucket to host the website.
11. Enter the required details for the prompts.
12. Make sure that all files are public.
13. Now go to the access point specified while using the bucket for hosting a static website.
14. Click on Object URL and you should see that the website has been hosted.

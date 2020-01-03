# Avalanche Pairing Exercise

The goal of this exercise is to see how you approach open ended engineering problems. I've designed the exercise with lots of possible improvements, but there's no expectation that we complete it all. Our goal is just to get as far as possible.

This is a pairing exercise meaning, I'm here to help! I won't give you the answers, but I will try to keep you on track, and answer any questions you have. This is supposed to emulate real life coding, and in real life, you can look things up on the internet, ask questions, and try a bunch of directions before settling on what works.

# Goals

In two hours we're going to build a small web app that lets a user upload a file and converts that file to black and white. We are not trying to do it efficiently, or even elegantly. We're prioritizing something that works.

![Demo result](readme_images/Demo.gif)

## Phase 1

We'll begin by building a small MVP. The goal is to receive the image on the backend, convert it to black and white within the request, and respond to the client with the black and white image in a json response.

We're using the Pillow library to manipulate the image. For this exercise please use the [PixelAccess Class](https://pillow.readthedocs.io/en/stable/reference/PixelAccess.html) to change each pixel to gray using the [luminosity formula here](https://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/). You'll likely also find the documentation for how to [open images](https://pillow.readthedocs.io/en/4.0.x/reference/Image.html) useful.

## Phase 2

We now want to display the received black and white image on the frontend. Once we've received the json response with the black and white image, we want to display it. You might find this [Stack Overflow](https://stackoverflow.com/questions/8499633/how-to-display-base64-images-in-html) answer useful.

## Phase 3

This works for small images, but with our nieve approach, large images can take a long time to convert. This leaves users confused why nothing is happening on the page, and if the request takes too long, it might timeout. Let's implement the same image conversion in a [Celery](http://docs.celeryproject.org/en/latest/index.html) job.

This requires a number of changes. First, we need to store the image somewhere accessible to both the worker and the server. We'll use (a mocked version of) S3 to do this. Second, we need to store the completed image in S3 as well so that the client can retrieve it. Third, we need to write to the database the location in S3 the file is stored so that we can retrieve it once the job is complete. Finally, we need to create a new polling endpoint that we can use to determine when the image is ready. The endpoint we use to start the job can return the job id which will be used when polling.

Note we already have a fake S3 service running. You can access it by calling `s3_client = s3.get_s3_client()` and using the Boto3 library. See the docs for how to [put objects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.put_object) and [get objects](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.get_object). We also have the job runner already running.

## Phase 4

We want to give users feedback on how the image processing job is going. To do this we can use the [message passing interface](https://buildwithdjango.com/blog/post/celery-progress-bars/) provided by Celery. This allows us to provide percent completed information to the client as it polls. We can use this to create a basic progress bar on the frontend that shows users how much of the conversion has been completed.

# Setup

We've dockerized this exercise to make setup as painless as possible. Make sure you have [docker](https://docs.docker.com/get-started/#install-docker-desktop)
and [docker-compose](https://docs.docker.com/compose/install/) installed, AND updated to the most recent version. If you get an error, make sure docker is running before you use these commands. ([Docker Desktop](https://hub.docker.com/editions/community/docker-ce-desktop-mac) is an easy way to do this.)

Now, clone this repository and in the root directory run `docker-compose build` and then
`docker-compose up`. Building might take a few minutes as it gathers all the needed dependencies. The first time you launch the containers it will also take some time to download all the JS packages.
Once up, you'll need to run: `docker-compose run web python manage.py migrate`
Then you can access the app at `localhost:3000`. The webpack bundle is served from a development server meaning building the frontend should be fast, and hot module reloading is on, so you shouldn't even need to refresh the app to see the updates.

To stop the containers, type `ctrl + c`

# Resources

[React quick start guide](https://reactjs.org/docs/hello-world.html)

[Django tutorial](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)

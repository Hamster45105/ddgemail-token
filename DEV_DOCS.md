# Developer Docs

Are you building an app which requires users to input a DuckDuckGo email API Key? DDG Email API Key Grabber makes it easier for you to get the key!

In simple terms:

Just redirect users to: `https://ddgemail-token.vercel.app?callback=CALLBACK_URL&app_name=APP_NAME`

Here, users will be prompted to follow the correct steps to get their API key, which will then be passed on to you.

Here is an example that you can try out: 

https://ddgemail-token.vercel.app?callback=https%3A%2F%2Fexample.com%2Fimport_key%3D__API_KEY__&app_name=My%20App

## Parameters

### Callback URL

The callback URL should be a valid URL where the site can input the key. Just put `__API_KEY__` where you want the API key to be inserted. For example:

`https://example.com/import_key=__API_KEY__` which is, when encoded: `https%3A%2F%2Fexample.com%2Fimport_key%3D__API_KEY__`

It is important that you encode the callback URL. A site like [URL Encode Online](https://www.urlencoder.io/) should do the trick. URL encoding is necessary to ensure that any parameters in the callback URL will not be misinterpreted as parameters of the main URL, which could cause errors

If the URL is invalid, an error message will be displayed and both the app name and callback will be removed from the parameters.

### App Name
The app name is optional, however if specified, when the user is required to get the key the button will display `Continue to: *App Name*` instead of `Get Key -->`. It will also be displayed on the third party app warning popup instead of `an unnamed app`.

Also: make sure if the app name has spaces these are replaced with `%20`, for example `My%20App`

## What does a user's API key allow me to do?

A user's API key allows you to generate private duck addresses on their behalf.

## How do I generate private duck addresses on a user's behalf?

Send a POST request to `https://quack.duckduckgo.com/api/email/addresses``

With these headers:

`Authorization`: `Bearer {api_key}`,

`Content-Type`: `application/json`

**NOTE:** This is a reverse engineered API, not officially supported by DuckDuckGo for third-party applications.

## Can users re-generate their API key?

No. Unless they create a new account, of course.
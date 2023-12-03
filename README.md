# DDG Email API Key Retriever
[![GitHub Watchers](https://img.shields.io/github/watchers/Hamster45105/ddgemail-token?style=social)](https://github.com/Hamster45105/ddgemail-token/watchers)
[![GitHub Stars](https://img.shields.io/github/stars/Hamster45105/ddgemail-token?style=social)](https://github.com/Hamster45105/ddgemail-token/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Hamster45105/ddgemail-token?style=social)](https://github.com/Hamster45105/ddgemail-token/forks)


[![Reported Bugs](https://img.shields.io/github/issues/Hamster45105/ddgemail-token/bug?label=Reported%20Bugs&style=flat&color=cc4453)](https://github.com/Hamster45105/ddgemail-token/issues?q=is%3Aopen+is%3Aissue+label%3Abug)
[![Current License](https://img.shields.io/github/license/Hamster45105/ddgemail-token?label=License&style=flat)](https://github.com/Hamster45105/ddgemail-token/blob/main/LICENSE)
![Deployment Status](https://img.shields.io/github/deployments/Hamster45105/ddgemail-token/Production?logo=vercel&label=Deployment)

This is a web application that will retrieve your DDG (DuckDuckGo) email API key. It's built with HTML, CSS, and JavaScript, and deployed with Vercel.

Your API key is needed for Bitwarden, [Send From Duck](https://hamster45105.github.io/DuckAddressSend/) etc...

Because DuckDuckGo does not officially support using third-party services with their email service, it is hard to get the API key unless you know how to use developer tools. This site is designed to make it easier.

## Usage

1. Enter your username, complete the captcha and click "Next".
2. Wait for an email to arrive from DuckDuckGo
3. Enter the OTP from the email (it will be four random words) and click "Get Token". Note: You can't click the link, it won't work.
4. Your API key will be displayed on the screen.

Note: Don't spam getting a token for the same user because the DuckDuckGo service will block you and you won't be able to make any more requests for a while.

If you can't get the key because an error occured, open an issue.

## Third Party Services
To prevent spam and bots, the website uses Google's reCatpcha. Here are their [terms of service](https://policies.google.com/terms) and [privacy policy](https://policies.google.com/privacy).

It also uses Vercel's web analytics. You can find out more about how this works [here](https://vercel.com/docs/analytics)

No data is stored by the server, you can check the source code to see.

## Deployment

This project is deployed with Vercel. To host your own version on Vercel, click the button below.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FHamster45105%2Fddgemail-token&env=RECAPTCHA_SECRET_KEY&envDescription=reCaptcha%20secret%20key%20required%20to%20verify%20requests&envLink=https%3A%2F%2Fwww.google.com%2Frecaptcha%2Fadmin%2Fcreate&project-name=ddgemail-token&repository-name=ddgemail-token)

## License

This project is licensed under the GNU General Public License v3.0.

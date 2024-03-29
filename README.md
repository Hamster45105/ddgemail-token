# DDG Email API Key Grabber
[![GitHub Watchers](https://img.shields.io/github/watchers/Hamster45105/ddgemail-token?style=social)](https://github.com/Hamster45105/ddgemail-token/watchers)
[![GitHub Stars](https://img.shields.io/github/stars/Hamster45105/ddgemail-token?style=social)](https://github.com/Hamster45105/ddgemail-token/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/Hamster45105/ddgemail-token?style=social)](https://github.com/Hamster45105/ddgemail-token/forks)


[![Reported Bugs](https://img.shields.io/github/issues/Hamster45105/ddgemail-token/bug?label=Reported%20Bugs&style=flat&color=cc4453)](https://github.com/Hamster45105/ddgemail-token/issues?q=is%3Aopen+is%3Aissue+label%3Abug)
[![Current License](https://img.shields.io/github/license/Hamster45105/ddgemail-token?label=License&style=flat)](https://github.com/Hamster45105/ddgemail-token/blob/main/LICENSE)
[![Deployment Status](https://img.shields.io/github/deployments/Hamster45105/ddgemail-token/Production?logo=vercel&label=Deployment)](https://github.com/Hamster45105/ddgemail-token/deployments/Production)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fddgemail-token.vercel.app%2F&label=Website%20Status)](https://isitup.org/ddgemail-token.vercel.app)
[![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/t/Hamster45105/ddgemail-token?label=Commits)](https://github.com/Hamster45105/ddgemail-token/graphs/commit-activity)
[![GitHub last commit (branch)](https://img.shields.io/github/last-commit/Hamster45105/ddgemail-token/main?label=Last%20Commit%20(main))](https://github.com/Hamster45105/ddgemail-token/commits/main)

This is a web application that will retrieve your DDG (DuckDuckGo) email API key. It's built with HTML, CSS, and JavaScript, and deployed with Vercel.

Your API key is needed for Bitwarden, [Send From Duck](https://hamster45105.github.io/DuckAddressSend/) and others.

Because DuckDuckGo does not officially support using third-party services with their email service, it is hard to get the API key unless you know how to use developer tools. This site is designed to make it easier.

If for whatever reason you don't want to use this site for getting your key, you can find other more difficult ways to get your key [on this wiki](https://github.com/Hamster45105/DuckAddressSend/wiki/Get-DDG-API-Key). If your worried about security/privacy check out the [third party services statement](https://github.com/Hamster45105/ddgemail-token#third-party-services).

## Usage

The website has instructions to help you through the process.

Note: Don't spam getting a token for the same user because the DuckDuckGo service will block you and you won't be able to make any more requests for a while.

If you can't get the key because an error occured, open an issue.

## Integrate YOUR service
Are you building an app which requires users to input a DuckDuckGo email API Key? DDG Email API Key Grabber makes it easier for you to get the key!

Visit the [developer docs](https://github.com/Hamster45105/ddgemail-token/blob/main/DEV_DOCS.md) for more info


## Third Party Services
To prevent spam and bots, the website uses [hCatpcha](https://www.hcaptcha.com/what-is-hcaptcha-about) (a more privacy friendly alternative to reCaptcha). Here are their [terms of service](https://hcaptcha.com/terms) and [privacy policy](https://hcaptcha.com/privacy).

hCaptcha aims to ensure seamless access for all users while maintaining security. For this reason they offer accessibility options for those users that are unable to complete visual challenges. You can learn more about how this works and how to sign up [at their website](https://www.hcaptcha.com/accessibility).

For translations, the site uses the Google Translate widget.

As the site uses Vercel, it can (and does) use Vercel's web analytics. You can find out more about how this works [here](https://vercel.com/docs/analytics).

No data is stored by the server and no one can read your personal duck address or API keys because the site connects to DuckDuckGo's servers directly and no data is stored. If your unsure you can check the source code or host your own version.

## Deployment

This project is deployed with Vercel. To host your own version on Vercel, click the button below.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FHamster45105%2Fddgemail-token%2F&env=HCAPTCHA_SECRET_KEY&envDescription=Create%20a%20hCaptcha%20secret%20key%20to%20protect%20your%20site%20from%20bots.&envLink=https%3A%2F%2Fdashboard.hcaptcha.com%2Fsites%2Fnew&project-name=ddgemail-grabber&repository-name=ddgemail-grabber)

## License

This project is licensed under the GNU General Public License v3.0.

See [LICENSE](https://github.com/Hamster45105/ddgemail-token/blob/main/LICENSE) file for details.


![GPLV3 Logo](https://www.gnu.org/graphics/gplv3-127x51.png)

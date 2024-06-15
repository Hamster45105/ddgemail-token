const axios = require('axios');
require('dotenv').config();
const qs = require('qs');

module.exports = async (req, res) => {
  if (!req.body || !req.body.username || !req.body.hcaptchaResponse) {
    return res.status(400).send({ error: 'Please enter username and complete captcha' });
  }

  const username = req.body.username;
  const hcaptchaResponse = req.body.hcaptchaResponse;

  const data = qs.stringify({
    'response': hcaptchaResponse,
    'secret': process.env.HCAPTCHA_SECRET_KEY,
  });

  const config = {
    method: 'post',
    url: 'https://api.hcaptcha.com/siteverify',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    data: data
  };

  const hcaptchaVerifyResponse = await axios(config);
  if (!hcaptchaVerifyResponse.data.success) {
    return res.status(400).send({ error: 'hCaptcha verification failed. Error code: ' + hcaptchaVerifyResponse.data['error-codes'] });
  }

  try {
    await axios.get(`https://quack.duckduckgo.com/api/auth/loginlink?user=${username}`, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0'
      }
    });
  } catch (error) {
    return res.status(500).send({ error: 'An error occurred, please try again later' });
  }
  res.status(200).send({ message: 'Email sent' });
};
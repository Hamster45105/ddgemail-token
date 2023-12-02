const axios = require('axios');
require('dotenv').config();

module.exports = async (req, res) => {
  if (!req.body || !req.body.username || !req.body.recaptchaResponse) {
    return res.status(400).send({ error: 'Please enter username and complete captcha' });
  }

  const username = req.body.username;
  const recaptchaResponse = req.body.recaptchaResponse;

  const recaptchaVerifyResponse = await axios.post(`https://www.google.com/recaptcha/api/siteverify?secret=${process.env.RECAPTCHA_SECRET_KEY}&response=${recaptchaResponse}`);
  if (!recaptchaVerifyResponse.data.success) {
    return res.status(400).send({ error: 'reCAPTCHA verification failed' });
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
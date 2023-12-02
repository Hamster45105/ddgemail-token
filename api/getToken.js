const axios = require('axios');

module.exports = async (req, res) => {
  try {
    if (!req.body || !req.body.username || !req.body.otp) {
      return res.status(400).send({ error: 'An OTP is required' });
    }

    const username = req.body.username;
    const otp = req.body.otp.replace(/ /g, '+');

    const loginResponse = await axios.get(`https://quack.duckduckgo.com/api/auth/login?otp=${otp}&user=${username}`, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0'
      }
    });

    const token = loginResponse.data.token;

    res.status(200).send({ token: token });
  } catch (error) {
    if (error.response && error.response.data && error.response.data.error === 'invalid_login_credentials') {
      return res.status(400).send({ error: 'Invalid login credentials' });
    }
    res.status(500).send({ error: 'Internal Server Error' });
  }
};
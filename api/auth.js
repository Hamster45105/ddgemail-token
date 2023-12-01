const axios = require('axios');

module.exports = async (req, res) => {
  if (!req.body || !req.body.username) {
    return res.status(400).send({ error: 'username is required' });
  }

  const username = req.body.username;

  await axios.get(`https://quack.duckduckgo.com/api/auth/loginlink?user=${username}`, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0'
    }
  });

  res.status(200).send({ message: 'Email sent' });
};
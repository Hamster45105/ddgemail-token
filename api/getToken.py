import json
import requests
from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Read request body
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            body = json.loads(post_data.decode('utf-8'))
            
            # Validate required fields
            if not body or 'username' not in body or 'otp' not in body:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'error': 'An OTP is required'
                }).encode())
                return
            
            username = body['username']
            otp = body['otp'].replace(' ', '+')
            
            # Get login token using OTP
            login_response = requests.get(
                f'https://quack.duckduckgo.com/api/auth/login?otp={otp}&user={username}',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0'
                },
                timeout=10
            )
            login_response.raise_for_status()
            login_data = login_response.json()
            
            ot_token = login_data['token']
            
            # Get access token using the login token
            token_response = requests.get(
                'https://quack.duckduckgo.com/api/email/dashboard',
                headers={
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0',
                    'Authorization': f'Bearer {ot_token}'
                },
                timeout=10
            )
            token_response.raise_for_status()
            token_data = token_response.json()
            
            access_token = token_data['user']['access_token']
            
            # Success response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'token': access_token
            }).encode())
            
        except requests.HTTPError as e:
            if e.response and e.response.status_code == 400:
                try:
                    error_data = e.response.json()
                    if error_data.get('error') == 'invalid_login_credentials':
                        self.send_response(400)
                        self.send_header('Content-Type', 'application/json')
                        self.end_headers()
                        self.wfile.write(json.dumps({
                            'error': 'Invalid login credentials'
                        }).encode())
                        return
                except (json.JSONDecodeError, KeyError):
                    pass
            
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': 'Internal Server Error'
            }).encode())
            
        except (json.JSONDecodeError, requests.RequestException, KeyError):
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'error': 'Internal Server Error'
            }).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

import json
import os
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
            if not body or 'username' not in body or 'hcaptchaResponse' not in body:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'error': 'Please enter username and complete captcha'
                }).encode())
                return
            
            username = body['username']
            hcaptcha_response = body['hcaptchaResponse']
            
            # Verify hCaptcha
            hcaptcha_data = {
                'response': hcaptcha_response,
                'secret': os.environ.get('HCAPTCHA_SECRET_KEY')
            }
            
            hcaptcha_verify_response = requests.post(
                'https://api.hcaptcha.com/siteverify',
                data=hcaptcha_data,
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
                timeout=10
            )
            
            hcaptcha_result = hcaptcha_verify_response.json()
            if not hcaptcha_result.get('success'):
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                error_codes = hcaptcha_result.get('error-codes', [])
                self.wfile.write(json.dumps({
                    'error': f'hCaptcha verification failed. Error code: {error_codes}'
                }).encode())
                return
            
            # Send login link request
            try:
                login_link_response = requests.get(
                    f'https://quack.duckduckgo.com/api/auth/loginlink?user={username}',
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0'
                    },
                    timeout=10
                )
                login_link_response.raise_for_status()
            except requests.RequestException:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    'error': 'An error occurred, please try again later'
                }).encode())
                return
            
            # Success response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'message': 'Email sent'
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

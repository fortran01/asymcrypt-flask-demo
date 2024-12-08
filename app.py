from flask import Flask, render_template, request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

app = Flask(__name__)

# Generate RSA key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_public_key')
def get_public_key():
    public_pem = public_key.export_key().decode()
    return jsonify({'public_key': public_pem})

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        data = request.json.get('data')
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        # Convert string to bytes
        data_bytes = data.encode()
        
        # Create cipher object and encrypt the data
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(data_bytes)
        
        # Convert to base64 for JSON transport
        encrypted_base64 = base64.b64encode(encrypted_data).decode()
        
        return jsonify({'encrypted_data': encrypted_base64})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        encrypted_data = request.json.get('encrypted_data')
        if not encrypted_data:
            return jsonify({'error': 'No encrypted data provided'}), 400

        # Convert from base64 and decrypt
        encrypted_bytes = base64.b64decode(encrypted_data)
        cipher = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher.decrypt(encrypted_bytes)
        
        return jsonify({'decrypted_data': decrypted_data.decode()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/sign', methods=['POST'])
def sign():
    try:
        message = request.json.get('message')
        if not message:
            return jsonify({'error': 'No message provided'}), 400

        # Create the hash object
        h = SHA256.new(message.encode())
        
        # Sign the hash
        signature = pkcs1_15.new(private_key).sign(h)
        
        # Convert to base64 for JSON transport
        signature_base64 = base64.b64encode(signature).decode()
        
        return jsonify({'signature': signature_base64})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/verify', methods=['POST'])
def verify():
    try:
        message = request.json.get('message')
        signature = request.json.get('signature')
        
        if not message or not signature:
            return jsonify({'error': 'Message and signature are required'}), 400

        # Convert from base64
        signature_bytes = base64.b64decode(signature)
        
        # Create the hash object
        h = SHA256.new(message.encode())
        
        # Verify the signature
        try:
            pkcs1_15.new(public_key).verify(h, signature_bytes)
            return jsonify({'verified': True})
        except (ValueError, TypeError):
            return jsonify({'verified': False})
            
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

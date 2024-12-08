# RSA Cryptography Flask Demo

This Flask application demonstrates RSA cryptographic operations including key generation, encryption/decryption, and digital signatures.

## Features

- RSA key pair generation
- Data encryption using public key
- Data decryption using private key
- Digital signature creation
- Signature verification
- Modern web interface for all operations

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

- Create a virtual environment:

```bash
python -m venv venv
```

- Activate the virtual environment:

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
.\venv\Scripts\activate
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

- Make sure your virtual environment is activated

- Start the Flask server:

```bash
python -m flask run
```

- Open your web browser and navigate to: http://127.0.0.1:5000

## Using the Application

1. **View Public Key**
   - Click "Show Public Key" to display the RSA public key in PEM format

2. **Encrypt Data**
   - Enter text in the "Data to Encrypt" field
   - Click "Encrypt" to get the encrypted data in base64 format

3. **Decrypt Data**
   - Paste encrypted data (base64 format) into the "Encrypted Data" field
   - Click "Decrypt" to recover the original text

4. **Sign Message**
   - Enter a message in the "Message to Sign" field
   - Click "Sign" to generate a digital signature

5. **Verify Signature**
   - Enter the original message and its signature
   - Click "Verify" to check if the signature is valid

## Security Note

This is a demonstration application. In a production environment, you should:

- Implement proper key management
- Use secure key storage
- Add user authentication
- Implement session management
- Add additional security headers
- Use HTTPS

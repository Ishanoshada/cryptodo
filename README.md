# Cryptodo

Cryptodo is a Python library for text encryption and decryption. It provides various encryption methods such as Caesar cipher, substitution cipher, rail fence cipher, and more. This library is designed to be easy to use and can be integrated into your Python projects for secure data handling.

## Installation

You can install Cryptodo using pip:

```bash
pip install cryptodo
```

## Usage

### Crypto Class

The `Crypto` class provides methods for basic text encryption and decryption.

```python
from cryptodo import Crypto

# Encryption
cipher = Crypto("Hello World!", 3)
encrypted_text = cipher.encrypt()  # Returns encrypted text

# Decryption
decipher = Crypto(encrypted_text, 3)
decrypted_text = decipher.decrypt()  # Returns decrypted text
```

### KeyGenerator Class

The `KeyGenerator` class offers methods to generate cryptographic keys.

```python
from cryptodo import KeyGenerator

# Generate a key (Example)
key = KeyGenerator.key_generator_num_v1(1, 10)  # Returns a random key
```

### CryptoV2 Class

The `CryptoV2` class introduces more advanced encryption techniques.

```python
from cryptodo import CryptoV2

# Encryption
cipher = CryptoV2("Hello World!", "key")
encrypted_text = cipher.encrypt()  # Returns encrypted text

# Decryption
decipher = CryptoV2(encrypted_text, "key")
decrypted_text = decipher.decrypt()  # Returns decrypted text
```

### CryptoV3Num Class

The `CryptoV3Num` class specializes in numeric encryption and decryption.

```python
from cryptodo import CryptoV3Num

# Encryption
cipher = CryptoV3Num(123456, 5)
encrypted_number = cipher.encrypt()  # Returns encrypted number

# Decryption
decipher = CryptoV3Num(encrypted_number, 5)
decrypted_number = decipher.decrypt()  # Returns decrypted number
```

### KeyVariable Class

The `KeyVariable` class provides predefined character sets for key generation.

```python
from cryptodo import KeyVariable

all_characters = KeyVariable.key_var_all  # Contains all alphanumeric and special characters
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

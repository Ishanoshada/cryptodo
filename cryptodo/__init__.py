import string
import random

class Crypto:
    def __init__(self, text, key):
        self.text = text
        self.key = key

    def encrypt(self):
        # Caesar cipher encryption
        shift = self.key  # Key determines the shift value
        key_range = 10  # Range of possible shift values
        plain_text = self.text
        shift %= key_range  # Ensure shift is within key_range
        alphabet = string.ascii_lowercase
        shifted = alphabet[shift:] + alphabet[:shift]  # Create shifted alphabet
        table = str.maketrans(alphabet, shifted)  # Create translation table
        encrypted = plain_text.translate(table)  # Apply encryption
        return '/V1_CRYPTO ' + encrypted  # Return encrypted text with identifier

    def decrypt(self):
        shift = self.key
        key_range = 10
        plain_text = self.text
        shift = key_range - shift  # Calculate reverse shift for decryption
        shift %= key_range
        if '/V1_CRYPTO ' in plain_text:
            alphabet = string.ascii_lowercase
            shifted = alphabet[shift:] + alphabet[:shift]
            table = str.maketrans(alphabet, shifted)
            decrypted = plain_text.translate(table)
            decrypted = decrypted.replace('/V1_CRYPTO ', '')  # Remove identifier
            return decrypted
        else:
            return 'Padding error! /V1_CRYPTO not found in the text'

    def substitution_encrypt(self):
        # Substitution cipher encryption
        key = list(KeyVariable.key_var_all)  # Get a shuffled key
        random.shuffle(key)
        table = str.maketrans(string.ascii_letters + string.digits + string.punctuation, ''.join(key))
        encrypted = self.text.translate(table)
        return '/SUBSTITUTION_CRYPTO ' + encrypted  # Return encrypted text with identifier

    def substitution_decrypt(self):
        key = list(KeyVariable.key_var_all)
        random.shuffle(key)
        table = str.maketrans(''.join(key), string.ascii_letters + string.digits + string.punctuation)
        decrypted = self.text.translate(table)
        decrypted = decrypted.replace('/SUBSTITUTION_CRYPTO ', '')  # Remove identifier
        return decrypted


class KeyGenerator:
    @staticmethod
    def key_generator_num_v1(min_val, max_val):
        key = random.randint(min_val, max_val)  # Generate a random key within specified range
        return key + 8

    @staticmethod
    def key_generator_num_v1_1(string_lowercase, key):
        out = int(string_lowercase, base=key)  # Convert string to integer using key as base
        return out

    @staticmethod
    def key_generator_num_v2(size, chars=string.ascii_letters + string.digits + '@#£_.&-+()/*:;!? \n\n~`|•√π÷×¶∆€¥$¢^°={}"%()©®™+✓[]<>'):
        return ''.join(random.choice(chars) for _ in range(size))  # Generate random string of specified size


class CryptoV2:
    def __init__(self, string, key):
        self.string = string
        self.key = key

    def encrypt(self):
        keys = self.key
        value = keys[-1] + keys[:-1]  # Perform a simple substitution based on key
        encrypt = dict(zip(keys, value))
        string = self.string
        encrypt_new = ''.join([encrypt[letter] for letter in string.lower()])
        return '/V2_CRYPTO ' + encrypt_new  # Return encrypted text with identifier

    def decrypt(self):
        keys = self.key
        string = self.string
        if '/V2_CRYPTO ' in string:
            value = keys[-1] + keys[:-1]
            decrypt = dict(zip(value, keys))
            decrypt_new = ''.join([decrypt[letter] for letter in string.lower()])
            decrypt_new = decrypt_new.replace('/V2_CRYPTO ', '')  # Remove identifier
            return decrypt_new
        else:
            return 'Padding error! /V2_CRYPTO not found in the text'

    def caesar_variation_encrypt(self):
        shift = self.key
        plain_text = self.string
        encrypted = ''.join(chr((ord(char) + shift) % 256) for char in plain_text)  # Perform variation of Caesar cipher
        return '/CAESAR_VARIATION_CRYPTO ' + encrypted  # Return encrypted text with identifier

    def caesar_variation_decrypt(self):
        shift = self.key
        cipher_text = self.string
        decrypted = ''.join(chr((ord(char) - shift) % 256) for char in cipher_text)  # Reverse variation of Caesar cipher
        decrypted = decrypted.replace('/CAESAR_VARIATION_CRYPTO ', '')  # Remove identifier
        return decrypted


class CryptoV3Num:
    def __init__(self, number, key):
        self.number = number
        self.key = key

    def encrypt(self):
        shift = self.key
        plain_text = str(self.number)
        encrypted = ''.join(chr((ord(char) + shift) % 10 + ord('0')) for char in plain_text)  # Encrypt numeric value
        return '/V3_NUM_CRYPTO ' + encrypted  # Return encrypted number with identifier

    def decrypt(self):
        shift = self.key
        cipher_text = str(self.number)
        decrypted = ''.join(chr((ord(char) - shift) % 10 + ord('0')) for char in cipher_text)  # Decrypt numeric value
        decrypted = decrypted.replace('/V3_NUM_CRYPTO ', '')  # Remove identifier
        return decrypted

    def rail_fence_encrypt(self):
        rails = self.key
        text = str(self.number)

        def encrypt(text, rails):
            # Perform Rail Fence encryption
            rail_dict = {i: [] for i in range(rails)}
            rail = 0
            direction = 1

            for char in text:
                rail_dict[rail].append(char)
                rail += direction

                if rail == rails - 1 or rail == 0:
                    direction = -direction

            encrypted = ''
            for i in range(rails):
                encrypted += ''.join(rail_dict[i])
            return encrypted

        encrypted = encrypt(text, rails)
        return '/RAIL_FENCE_CRYPTO ' + encrypted  # Return encrypted text with identifier

    def rail_fence_decrypt(self):
        rails = self.key
        text = self.number

        def decrypt(text, rails):
            # Reverse Rail Fence encryption
            rail_dict = {i: [] for i in range(rails)}
            rail = 0
            direction = 1

            for i in range(len(text)):
                rail_dict[rail].append(None)
                rail += direction

                if rail == rails - 1 or rail == 0:
                    direction = -direction

            index = 0
            for i in range(rails):
                for j in range(len(rail_dict[i])):
                    rail_dict[i][j] = text[index]
                    index += 1

            rail = 0
            direction = 1
            decrypted = ''
            for i in range(len(text)):
                decrypted += rail_dict[rail].pop(0)
                rail += direction

                if rail == rails - 1 or rail == 0:
                    direction = -direction

            return decrypted

        text = text.replace('/RAIL_FENCE_CRYPTO ', '')
        decrypted = decrypt(text, rails)
        return decrypted


class KeyVariable:
    key_var_all = string.ascii_letters + string.digits + '@#£_.&-+()/*:;!? \n\n~`|•√π÷×¶∆€¥$¢^°={}"%()©®™+✓[]<>'  # All possible characters
    key_var_alp_number = string.ascii_letters + string.digits  # Alphabets and numbers
    key_var_number = string.digits  # Only numbers
    key_var_sim = '@#£_"&-+()/*:;!?~`|•√π÷×¶∆€¥$¢^°={}"%©®™✓[]<>' + " '"  # Special characters and some common symbols
    key_var_more = 'àáâäæãåāqwêéèëērtyūüúûùìīïíîõōøœòöôópßdfghjklzxçvbñmqwertyuioplkjhgfdsazxcvbnm1234567890රු'  # Extended character set
      

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encoded = ""
        for char in longUrl:
            encoded += chr(ord(char)+12)
        return encoded

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        decoded = ""
        for char in shortUrl:
            decoded += chr(ord(char)-12)
        return decoded

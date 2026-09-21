# Q8. Create an abstract class Authentication with an abstract method authenticate(). Implement the method using Password authentication, OTP authentication, and Biometric authentication. Demonstrate abstraction by interacting with objects through the abstract interface.

from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass

class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authentication using Password")

class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authentication using OTP")

class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authentication using Biometric")

password = PasswordAuthentication()
otp = OTPAuthentication()
biometric = BiometricAuthentication()

authentications = [password, otp, biometric]

for authentication in authentications:
    authentication.authenticate()
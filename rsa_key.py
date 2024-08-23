from Crypto.PublicKey import RSA

key64 = open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r')

k = RSA.importKey(key64.read())



pub_key_der = open('2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der', 'rb').read()

pub_key = RSA.importKey(pub_key_der)


k = RSA.importKey(open('bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub', 'r').read())

print(k.n)
from Crypto.Cipher import AES
import os
from dotenv import load_dotenv

# 📥 โหลดค่า Environment Variables จาก .env
load_dotenv()


# # 🗝 กำหนด Key และ IV (ควรใช้ Secure Storage แทน Hardcoded)
# SECRET_KEY = b"phetisaverysecretkey123456789101"  # 32-byte Key
# IV = b"phetisasecretiv1"  # 16-byte 

# 🗝 ดึงค่า Key และ IV จาก Environment Variables
SECRET_KEY = os.getenv("SECRET_KEY").encode()  # แปลงเป็น bytes
IV = os.getenv("IV").encode()  # แปลงเป็น bytes

# ✅ ฟังก์ชันเข้ารหัสไฟล์รูป (Encryption)
def encrypt_image(input_file, output_file):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)

    with open(input_file, "rb") as f:
        file_data = f.read()

    # 🔹 Padding ให้ครบ 16-byte
    padding = 16 - (len(file_data) % 16)
    file_data += bytes([padding]) * padding

    encrypted_data = cipher.encrypt(file_data)

    with open(output_file, "wb") as f:
        f.write(encrypted_data)

    print(f"🔐 รูปภาพถูกเข้ารหัสแล้ว: {output_file}")

# 🔓 ฟังก์ชันถอดรหัสไฟล์รูป (Decryption)
def decrypt_image(input_file, output_file):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, IV)

    with open(input_file, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    # 🔹 ลบ Padding ที่เติมไว้
    padding = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding]

    with open(output_file, "wb") as f:
        f.write(decrypted_data)

    print(f"🔓 รูปภาพถูกถอดรหัสแล้ว: {output_file}")

# 🔥 ทดสอบการเข้ารหัสและถอดรหัส
if __name__ == "__main__":
    input_file = "phet.jpg"  # ไฟล์รูปภาพต้นฉบับ
    encrypted_file = "phet_encrypted.bin"  # ไฟล์ที่ถูกเข้ารหัส
    decrypted_file = "phet_decrypted.jpg"  # ไฟล์รูปที่ถอดรหัสกลับมา

    encrypt_image(input_file, encrypted_file)
    decrypt_image(encrypted_file, decrypted_file)
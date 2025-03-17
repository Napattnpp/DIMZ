from Module.bb64u8 import BB64U8

bb64u8 = BB64U8()

bb64u8.encode(".jpg")
bb64u8.saveTextImg("...2B64U8/Output/encode.txt", bb64u8.base64_img)

print("UTF-8")
print(bb64u8.utf8_img)

bb64u8.decode("...2B64U8/Output/decode_img.png", bb64u8.base64_img)

from deepface import DeepFace 

ogrenci_listesi = ["Ali1234.jpg","Linus01.jpg","elon1.jpg"]

kamera_fotolar = ["OzAbim2.jpg","3.jpg","elon2.jpg"]

varOlan = []
for foto in kamera_fotolar:
  for i in range(len(ogrenci_listesi)-1):
    rst = DeepFace.verify(img1_path = foto, img2_path = ogrenci_listesi[i])
    vrf = rst["verified"]
    if vrf == True:
      varOlan.append(ogrenci_listesi[i])
    print(varOlan)

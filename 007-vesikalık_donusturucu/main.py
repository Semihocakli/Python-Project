import cv2

def vesikalik_boyutlandir(foto_path):
    # Fotoğrafı oku
    foto = cv2.imread(foto_path)

    # Vesikalık boyutları
    vesikalik_genislik = 240  # cm cinsinden
    vesikalik_yukseklik = 320  # cm cinsinden

    # Fotoğrafın orijinal boyutları
    orijinal_genislik = foto.shape[1]
    orijinal_yukseklik = foto.shape[0]

    # Vesikalık boyutlarına orantılı olarak yeniden boyutlandırma
    oran = max(vesikalik_genislik / orijinal_genislik, vesikalik_yukseklik / orijinal_yukseklik)
    yeni_genislik = int(orijinal_genislik * oran)
    yeni_yukseklik = int(orijinal_yukseklik * oran)
    yeniden_boyutlandirilmis = cv2.resize(foto, (yeni_genislik, yeni_yukseklik))

    # Vesikalık boyutunda kırpma
    sol_bosluk = int((yeni_genislik - vesikalik_genislik) / 2)
    ust_bosluk = int((yeni_yukseklik - vesikalik_yukseklik) / 2)
    vesikalik_foto = yeniden_boyutlandirilmis[ust_bosluk:ust_bosluk+int(vesikalik_yukseklik),
                                              sol_bosluk:sol_bosluk+int(vesikalik_genislik)]

    return vesikalik_foto

# Kullanım örneği
foto_yolu = "C:\\Users\\Semih\\PycharmProjects\\fotodonusturme\\images\\IMG_4089.JPG"  # Dönüştürmek istediğiniz fotoğrafın yolunu buraya girin
vesikalik_foto = vesikalik_boyutlandir(foto_yolu)
cv2.imwrite("vesikalik_foto.jpg", vesikalik_foto)

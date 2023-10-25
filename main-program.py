"""
import cv2

# Inisialisasi kamera
cap = cv2.VideoCapture(0)  # Nomor 0 mengacu pada kamera utama, Anda bisa mengubahnya jika memiliki kamera tambahan.

while True:
    ret, frame = cap.read()  # Membaca frame dari kamera

    if not ret:
        print("Gagal mengambil frame dari kamera.")
        break

    cv2.imshow("Camera Feed", frame)  # Menampilkan feed kamera

    key = cv2.waitKey(1)
    if key == 27:  # Tekan tombol 'Esc' (kode ASCII 27) untuk keluar
        break
    elif key == 32:  # Tekan tombol 'Space' (kode ASCII 32) untuk mengambil gambar
        filename = "captured_image.jpg"
        cv2.imwrite(filename, frame)
        print(f"Gambar disimpan sebagai {filename}")

# Setelah selesai, lepaskan kamera dan tutup jendela tampilan
cap.release()
cv2.destroyAllWindows()
"""

import cv2

# Membuat objek CascadeClassifier untuk wajah dan hidung
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
noseCascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
face_mask = cv2.CascadeClassifier('face_mask.xml')

cap = cv2.VideoCapture(0)
mask_on = False

while True:
    ret, frame = cap.read()

    if not ret:
        print("Gagal mengambil frame dari kamera")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    wajah = faceCascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in wajah:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        if mask_on:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
            cv2.putText(frame, 'Mask On', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
            cv2.putText(frame, 'Mask Off', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    hidung = noseCascade.detectMultiScale(gray, 1.18, 35)
    for (ax, ay, aw, ah) in hidung:
        cv2.rectangle(frame, (ax, ay), (ax + aw, ay + ah), (255, 0, 0), 1)
        cv2.putText(frame, 'Hidung', (ax, ay), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

    masker = face_mask.detectMultiScale(gray, 1.1, 4)
    for (bx, by, bw, bh) in masker:
        cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (255, 0, 0), 1)
        cv2.putText(frame, 'Masker', (bx, by), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1)

    if len(wajah) > 0 and len(hidung) == 0:
        mask_on = True
    elif len(hidung) == 0:
        mask_on = True
    else:
        mask_on = False

    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


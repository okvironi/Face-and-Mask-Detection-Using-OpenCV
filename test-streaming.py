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
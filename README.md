# Lilith Project 🌌

> ⚠️ **Status:** Proyek ini masih dalam tahap pengembangan aktif (*Work in Progress*). Fitur, arsitektur, dan stabilitas masih akan terus disempurnakan.

Lilith adalah sistem agen kecerdasan buatan (AI) berbasis arsitektur modular yang dirancang untuk merespons instruksi melalui siklus persepsi, penalaran, dan aksi. 

## 🛠️ Teknologi yang Digunakan

*   **Python:** Bahasa pemrograman utama yang mendasari logika sistem.
*   **Ollama:** Digunakan untuk menjalankan model bahasa besar (LLM) secara lokal sebagai mesin utama untuk modul *reasoning* (penalaran) dan pemrosesan bahasa.

## 📂 Struktur Proyek

Arsitektur Lilith dibagi menjadi beberapa komponen utama:

*   `/perception` : Modul untuk menerima, mengenali, dan memproses input dari pengguna atau lingkungan sekitar.
*   `/reasoning` : Mesin pemikir (*otak*) utama yang menggunakan Ollama untuk menganalisis input, menyusun rencana, dan mengambil keputusan.
*   `/action` : Modul yang bertugas mengeksekusi tindakan berdasarkan hasil keputusan dari modul *reasoning*.
*   `/ui` : Antarmuka sistem untuk memudahkan interaksi dengan pengguna.
*   `memory.py` : Komponen untuk mengelola penyimpanan konteks, riwayat interaksi, dan ingatan agen agar percakapan tetap berkesinambungan.
*   `config.py` : Berisi pengaturan sistem, konfigurasi LLM, dan variabel lingkungan lainnya.

## 🚀 Cara Penggunaan (Draft)

*Petunjuk instalasi dan penggunaan akan diperbarui setelah sistem inti sudah stabil.*

Untuk saat ini, pastikan [Ollama](https://ollama.com/) sudah terinstal dan berjalan di sistem Anda sebelum mengeksekusi agen.

---
*Dibuat untuk eksplorasi arsitektur multi-agent AI.*

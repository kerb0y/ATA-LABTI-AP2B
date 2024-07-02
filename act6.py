import sys
from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QListWidget,
    QMessageBox,
)

class AplikasiAktivitasPembelajaran(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Pengelola Aktivitas Pembelajaran")
        self.setGeometry(100, 100, 400, 300)
        
        self.layout = QVBoxLayout()
        
        self.label_nama_aktivitas = QLabel("Nama Aktivitas: ")
        self.input_nama_aktivitas = QLineEdit()
        self.label_deskripsi_aktivitas = QLabel("Deskripsi: ")
        self.input_deskripsi_aktivitas = QTextEdit()
        
        self.layout.addWidget(self.label_nama_aktivitas)
        self.layout.addWidget(self.input_nama_aktivitas)
        self.layout.addWidget(self.label_deskripsi_aktivitas)
        self.layout.addWidget(self.input_deskripsi_aktivitas)
    
        self.tombol_tambah = QPushButton("Tambah Aktivitas ")
        self.tombol_edit = QPushButton("Edit Aktivitas ")
        self.tombol_hapus = QPushButton("Hapus Aktivitas ")
        
        self.layout_tombol = QHBoxLayout()
        self.layout_tombol.addWidget(self.tombol_tambah)
        self.layout_tombol.addWidget(self.tombol_edit)
        self.layout_tombol.addWidget(self.tombol_hapus)
        
        self.layout.addLayout(self.layout_tombol)
        
        self.daftar_aktivitas = QListWidget()
        self.layout.addWidget(self.daftar_aktivitas)
        
        self.setLayout(self.layout)
        
        self.tombol_tambah.clicked.connect(self.tambah_aktivitas)
        self.tombol_edit.clicked.connect(self.edit_aktivitas)
        self.tombol_hapus.clicked.connect(self.hapus_aktivitas)
        
    def tambah_aktivitas(self):
        nama = self.input_nama_aktivitas.text()
        deskripsi = self.input_deskripsi_aktivitas.toPlainText()
        if nama and deskripsi:
            self.daftar_aktivitas.addItem(f"{nama}: {deskripsi}")
            self.bersihkan_input()
        else:
            self.tampilkan_pesan_error("Harap isi kedua bidang")

    def edit_aktivitas(self):
        item_terpilih = self.daftar_aktivitas.currentItem()
        if item_terpilih:
            nama = self.input_nama_aktivitas.text()
            deskripsi = self.input_deskripsi_aktivitas.toPlainText()
            if nama and deskripsi:
                item_terpilih.setText(f"{nama}: {deskripsi}")
                self.bersihkan_input()
            else:
                self.tampilkan_pesan_error("Harap isi kedua bidang")
        else:
            self.tampilkan_pesan_error("Harap pilih aktivitas yang akan diedit")

    def hapus_aktivitas(self):
        item_terpilih = self.daftar_aktivitas.currentItem()
        if item_terpilih:
            self.daftar_aktivitas.takeItem(self.daftar_aktivitas.row(item_terpilih))
        else:
            self.tampilkan_pesan_error("Harap pilih aktivitas yang akan dihapus")

    def bersihkan_input(self):
        self.input_nama_aktivitas.clear()
        self.input_deskripsi_aktivitas.clear()

    def tampilkan_pesan_error(self, pesan):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(pesan)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AplikasiAktivitasPembelajaran()
    ex.show()
    sys.exit(app.exec_())
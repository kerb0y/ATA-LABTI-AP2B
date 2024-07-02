
# main.py
import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QFormLayout,
    QTextEdit,
    QMessageBox,
)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Manajemen Daftar Mahasiswa"
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)

        self.layout = QVBoxLayout()

        self.label = QLabel("Daftar Mahasiswa:", self)
        self.layout.addWidget(self.label)

        self.get_button = QPushButton("Ambil Daftar Mahasiswa", self)
        self.get_button.clicked.connect(self.get_students)
        self.layout.addWidget(self.get_button)

        self.form_layout = QFormLayout()

        self.nama_input = QLineEdit(self)
        self.kelas_input = QLineEdit(self)
        self.npm_input = QLineEdit(self)
        self.jurusan_input = QLineEdit(self)
        self.fakultas_input = QLineEdit(self)

        self.form_layout.addRow("Nama:", self.nama_input)
        self.form_layout.addRow("Kelas:", self.kelas_input)
        self.form_layout.addRow("NPM:", self.npm_input)
        self.form_layout.addRow("Jurusan:", self.jurusan_input)
        self.form_layout.addRow("Fakultas:", self.fakultas_input)

        self.layout.addLayout(self.form_layout)

        self.post_button = QPushButton("Tambah Mahasiswa", self)
        self.post_button.clicked.connect(self.add_student)
        self.layout.addWidget(self.post_button)

        self.delete_form_layout = QFormLayout()

        self.delete_npm_input = QLineEdit(self)
        self.delete_form_layout.addRow("NPM (Hapus):", self.delete_npm_input)

        self.layout.addLayout(self.delete_form_layout)

        self.delete_button = QPushButton("Hapus Mahasiswa", self)
        self.delete_button.clicked.connect(self.delete_student)
        self.layout.addWidget(self.delete_button)

        self.students_list = QTextEdit(self)
        self.students_list.setReadOnly(True)
        self.layout.addWidget(self.students_list)

        self.setLayout(self.layout)
        self.show()

    def get_students(self):
        response = requests.get("http://127.0.0.1:5000/get_students")
        
        self.layout.addWidget(self.students_list)

        self.setLayout(self.layout)
        self.show()

    def get_students(self):
        response = requests.get("http://127.0.0.1:5000/get_students")
        if response.status_code == 200:
            students = response.json()
            self.display_students(students)
        else:
            self.label.setText("Gagal mengambil daftar mahasiswa dari Flask")

    def add_student(self):
        nama = self.nama_input.text()
        kelas = self.kelas_input.text()
        npm = self.npm_input.text()
        jurusan = self.jurusan_input.text()
        fakultas = self.fakultas_input.text()

        if not nama or not kelas or not npm or not jurusan or not fakultas:
            QMessageBox.warning(self, "Kesalahan Input", "Semua field harus diisi.")
            return
        if len(npm) != 8:
            QMessageBox.warning(self, "Kesalahan Input", "NPM harus tepat 8 karakter.")
            return

        new_student = {
            "nama": nama,
            "kelas": kelas,
            "npm": npm,
            "jurusan": jurusan,
            "fakultas": fakultas,
        }

        response = requests.post("http://127.0.0.1:5000/add_student", json=new_student)
        if response.status_code == 200:
            students = response.json()["students"]
            self.display_students(students)
        elif response.status_code == 400 and response.json().get("message") == "NPM sudah ada":
            QMessageBox.warning(self, "Kesalahan Input", "NPM sudah ada.")
        else:
            self.label.setText("Gagal menambahkan mahasiswa ke Flask")

    def delete_student(self):
        npm = self.delete_npm_input.text()

        if not npm:
            QMessageBox.warning(self, "Kesalahan Input", "NPM harus diisi.")
            return
        if len(npm) != 8:
            QMessageBox.warning(self, "Kesalahan Input", "NPM harus tepat 8 karakter.")
            return

        response = requests.delete(
            f"http://127.0.0.1:5000/delete_student", params={"npm": npm}
        )
        if response.status_code == 200:
            students = response.json()["students"]
            self.display_students(students)
        else:
            self.label.setText("Gagal menghapus mahasiswa dari Flask")

    def display_students(self, students):
        student_list_text = "\n".join(
            [f"{s['nama']}, {s['kelas']}, {s['npm']}, {s['jurusan']}, {s['fakultas']}" for s in students]
        )
        self.students_list.setPlainText(student_list_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
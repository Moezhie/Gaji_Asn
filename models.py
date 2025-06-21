from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Pegawai(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    tanggal_lahir = db.Column(db.String(20))
    nip = db.Column(db.String(30))
    status_pegawai = db.Column(db.String(10))
    golongan = db.Column(db.String(30))
    npwp = db.Column(db.String(30))
    status_kawin = db.Column(db.String(20))
    jumlah_anak = db.Column(db.Integer)           # kolom baru
    jumlah_jiwa = db.Column(db.Integer)
    gaji_pokok = db.Column(db.Float)
    tunjangan_pasangan = db.Column(db.Float)
    tunjangan_anak = db.Column(db.Float)
    potongan_pajak = db.Column(db.Float)
    bpjs = db.Column(db.Float)

    @property
    def total_penghasilan(self):
        return self.gaji_pokok + self.tunjangan_pasangan + self.tunjangan_anak

    @property
    def total_potongan(self):
        return self.potongan_pajak + self.bpjs

    @property
    def gaji_bersih(self):
        return self.total_penghasilan - self.total_potongan

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    role = db.Column(db.String(10))

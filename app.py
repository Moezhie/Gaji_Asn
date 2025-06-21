from flask import Flask, render_template, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Pegawai, User

app = Flask(__name__)
app.secret_key = 'rahasia_gaji_asn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
@login_required
def index():
    status = request.args.get('status')
    pegawai = Pegawai.query.filter_by(status_pegawai=status).all() if status else Pegawai.query.all()
    return render_template('index.html', pegawai=pegawai)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = User.query.filter_by(username=request.form['username']).first()
        if u and u.password == request.form['password']:
            login_user(u)
            return redirect('/')
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

@app.route('/input', methods=['GET', 'POST'])
@login_required
def input_data():
    if current_user.role != 'admin':
        return "Unauthorized", 403
    if request.method == 'POST':
        status_kawin = request.form['status_kawin']
        jumlah_anak = int(request.form.get('jumlah_anak', 0))
        jumlah_jiwa = 1 + jumlah_anak + (1 if status_kawin == 'Kawin' else 0)
        p = Pegawai(
            nama=request.form['nama'],
            tanggal_lahir=request.form['tanggal_lahir'],
            nip=request.form['nip'],
            status_pegawai=request.form['status_pegawai'],
            golongan=request.form['golongan'],
            npwp=request.form['npwp'],
            status_kawin=status_kawin,
            jumlah_anak=jumlah_anak,
            jumlah_jiwa=jumlah_jiwa,
            gaji_pokok=float(request.form['gaji_pokok']),
            tunjangan_pasangan=float(request.form['tunjangan_pasangan']),
            tunjangan_anak=float(request.form['tunjangan_anak']),
            potongan_pajak=float(request.form['potongan_pajak']),
            bpjs=float(request.form['bpjs'])
        )
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    return render_template('input_form.html')

@app.route('/cetak/<int:id>')
@login_required
def cetak_html(id):
    p = Pegawai.query.get_or_404(id)
    return render_template('slip_gaji.html', p=p)

@app.route('/export')
@login_required
def export_csv():
    data = Pegawai.query.all()
    rows = ["Nama,NIP,Golongan,Status Kawin,Jumlah Anak,Jumlah Jiwa,Gaji Bersih"]
    for p in data:
        rows.append(f"{p.nama},{p.nip},{p.golongan},{p.status_kawin},{p.jumlah_anak},{p.jumlah_jiwa},{p.gaji_bersih:.2f}")
    isi = "\n".join(rows)
    return Response(isi, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment; filename=gaji_asn.csv"})

@app.route('/lupa', methods=['GET', 'POST'])
def lupa_kata_sandi():
    if request.method == 'POST':
        nip = request.form['nip']
        email = request.form['email']
        return f"Link reset dikirim ke {email} (simulasi)"
    return render_template('lupa.html')

@app.route('/daftar', methods=['GET', 'POST'])
def daftar():
    if request.method == 'POST':
        user = User(
            username=request.form['nip'],
            password=request.form['password'],
            role='user'
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('daftar.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', password='admin123', role='admin')
            db.session.add(admin)
            db.session.commit()
    app.run(debug=True)

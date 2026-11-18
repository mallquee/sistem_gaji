def rupiah(angka):
    return "Rp {:,.0f}".format(angka).replace(",", ".")


JAM_KERJA_STANDAR = 176
JAM_PER_HARI = 8
DENDA_TELAT_PER_JAM = 15000

print("=== SISTEM PENGGAJIAN PEGAWAI PT MAJU JAYA ===")
periode = input("Periode (contoh: November 2026) : ")
jumlah = int(input("Jumlah Pegawai : "))

total_gaji_bersih = 0
daftar_slip = []

print("\n--- Input Data Pegawai ---")
print(f"(Jam kerja standar per bulan: {JAM_KERJA_STANDAR} jam)")
for i in range(1, jumlah + 1):
    print(f"\nPegawai {i}")
    nama = input("Nama            : ")
    jabatan = input("Jabatan (Staf/Supervisor/Manager) : ").lower()
    gaji_pokok = int(input("Gaji Pokok      : "))
    jam_lembur = int(input("Jam Lembur      : "))
    hari_alpa = int(input("Hari Alpa       : "))
    jam_kerja = int(input("Jam Kerja Sebulan : "))

    if jabatan == "staf":
        tunjangan = 500000
    elif jabatan == "supervisor":
        tunjangan = 1500000
    elif jabatan == "manager":
        tunjangan = 3000000
    else:
        tunjangan = 0
        print("-> Jabatan tidak dikenal, tunjangan jabatan Rp 0")

    jam_seharusnya = JAM_KERJA_STANDAR - hari_alpa * JAM_PER_HARI
    if jam_kerja < jam_seharusnya:
        jam_telat = jam_seharusnya - jam_kerja
    else:
        jam_telat = 0
    potongan_telat = jam_telat * DENDA_TELAT_PER_JAM
    print(f"-> Terlambat/kurang jam kerja: {jam_telat} jam")

    upah_lembur = jam_lembur * 20000
    gaji_kotor = gaji_pokok + tunjangan + upah_lembur

    potongan_alpa = hari_alpa * 100000
    potongan_bpjs = gaji_pokok * 2 / 100

    if gaji_kotor > 10000000:
        pajak = gaji_kotor * 5 / 100
    else:
        pajak = 0

    total_potongan = potongan_alpa + potongan_telat + potongan_bpjs + pajak
    gaji_bersih = gaji_kotor - total_potongan
    total_gaji_bersih += gaji_bersih

    daftar_slip.append({
        "nama": nama,
        "jabatan": jabatan.capitalize(),
        "gaji_pokok": gaji_pokok,
        "tunjangan": tunjangan,
        "lembur": upah_lembur,
        "gaji_kotor": gaji_kotor,
        "alpa": potongan_alpa,
        "jam_kerja": jam_kerja,
        "jam_telat": jam_telat,
        "telat": potongan_telat,
        "bpjs": potongan_bpjs,
        "pajak": pajak,
        "gaji_bersih": gaji_bersih,
    })

    print(f"-> Gaji Bersih: {rupiah(gaji_bersih)}")

for slip in daftar_slip:
    print("\n" + "-" * 40)
    print("=== SLIP GAJI ===")
    print("Periode             :", periode)
    print("Nama                :", slip["nama"])
    print("Jabatan             :", slip["jabatan"])
    print("Jam Kerja           :", slip["jam_kerja"], "jam")
    print("Gaji Pokok          :", rupiah(slip["gaji_pokok"]))
    print("Tunjangan Jabatan   :", rupiah(slip["tunjangan"]))
    print("Upah Lembur         :", rupiah(slip["lembur"]))
    print("Gaji Kotor          :", rupiah(slip["gaji_kotor"]))
    if slip["alpa"] > 0:
        print("Potongan Alpa       :", rupiah(slip["alpa"]))
    if slip["telat"] > 0:
        print(f"Potongan Telat ({slip['jam_telat']} jam):", rupiah(slip["telat"]))
    print("Potongan BPJS (2%)  :", rupiah(slip["bpjs"]))
    if slip["pajak"] > 0:
        print("Pajak (5%)          :", rupiah(slip["pajak"]))
    print("-" * 40)
    print("GAJI BERSIH         :", rupiah(slip["gaji_bersih"]))
    print("=" * 40)

print("\n" + "=" * 40)
print("=== REKAP PENGGAJIAN ===")
print("Periode             :", periode)
print("Jumlah Pegawai      :", jumlah, "orang")
print("TOTAL GAJI DIBAYAR  :", rupiah(total_gaji_bersih))
print("=" * 40)
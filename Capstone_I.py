from tabulate import tabulate #digunakan untuk import tabulate

# Main Menu
def menu():
    print('''
    ------- WELCOME TO ORIONGYO'S MARKET -------
    --------------------------------------------
           Spesialis alat Proteksi Radiasi       
    
    1. Menu Employee
    2. Menu Customer
    3. Exit Programm
    ''')

# database stock dan keranjang
dataStock = {
    'produk01': {'Jenis': 'Surveymeter', 'Tipe': 'ND2000A', 'Brand': 'NDS Product', 'S/N': 'EA203988929', 'Harga': 10000000},
    'produk02': {'Jenis': 'Surveymeter', 'Tipe': 'ND2000A', 'Brand': 'NDS Product', 'S/N': 'FB206849832', 'Harga': 10000000},
    'produk03': {'Jenis': 'Surveymeter', 'Tipe': 'ND2000A', 'Brand': 'NDS Product', 'S/N': 'GJ538492010', 'Harga': 10000000},
    'produk04': {'Jenis': 'Surveymeter', 'Tipe': 'ND2000A', 'Brand': 'NDS Product', 'S/N': 'NA874583022', 'Harga': 10000000},
    'produk05': {'Jenis': 'Pendose', 'Tipe': 'W-138', 'Brand': 'Arrow Tech', 'S/N': '888942', 'Harga': 8000000},
    'produk06': {'Jenis': 'Pendose', 'Tipe': 'W-138', 'Brand': 'Arrow Tech', 'S/N': '649429', 'Harga': 8000000},
    'produk07': {'Jenis': 'Pendose', 'Tipe': 'W-138', 'Brand': 'Arrow Tech', 'S/N': '329102', 'Harga': 8000000},
    'produk08': {'Jenis': 'Pendose', 'Tipe': 'W-138', 'Brand': 'Arrow Tech', 'S/N': '321030', 'Harga': 8000000},
    'produk09': {'Jenis': 'Pendose', 'Tipe': 'W-138', 'Brand': 'Arrow Tech', 'S/N': '738291', 'Harga': 8000000},
    'produk10': {'Jenis': 'Pendose', 'Tipe': 'W-138', 'Brand': 'Arrow Tech', 'S/N': '563818', 'Harga': 8000000}
}

keranjang = {}

#Main Menu Employee
def mainMenuEmployee():
    while True:
        username = input("Masukkan Kode Employee atau 'back' untuk ke main menu: ")
        if username == '101': #username untuk saat ini hanya 101
            menuEmployee()
            break
        elif username.lower() == 'back':
            break
        else:
            print("Kode anda salah, silahkan coba lagi")

# Menu Employee
def menuEmployee():
    while True:
        print('''
    Selamat Datang Kembali, Dhiyafath Anargyo Orion!
              
        Menu Employee
    ---------------------
    1. Lihat Stock
    2. Tambah Stock
    3. Hapus Stock
    4. Main Menu
    ''')
        employeePick = input("Masukkan Sub-Menu Employee: ")
        if employeePick == '1': #print stock barang
            print_stock()
        elif employeePick == '2': #nambah stock barang
            tambah()
            print_stock()
        elif employeePick == '3': #hapus stock barang
            hapusStock()
        elif employeePick == '4': #balik ke main menu
            break
        else:
            print('Pilihan menu Hanya 1 - 4')

# Tambah Stock
def tambah(): 
    while True:   
        produkBaru = input("Masukkan nomor produk baru (produkxx) atau ketik 'back' untuk ke main menu employee: ")
        if produkBaru.lower() in dataStock or keranjang:
            print('Produk sudah ada didalam stock.')
        elif produkBaru.lower() == 'back':
            break
        else :
            jenisBaru  = input('Masukkan Jenis produk baru     : ')
            tipeBaru   = input('Masukkan Tipe produk baru      : ')
            brandBaru  = input('Masukkan Nama Brand produk baru: ')
            snBaru     = input('Serial Number                  : ')
            hargaBaru  = int(input('Harga Produk                   : '))
            for product_info in dataStock.values():
                if product_info['S/N'] == snBaru:
                    print("Error: Serial number sudah terdaftar.")
                    return
            print('\n')
            dataStock[produkBaru] = {'Jenis': jenisBaru , 'Tipe' : tipeBaru , 'Brand' : brandBaru, 'Serial Number' : snBaru, 'Harga' : hargaBaru}
            print(f'\n{produkBaru} berhasil ditambahkan, berikut stock yang telah di perbarui:')
            break

# Hapus Stock 
def hapusStock():
    while True:
        hapusProduk = input("Masukkan nomor produk yang ingin dihapus atau ketik 'back' untuk ke main menu employee : ")
        if hapusProduk in dataStock:
            del dataStock[hapusProduk]
            print('\nStock telah berhasil di hapus. Berikut stock yang telah diperbarui:')
            print_stock()
            break
        elif hapusProduk.lower() == 'back':
            break
        else:
            print('Produk Tidak ada didalam stock')

# Main Menu Cust
def mainMenuCust():
    print('''
          Menu Customer
    -------------------------
    1. Lihat Katalog
    2. Lihat Keranjang Pembelian
    3. Checkout
    4. Main Menu
    ''')
   
# Menu Cust
def menuCust():
    while True:
        mainMenuCust()
        custPick = input("Masukkan Sub-Menu Customer : ")
        if custPick == '1': #lihat catalog
            print_stock()
            masukinKeranjang()
        elif custPick == '2': #lihat keranjang
            print_keranjang()
            hapusKeranjang()
        elif custPick == '3': #checkout
            checkout()
        elif custPick == '4': #main menu
            break
        else:
            print('Pilihan menu Hanya 1 - 4')

# Print Stock
def print_stock():
    sorteddataStock = dict(sorted(dataStock.items()))
    table = []
    for key, value in sorteddataStock.items():
        row = [key] + [v for v in value.values()]
        table.append(row)
    headers = ['Nama Produk', 'Jenis', 'Tipe', 'Brand', 'Serial Number', 'Harga']
    print(tabulate(table, headers=headers, tablefmt='github'))

# Masukin Keranjang
def masukinKeranjang():
    while True:
        print('\n')
        inputKeranjang = input("Pilih nomor produk (produkxx) untuk dimasukkan ke keranjang atau ketik 'back' untuk kembali: ")
        if inputKeranjang in dataStock: 
            keranjang[inputKeranjang] = dataStock.pop(inputKeranjang)
            print('Produk telah dimasukkan kedalam keranjang')
            print('\n')
            print('Keranjang Anda:')
            print_keranjang()
        elif inputKeranjang in keranjang:
            print('Produk sudah ada di dalam keranjang')
        elif inputKeranjang.lower() == 'back':
            break
        else:
            print('\nProduk tidak terdaftar. ketik sesuai dengan nama produk:')

# Print Keranjang
def print_keranjang():
    sortedKeranjang = dict(sorted(keranjang.items()))
    table2 = []
    for key2, value2 in sortedKeranjang.items():
        row2 = [key2] + [v2 for v2 in value2.values()]
        table2.append(row2)

    headers = ['Nama Produk', 'Jenis', 'Tipe', 'Brand', 'Serial Number', 'Harga']
    print(tabulate(table2, headers=headers, tablefmt='github'))
        
# hapus stock di keranjang
def hapusKeranjang():
    while True:
        konfirmHapus = input('Apakah anda ingin menghapus produk dalam keranjang (Y/N) = ')
        if konfirmHapus.upper() == 'Y':
            if len(keranjang) == 0 :
                print('Keranjang anda masih kosong, Anda tidak dapat menghapus Produk')
                break
            else:
                hapusKeranjang = input("Masukkan nomor produk yang ingin dihapus atau ketik 'back' untuk kembali : ")
                if hapusKeranjang in keranjang:
                    dataStock[hapusKeranjang] = keranjang.pop(hapusKeranjang)
                    print('\nProduk telah berhasil di hapus. Berikut keranjang yang telah diperbarui:')
                    print('\nKeranjang anda:')
                    print('\n')
                    print_keranjang()
                    break
                elif hapusKeranjang.lower() == 'back':
                    break
                else:
                    print('Produk Tidak ada didalam keranjang')
        elif konfirmHapus.upper() == 'N':
            break
        else:
            print('Pilihan hanya Y atau N')

# checkout
def checkout():
    print_keranjang()
    while True :
        checkoutProduk = input('Apakah anda ingin checkout (Y/N)= ')
        if checkoutProduk.upper() == 'Y':
            if len(keranjang) == 0 :
                print('Keranjang anda masih kosong, silahkan kembali ke main menu Customer')
                break
            else:
                custName  = input('Nama Anda          = ')
                custEmail = input('Email Anda         = ')
                custPhone = input('Nomor Telfon Anda  = ')
                print(f'''
------------------------------------------- INVOICE -------------------------------------------

Kepada Yth:
{custName.capitalize()}
{custEmail}
{custPhone}

berikut pesanan anda
            ''')
                printCheckout()
                print('''

Metode Pembayaran (Wajib Cash on Delivery. Debit/Kredit Sedang Maintenance)
Barang akan dikirimkan maksimal H+5 (hari kerja) setelah pembayaran

Hormat Kami,
                  
 TTD

Dhiyafath A.O
Direktur

===============================================================================================
                                  
Terimakasih telah berbelanja di Oriongyo's Market, anda akan dikembalikan ke menu utama
                  ''')
                keranjang.clear()
                break  
        elif checkoutProduk.upper() == 'N':
            break
        else:
            print('Pilihan hanya Y atau N')
    
# print checkout
def printCheckout():
    print_keranjang()
    total_harga = sum(item['Harga'] for item in keranjang.values())
    print('\n')
    print("Total Harga: ", total_harga)

# MAIN Program
while True:
    try:
        menu()
        menuDipilih = input("Masukkan nomor pilihan menu : ")
        if menuDipilih == '1': #Masuk ke Menu Employee
            mainMenuEmployee()
        elif menuDipilih == '2': #Masuk ke Menu Cust
            menuCust()
        elif menuDipilih == '3': #Stop Programm
            print("Terimakasih, Datang dan berbelanja kembali di Oriongyo's Market")
            print("Anda Sehat, Nyaman, Selamat adalah prioritas kami")
            print("\n")
            break
        else :
            print("Pilihan Menu Hanya 1, 2, dan 3")
    except Exception as e:
        print(f'Terjadi kesalahan: {e}')
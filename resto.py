list_menu = ['Makanan', 'Minuman' , 'Snack']
list_makanan = ["Nasi Goreng", "Mie Goreng", "Nasi Pecel", "Nasi Tempong", "Ayam Geprek", "Bakso", "Mie Ayam", "Lalapan"]
list_minuman = ["Es Teh", "Teh Hangat", "Es Jeruk", "Jeruk Hangat", "Aneka Jus", "Coklat Panas", "Es Campur", "Air Mineral"]
list_snack = ["Tahu Walik", "Tahu Petis", "Sosis Bakar", "Sosis Goreng", "Pisang Goreng", "Kentang Goreng", "Cimol", "Cireng"]

nota = []

while True:
    print('~~~~~~~~ Selamat Datang di Resto Semangat ~~~~~~~~')
    print("=" * 50)
    print('Silahkan Pilih Menu')
    for menu in range(0, len(list_menu)):
        print(f'{menu + 1}. {list_menu[menu]} ')
    print("=" * 50)
    menu = input('Masukkan Pilihan : ')
    print(" ")
    if menu == '1':
        print ("~~~~ Menu Makanan ~~~~")
        for menu_makanan in range(0, len(list_makanan)):
            print(f'{menu_makanan + 1}. {list_makanan[menu_makanan]} ')
        ulang = True
        while ulang :
            makanan = int(input(f'Silahkan Pilih Makanan (1-{len(list_makanan)}) : '))
            if makanan <= 0 or makanan > len(list_makanan):
                print("=" * 50)
                print('Maaf pesanan tidak ada. Silahkan masukan menu dengan benar')
                for menu_makanan in range(0, len(list_makanan)):
                    print(f'{menu_makanan + 1}. {list_makanan[menu_makanan]} ')
                continue
            else:
                nota.append(list_makanan[makanan - 1])
                print(" ")
                print('==== List Pesanan ====')
                for list_nota in range(0, len(nota)):
                    print(f'{list_nota +1} . {nota[list_nota]}')
                print("=" * 50)
                print(" ")
                ulang = False
            continue
    elif menu == '2':
        print ("~~~~ Menu Minuman ~~~~")
        for menu_minuman in range(0, len(list_minuman)):
            print(f'{menu_minuman + 1}. {list_minuman[menu_minuman]} ')
        ulang = True
        while ulang :
            minuman = int(input(f'Silahkan Pilih Minuman (1-{len(list_minuman)}) : '))
            if minuman <= 0 or minuman > len(list_minuman):
                print("=" * 50)
                print('Maaf pesanan tidak ada. Silahkan masukan menu dengan benar')
                for menu_minuman in range(0, len(list_minuman)):
                    print(f'{menu_minuman + 1}. {list_minuman[menu_minuman]} ')
                continue
            else:
                nota.append(list_minuman[minuman - 1])
                print(" ")
                print('==== List Pesanan ====')
                for list_nota in range(0, len(nota)):
                    print(f'{list_nota +1} . {nota[list_nota]}')
                print("=" * 50)
                print(" ")
                ulang = False
            continue
    elif menu == '3':
        print ("~~~~ Menu Snack ~~~~")
        for menu_snack in range(0, len(list_snack)):
            print(f'{menu_snack + 1}. {list_snack[menu_snack]} ')
        ulang = True
        while ulang :
            snack = int(input(f'Silahkan Pilih Snack (1-{len(list_snack)}) : '))
            if snack <= 0 or snack > len(list_snack):
                print("=" * 50)
                print('Maaf pesanan tidak ada. Silahkan masukan menu dengan benar')
                for menu_snack in range(0, len(list_snack)):
                    print(f'{menu_snack + 1}. {list_snack[menu_snack]} ')
                continue
            else:
                nota.append(list_snack[snack - 1])
                print(" ")
                print('==== List Pesanan ====')
                for list_nota in range(0, len(nota)):
                    print(f'{list_nota +1} . {nota[list_nota]}')
                print("=" * 50)
                print(" ")
                ulang = False
            continue
    else :
        print('Menu yang anda masukkan tidak ditemukan, Harap isi kembali')
        continue
    lanjut = input('Apakah anda ingin memesan Lagi [Y/N] ? ')
    if lanjut == 'Y':
        continue
    else:
        Pembeli = input('Masukkan Nama Pembeli : ')
        print(f'Pesanan atas nama {Pembeli}')
        print('==== list Menu ====')
        for list_nota in range(0, len(nota)):
            print(f'{list_nota +1} . {nota[list_nota]}')
        print("=" * 18)
        print(" ")
        print('Terima Kasih.... Pesanan anda sedang di proses')
        break
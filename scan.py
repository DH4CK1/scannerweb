#!/usr/bin/python
#Code By: Mr.Đ`HACK
#Code Date: 23/12/2019
#Tools: Scanner
################################################################
#                       import module                          #
#                     kesalahan module                         #
################################################################
try:
        import os, requests, time, json
except ModuleNotFoundError:
        print ("\nSepertinya module requests BELUM Di Install")
################################################################
#                       banner                                 #
################################################################
os.system('clear')
banner = """
          _______
         <\> | </>
           \/ \/
            \|/
            <|>
             =
         {Scanner}
   ======================
  <\>Code By Mr.D'HACK</>
  </>Black Coder Crush<\>
   ======================
"""
print(banner)
print ("* Masukan Website Hanya Dengan Domain (?.com) *")
print ("      * Tanpa ('www/http dan https') *\n")  
web = input('Website ~> ')
time.sleep(0.50)
os.system('clear')
print(banner)
scanner = """
      SCANNER
===================
[1].Scan DNS LOOKUP
===================
[2].Scan Whois
===================
[3].Scan IP WEB
==================="""
print(scanner)
pilih = input('Scan ~> ') #user melakukan input
print("===================")
########## PROSES........
time.sleep(1)
print ("[+] Scanning " + web)

if pilih == "1" or pilih == "01":
  print ("[+] SCAN BERHASIL HASIL:")

  print ("======================================================================")
  api1 = requests.get('https://api.hackertarget.com/dnslookup/?q=' + web)

  print(api1.text)
  print ("======================================================================")
  Kembali = input("Kembali Ke Tools/Keluar?[ Y/N ]: ")
  if Kembali == "y" or Kembali == "Y":
    print ("[+] Loading.......")
    time.sleep(1)
    os.system('python scan.py')
  elif Kembali == "n" or Kembali == "N":
    print ("[+] Loading.......")
    time.sleep(1)
    exit()
  else:
    print ("[-] Maaf  Input Anda salah")
    time.sleep(1)
    exit()

elif pilih == "2" or pilih == "02":
  print ("[+] SCAN BERHASIL HASIL:")

  print ("======================================================================")
  api2 = requests.get('http://api.hackertarget.com/whois/?q=' + web)

  print(api2.text)
  print ("======================================================================")
  Kembali = input("Kembali Ke Tools/Keluar?[ Y/N ]: ")
  if Kembali == "y" or Kembali == "Y":
    print ("[+] Loading.......")
    time.sleep(1)
    os.system('python scan.py')
  elif Kembali == "n" or Kembali == "N":
    print ("[+] Loading.......")
    time.sleep(1)
    exit()
  else:
    print ("[-] Maaf Input Anda salah")
    time.sleep(1)
    exit()

elif pilih == "3" or pilih == "03":
  print ("[+] SCAN BERHASIL HASIL:")

  print ("======================================================================")
  api3 = requests.get('http://api.hackertarget.com/geoip/?q=' + web)

  print(api3.text)
  print ("======================================================================")
  Kembali = input("Kembali Ke Tools/Keluar?[ Y/N ]: ")
  if Kembali == "y" or Kembali == "Y":
    print ("[+] Loading.......")
    time.sleep(1)
    os.system('python scan.py')
  elif Kembali == "n" or Kembali == "N":
    print ("[+] Loading.......")
    time.sleep(1)
    exit()
  else:
    print ("[-] Maaf Input Anda salah")
    exit()
else:
  print ("[!] Maaf input anda salah silahkan kembali dan coba lagi!")


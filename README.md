# simbaf4r
Bu proje, belirli bir IP adresine farklı servisler (SSH, FTP, RDP ve SMB) için brute force saldırıları gerçekleştirmek amacıyla geliştirilmiş bir araçtır. Kullanıcı adı ve parola listeleri kullanılarak hedef sistemde geçerli kimlik bilgileri bulunmaya çalışılır.

Projenin İçeriği
paramiko, ftplib, smbprotocol, socket gibi modüller kullanılarak çeşitli servislerde bağlantı denemeleri yapılır.
ThreadPoolExecutor kullanılarak paralel işlem gerçekleştirilir.
Kullanıcıdan gerekli bilgiler alındıktan sonra belirlenen servis için kullanıcı adı ve parola kombinasyonları denenir.
Geçerli kimlik bilgileri bulunduğunda sonuçlar ekranda tablo olarak gösterilir.

# SIMBAF4R - Brute Force Attack Tool

SIMBAF4R, belirli bir IP adresine farklı servisler (SSH, FTP, RDP ve SMB) için brute force saldırıları gerçekleştiren bir araçtır. Kullanıcı adı ve parola listeleri kullanılarak hedef sistemde geçerli kimlik bilgileri bulunmaya çalışılır.

## Özellikler

- SSH, FTP, RDP ve SMB servisleri için brute force denemeleri yapar.
- Kullanıcı adı ve parola listeleri kullanarak geçerli kimlik bilgilerini bulmaya çalışır.
- Çoklu iş parçacığı kullanarak deneme işlemlerini hızlandırır.
- Geçerli kimlik bilgilerini tablo olarak gösterir.

## Gereksinimler

- Python 3.x
- Gerekli Python modülleri:
  - paramiko
  - ftplib
  - smbprotocol
  - socket
  - concurrent.futures
  - tabulate
  - colorama
  - uuid
  - pyfiglet

## Kurulum

Gerekli Python modüllerini yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install paramiko ftplib smbprotocol tabulate colorama pyfiglet



Elbette, aşağıda kodun nasıl çalıştığını ve ne işe yaradığını anlatan bir yazı ve README dosyasının içeriğini bulabilirsiniz.

Açıklama Yazısı
Bu proje, belirli bir IP adresine farklı servisler (SSH, FTP, RDP ve SMB) için brute force saldırıları gerçekleştirmek amacıyla geliştirilmiş bir araçtır. Kullanıcı adı ve parola listeleri kullanılarak hedef sistemde geçerli kimlik bilgileri bulunmaya çalışılır. Araç, çoklu iş parçacığı kullanarak deneme işlemlerini hızlandırır.

Projenin İçeriği
paramiko, ftplib, smbprotocol, socket gibi modüller kullanılarak çeşitli servislerde bağlantı denemeleri yapılır.
ThreadPoolExecutor kullanılarak paralel işlem gerçekleştirilir.
Kullanıcıdan gerekli bilgiler alındıktan sonra belirlenen servis için kullanıcı adı ve parola kombinasyonları denenir.
Geçerli kimlik bilgileri bulunduğunda sonuçlar ekranda tablo olarak gösterilir.
README Dosyası (README.md)
markdown
Kodu kopyala
# SIMBAF4R - Brute Force Attack Tool

SIMBAF4R, belirli bir IP adresine farklı servisler (SSH, FTP, RDP ve SMB) için brute force saldırıları gerçekleştiren bir araçtır. Kullanıcı adı ve parola listeleri kullanılarak hedef sistemde geçerli kimlik bilgileri bulunmaya çalışılır.

## Özellikler

- SSH, FTP, RDP ve SMB servisleri için brute force denemeleri yapar.
- Kullanıcı adı ve parola listeleri kullanarak geçerli kimlik bilgilerini bulmaya çalışır.
- Çoklu iş parçacığı kullanarak deneme işlemlerini hızlandırır.
- Geçerli kimlik bilgilerini tablo olarak gösterir.

## Gereksinimler

- Python 3.x
- Gerekli Python modülleri:
  - paramiko
  - ftplib
  - smbprotocol
  - socket
  - concurrent.futures
  - tabulate
  - colorama
  - uuid
  - pyfiglet

## Kurulum

Gerekli Python modüllerini yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install paramiko ftplib smbprotocol tabulate colorama pyfiglet


Elbette, aşağıda kodun nasıl çalıştığını ve ne işe yaradığını anlatan bir yazı ve README dosyasının içeriğini bulabilirsiniz.

Açıklama Yazısı
Bu proje, belirli bir IP adresine farklı servisler (SSH, FTP, RDP ve SMB) için brute force saldırıları gerçekleştirmek amacıyla geliştirilmiş bir araçtır. Kullanıcı adı ve parola listeleri kullanılarak hedef sistemde geçerli kimlik bilgileri bulunmaya çalışılır. Araç, çoklu iş parçacığı kullanarak deneme işlemlerini hızlandırır.

Projenin İçeriği
paramiko, ftplib, smbprotocol, socket gibi modüller kullanılarak çeşitli servislerde bağlantı denemeleri yapılır.
ThreadPoolExecutor kullanılarak paralel işlem gerçekleştirilir.
Kullanıcıdan gerekli bilgiler alındıktan sonra belirlenen servis için kullanıcı adı ve parola kombinasyonları denenir.
Geçerli kimlik bilgileri bulunduğunda sonuçlar ekranda tablo olarak gösterilir.
README Dosyası (README.md)
markdown
Kodu kopyala
# SIMBAF4R - Brute Force Attack Tool

SIMBAF4R, belirli bir IP adresine farklı servisler (SSH, FTP, RDP ve SMB) için brute force saldırıları gerçekleştiren bir araçtır. Kullanıcı adı ve parola listeleri kullanılarak hedef sistemde geçerli kimlik bilgileri bulunmaya çalışılır.

## Özellikler

- SSH, FTP, RDP ve SMB servisleri için brute force denemeleri yapar.
- Kullanıcı adı ve parola listeleri kullanarak geçerli kimlik bilgilerini bulmaya çalışır.
- Çoklu iş parçacığı kullanarak deneme işlemlerini hızlandırır.
- Geçerli kimlik bilgilerini tablo olarak gösterir.

## Gereksinimler

- Python 3.x
- Gerekli Python modülleri:
  - paramiko
  - ftplib
  - smbprotocol
  - socket
  - concurrent.futures
  - tabulate
  - colorama
  - uuid
  - pyfiglet

## Kurulum

Gerekli Python modüllerini yüklemek için aşağıdaki komutu kullanabilirsiniz:

```bash
pip install paramiko ftplib smbprotocol tabulate colorama pyfiglet

Kullanım
Aracı çalıştırın:
bash
Kodu kopyala
python simbarf4r.py
IP adresini, kullanıcı adı dosyasını ve parola dosyasını girin.
Denemek istediğiniz servisi seçin (SSH, FTP, RDP veya SMB).
Geçerli kimlik bilgileri bulunduğunda sonuçlar ekranda tablo olarak gösterilecektir.
Örnek Kullanım
bash
Kodu kopyala
Enter IP address: 192.168.1.100
Select port to try:
1. SSH (22)
2. FTP (21)
3. RDP (3389)
4. SMB (445)
Enter your choice: 1
Enter username file path: usernames.txt
Enter password file path: passwords.txt

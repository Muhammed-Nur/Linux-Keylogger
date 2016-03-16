# Linux-Keylogger

Linux üzerinde çalışan ve bize bilgi sızdıran program

Programın Amacı Nedir?
--------------------------------

Program, Linux üzerinde sistem ile aktif olarak klavye aktivitelerini izlemekte ve bu aktiviteleri bir txt dosyasına yazarak belirli sürelerle bu txt dosyayısını şifreleyip mail olarak bilgi sızdırmak isteyen kişiye göndermek için kullanılır.


Programın Yapılma Nedeni Nedir?
--------------------------------

Süleyman Demirel Üniversitesi - Mühendislik Fakültesi, Bilgisayar Mühendisliği bölümünden Sayın Doç. Dr. Ecir Uğur KÜÇÜKSİLLE tarafından Sistem Programlama dersi için proje olarak verilmiştir.


Programda Karşılaşılan Zorluklar
--------------------------------

* Sistemin TR karakterlere yabancı olması bundan dolayı yazılan tanımlamaların US Klavyeye göre yazılması.

* Klavye türlerine göre değişen Numpad, sağ Ctrl ve F(1,2,3...) tuşlarının tanımlanması

* Zor kırlıcak bir şifreleme algoritması bulma


Programın Gelişim Süreci
--------------------------------

(26/02/2016) : Progamın giriş parçaları olarak txt dosyası için Dosya_islemleri.py yazıldı.

(26/02/2016) : Txt dosyasının şifrelenmesi için Sifreleme.py yazıldı. Burda Sezar şifreleme algoritması kullanıldı.(İleride değiştirilebilir!)

(27/02/2016) : Programın ana mekanızması olan Keylogger.py yazılmaya başlandı.

(28/02/2016) : Keylogger.py için araştırmlar yapıldı.

(03/03/2016) : Program için yazılan Dosya_islemleri.py ve Sifreleme.py sisteme yüklendi.

(01/03/2016) : Keylogger.py tuş tanımlamaları yapılarak kodlanmaya başlandı.

(05/03/2016) : Keylogger.py testler başlandı.

(07/03/2016) : Keylogger.py bir kaç eksiğe rağmen çalışır bir şekilde sisteme yüklendi.(Hatalar v.1 sürümünde içinde not olarak yazmaktadır)

(08/03/2016) : Keylogger.py Türkçe karakter sorunu unicode kullanarak çözüldü.

(09/03/2016) : Keylogger.py Numpad tuşları (Numpad içerisindeki "ENTER" tuşu hariç) ve F fonksiyon tuşları ("F11" hariç) tanımlandı.

(11/03/2016) : Keylogger.py ALT-GR tuş fonksiyonu yapıldı.

Linux-Keylogger
---------------------------------------
Programs running on Linux and leaking information to us


What Is The Purpose Of The Program?
---------------------------------------
The program is actively monitor keyboard activity on Linux systems, and these activities are used to send the e-mail leaked information to people who want to encrypt this txt file with a .txt file by typing in a specific period of time.

Why Was This Program Created?
---------------------------------------
Süleyman Demirel University - Faculty of Engineering of Computer Engineering department. , Mr. Assoc. Dr. Ecir Uğur KÜÇÜKSİLLE has been given by the project for System Programming course.

The problems Encountered In The Program
----------------------------------------
* System does not recognize the Turkish characters and transactions made by us keyboard

* Numpad, right Ctrl and F (1,2,3 ...) to identify the key

* Finding difficult to break an encryption algorithm

The Program Development Process
---------------------------------------

(26/02/2016) : As part of the program's introduction written Dosya_islemleri.py to txt file.

(26/02/2016) : It placed Sifreleme.py to encrypt the TXT file. Here Caesar was used encryption algorithm. (It can be changed in the future!) 

(27/02/2016) : The main mechanism of the program which began to be written Keylogger.py.

(28/02/2016) : The main mechanism of the program which began to be written Keylogger.py.

(03/03/2016) : Sifreleme.py system was installed on the Dosya_islemleri.py and written to the program.

(01/03/2016) : Keylogger.py began to be coded by key definitions. 

(05/03/2016) : Keylogger.py testing began.

(07/03/2016) : Keylogger.py runs despite missing a few uploaded to the one way system. (Errors writes a note in the version v.1)

(08/03/2016) : Keylogger.py Turkish character problem is solved using Unicode.

(09/03/2016) : Keylogger.py the numpad keys (Numpad "Enter" key, except) and F function keys ("F11") is described.

(11/03/2016) : Keylogger.py ALT-GR key functionality.

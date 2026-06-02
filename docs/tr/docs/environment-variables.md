# Ortam Değişkenleri

/// tip

"Ortam değişkenlerinin" ne olduğunu ve nasıl kullanılacağını zaten biliyorsanız, bu bölümü atlayabilirsiniz.

///

Ortam değişkeni ("**env var**" olarak da bilinir), Python kodunun **dışında**, **işletim sisteminde** yaşayan ve Python kodunuz (veya diğer programlar) tarafından okunabilen bir değişkendir.

Ortam değişkenleri, uygulama **ayarlarını** yönetmek, Python **kurulumunun** bir parçası olarak vb. için yararlı olabilir.

## Ortam Değişkenleri Oluşturma ve Kullanma

Python'a ihtiyaç duymadan **shell'de (terminalde)** ortam değişkenleri **oluşturabilir** ve kullanabilirsiniz:

//// tab | Linux, macOS, Windows Bash

<div class="termy">

```console
// You could create an env var MY_NAME with
$ export MY_NAME="Wade Wilson"

// Then you could use it with other programs, like
$ echo "Hello $MY_NAME"

Hello Wade Wilson
```

</div>

////

//// tab | Windows PowerShell

<div class="termy">

```console
// Create an env var MY_NAME
$ $Env:MY_NAME = "Wade Wilson"

// Use it with other programs, like
$ echo "Hello $Env:MY_NAME"

Hello Wade Wilson
```

</div>

////

## Python'da Ortam Değişkenlerini Okuma

Ayrıca ortam değişkenlerini Python'un **dışında**, terminalde (veya başka herhangi bir yöntemle) oluşturabilir ve ardından **Python'da okuyabilirsiniz**.

Örneğin bir `main.py` dosyanız olabilir:

```Python hl_lines="3"
import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")
```

/// tip

<a href="https://docs.python.org/3.8/library/os.html#os.getenv" class="external-link" target="_blank">`os.getenv()`</a> fonksiyonunun ikinci argümanı, döndürülecek varsayılan değerdir.

Sağlanmazsa, varsayılan olarak `None` olur, burada kullanılacak varsayılan değer olarak `"World"` sağlıyoruz.

///

Ardından o Python programını çağırabilirsiniz:

//// tab | Linux, macOS, Windows Bash

<div class="termy">

```console
// Here we don't set the env var yet
$ python main.py

// As we didn't set the env var, we get the default value

Hello World from Python

// But if we create an environment variable first
$ export MY_NAME="Wade Wilson"

// And then call the program again
$ python main.py

// Now it can read the environment variable

Hello Wade Wilson from Python
```

</div>

////

//// tab | Windows PowerShell

<div class="termy">

```console
// Here we don't set the env var yet
$ python main.py

// As we didn't set the env var, we get the default value

Hello World from Python

// But if we create an environment variable first
$ $Env:MY_NAME = "Wade Wilson"

// And then call the program again
$ python main.py

// Now it can read the environment variable

Hello Wade Wilson from Python
```

</div>

////

Ortam değişkenleri kodun dışında ayarlanabildiğinden, ancak kod tarafından okunabildiğinden ve dosyaların geri kalanıyla birlikte saklanmak (`git`'e commit edilmek) zorunda olmadığından, bunları yapılandırmalar veya **ayarlar** için kullanmak yaygındır.

Ayrıca yalnızca **belirli bir program çağrısı** için bir ortam değişkeni oluşturabilirsiniz, bu yalnızca o program için ve yalnızca süresi boyunca kullanılabilir.

Bunu yapmak için, programın hemen önünde, aynı satırda oluşturun:

<div class="termy">

```console
// Create an env var MY_NAME in line for this program call
$ MY_NAME="Wade Wilson" python main.py

// Now it can read the environment variable

Hello Wade Wilson from Python

// The env var no longer exists afterwards
$ python main.py

Hello World from Python
```

</div>

/// tip

Bunu <a href="https://12factor.net/config" class="external-link" target="_blank">The Twelve-Factor App: Config</a>'de daha fazla okuyabilirsiniz.

///

## Türler ve Doğrulama

Bu ortam değişkenleri yalnızca **metin dizeleri** işleyebilir, çünkü Python'un dışındadırlar ve diğer programlar ve sistemin geri kalanıyla (ve hatta Linux, Windows, macOS gibi farklı işletim sistemleriyle) uyumlu olmaları gerekir.

Bu, Python'da bir ortam değişkeninden okunan **herhangi bir değerin** bir **`str` olacağı** ve farklı bir türe dönüştürme veya herhangi bir doğrulamanın kodda yapılması gerektiği anlamına gelir.

Uygulama **ayarlarını** yönetmek için ortam değişkenlerini kullanma hakkında daha fazla bilgiyi [Gelişmiş Kullanıcı Kılavuzu - Ayarlar ve Ortam Değişkenleri](./advanced/settings.md){.internal-link target=_blank} bölümünde öğreneceksiniz.

## `PATH` Ortam Değişkeni

Çalıştırılacak programları bulmak için işletim sistemleri (Linux, macOS, Windows) tarafından kullanılan **`PATH`** adlı **özel** bir ortam değişkeni vardır.

`PATH` değişkeninin değeri, Linux ve macOS'ta iki nokta üst üste `:` ile ve Windows'ta noktalı virgül `;` ile ayrılmış dizinlerden oluşan uzun bir dizedir.

Örneğin, `PATH` ortam değişkeni şöyle görünebilir:

//// tab | Linux, macOS

```plaintext
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

Bu, sistemin programları şu dizinlerde araması gerektiği anlamına gelir:

* `/usr/local/bin`
* `/usr/bin`
* `/bin`
* `/usr/sbin`
* `/sbin`

////

//// tab | Windows

```plaintext
C:\Program Files\Python312\Scripts;C:\Program Files\Python312;C:\Windows\System32
```

Bu, sistemin programları şu dizinlerde araması gerektiği anlamına gelir:

* `C:\Program Files\Python312\Scripts`
* `C:\Program Files\Python312`
* `C:\Windows\System32`

////

Terminalde bir **komut** yazdığınızda, işletim sistemi `PATH` ortam değişkeninde listelenen **her bir dizinde** programı **arar**.

Örneğin, terminalde `python` yazdığınızda, işletim sistemi o listedeki **ilk dizinde** `python` adlı bir programı arar.

Bulursa, onu **kullanır**. Aksi takdirde **diğer dizinlerde** aramaya devam eder.

### Python'u Yükleme ve `PATH`'i Güncelleme

Python'u yüklediğinizde, `PATH` ortam değişkenini güncellemek isteyip istemediğiniz sorulabilir.

//// tab | Linux, macOS

Python'u yüklediniz ve `/opt/custompython/bin` dizininde bulunduğunu varsayalım.

`PATH` ortam değişkenini güncellemeyi kabul ederseniz, yükleyici `/opt/custompython/bin`'i `PATH` ortam değişkenine ekleyecektir.

Şöyle görünebilir:

```plaintext
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/custompython/bin
```

Bu şekilde, terminalde `python` yazdığınızda, sistem `/opt/custompython/bin` (son dizin) içindeki Python programını bulacak ve onu kullanacaktır.

////

//// tab | Windows

Python'u yüklediniz ve `C:\opt\custompython\bin` dizininde bulunduğunu varsayalım.

`PATH` ortam değişkenini güncellemeyi kabul ederseniz, yükleyici `C:\opt\custompython\bin`'i `PATH` ortam değişkenine ekleyecektir.

```plaintext
C:\Program Files\Python312\Scripts;C:\Program Files\Python312;C:\Windows\System32;C:\opt\custompython\bin
```

Bu şekilde, terminalde `python` yazdığınızda, sistem `C:\opt\custompython\bin` (son dizin) içindeki Python programını bulacak ve onu kullanacaktır.

////

Yani şunu yazarsanız:

<div class="termy">

```console
$ python
```

</div>

//// tab | Linux, macOS

Sistem `/opt/custompython/bin` içindeki `python` programını **bulacak** ve çalıştıracaktır.

Bu, kabaca şunu yazmaya eşdeğer olacaktır:

<div class="termy">

```console
$ /opt/custompython/bin/python
```

</div>

////

//// tab | Windows

Sistem `C:\opt\custompython\bin\python` içindeki `python` programını **bulacak** ve çalıştıracaktır.

Bu, kabaca şunu yazmaya eşdeğer olacaktır:

<div class="termy">

```console
$ C:\opt\custompython\bin\python
```

</div>

////

Bu bilgi [Sanal Ortamlar](virtual-environments.md){.internal-link target=_blank} hakkında öğrenirken yararlı olacaktır.

## Sonuç

Bununla birlikte, **ortam değişkenlerinin** ne olduğu ve Python'da nasıl kullanılacağı hakkında temel bir anlayışa sahip olmalısınız.

Bunlar hakkında <a href="https://en.wikipedia.org/wiki/Environment_variable" class="external-link" target="_blank">Ortam Değişkeni için Wikipedia</a>'da daha fazla okuyabilirsiniz.

Birçok durumda ortam değişkenlerinin nasıl yararlı ve uygulanabilir olacağı hemen çok açık değildir. Ama geliştirme yaparken birçok farklı senaryoda karşınıza çıkmaya devam ederler, bu yüzden onları bilmek iyidir.

Örneğin, bir sonraki bölüm olan [Sanal Ortamlar](virtual-environments.md) hakkında bu bilgiye ihtiyacınız olacaktır.

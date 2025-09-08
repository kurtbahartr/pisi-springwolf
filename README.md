# pisi-springwolf
Bir Linux dağıtımında olmazsa olmazlarım olan ancak Pisi Linux depolarında yer almayan paketler.

# Dokümantasyon
Yakında, önce test edilmesi lazım.

## Depo kullanımı
İkili paket deposu olmadığı için burada yer alan paketleri elle derlemeniz gerekiyor.

```
sudo pisi bi https://github.com/kurtbahartr/pisi-springwolf/raw/master/<packagename>/pspec.xml # Paketin pspec ve actions dosyalarını depodan çeker, işler ve bununla paketi derler.
sudo pisi it ./<packagename>*.pisi # Yerel olarak derlediğimiz paketi kurar.
```

# SSS (Sık ~~Sorulan~~ Sorulabilecek Sorular)
## Böyle bir şeye gerçekten gerek var mıydı?
Her dağıtım her paketi kendi bünyesinde barındırmak istemez. Birinin beğendiğini diğeri beğenmeyebilir. Dolayısıyla evet, gerek vardı.

Ayrıca bu depoyu sadece kendim tercih ettiğim paketleri depolamak için değil, aynı zamanda resmi depolara sunmayı düşündüğüm paketleri de önceden yapıp zaman kazanmak için yaptım.

## Bu paketler de neyin nesi? Sen <burada politik bir görüş olduğunu varsayın> yanlısı mısın?
Benim şahsen sabit bir politik görüşüm yok. Dediğim gibi, bu depoda kendim kişisel olarak bir dağıtımda olmazsa olmaz olarak gördüklerim bulunmakta. Kişisel tercihlerim her ne kadar belli başlı politik görüşleri destekleyecek nitelikte görünse bile bu tip önyargıların başkalarına çamur atma çalışmasından başka bir şey olduğunu unutmamak gerek. ;)

## Peki neden Pisi Linux?
Çünkü paket yönetimi konusunda Arch gibi bir tarza sahip. Aynı zamanda yerli, özgür ve bağımsız bir dağıtımdır kendisi - Pardus'un güncel sürümleri için aynısını söyleyemem çünkü artık sadece modlu bir Debian haline geldi.

## Bunları kim test ediyor?
Yours truly. :D

## Bu depodaki paketlerden biri/birkaçı Pisi Linux'taki paketlerle dosya yönünden çakışıyor.
OLDUĞUNUZ YERDE DURUN! Böyle bir şeyin olmaması gerek ama olursa direkt bu repoda hata kaydı açın ki doğrulayıp bakabileyim. Ben düzeltene kadar siz düzeltmiş olursanız PR atmaktan çekinmeyin.

## Bu depodaki paketlerden birinin/birkaçının sürümü eskimiş.
Hayallerinizi yıkmak istemem ama ancak boş zamanımda bakabilirim. Siz benden önce fark ederseniz hata kaydı açmayı ihmal etmeyiniz.

> [!NOTE]
> hyfetch paketi bu durumdan muaftır ve bunun hakkında açılan kayıtlar ilgili commit mesajına yönlendirilip kapatılacaktır.
>
> Rust sürümü için pspec yazabilirseniz PR açmaktan çekinmeyin.

## Bu depodaki paketlerden birinde/birkaçında güvenlik açığı olduğunu duydum/gördüm/biliyorum.
Harika ama ben bunları sadece derletebilmek için dosyalarını yazıyorum, aktif geliştiriciliklerinde yer almıyorum. Eğer güvenlik açığı bulursanız hata kaydı açmanız ve o anlık en uygun çözümün ne olduğunu konuşmamız en iyisi olacaktır.

## İkili paket deposu da gelir mi?
Gelmez. İkili paket deposu ayrı bir baş ağrısı oluşturur, o yüzden şimdilik sadece pspec'ler yeterli gibime geliyor.

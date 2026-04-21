# Veri Üzerinde Çalışmak: Verinin Hazırlanması

|![ Sketchnote by [(@sketchthedocs)](https://sketchthedocs.dev) ](../../../sketchnotes/08-DataPreparation.png)|
|:---:|
|Veriyi Hazırlamak - _Sketchnote by [@nitya](https://twitter.com/nitya)_ |

## [Ders Öncesi Kısa Sınavı](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/14)



Veriye bağlı olarak ham veriler, analiz ve modellemede zorluk çıkarabilecek bazı tutarsızlıklar içerebilir. Başka bir deyişle bu veriler "kirli" olarak sınıflandırılabilir ve temizlenmeleri gerekir. Bu derste kayıp, tutarsız ve eksik verilerle ilgili zorlukların üstesinden gelmek için verileri temizleme ve dönüştürne tekniklerine odaklanacağız. Bu derste işlenen konular Python programlama dili ve Pandas kitaplığını kullanacak ve [bu dizindeki](../notebook.ipynb) not defterinde gösterilecektir.

## Veriyi temizlemenin önemi

- **Kullanım kolaylığı ve yeniden kullanılabilirlik**: Veriler düzgün bir şekilde düzenlendiğinde ve normalize edildiğinde, veri içinde arama yapmak, veriyi kullanmak ve başkalarıyla paylaşmak daha kolaydır.

- **Tutarlılık**: Veri bilimi genellikle, farklı kaynaklardan gelen veri setlerinin bir araya getirilmesinin gerektiği birden fazla veri setiyle çalışmayı gerektirir. Her bir veri setinin ortak standardizasyona sahip olduğundan emin olmak, verilerin tümü tek bir veri kümesinde birleştirildiğinde dahi veri setlerinin hala işe yarar olmasını sağlayacaktır. 

- **Model doğruluğu**: Temiz veriler, üzerinde kullanıldıkları modellerin doğruluğunu arttırır. 

## Veriyi temizlemede genel hedef ve stratejiler

- **Veri setini araştırmak**: Daha [sonraki derslerde](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle/15-analyzing) ele alacağımız veri araştırması, temizlenmesi gereken verilerin tespitinde yardımcı olabilir. Bir veri setindeki değerleri görsel olarak gözlemlemek, geri kalanının nasıl görüneceğine dair beklentileri belirleyebilir veya çözülebilecek sorunlar hakkında bir fikir verebilir. Veri setini araştırmak, temel sorgulamayı, görselleştirmeleri ve örneklemeyi içerebilir.

-  **Biçimlendirme**: Kaynağa bağlı olarak, verilerin sunulma biçiminde tutarsızlıklar olabilir. Bu tutarsızlık veri setinde görülebilir fakat görselleştirme ve arama sonuçlarında düzgün bir şekilde gözükmeyebilir ayrıca tutarsızlık veriyi aramada ve verinin gösterilmesinde problemlere yol açabilir. Yaygın biçimlendirme sorunları, boşlukları, tarihleri ​​ve veri türlerini düzenlemeyi içerir. Biçimlendirme sorunlarını çözmek genellikle veriyi kullanan kişilere bağlıdır. Örneğin, tarihlerin ve sayıların nasıl sunulduğuna ilişkin standartlar ülkeye göre farklılık gösterebilir.

-  **Kopya veriler**: Veri setinde birden fazla kez kullanılan veriler yanlış sonuçlar verebilir ve genellikle kaldırılmalıdır. Birden fazla kullanılan veriler genellikle iki veya daha fazla veri setinin birleştirilmesi sırasında ortaya çıkar. Ancak, bazı birleştirilmiş veri setlerinde ortaya çıkan kopya veriler önemli detaylar içerebilir ve korunması gerekir.

- **Kayıp veri**: Eksik veriler, yanlışlıkların yanı sıra zayıf veya yanlı sonuçlara neden olabilir. Bazen bunlar verinin "yeniden yüklenmesi", yani eksik değerlerin Python koduyla işlenip doldurulması veya yalnızca değer ve ilgili verinin silinmesiyle çözülebilir. Verilerin neden eksik olabileceğiyle ilgili birçok neden vardır ve bu eksik veriyi düzeltmek için alınan önlemler, ilk etapta nasıl ve neden kaybolduklarına bağlı olabilir.

## Veri Setiyle İlgili Bilgileri Araştırma
> **Öğrenme hedefi:** Bu alt başlığın sonunda, pandas veri setlerinin içinde depolanan veriyle ilgili genel bilgilere ulaşmakta sorun yaşamıyor olacaksınız. 

Verilerinizi pandas'a yükledikten sonra, büyük ihtimalle veriler bir veri çerçevesinin(DataFrame) içerisinde değilmiş gibi hissettirecektir.(ayrıntılı genel bakış için önceki [derse](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data/07-python#dataframe) bakın). Ancak, veri çerçevenizdeki(DataFrame) veri setinde 60.000 satır ve 400 sütun varsa, neyle çalıştığınıza dair bir fikir edinmeye nasıl başlarsınız? Neyse ki, [pandas](https://pandas.pydata.org/) ilk birkaç ve son birkaç satıra ek olarak bir veri çerçevesiyle ilgili genel bilgilere hızlı bir şekilde bakmak için bazı kullanışlı araçlar sağlar.

Bu işlevselliği keşfetmek için Python scikit-learn kitaplığını içe aktaracağız ve ikonik bir veri seti kullanacağız: **Iris veri seti**.

```python
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])
```
|                                        |sepal length (cm)|sepal width (cm)|petal length (cm)|petal width (cm)|
|----------------------------------------|-----------------|----------------|-----------------|----------------|
|0                                       |5.1              |3.5             |1.4              |0.2             |
|1                                       |4.9              |3.0             |1.4              |0.2             |
|2                                       |4.7              |3.2             |1.3              |0.2             |
|3                                       |4.6              |3.1             |1.5              |0.2             |
|4                                       |5.0              |3.6             |1.4              |0.2             |

- **DataFrame.info**: Başlangıç ​​olarak, bir `DataFrame`de bulunan içeriğin bir özetini yazdırmak için `info()` metodu kullanılır. Elimizde ne olduğunu görmek için bu veri kümesine bir göz atalım:

```python
iris_df.info()
```
```
RangeIndex: 150 entries, 0 to 149
Data columns (total 4 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   sepal length (cm)  150 non-null    float64
 1   sepal width (cm)   150 non-null    float64
 2   petal length (cm)  150 non-null    float64
 3   petal width (cm)   150 non-null    float64
dtypes: float64(4)
memory usage: 4.8 KB
```
Buradan itibaren, *Iris* veri setinin dört sütunda boş(null) girdi içermeyen 150 girdiye sahip olduğunu biliyoruz. Tüm veriler 64 bit kayan noktalı sayılar olarak saklanıyor.

- **DataFrame.head()**: Ardından, `DataFrame'in` gerçek içeriğini kontrol etmek için `head()` metodunu kullanıyoruz. `iris_df`'nin ilk birkaç satırının neye benzediğini görelim:
```python
iris_df.head()
```
```
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0                5.1               3.5                1.4               0.2
1                4.9               3.0                1.4               0.2
2                4.7               3.2                1.3               0.2
3                4.6               3.1                1.5               0.2
4                5.0               3.6                1.4               0.2
```
- **DataFrame.tail()**: Tersine, `Veri çerçevesinin` son birkaç satırını kontrol etmek için `tail ()` yöntemini kullanırız:
```python
iris_df.tail()
```
```
     sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
145                6.7               3.0                5.2               2.3
146                6.3               2.5                5.0               1.9
147                6.5               3.0                5.2               2.0
148                6.2               3.4                5.4               2.3
149                5.9               3.0                5.1               1.8
```
> **Bilgi:** Yalnızca bir DataFrame'deki bilgilerle ilgili metadata'ya(diğer bilgileri tanımlamak veya kullanmanıza yardımcı olmak için verilen bilgiler) veya birindeki ilk ve son birkaç değere bakarak bile, uğraştığınız verilerin boyutu, şekli ve içeriği hakkında anında bir fikir edinebilirsiniz.

## Kayıp Verinin Üstesinden Gelmek
> **Öğrenme hedefi:** Bu alt başlığın sonunda, null(boş) verileri nasıl doldurabileceğinizi veya silebileceğinizi öğrenmiş olacaksınız.

Çoğu zaman, kullanmak istediğiniz veri kümelerinin (kullanmak zorunda olduğunuz) içinde eksik değerler bulunur. Eksik verilerin nasıl ele alındığı, nihai analizinizi ve gerçek dünyadaki sonuçlarınızı etkileyebilecek ince uzlaşmaları beraberinde getirir. 

Pandas eksik verileri iki şekilde ele alır. İlki önceki bölümlerde gördüğünüz şekildedir: `NaN`, başka bir deyişle Bir sayı Değil (Not a Number). Bu aslında IEEE kayan nokta tanımlamasının bir parçası olan ve yalnızca eksik kayan nokta verilerini belirtmek için kullanılan özel bir değerdir.

Float(kayan noktalı sayı/ondalıklı sayı) dışındaki eksik değerler için pandas, Python `None` nesnesini kullanır. Aslında aynı şeyi söyleyen iki farklı değer türüyle karşılaşmanız kafa karıştırıcı görünse de, bu tasarım seçiminin sağlam programatik nedenleri vardır ve pratikte bu seçim birçok durumda pandas'ın düzgün çalışmasını sağlar. Buna rağmen, hem `None` hem de `NaN`, bunların nasıl kullanılabileceği konusunda dikkat etmeniz gereken kısıtlamalar taşır.

[Buradan](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb) `NaN` ve `None` hakkında daha fazla bilgi edinin!

- **Null değerleri tespit etme**: Pandas'ta `isnull()` ve `notnull()` metodları null verileri tespit etmek için birincil metodlardır. İkisi de veri için Boolean maskesi döndürür. `NaN` değerler için `numpy` kullanacağız:
```python
import numpy as np

example1 = pd.Series([0, np.nan, '', None])
example1.isnull()
```
```
0    False
1     True
2    False
3     True
dtype: bool
```
Çıktıya dikkatlice bakın. `0` aritmetik olarak null olsa da, yine de mükemmel bir tam sayıdır ve pandas buna göre davranır. `''` biraz daha farklıdır. Bölüm 1'de boş bir string değerini temsil etmek için kullanmış olsak da, yine de bir string nesnesidir ve pandas söz konusu olduğunda null değer değildir.

Şimdi bu metotları pratikte kullanacağınız şekilde kullanalım. Boole maskelerini doğrudan ``Seri`` veya ``DataFrame`` dizini olarak kullanabilirsiniz; bu, soyutlanmış eksik değerlerle çalışmaya çalışırken yararlı olabilir.

> **Bilgi**: `isnull()` ve `notnull()` metodlarının ikiside `DataFrame`'lerin içinde kullanıldığında benzer sonuçlar verir: sonuçları ve bu sonuçların indeksini gösterirler ki bu, verilerinizle boğuşurken size çok yardımcı olacaktır.

- **Null değerlerin silinmesi**: Kayıp verileri belirlemenin ötesinde, pandas `Seriler` ve `DataFrame`'lerden boş verileri silmek için uygun bir yol sunar. (Büyük veri setlerinde [NA] verileri silmek bunlarla uğraşmaktan daha çok önerilir.) Bunu görebilmek için `example1`'e geri dönelim:
```python
example1 = example1.dropna()
example1
```
```
0    0
2     
dtype: object
```
Bunun `example3[example3.notnull()]` çıktısı gibi görünmesi gerketiğini not edelim. Buradaki fark, yalnızca maskelenmiş değerleri indekslemek yerine, `dropna`'nın bu eksik değerleri `Seriler` `example1`'den silmesidir.

`DataFrame`'lerin iki boyutu olduğundan verileri silmek için daha fazla seçenek sunarlar.
```python
example2 = pd.DataFrame([[1,      np.nan, 7], 
                         [2,      5,      8], 
                         [np.nan, 6,      9]])
example2
```
|      | 0 | 1 | 2 |
|------|---|---|---|
|0     |1.0|NaN|7  |
|1     |2.0|5.0|8  |
|2     |NaN|6.0|9  |

(Pandas'ın, NaN'leri yerleştirmek için sütunlardan ikisini float'a çevirdiğini fark ettiniz mi?)

`DataFrame`'den tek bir değeri silemezsiniz, bu yüzden tüm bir satırı yada sütunu silmeniz gerekir. Ne yaptığınıza bağlı olarak, birini veya diğerini yapmak isteyebilirsiniz ve bu nedenle pandas size her ikisi için de seçenekler sunar. Veri biliminde sütunlar genellikle değişkenleri ve satırlar değişken gruplarının isimlerini(okul numaraları, köpek sayısı vb) temsil ettiğinden, satırları silme olasılığınız daha yüksektir; "dropna()" için varsayılan ayar, herhangi bir boş değer içeren tüm satırları silmektir:

```python
example2.dropna()
```
```
	0	1	2
1	2.0	5.0	8
```
Eğer gerekliyse, NA değerleri sütunlar için silmek mümkündür. Bunu yapmak için `axis=1` kullanılır:
```python
example2.dropna(axis='columns')
```
```
	2
0	7
1	8
2	9
```
Bunun, özellikle daha küçük veri setlerinde saklamak isteyebileceğiniz çok sayıda veriyi silebileceğine dikkat edin. Birkaç veya hatta tüm boş değerleri içeren satırları veya sütunları silmek isterseniz ne olur? Bu ayarı, `how` ve `thresh` parametreleriyle `dropna`'da belirtirsiniz.

Varsayılan olarak, `how='any'` (kendiniz kontrol etmek veya yöntemin diğer parametrelerinin neler olduğunu görmek isterseniz, bir kod hücresinde `example4.dropna?` komutunu çalıştırın). Alternatif olarak, yalnızca tüm boş değerleri içeren satırları veya sütunları silmek için `how='all'` olarak belirtebilirsiniz. Bunu çalışırken görmek için `DataFrame` örneğimizi genişletelim.

```python
example2[3] = np.nan
example2
```
|      |0  |1  |2  |3  |
|------|---|---|---|---|
|0     |1.0|NaN|7  |NaN|
|1     |2.0|5.0|8  |NaN|
|2     |NaN|6.0|9  |NaN|

`thresh` parametresi size daha ayrıntılı kontrol sağlar: bir satır veya sütunun silinmemesi için sahip olması gereken *boş olmayan(non-null)* değerlerin sayısını ayarlarsınız:
```python
example2.dropna(axis='rows', thresh=3)
```
```
	0	1	2	3
1	2.0	5.0	8	NaN
```
Burada, yalnızca iki boş olmayan değer içerdiğinden, ilk ve son satır silinmiştir.

- **Null değerleri doldurmak**: Veri setine bağlı olarak bazen null değerleri doldurmak onları silmekten daha mantıklıdır. Bunu yapmak için `isnull`'u kullanabilirsiniz, ancak bu, özellikle doldurmanız gereken çok fazla değer varsa, zahmetli olabilir. Bu, veri biliminde çok yaygın bir durum olduğundan, pandas, eksik değerlerin seçtiğiniz bir değerle değiştirildiği `Series` veya `DataFrame`'in bir kopyasını döndüren `fillna`'yı sağlar. Bunun pratikte nasıl çalıştığını görmek için başka bir `Series` örneği yapalım.
```python
example3 = pd.Series([1, np.nan, 2, None, 3], index=list('abcde'))
example3
```
```
a    1.0
b    NaN
c    2.0
d    NaN
e    3.0
dtype: float64
```
Tüm boş girdileri `0` gibi tek bir değerle doldurabilirsiniz:
```python
example3.fillna(0)
```
```
a    1.0
b    0.0
c    2.0
d    0.0
e    3.0
dtype: float64
```
Bir boş değeri doldurmak için son geçerli değeri kullanmak üzere boş değerleri **ileri doldurabilirsiniz(forward-fill)**:
```python
example3.fillna(method='ffill')
```
```
a    1.0
b    1.0
c    2.0
d    2.0
e    3.0
dtype: float64
```
Bir boş değeri doldurmak için bir sonraki geçerli değeri geriye doğru atamak için **geri doldur(back-fill)** da yapabilirsiniz:
```python
example3.fillna(method='bfill')
```
```
a    1.0
b    2.0
c    2.0
d    3.0
e    3.0
dtype: float64
```
Tahmin edebileceğiniz gibi, bu `DataFrame`'lerle de aynı şekilde çalışır, ayrıca boş değerlerin doldurulacağı bir `eksen(axis)` de belirtebilirsiniz. daha önce kullanılan `example2`'yi tekrar kullanarak:
```python
example2.fillna(method='ffill', axis=1)
```
```
	0	1	2	3
0	1.0	1.0	7.0	7.0
1	2.0	5.0	8.0	8.0
2	NaN	6.0	9.0	9.0
```
İleriye doğru doldurma için önceki bir değer mevcut olmadığında, boş değerin aynı kaldığına dikkat edin.

> **Bilgi:** Veri setlerinizdeki kayıp değerlerle başa çıkmanın birden çok yolu vardır. Kullandığınız strateji (bunları kaldırmak, değiştirmek veya hatta nasıl değiştireceğiniz) bu verilerin ayrıntılarına göre belirlenmelidir. Veri kümelerini ne kadar çok ele alır ve etkileşime girerseniz, eksik değerlerle nasıl başa çıkacağınız konusunda o kadar başarılı olursunuz.

## Yinelenen verileri silme

> **Öğrenme hedefi:** Bu alt başlığın sonunda DataFrame'lerin içindeki yinelenen verileri bulma ve silme konusunda bilgi sahibi olacaksınız.

Eksik verilere ek olarak, gerçek dünyadaki veri setlerinde sıklıkla yinelenen verilerle karşılaşacaksınız. Neyse ki, `pandas` yinelenen girdileri tespit etmek ve kaldırmak için kolay yollar sağlar.

- **Yinelenen verilerin saptanması: `duplicated`**: Pandas'da `duplicated` metodunu kullanarak yinelenen değerleri kolayca tespit edebilirsiniz; bu, `DataFrame`'deki bir girdinin daha önceki bir girdinin kopyası olup olmadığını gösteren bir Boole maskesi döndürür. Bunu çalışırken görmek için başka bir `DataFrame` örneği oluşturalım.
```python
example4 = pd.DataFrame({'letters': ['A','B'] * 2 + ['B'],
                         'numbers': [1, 2, 1, 3, 3]})
example4
```
|      |letters|numbers|
|------|-------|-------|
|0     |A      |1      |
|1     |B      |2      |
|2     |A      |1      |
|3     |B      |3      |
|4     |B      |3      |

```python
example4.duplicated()
```
```
0    False
1    False
2     True
3    False
4     True
dtype: bool
```
- **Yinelenen verilerin silinmesi**: `drop_duplicates`: `drop_duplicates`, tüm `yinelenen` değerlerin `False` olduğu verilerin bir kopyasını döndürür:
```python
example4.drop_duplicates()
```
```
	letters	numbers
0	A	1
1	B	2
3	B	3
```
Hem `duplicated` hem de `drop_duplicates` varsayılan olarak tüm sütunları dikkate alır, ancak bunların `DataFrame`'inizdeki yalnızca bir sütunun alt kümesini incelemelerini sağlayabilirsiniz:
```python
example6.drop_duplicates(['letters'])
```
```
letters	numbers
0	A	1
1	B	2
```

> **Bilgi:** Yinelenen verileri kaldırmak, hemen hemen her veri bilimi projesinin önemli bir parçasıdır. Yinelenen veriler, analizlerinizin sonuçlarını değiştirebilir ve size yanlış sonuçlar verebilir!


## 🚀 Challenge

Konuştuğumuz bütün materyaller burada sağlanıyor [Jupyter Notebook](https://github.com/microsoft/Data-Science-For-Beginners/blob/main/4-Data-Science-Lifecycle/15-analyzing/notebook.ipynb). Ek olarak, her bölümden sonra alıştırmalar var, bunları yapmayı deneyin!

## [Ders Sonu Kısa Sınavı](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/15)



## İnceleme & Bireysel Çalışma

Veriyi analiz ve modelleme için hazırlamanın ve veriyi temizlemenin "uygulamalı" bir deneyim olan önemli bir adım olduğunu keşfetmenin birçok yolu vardır. Bu dersin kapsamadığı teknikleri keşfetmek için Kaggle'dan bu challengeları deneyin.

- [Data Cleaning Challenge: Parsing Dates](https://www.kaggle.com/rtatman/data-cleaning-challenge-parsing-dates/)

- [Data Cleaning Challenge: Scale and Normalize Data](https://www.kaggle.com/rtatman/data-cleaning-challenge-scale-and-normalize-data)


## Ödev

[Bir Formdaki Verilerin Değerlendirilmesi](../08_assignment.md)

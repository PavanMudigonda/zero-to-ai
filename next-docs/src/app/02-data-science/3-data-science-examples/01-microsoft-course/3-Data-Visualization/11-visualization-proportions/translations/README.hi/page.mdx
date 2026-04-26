# विज़ुअलाइज़िंग अनुपात

|![ सकेटच्नोते करने वाला [(@sketchthedocs)](https://sketchthedocs.dev) ](../../sketchnotes/11-Visualizing-Proportions.png)|
|:---:|
|विज़ुअलाइज़िंग अनुपात - _सकेटच्नोते करने वाला [@nitya](https://twitter.com/nitya)_ |

इस पाठ में, आप अनुपात की कल्पना करने के लिए एक अलग प्रकृति-केंद्रित डेटासेट का उपयोग करेंगे, जैसे कि मशरूम के बारे में दिए गए डेटासेट में कितने अलग-अलग प्रकार के कवक आते हैं। आइए ऑडबोन सूची से प्राप्त डेटासेट का उपयोग करके इन आकर्षक कवक का पता लगाएं, एग्रिकस और लेपियोटा परिवारों में ग्रील्ड मशरूम की 23 प्रजातियों के बारे में विवरण। आप स्वादिष्ट विज़ुअलाइज़ेशन के साथ प्रयोग करेंगे जैसे:

- पाई चार्ट 🥧
- डोनट चार्ट 🍩
- वफ़ल चार्ट 🧇


> 💡 माइक्रोसॉफ्ट अनुसंधान द्वारा [चार्टिकुलेटर](https://charticulator.com) नामक एक बहुत ही रोचक परियोजना डेटा विज़ुअलाइज़ेशन के लिए एक निःशुल्क ड्रैग एंड ड्रॉप इंटरफ़ेस प्रदान करती है। अपने एक ट्यूटोरियल में वे इस मशरूम डेटासेट का भी उपयोग करते हैं! तो आप एक ही समय में डेटा का पता लगा सकते हैं और पुस्तकालय सीख सकते हैं: [चार्टिकुलेटर ट्यूटोरियल](https://charticulator.com/tutorials/tutorial4.html)।

## [प्री-लेक्चर क्विज](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/20)

## अपने मशरूम को जानें 🍄

मशरूम बहुत दिलचस्प हैं। आइए उनका अध्ययन करने के लिए एक डेटासेट आयात करें:

```python
import pandas as pd
import matplotlib.pyplot as plt
mushrooms = pd.read_csv('../../data/mushrooms.csv')
mushrooms.head()
```
विश्लेषण के लिए कुछ महान डेटा के साथ एक तालिका मुद्रित की जाती है:


| class     | cap-shape | cap-surface | cap-color | bruises | odor    | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | stalk-root | stalk-surface-above-ring | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ------- | --------------- | ------------ | --------- | ---------- | ----------- | ---------- | ------------------------ | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| Poisonous | Convex    | Smooth      | Brown     | Bruises | Pungent | Free            | Close        | Narrow    | Black      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |
| Edible    | Convex    | Smooth      | Yellow    | Bruises | Almond  | Free            | Close        | Broad     | Black      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Grasses |
| Edible    | Bell      | Smooth      | White     | Bruises | Anise   | Free            | Close        | Broad     | Brown      | Enlarging   | Club       | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Brown             | Numerous   | Meadows |
| Poisonous | Convex    | Scaly       | White     | Bruises | Pungent | Free            | Close        | Narrow    | Brown      | Enlarging   | Equal      | Smooth                   | Smooth                   | White                  | White                  | Partial   | White      | One         | Pendant   | Black             | Scattered  | Urban   |

तुरंत, आप देखते हैं कि सभी डेटा टेक्स्टुअल है। चार्ट में इसका उपयोग करने में सक्षम होने के लिए आपको इस डेटा को परिवर्तित करना होगा। अधिकांश डेटा, वास्तव में, एक वस्तु के रूप में दर्शाया जाता है:

```python
print(mushrooms.select_dtypes(["object"]).columns)
```

आउटपुट है:

```output
Index(['class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
       'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
       'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
       'stalk-surface-below-ring', 'stalk-color-above-ring',
       'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
       'ring-type', 'spore-print-color', 'population', 'habitat'],
      dtype='object')
```
यह डेटा लें और 'वर्ग' कॉलम को एक श्रेणी में बदलें:

```python
cols = mushrooms.select_dtypes(["object"]).columns
mushrooms[cols] = mushrooms[cols].astype('category')
```
अब, यदि आप मशरूम डेटा का प्रिंट आउट लेते हैं, तो आप देख सकते हैं कि इसे जहरीले/खाद्य वर्ग के अनुसार श्रेणियों में बांटा गया है:


|           | cap-shape | cap-surface | cap-color | bruises | odor | gill-attachment | gill-spacing | gill-size | gill-color | stalk-shape | ... | stalk-surface-below-ring | stalk-color-above-ring | stalk-color-below-ring | veil-type | veil-color | ring-number | ring-type | spore-print-color | population | habitat |
| --------- | --------- | ----------- | --------- | ------- | ---- | --------------- | ------------ | --------- | ---------- | ----------- | --- | ------------------------ | ---------------------- | ---------------------- | --------- | ---------- | ----------- | --------- | ----------------- | ---------- | ------- |
| class     |           |             |           |         |      |                 |              |           |            |             |     |                          |                        |                        |           |            |             |           |                   |            |         |
| Edible    | 4208      | 4208        | 4208      | 4208    | 4208 | 4208            | 4208         | 4208      | 4208       | 4208        | ... | 4208                     | 4208                   | 4208                   | 4208      | 4208       | 4208        | 4208      | 4208              | 4208       | 4208    |
| Poisonous | 3916      | 3916        | 3916      | 3916    | 3916 | 3916            | 3916         | 3916      | 3916       | 3916        | ... | 3916                     | 3916                   | 3916                   | 3916      | 3916       | 3916        | 3916      | 3916              | 3916       | 3916    |

यदि आप अपने वर्ग श्रेणी लेबल बनाने के लिए इस तालिका में प्रस्तुत क्रम का पालन करते हैं, तो आप एक पाई चार्ट बना सकते हैं:

## Pie!

```python
labels=['Edible','Poisonous']
plt.pie(edibleclass['population'],labels=labels,autopct='%.1f %%')
plt.title('Edible?')
plt.show()
```
वोइला, मशरूम के इन दो वर्गों के अनुसार इस डेटा के अनुपात को दर्शाने वाला एक पाई चार्ट। लेबल के क्रम को सही करना बहुत महत्वपूर्ण है, विशेष रूप से यहां, इसलिए उस क्रम को सत्यापित करना सुनिश्चित करें जिसके साथ लेबल सरणी बनाई गई है!

![पाई चार्ट](images/pie1.png)

## डोनट्स!

कुछ अधिक नेत्रहीन दिलचस्प पाई चार्ट एक डोनट चार्ट है, जो बीच में एक छेद के साथ एक पाई चार्ट है। आइए इस पद्धति का उपयोग करके हमारे डेटा को देखें।

विभिन्न आवासों पर एक नज़र डालें जहाँ मशरूम उगते हैं:

```python
habitat=mushrooms.groupby(['habitat']).count()
habitat
```
यहां, आप अपने डेटा को आवास के आधार पर समूहित कर रहे हैं। 7 सूचीबद्ध हैं, इसलिए उन्हें अपने डोनट चार्ट के लिए लेबल के रूप में उपयोग करें:

```python
labels=['Grasses','Leaves','Meadows','Paths','Urban','Waste','Wood']

plt.pie(habitat['class'], labels=labels,
        autopct='%1.1f%%', pctdistance=0.85)
  
center_circle = plt.Circle((0, 0), 0.40, fc='white')
fig = plt.gcf()

fig.gca().add_artist(center_circle)
  
plt.title('Mushroom Habitats')
  
plt.show()
```

![डोनट चार्ट](images/donut.png)

यह कोड एक चार्ट और एक केंद्र वृत्त बनाता है, फिर उस केंद्र वृत्त को चार्ट में जोड़ता है। `0.40` को दूसरे मान में बदलकर केंद्र वृत्त की चौड़ाई संपादित करें।

डोनट चार्ट को लेबल बदलने के लिए कई तरह से ट्वीक किया जा सकता है। विशेष रूप से लेबल को पठनीयता के लिए हाइलाइट किया जा सकता है। [दस्तावेज़] (https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html?highlight=donut) में और जानें।

अब जबकि आप जानते हैं कि अपने डेटा को कैसे समूहबद्ध करना है और फिर उसे पाई या डोनट के रूप में प्रदर्शित करना है, तो आप अन्य प्रकार के चार्टों को एक्सप्लोर कर सकते हैं। एक वफ़ल चार्ट आज़माएं, जो मात्रा की खोज का एक अलग तरीका है।
## Waffles!

एक 'वफ़ल' प्रकार का चार्ट मात्राओं को वर्गों के 2डी सरणी के रूप में देखने का एक अलग तरीका है। इस डेटासेट में मशरूम कैप रंगों की विभिन्न मात्राओं को देखने का प्रयास करें। ऐसा करने के लिए, आपको [PyWaffle](https://pypi.org/project/pywaffle/) नामक एक सहायक पुस्तकालय स्थापित करने और Matplotlib का उपयोग करने की आवश्यकता है:

```python
pip install pywaffle
```

समूह के लिए अपने डेटा का एक खंड चुनें:

```python
capcolor=mushrooms.groupby(['cap-color']).count()
capcolor
```

लेबल बनाकर और फिर अपने डेटा को समूहीकृत करके एक वफ़ल चार्ट बनाएं:

```python
import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
  
data ={'color': ['brown', 'buff', 'cinnamon', 'green', 'pink', 'purple', 'red', 'white', 'yellow'],
    'amount': capcolor['class']
     }
  
df = pd.DataFrame(data)
  
fig = plt.figure(
    FigureClass = Waffle,
    rows = 100,
    values = df.amount,
    labels = list(df.color),
    figsize = (30,30),
    colors=["brown", "tan", "maroon", "green", "pink", "purple", "red", "whitesmoke", "yellow"],
)
```

वफ़ल चार्ट का उपयोग करके, आप स्पष्ट रूप से इस मशरूम डेटासेट के कैप रंगों के अनुपात को देख सकते हैं। दिलचस्प बात यह है कि कई हरे-छिपे हुए मशरूम हैं!

![वफ़ल चार्ट](images/waffle.png)

✅ Pywaffle उन चार्ट के भीतर आइकन का समर्थन करता है जो [Font Awesome](https://fontawesome.com/) में उपलब्ध किसी भी आइकन का उपयोग करते हैं। वर्गों के बजाय आइकन का उपयोग करके और भी अधिक रोचक वफ़ल चार्ट बनाने के लिए कुछ प्रयोग करें।

इस पाठ में, आपने अनुपातों की कल्पना करने के तीन तरीके सीखे। सबसे पहले, आपको अपने डेटा को श्रेणियों में समूहित करना होगा और फिर यह तय करना होगा कि डेटा प्रदर्शित करने का सबसे अच्छा तरीका कौन सा है - पाई, डोनट, या वफ़ल। सभी स्वादिष्ट हैं और डेटासेट के तत्काल स्नैपशॉट के साथ उपयोगकर्ता को संतुष्ट करते हैं।
## 🚀 चुनौती

इन स्वादिष्ट चार्ट को फिर से बनाने का प्रयास करें [चार्टिकुलेटर](https://charticulator.com).
## [व्याख्यान के बाद प्रश्नोत्तरी](https://purple-hill-04aebfb03.1.azurestaticapps.net/quiz/21)

## समीक्षा और आत्म अध्ययन

कभी-कभी यह स्पष्ट नहीं होता कि पाई, डोनट, या वफ़ल चार्ट का उपयोग कब करना है। इस विषय पर पढ़ने के लिए यहां कुछ लेख दिए गए हैं:

https://www.beautiful.ai/blog/battle-of-the-charts-pie-chart-vs-donut-chart

https://medium.com/@hypsypops/pie-chart-vs-donut-chart-showdown-in-the-ring-5d24fd86a9ce

https://www.mit.edu/~mbarker/formula1/f1help/11-ch-c6.htm

https://medium.datadriveninvestor.com/data-visualization-done-the-right-way-with-tableau-waffle-chart-fdf2a19be402

इस चिपचिपे निर्णय के बारे में अधिक जानकारी प्राप्त करने के लिए कुछ शोध करें।
## कार्यभार

[इसे एक्सेल में आज़माएं](08_assignment.md)

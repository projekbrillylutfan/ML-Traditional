# -*- coding: utf-8 -*-
"""Proyek_Pertama_Predictive_Analytics_Dicoding_Machine_Learning_Terapan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15trJJB9PAdTxTfXu_eB1bXRkCeUgfNg-

# **Prediksi Harga Rumah di Wilayah California**
* Nama : Brilly Lutfan Qasthari
* Dataset : https://www.kaggle.com/datasets/shibumohapatra/house-price

## Domain Proyek
### Latar Belakang
Pasar real estat adalah salah satu sektor ekonomi terpenting dan harga real estat merupakan faktor kunci dalam keputusan pembelian real estat. Kemampuan memprediksi harga rumah dengan akurasi tinggi dapat membantu calon pembeli, penjual, dan pemangku kepentingan lainnya membuat keputusan yang lebih tepat. 

Pasar real estate di California sangat dinamis dan harga real estate seringkali sangat berfluktuasi. Oleh karena itu, memprediksi real estat dalam konteks ini merupakan tantangan yang menarik. Dalam *submission* ini, berfokus pada penggunaan model regresi pembelajaran mesin untuk memprediksi harga rumah di California [[1](https://www.researchgate.net/publication/350345452_Prediksi_Harga_Rumah_Menggunakan_Web_Scrapping_dan_Machine_Learning_Dengan_Algoritma_Linear_Regression)]. 

Model regresi *machine learning* adalah cara ampuh untuk mengeksplorasi pola dan hubungan antara karakteristik data dan variabel target, dalam hal ini harga rumah. Dengan menggunakan teknik regresi, model tersebut dapat digunakan untuk mempelajari pola harga properti berdasarkan karakteristik seperti lokasi, ukuran rumah, jumlah kamar tidur, dan faktor lain yang relevan [[2](https://ejournal.bsi.ac.id/ejurnal/index.php/ji/article/download/9036/pdf)].

Tujuan dari *submission* ini adalah mengembangkan model *machine learning* yang dapat memprediksi harga real estat di California dengan MSE(*Mean Squared Error*) kecil. Model ini dapat memberikan informasi berharga kepada calon pembeli rumah, agen real estat, dan pemangku kepentingan lainnya dalam keputusan penetapan harga rumah mereka.

## **Data Collection**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

!git clone https://github.com/projekbrillylutfan/kumpulan_dataset

df_train = pd.read_csv("/content/kumpulan_dataset/california house price dataset/train.csv")
df_train

"""## Business Understanding
Wawasan bisnis dari dataset harga rumah California adalah membangun model *machine learning* yang dapat memprediksi harga rumah berdasarkan karakteristik seperti lokasi geografis, ukuran rumah, jumlah kamar tidur dan kamar mandi, dan faktor terkait lainnya. Tujuan dari *submission* ini adalah untuk menyediakan calon pembeli rumah, penjual, agen real estate dan investor dengan informasi yang akurat dan berharga untuk membuat keputusan pembelian, penjualan dan investasi yang terinformasi di pasar real estate California yang dinamis. 

### Problem Statements
- Fitur apa saja yang mempengaruhi dalam menentukan prediksi harga rumah di California ?
- Bagaimana data diproses agar model dapat melatihnya dengan baik ? 
- Bagaimana peran *hyperparameter tuning* dalam peforma model *machine learning* ? 

### Goals
- Mengetahui jenis fitur yang berpengaruh terhadap harga rumah di California.
- Melakukan sebuah persiapan data untuk dilakukan proses pelatihan model.
- Mengetahui apakah *hyperparameter tuning* berpengaruh terhadap model yang dihasilkan.

### Solution statements
- Menganalisis data dengan melakukan analisis *univariate* dan *multivariate*. Memahami informasi juga dapat dilakukan dengan bantuan visualisasi. Memahami data dapat membantu menemukan korelasi antara karakteristik dan mengidentifikasi outlier. 
- Mempersiapkan data yang akan digunakan untuk membuat model.
- Menggunakan 1 model *machine learning* bernama XGBoost regresi untuk mengetahui apakah *hyperparameter tuning* berpengaruh terhadap data yang telah disediakan. Model akan terdefinisi menjadi 2 kategori yaitu yang menggunakan *hyperparameter tuning* dan yang tidak menggunakan
- Menggunakan data testing yang telah disediakan untuk menganalisis prediksi harga rumah di California

# **Data Understanding**
Dataset yang digunakan pada submisson ini merupaka data yang memuat karakteristik yang ada di daerah california. Dataset ini dapat di unduh melalui website kaggle dengan judul berupa [*California House Price*](https://www.kaggle.com/datasets/shibumohapatra/house-price).

Berikut merupakan rincian dari informasi dataset :
+ Dataset bertipe format CSV (Comma-Seperated Values).
+ Dataset ini memiliki 20640 baris dan 10 kolom.
+ Dataset hanya memiliki 1 data kategorika dan sisanya merupakan data numerik.
+ Dataset memiliki *missing value* di kolom total_bedrooms dan bisa diatasi dengan teknik imputasi.

### Rincian variabel pada dataset
+ longitude (signed numeric - float) : Nilai bujur untuk blok di California Amerika Serikat
+ latitude (numeric - float ) : Nilai lintang untuk blok di California, AS
+ housing_median_age (numeric - int ) : Usia rata-rata rumah di blok tersebut
+ total_rooms (numeric - int ) : Hitungan jumlah total kamar (tidak termasuk kamar tidur) di semua rumah di blok tersebut
+ total_bedrooms (numeric - float ) : Hitungan jumlah total kamar tidur di semua rumah di blok tersebut
+ population (numeric - int ) : Hitungan jumlah total populasi di blok
+ households (numeric - int ) : Hitungan jumlah total rumah tangga di blok tersebut
+ median_income (numeric - float ) : Median dari total pendapatan rumah tangga dari semua rumah di blok tersebut
+ ocean_proximity (numeric - categorical ) : Jenis lanskap blok [ Unique Values : 'NEAR BAY', '1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND' ]
+ median_house_value (numeric - int ) : Median harga rumah tangga dari semua rumah di blok tersebut
"""

df_train.info()

df_train.describe()

df_train.shape

"""## **Missing Value**"""

df_train.isna().sum()

df_train.duplicated().sum()

for col in df_train.select_dtypes(include=[np.number]).columns:
    count = (df_train[col] == 0).sum()
    print(f"Nilai 0 di kolom {col} ada: {count}")

#mengisi nilai null di kolom total bedrooms
df_train['total_bedrooms'] = df_train['total_bedrooms'].fillna(df_train['total_bedrooms'].median())

df_train.isna().sum()

df_train.describe()

df_train["ocean_proximity"].value_counts()

df_train['ocean_proximity'] = df_train['ocean_proximity'].replace('<1H OCEAN', '1H OCEAN')

df_train["ocean_proximity"].value_counts()

"""# **Menangani Outliers**"""

sns.boxplot(x=df_train['longitude'])

sns.boxplot(x=df_train['latitude'])

sns.boxplot(x=df_train['housing_median_age'])

sns.boxplot(x=df_train['total_rooms'])

sns.boxplot(x=df_train['total_bedrooms'])

sns.boxplot(x=df_train['population'])

sns.boxplot(x=df_train['households'])

sns.boxplot(x=df_train['median_income'])

sns.boxplot(x=df_train['median_house_value'])

df_train.shape

Q1 = df_train.quantile(0.25)
Q3 = df_train.quantile(0.75)
IQR=Q3-Q1
df_train=df_train[~((df_train<(Q1-1.5*IQR))|(df_train>(Q3+1.5*IQR))).any(axis=1)]
 
# Cek ukuran dataset setelah kita drop outliers
df_train.shape

"""# **Univariate Analysis**
proses menganalisis dan memahami suatu variabel dalam kumpulan data tanpa mempertimbangkan hubungannya dengan variabel lain. Tujuan dari analisis univariat adalah untuk mendapatkan gambaran mengenai distribusi, karakteristik dan pola dari variabel-variabel tersebut. 

#### Analisis fitur kategori
Untuk dataset ini, fitur kategori hanya berjumlah satu kolom yaitu fitur ocean_proximity. berikut rincian dari fitur ocean_proximity :

![ocean_proximity](https://i.ibb.co/Mnq5ccT/ocean.png)
Pada kolom ocean_proximity distribusi data tidak merata hal ini dapat dilihat pada rincian visualisai tersebut, dimana 1H OCEAN memiliki data terbanya dengan total sebesar 7531 sampel dengan presentase sebesar 43%. Data ISLAND memiliki jumlah perseberan yang sedikit yaitu sebesar 5 sampel saja.

#### Analisis fitur numerik
![numerik_1](https://i.ibb.co/6HBQmXv/numerik-1.png)
![numerik_2](https://i.ibb.co/Sd93yPJ/numerik-2.png)

Berikut merupakan rincian persebaran fitur numerik :
+ Fitur bujur dan lintang memiliki korelasi yang kuat dikarenakan kedua fitur tersebut memiliki korelasi tinggi.
+ Rata-rata median dari umur rumah terbanyak yaitu di rentang umur 10 - 50.
+ Rata-rata terbanyak pada fitur total room dan total bedroom ada di angka 2634 room dan 536 bedroom.
+ Populasi terbanyak ada di angka 35682 jiwa dan memiliki nila rata-rata sebesar 1424 jiwa.
+ Jumlah rumah tangga terbanyak di angka 6082 dan memiliki nilai rata-rata sebesar 499.
+ Untuk fitur median_income, longitude dan latitude sebenarnya tidak diperlukan. Akan tetapi fitur ini dimasukkan guna untuk pengujian kualitas model yang akan dihasilkan.
"""

data_numerik = df_train.select_dtypes(include=[np.number]).columns
data_numerik

data_kategori = df_train.select_dtypes(exclude=[np.number]).columns
data_kategori

fitur_numerik = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value']

fitur_kategori = ['ocean_proximity']

#mengecek distribusi data untuk kolom kategori ocean proximity
feature = fitur_kategori[0]
count = df_train[feature].value_counts()
percent = 100 * df_train[feature].value_counts(normalize = True)
df = pd.DataFrame({'jumlah sampel':count, 'persentase':percent.round(1)})
print(df)
count.plot(kind='bar', title=feature);

df_train.hist(bins = 50, figsize = (20,15))
plt.show()

"""# **Multivariate Analysis**
Multivariate Analysis adalah Suatu analisis dilakukan untuk memahami hubungan antara dua variabel atau lebih secara bersamaan. Dalam analisis multivariat, kita melihat lebih dari satu variabel dalam analisis yang sama untuk melihat bagaimana variabel tersebut berhubungan, berinteraksi, atau saling mempengaruhi. Tujuan analisis multivariat adalah untuk mendapatkan pemahaman yang lebih lengkap tentang pola, tren, dan hubungan yang mungkin ada di antara variabel-variabel tersebut. Teknik yang biasa digunakan dalam analisis multivariat antara lain analisis regresi, analisis faktor, analisis kluster, analisis diskriminan, dll.

#### Analisis fitur kategori

![Multi_kategori](https://i.ibb.co/vQL0DZL/multi-kategori.png)
Untuk analisis Multi fitur yang digunakan untuk pengujian ini merupakan fitur yang akan di prediksi yaitu fitur median_house_value. harga rumah tertinggi ada di daerah pulau dan harga rumah terendah berada di daerah pedalaman atau pedesaan.

#### Analisis fitur numerik

![Multi_numerik](https://i.ibb.co/C8mHgxr/multi-korelasi.png)

Berikut merupakan rincian korelasi fitur numerik :
+ Fitur bujur tidak memiliki korelasi yang tinggi terhadap median house value hal ini terbukti dengan nilai korelai negatif -0.04.
+ Fitur lintang sama dengan fitur bujur yaitu tidak memiliki korelasi yang tinggi terhadap median house value dengan nilai korelasi sebesar negatif -0.16.
+ Fitur median umur rumah juga tidak memiliki nilai korelasi yang tinggi terhadap median house value dengan nilai korelasi positif 0.1.
+ Fitur jumlah kamar tidak memiliki nilai korelasi yang tinggi dengan median house value dengan nilai korelasi sebesar positif 0.09.
+ nilai korelasi dari fitur populasi dan rumah tangga juga tidak memiliki korelasi yang tinggi terhadap median house value dengan nilai korelasi sebesar negatif -0.01 untuk populasi dan positif 0.12 untuk rumah tangga.
+ Median income hanya satu-satu nya yang memiliki nilai korelasi yang besar yaitu 0.63

Untuk itu, fitur populasi memiliki nilai korelasi terkecil dari nilai korelasi fitur lainnya. Sehingga fitur populasi dihapus dari dataset.
"""

cat_features = df_train.select_dtypes(include='object').columns.to_list()
 
for col in cat_features:
  sns.catplot(x=col, y="median_house_value", kind="bar", dodge=False, height = 4, aspect = 3,  data=df_train, palette="Set3")
  plt.title("Rata-rata harga rumah Relatif terhadap - {}".format(col))

sns.pairplot(df_train, diag_kind = 'kde')

plt.figure(figsize=(10, 8))
correlation_matrix = df_train.corr().round(2)
 
# Untuk menge-print nilai di dalam kotak, gunakan parameter anot=True
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, )
plt.title("Correlation Matrix untuk Fitur Numerik ", size=20)

df_train.drop(['population'], inplace=True, axis=1)
df_train.head()

"""# **Data Preparation**
Persiapan data adalah proses persiapan data sebelum dilakukan analisis atau pemodelan. Tujuan dari persiapan data adalah untuk memastikan bahwa data yang digunakan dalam analisis atau pemodelan telah disiapkan, terstruktur dan memenuhi persyaratan. Beberapa langkah yang dilakukan dalam Data Preparation meliputi:

- Cleaning (Pembersihan): Melakukan identifikasi dan penanganan terhadap missing values (nilai kosong), outlier (nilai ekstrim), atau data yang tidak konsisten.
- Transformation (Transformasi): Melakukan transformasi terhadap data seperti normalisasi, standarisasi, atau pengubahan skala untuk memastikan data memiliki distribusi yang tepat.
- One Hot Encoding : Algoritma *machine learning* biasanya hanya dapat memproses data numerik. Pengkodean satu-panas memungkinkan variabel kategori untuk diubah menjadi representasi biner yang dapat dimanipulasi oleh suatu algoritma. 
- Train Test Split : Dalam *machine learning*, kita ingin mengevaluasi seberapa baik model dapat melakukan prediksi pada data yang belum pernah dilihat sebelumnya. Dengan membagi data menjadi train dan test set, dapat melatih model pada train set dan kemudian menguji performanya pada test set. Ini memberikan indikasi seberapa baik model dapat menggeneralisasi pada data yang baru.
"""

from sklearn.preprocessing import OneHotEncoder

df_train = pd.concat([df_train, pd.get_dummies(df_train['ocean_proximity'], prefix='ocean_proximity')],axis=1)

df_train.drop(['ocean_proximity'], axis=1, inplace=True)
df_train.head()

"""# **Train-Test-Split**"""

from sklearn.model_selection import train_test_split
 
X = df_train.drop(["median_house_value"],axis =1)
y = df_train["median_house_value"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 123)

print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

from sklearn.preprocessing import StandardScaler

fitur_numerik2 = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'households', 'median_income']
scaler = StandardScaler()
scaler.fit(X_train[fitur_numerik2])
X_train[fitur_numerik2] = scaler.transform(X_train.loc[:, fitur_numerik2])
X_train[fitur_numerik2].head()

X_train[fitur_numerik2].describe().round(4)

X_train.head()

y_train.head()

"""# **Modeling With Machine Learning**
Pada tahap modeling ini akan menjadi tahap jawaban untuk problem statement sebelum nya yaitu mengenai diproses nya data agar model dapat melatihnya dan peran *hyperparameter tuning* pada model yang digunakan. Untuk model yang digunakan merupakan model bertipa regresi dengan pemanfaatan model XGBoost.

+ XGBoost regresi merupakan adalah sebuah algoritma machine learning yang populer dan efektif dalam melakukan tugas-tugas regresi. XGBoost regresi merupakan varian dari algoritma XGBoost yang digunakan khusus untuk memodelkan dan memprediksi variabel target kontinu (numerik). XGBoost regresi bekerja dengan membangun serangkaian pohon keputusan secara bertahap. Pada setiap tahap, model mencoba memperbaiki kesalahan prediksi dari tahap sebelumnya dengan menambahkan pohon baru. Proses ini dilakukan secara berulang hingga mencapai jumlah pohon yang ditentukan atau mencapai titik di mana penambahan pohon tidak memberikan peningkatan yang signifikan dalam kinerja model.XGBoost regresi memiliki beberapa keunggulan, antara lain: 
  + Kemampuan untuk menangani data dengan fitur-fitur yang beragam, baik kategorikal maupun numerik.
  + Kecepatan dan efisiensi yang tinggi, sehingga cocok untuk dataset yang besar.
  + Mampu menangani interaksi non-linear antar fitur.
  + Kemampuan untuk menangani missing values pada dataset.
  + Adanya mekanisme regularisasi yang membantu mengurangi overfitting.
+ Penggunaan *Hyperparameter Tuning*
  Grid Search adalah salah satu teknik yang digunakan dalam pemilihan parameter optimal untuk model machine learning. Tujuan dari Grid Search adalah untuk mencari kombinasi parameter terbaik yang memberikan performa model yang optimal. berikut parmeter yang digunakan pada proyek ini :
  + `n_estimators` : jumlah estimator ketika boosting dihentikan.
  + `max_depth` : jumlah kedalaman maksimum dari semua tree.
  + `learning_rate` : untuk memperkuat kontribusi dalam setiap regresor.
+ Setingan parmeter yang digunakan GridSearch untuk proyek ini:
   model    | best_params                                                     |
  |----------|-----------------------------------------------------------------|
  | XGBoost Regresor    | {'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 300}                                              |
"""

from sklearn.model_selection import GridSearchCV
#from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor

"""##Tidak Menggunakan Fine Tuning"""

model = XGBRegressor()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

"""##Menggunakan Fine Tuning"""

param_Grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 4, 5],
    'learning_rate': [0.1, 0.01, 0.001]
}

model2 = XGBRegressor()

grid_search = GridSearchCV(estimator=model, param_grid=param_Grid, scoring='neg_mean_squared_error', cv=5)

grid_search.fit(X_train, y_train)

print("Parameter Terbaik :", grid_search.best_params_)

print("Best MSE:", -grid_search.best_score_)

xgb_FT_Param = XGBRegressor(learning_rate = 0.1, max_depth = 5, n_estimators = 300)

xgb_FT_Param.fit(X_train, y_train)

y_pred2 = xgb_FT_Param.predict(X_test)

mse = mean_squared_error(y_test, y_pred2)
print("Mean Squared Error:", mse)

mse = pd.DataFrame(columns=['train', 'test'], index=['XGBoost_Non_HP','XGBoost_Wth_HP'])
model_save = {'XGBoost_Non_HP': model, 'XGBoost_Wth_HP': xgb_FT_Param}

for name, model in model_save.items():
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
      
    mse.loc[name, 'train'] = mean_squared_error(y_train, y_train_pred) / 1e3
    mse.loc[name, 'test'] = mean_squared_error(y_test, y_test_pred) / 1e3

mse

"""#**Prediksi Menggunakan Data Testing**"""

df_tes = pd.read_csv('/content/kumpulan_dataset/california house price dataset/test.csv')

df_tes.head()

df_tes.drop(['median_house_value', 'population'], inplace=True, axis=1)
df_tes.head()

df_tes.isna().sum()

df_tes.duplicated().sum()

for col in df_tes.select_dtypes(include=[np.number]).columns:
    count = (df_tes[col] == 0).sum()
    print(f"Nilai 0 di kolom {col} ada: {count}")

#mengisi nilai null di kolom total bedrooms
df_tes['total_bedrooms'] = df_tes['total_bedrooms'].fillna(df_tes['total_bedrooms'].median())

df_tes.isna().sum()

df_tes['ocean_proximity'] = df_tes['ocean_proximity'].replace('<1H OCEAN', '1H OCEAN')

df_tes.head()

df_tes.describe()

df_tes = pd.concat([df_tes, pd.get_dummies(df_tes['ocean_proximity'], prefix='ocean_proximity')],axis=1)

df_tes.drop(['ocean_proximity'], axis=1, inplace=True)
df_tes.head()

fitur_numerik3 = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'households', 'median_income']
scaler = StandardScaler()
scaler.fit(df_tes[fitur_numerik3])
df_tes[fitur_numerik3] = scaler.transform(df_tes.loc[:, fitur_numerik3])
df_tes[fitur_numerik3].head()

df_tes

df_tes.insert(9, 'ocean_proximity_ISLAND', None)

df_tes.loc[:, 'ocean_proximity_ISLAND'] = 0

df_tes.shape

df_tes

Pred_XG_Tes_data = xgb_FT_Param.predict(df_tes)

output_XG = pd.DataFrame({'longitude': df_tes.longitude, 'latitude': df_tes.latitude, 'housing median age': df_tes.housing_median_age, 'prediksi': Pred_XG_Tes_data })
output_XG.to_csv('result.RF.csv', index=False)

df_pred = pd.read_csv('/content/result.RF.csv')

df_pred

df_pred.hist(bins = 50, figsize = (20,15))
plt.show()
# Proyek Pertama California House Price Predict

### Disusun Oleh : Brilly Lutfan Qasthari
ini merupakan proyek submission pertama dari dicoding Mahine Learning Terapan. Proyek ini membangun sebuah model *machine learning regresi* untuk mengatasi masalah seputar prediksi harga rumah di California Amerika Serikat.

## Domain Proyek
### Latar Belakang
Pasar real estat adalah salah satu sektor ekonomi terpenting dan harga real estat merupakan faktor kunci dalam keputusan pembelian real estat. Kemampuan memprediksi harga rumah dengan akurasi tinggi dapat membantu calon pembeli, penjual, dan pemangku kepentingan lainnya membuat keputusan yang lebih tepat. 

Pasar real estate di California sangat dinamis dan harga real estate seringkali sangat berfluktuasi. Oleh karena itu, memprediksi real estat dalam konteks ini merupakan tantangan yang menarik. Dalam *submission* ini, berfokus pada penggunaan model regresi pembelajaran mesin untuk memprediksi harga rumah di California [[1](https://www.researchgate.net/publication/350345452_Prediksi_Harga_Rumah_Menggunakan_Web_Scrapping_dan_Machine_Learning_Dengan_Algoritma_Linear_Regression)]. 

Model regresi *machine learning* adalah cara ampuh untuk mengeksplorasi pola dan hubungan antara karakteristik data dan variabel target, dalam hal ini harga rumah. Dengan menggunakan teknik regresi, model tersebut dapat digunakan untuk mempelajari pola harga properti berdasarkan karakteristik seperti lokasi, ukuran rumah, jumlah kamar tidur, dan faktor lain yang relevan [[2](https://ejournal.bsi.ac.id/ejurnal/index.php/ji/article/download/9036/pdf)].

Tujuan dari *submission* ini adalah mengembangkan model *machine learning* yang dapat memprediksi harga real estat di California dengan MSE(*Mean Squared Error*) kecil. Model ini dapat memberikan informasi berharga kepada calon pembeli rumah, agen real estat, dan pemangku kepentingan lainnya dalam keputusan penetapan harga rumah mereka. 

## Business Understanding
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

## Data Understanding
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

### Univariate Analysis
proses menganalisis dan memahami suatu variabel dalam kumpulan data tanpa mempertimbangkan hubungannya dengan variabel lain. Tujuan dari analisis univariat adalah untuk mendapatkan gambaran mengenai distribusi, karakteristik dan pola dari variabel-variabel tersebut. 

#### Analisis fitur kategori
Untuk dataset ini, fitur kategori hanya berjumlah satu kolom yaitu fitur ocean_proximity. berikut rincian dari fitur ocean_proximity :

![ocean_proximity](https://i.ibb.co/Mnq5ccT/ocean.png)
Gambar 1. Persebaran fitur ocean proximity

Pada Gambar 1 distribusi data tidak merata hal ini dapat dilihat pada rincian visualisai tersebut, dimana 1H OCEAN memiliki data terbanya dengan total sebesar 7531 sampel dengan presentase sebesar 43%. Data ISLAND memiliki jumlah perseberan yang sedikit yaitu sebesar 5 sampel saja.

#### Analisis fitur numerik
![numerik_1](https://i.ibb.co/6HBQmXv/numerik-1.png)
Gambar 2. Persebaran fitur longitude sampai population
![numerik_2](https://i.ibb.co/Sd93yPJ/numerik-2.png)
Gambar 3. Persebaran fitur households sampai median_house_value

Berikut merupakan rincian persebaran fitur numerik pada Gambar 2 dan 3 :
+ Fitur bujur dan lintang memiliki korelasi yang kuat dikarenakan kedua fitur tersebut memiliki korelasi tinggi.
+ Rata-rata median dari umur rumah terbanyak yaitu di rentang umur 10 - 50.
+ Rata-rata terbanyak pada fitur total room dan total bedroom ada di angka 2634 room dan 536 bedroom.
+ Populasi terbanyak ada di angka 35682 jiwa dan memiliki nila rata-rata sebesar 1424 jiwa.
+ Jumlah rumah tangga terbanyak di angka 6082 dan memiliki nilai rata-rata sebesar 499.
+ Untuk fitur median_income, longitude dan latitude sebenarnya tidak diperlukan. Akan tetapi fitur ini dimasukkan guna untuk pengujian kualitas model yang akan dihasilkan.

### Multivariate Analysis
Multivariate Analysis adalah Suatu analisis dilakukan untuk memahami hubungan antara dua variabel atau lebih secara bersamaan. Dalam analisis multivariat, kita melihat lebih dari satu variabel dalam analisis yang sama untuk melihat bagaimana variabel tersebut berhubungan, berinteraksi, atau saling mempengaruhi. Tujuan analisis multivariat adalah untuk mendapatkan pemahaman yang lebih lengkap tentang pola, tren, dan hubungan yang mungkin ada di antara variabel-variabel tersebut. Teknik yang biasa digunakan dalam analisis multivariat antara lain analisis regresi, analisis faktor, analisis kluster, analisis diskriminan, dll.

#### Analisis fitur kategori

![Multi_kategori](https://i.ibb.co/vQL0DZL/multi-kategori.png)
Gambar 4. Persebaran fitur Ocean Proximity dengan Median House Value

Pada Gambar 4, Untuk analisis Multi fitur yang digunakan untuk pengujian ini merupakan fitur yang akan di prediksi yaitu fitur median_house_value. harga rumah tertinggi ada di daerah pulau dan harga rumah terendah berada di daerah pedalaman atau pedesaan.

#### Analisis fitur numerik

![Multi_numerik](https://i.ibb.co/C8mHgxr/multi-korelasi.png)
Gambar 5. Tabel ditribusi korelasi antar fitur 

Berikut merupakan rincian korelasi fitur numerik pada Gambar 5 :
+ Fitur bujur tidak memiliki korelasi yang tinggi terhadap median house value hal ini terbukti dengan nilai korelai negatif -0.04.
+ Fitur lintang sama dengan fitur bujur yaitu tidak memiliki korelasi yang tinggi terhadap median house value dengan nilai korelasi sebesar negatif -0.16.
+ Fitur median umur rumah juga tidak memiliki nilai korelasi yang tinggi terhadap median house value dengan nilai korelasi positif 0.1.
+ Fitur jumlah kamar tidak memiliki nilai korelasi yang tinggi dengan median house value dengan nilai korelasi sebesar positif 0.09.
+ nilai korelasi dari fitur populasi dan rumah tangga juga tidak memiliki korelasi yang tinggi terhadap median house value dengan nilai korelasi sebesar negatif -0.01 untuk populasi dan positif 0.12 untuk rumah tangga.
+ Median income hanya satu-satu nya yang memiliki nilai korelasi yang besar yaitu 0.63

Untuk itu, fitur populasi memiliki nilai korelasi terkecil dari nilai korelasi fitur lainnya. Pada Gambar 5 fitur populasi hanya memiliki nilai korelasi sebesar negatif -0.01 dan mengapa fitur terkecil harus di drop dari dataset, berikut penjelasannya :
* Redundansi: Fitur yang memiliki korelasi sangat rendah dengan variabel target atau fitur lainnya mungkin tidak memberikan informasi tambahan yang signifikan. Fitur tersebut mungkin tidak memberikan kontribusi yang berarti dalam meningkatkan kinerja model dan dapat dianggap sebagai redundan.
* Efisiensi Komputasional: Fitur dengan korelasi terkecil dapat dihapus untuk mengurangi dimensi data. Dalam beberapa kasus, mengurangi jumlah fitur dapat mempercepat waktu komputasi dan mengurangi kompleksitas model.
* Interpretasi yang lebih mudah: Dalam beberapa kasus, memiliki fitur dengan korelasi terkecil dapat mempersulit interpretasi hasil. Dengan menghapus fitur-fitur tersebut, interpretasi dan pemahaman model dapat menjadi lebih sederhana dan mudah dipahami.

## Data Preparation
Persiapan data adalah proses persiapan data sebelum dilakukan analisis atau pemodelan. Tujuan dari persiapan data adalah untuk memastikan bahwa data yang digunakan dalam analisis atau pemodelan telah disiapkan, terstruktur dan memenuhi persyaratan. Beberapa langkah yang dilakukan dalam Data Preparation meliputi:

- Cleaning (Pembersihan): Melakukan identifikasi dan penanganan terhadap missing values (nilai kosong), outlier (nilai ekstrim), atau data yang tidak konsisten.
- Transformation (Transformasi): Melakukan transformasi terhadap data seperti normalisasi, standarisasi, atau pengubahan skala untuk memastikan data memiliki distribusi yang tepat.
- One Hot Encoding : Algoritma *machine learning* biasanya hanya dapat memproses data numerik. Pengkodean satu-panas memungkinkan variabel kategori untuk diubah menjadi representasi biner yang dapat dimanipulasi oleh suatu algoritma. 
- Train Test Split : Dalam *machine learning*, kita ingin mengevaluasi seberapa baik model dapat melakukan prediksi pada data yang belum pernah dilihat sebelumnya. Dengan membagi data menjadi train dan test set, dapat melatih model pada train set dan kemudian menguji performanya pada test set. Ini memberikan indikasi seberapa baik model dapat menggeneralisasi pada data yang baru. Untuk proyek ini, rasio pembagian dataset yaitu 9:1 dengan rincian:
  + Jumlah sampel di train dataset : 15686
  + Jumlah sampel di test dataset : 1743
- Metode IQR (Interquartile Range): Metode ini melibatkan penggunaan rentang antara kuartil pertama (Q1) dan kuartil ketiga (Q3) dari data. Outlier diidentifikasi sebagai nilai yang berada di luar rentang Q1 - 1,5 * IQR hingga Q3 + 1,5 * IQR. Data yang dianggap sebagai outlier dapat dihapus atau diisi kembali dengan nilai yang lebih tepat.


## Modeling
Pada tahap modeling ini akan menjadi tahap jawaban untuk problem statement sebelum nya yaitu mengenai diproses nya data agar model dapat melatihnya dan peran *hyperparameter tuning* pada model yang digunakan. Untuk model yang digunakan merupakan model bertipa regresi dengan pemanfaatan model XGBoost.

+ XGBoost regresi merupakan adalah sebuah algoritma machine learning yang populer dan efektif dalam melakukan tugas-tugas regresi. XGBoost regresi merupakan varian dari algoritma XGBoost yang digunakan khusus untuk memodelkan dan memprediksi variabel target kontinu (numerik). XGBoost merupakan salah satu algoritma populer dalam machine learning yang sering kali memberikan performa yang lebih baik dibandingkan dengan model lainnya dalam beberapa kasus. Beberapa alasan mengapa XGBoost dianggap lebih baik adalah: 
  + Kecepatan dan Skalabilitas: XGBoost dirancang dengan fokus pada kecepatan dan skalabilitas. Implementasi yang efisien dan kemampuan untuk memproses data besar membuat XGBoost menjadi pilihan yang baik untuk dataset yang besar.
  + Regularisasi: XGBoost menyediakan opsi untuk regularisasi yang dapat mengurangi overfitting pada model. Regularisasi termasuk regularisasi L1 dan L2, yang membantu mencegah kompleksitas yang berlebihan dan meningkatkan generalisasi model.
  + Handle Missing Values: XGBoost dapat secara langsung menangani nilai yang hilang pada dataset tanpa memerlukan imputasi nilai-nilai tersebut. Ini dapat mengurangi kerumitan pra-pemrosesan data.
  + Kemampuan untuk Menangani Fitur dengan Skala Berbeda: XGBoost dapat bekerja dengan baik pada dataset yang memiliki fitur dengan skala yang berbeda. Tidak perlu melakukan penskalaan khusus atau transformasi data tambahan sebelum menggunakan XGBoost.

  Sehingga dari penjelasan sebelumnya, model XGBoost cocok dengan kasus pada proyek ini (Prediksi Harga Rumah di Wilayah California)
 
+ Penggunaan *Hyperparameter Tuning*
  Grid Search adalah salah satu teknik yang digunakan dalam pemilihan parameter optimal untuk model machine learning. Tujuan dari Grid Search adalah untuk mencari kombinasi parameter terbaik yang memberikan performa model yang optimal. berikut parmeter yang digunakan pada proyek ini :
  + `n_estimators` : jumlah estimator ketika boosting dihentikan.
  + `max_depth` : jumlah kedalaman maksimum dari semua tree.
  + `learning_rate` : untuk memperkuat kontribusi dalam setiap regresor.
+ Parameter terbaik dipilih melalui proses seleksi parameter untuk *hyperparameter tuning* GridSearch dengan rincian pengujian sebagai berikut :
  ```
  param_Grid = {
    'n_estimators': [100, 200, 300], #jumlah pohon di setiap iterasi
    'max_depth': [3, 4, 5], #mengontrol kedalaman maksimum dari setiap pohon keputusan dalam model.
    'learning_rate': [0.1, 0.01, 0.001] } #mengontrol tingkat pembelajaran model
  ```
  lalu parameter tersebut akan diuji menggunakan variabel X dan Y dengan rincian kodingan sebagai berikut :
  ```
  grid_search = GridSearchCV(estimator=model, param_grid=param_Grid, scoring='neg_mean_squared_error', cv=5)
  grid_search.fit(X_train, y_train)
  ```
+ Setelah pengujian selesai hasil parmeter terbaik yang digunakan untuk proyek sebagai berikut:
  Tabel 1. Parameter Terbaik GridSearch
   model    | best_params                                                     |
  |----------|-----------------------------------------------------------------|
  | XGBoost Regresor    | {'learning_rate': 0.1, 'max_depth': 5, 'n_estimators': 300}                                              |

## Evaluation
![metrik_mse](https://i.ibb.co/9N2Y95x/MSE.png)
Gambar 6. Rumus MSE

Pada Gambar 6, Mean Squared Error (MSE) adalah salah satu metrik evaluasi yang umum digunakan dalam masalah regresi dalam machine learning. MSE mengukur rata-rata dari kuadrat selisih antara nilai prediksi dan nilai sebenarnya dari data. cara kerja MSE adalah dengan menjumlahkan selisih kuadrat antara nilai prediksi (y_pred) dan nilai sebenarnya (y_true) dari setiap sampel data, kemudian diambil rata-ratanya. MSE memberikan perhatian lebih pada data yang memiliki selisih besar antara nilai prediksi dan nilai sebenarnya, karena selisih kuadrat memperbesar perbedaan antara nilai tersebut.

pada proyek ini menggunakan dua model yang sama dengan indikator yang menggunakan *hyperparmeter tuning* dan yang tidak menggunakan. lalu hasil dari model yang telah ditraining dan menggunakan metrik MSE dapat dilihat sebagai berikut :

Tabel 2. Rician Hasil Evaluasi Metrik MSE
model    | Training                     | Testing |
  |----------|-------------------------|-------------------------|
  | XGBoost Regresor dengan  *hyperparmeter tuning*  | 1077382.035362 |21454726.96944|
  | XGBoost Regresor  tidak dengan  *hyperparmeter tuning*  | 788683.201051 |20769573.194765|

Dari Tabel 2 hasil metrik tersebut penggunaan *hyperparmeter tuning* tidak mendapatkan hasil yang maksimal hal ini dikarenakan hasil testing dapat dilihat kalau metrik MSE terkecil dimiliki oleh model yang tidak menggunakan *hyperparmeter tuning* mengapa hal ini bisa terjadi, ada beberapa indikator berpengaruh seperti :

* Parameter yang diuji tidak mencakup kombinasi yang optimal: GridSearchCV akan menguji semua kombinasi parameter yang diberikan dalam param_grid. Jika param_grid tidak mencakup kombinasi yang optimal, maka hasilnya mungkin tidak lebih baik daripada yang tidak menggunakan Grid Search.
* Overfitting: Ketika menggunakan GridSearchCV dengan cross-validation, ada kemungkinan model terbaik yang dipilih di setiap lipatan validasi akan overfitting pada data pelatihan yang spesifik pada lipatan tersebut. Hal ini dapat mengakibatkan hasil yang buruk pada data uji yang baru.
* Jumlah data yang terbatas: Jika jumlah data pelatihan terbatas, maka performa GridSearchCV dapat terbatas karena keterbatasan dalam menguji berbagai kombinasi parameter.
* Interaksi antara parameter: GridSearchCV mungkin tidak mampu menemukan interaksi yang kompleks antara parameter-parameter yang diuji. Beberapa parameter dapat memiliki efek yang saling mempengaruhi, dan GridSearchCV tidak selalu mampu mengeksplorasi interaksi tersebut dengan baik.

lalu untuk solusi dari permasalahan tersebut sebagai berikut :
* Memperluas param_grid untuk mencakup lebih banyak kombinasi parameter yang mungkin, termasuk nilai-nilai yang lebih luas dan beragam.
* Mencoba algoritma optimasi parameter yang lebih canggih, seperti Bayesian Optimization atau Randomized Search.
* Memperhatikan preprocessing data yang tepat, seperti normalisasi atau pengurangan fitur.

---Ini adalah bagian akhir laporan---


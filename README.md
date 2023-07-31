# MST Minimum Finder
MST minim finder adalah sebuah aplikasi berbasis desktop yang dibangun menggunakan bahasa python dibantu dengan PyQt. aplikasi ini dapat mencari MST Minimum dari graph yang sudah dimasukkan oleh pengguna menggunakan algoritma kruskal dan prim.

## Cara Penggunaan
1. pertama tama pengguna sangat diharuskan untuk memasukkan file .txt dengan menekan tombol `Choose File` yang berisi array ketetanggaan dengan contoh seperti test.txt dalam folder utama project ini
2. setelah menambahkan file.txt pengguna dapat menampilkan graph dengan menekan `Show Graph`
3. jika pengguna ingin mencari MST Minimum dari graph bisa menekan `Show MST Prim` atau `Show MST Kruskal`
4. jika pengguna ingin menghapus node pada graph, maka pengguna harus mengisi text field `delete node` dengan nomor sesuai dengan yang ingin dihapus lalu tekan tombol `delete`
5. jika pengguna ingin menambahkan node, maka pengguna dapat mengisi textfield `add_node` dengan array yang berisi bobot dan jumlah element yang sesuai dengan node yang ada di graph contoh `[0,0,0,1,2,3,..]`
6. pengguna juga dapat mencari cluster dengan mengisi textfield `cluster` sesuai dengan yang pengguna mau
![img.png](assets%2Fimg.png)

## Author
```
Nama : Fahrian Afdholi
NIM  : 13521031
```
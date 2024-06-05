by mafia m16
cython.py :
It's native Cython, meaning a file is converted directly into Cython with all the functions and everything
cython1.py :
It is cython and is not converted directly. This means that before converting to cython, it is encrypted using Base64. After that, the cipher text is divided into parts to make it difficult for a hacker to decode the code. The reason for using this method is that Cyton fails to convert some times due to strange formatting of text and symbols

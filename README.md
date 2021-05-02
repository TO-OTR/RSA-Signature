# ALL BASED ON RSA

## Realize
* Unlimited length of message
* personalized size of block
* Fasten x^y mod n
* CBC padding
* sha256
--------------------------------
## Usage
* run MD5.py to see basic RSA/MD5
* run sha256.py to see basic RSA/sha256
* run MD5&CBC.py to see CBC/RSA/PADDING/MD5, personalized size of block, unlimitited length of message
* open MathWork.py to see Chinese rest method
* q,p of Bob and Alice are 64bit or 32bit, you can change by annotating unnecessary parts.
* for sha256.py you should only use 64bit q,p
* Block size : 0<B_S<n

--------------------------------
## Files
### MD5.py & sha256
* Based on original file.
* hashlib.md5 and hashlib.sha256


### MD5CBC.py
* Based on original file.
* Add some method, work with CBC.py and MathWork.py

### CBC.py
* Methods to realize CBC, RSA, PADDING	
* Normally it is AES+CBC, but TP requires RSA. So replace AES with RSA and do the encryption after XOR
* Process of CBC:  
1.chose block size (0<block size<n, n is length of public key na or nb)  
2.input message -> askii -> a big int number noted as msg  
3.msg -> separate blocks (block size) and do padding  
4.random iv and do CBC(XOR)  
5.RSA encrypt blcoks -> form a big int number  
6.send and receive  
7.a big int number -> separate blocks and RSA decrepy  
8.de_CBC(XOR) and de_padding  
9.transform int to string ->get the information  
10.do hash and match with the signature  
* Method:  
1.SelectBlockSize(na):int -> int  
*Accoding to definition, for each block size 0<B_S<n.*  
2.Separate_block(msg,n)	int, int -> list_int, int  
*Transfer the num_sec into blocks and do the padding.*  
3.Padding(block_list,default_len)	list_str, int -> list_str, int  
*To do padding to the block data*  
4.Combine_block(C,n,n_pad)	list_int, int, int -> int  
*Combine the blocks.*  
5.CombineIntListToInt_add0(S,n,n_pad)	list_int, int, int ->int  
*Add 0 back to blcoks who lost some 0 on the left during str->int*  
6.dePadding(block_list,default_len,n_pad)	list_int, int, int -> list_int  
*Do depadding to blocks*  
7.CombineIntListToInt_unitlen(M)	list_int -> int, list_int  
*Combine the list to a large in number and get the list of length of each blocks*  
8.SeparateIntToIntList(C_int,unit_len)	int, list_int -> list_int  
*Separate the large number received into list by using the list of length of each blocks*  
9.en_CBC(msg,ea,na,block_size)		int, int, int, int ->int, int, list_int  
*The main process of CBC/RSA/Padding encryption*  
10.de_CBC(C_int,n_pad,iv,da,na,unit_len,block_size)	int, int, int, int, int, list_int, int -> int  
*The main process of CBC/RSA/Padding decryption*  
* Block size must be smaller than rsa_n
* The process of CBC/RSA/PADDING is shown in picture in the folder
* If replace AES with RSA during CBC, block size will equal to rsa_n, which means m > n! ERROR. This TP is about RSA, I don't know if it is OK to use AESlib, so I only do XOR and SKIP AES. After all blocks finish XOR, I do RSA on each Block and combine them.  Send and receive it. Separate to block and do RSA. Then do CBC_XOR to blocks and do padding. Finally, combine them to form the result.
  

### MathWork.py
* Mainly about the math calculation methods
* Method:  
1.home_mod_expnoent(x,y,n) 	int, int, int -> int  
*exponentiation modulaire, Chinese method*  
2.home_ext_euclide(y,b)	int, int -> int  
*algorithme d'euclide étendu pour la recherche de l'exposant secret*  
3.home_pgcd_plus(y,b,q)	int, int, int-> int  
*expend euclide calculate q_list*  
4.home_pgcd(a,b)		int, int -> int  
*calculate pgcd*
5.home_string_to_int(x)	string -> int  
*pour transformer un string en int*  
6.home_int_to_string(x)	int -> string  
*pour transformer un int en string*  

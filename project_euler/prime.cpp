#include<iostream>
using namespace std;
int main(){
     const long numm=600851475143;
     long z=numm;
     long lfact=numm;
    int p=2;
    while(p*p <= z){
        if(z%p==0){
            z=z/p;
            lfact=p; 
        }
        else{
            p++;
        }           

        }
        if(z>lfact){
            lfact=z;
        }


    
 
cout<<"The output is="<<lfact;
return 0;
}
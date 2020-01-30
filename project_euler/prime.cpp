#include<iostream>
using namespace std;
int main(){
     const long n=24;
     long z=n;
     long fact=0;
    int p=2;
    while(p*p<=z){
        if(z%p==0){
            z/=p;
            fact=p; 

        }
        else{
            p++;
        }           

        }


    
 
cout<<"The output is="<<fact;
return 0;
}
#include <stdio.h>

int main(){

    int n;
    scanf("%d", &n);
    int tem = 0;

    for(int i = 2; i < n; i++){
        int soma = i;
        while(soma < n) soma += i;

        if(soma == n){
            printf("raiz de %d eh %d\n", n, i);
            tem = 1;
            break;
        }
    }

    if(!tem){
        printf("Nao tem raiz\n");
    }

    return 0;
}

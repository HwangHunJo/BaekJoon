#include <stdio.h>
main(){
    int t;
	int n, k;
	int i, j, l;
	int people;
	scanf("%d", &t);
	for(i = 0; i < t; i++){
		scanf("%d", &n);
		scanf("%d", &k);
		
		int apart[n + 1][14];
		for(j = 0; j < 14; j++)
			apart[0][j] = j + 1;
		
		for(l = 0; l <= n; l++)
			apart[l][0] = 1;
		
		for(l = 1; l <= n; l++){
			for(j = 1; j < 14; j++){
				apart[l][j] = apart[l][j - 1] + apart[l - 1][j];
				
			}
		}
		
		printf("%d\n", apart[n][k - 1]);
	}
   }
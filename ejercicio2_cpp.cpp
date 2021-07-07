#include <iostream>
#include <vector>
using namespace std;

void organizar(vector<int> Z){ //ordenamiento burbuja
  float temporal;
	
	for (int i = 0;i < Z.size(); i++){
		for (int j = 0; j< Z.size()-1; j++){
			if (Z[j] < Z[j+1]){ // Ordena el array de mayor a menor
			temporal = Z[j]; 
			Z[j] = Z[j+1]; 
			Z[j+1] = temporal;
			}
		}
	}
  for (int i = 0 ; i < Z.size() ; i++){//imprime los elementos del vector
    cout << Z[i] << endl;
  }
}

int main() {

  
  vector<int> X, W, Z; //inicia variables
  X = {9,7,5,3,1};
  W = {16,14,12,10,8,6,4,2};

  for (int i = 0 ; i < X.size() ; i++){ //agrega el vector x al vector z
    Z.push_back(X[i]);
  }
  for (int i = 0 ; i <W.size() ; i++){ //agrega el vector w al vector z
    Z.push_back(W[i]);
  }
  organizar(Z); //llama a la función
}
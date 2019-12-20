import java.util.ArrayList;

public class Arbol {

    public class Nodo {
        private Integer frecuencia;
        private Nodo izq;
        private Nodo der;
     
        public Nodo(Integer frecuencia) {
            this.frecuencia = frecuencia;
        }
    
        public Nodo getNodoIzq() {
            return izq;
        }
    
        public Nodo getNodoDer() {
            return der;
        }
    
        public void setNodoDer(Nodo nodo){
            der = nodo;
        }
    
        public void setNodoIzq(Nodo nodo){
            izq = nodo;
        }
        public int getFrecuencia(){
            return frecuencia;
        }

    }

    public Nodo crearArbol(Nodo nodoCero,Nodo NodoUno){
        Nodo raiz = new Nodo(nodoCero.getFrecuencia()+ NodoUno.getFrecuencia());
        raiz.setNodoDer(nodoCero);
        raiz.setNodoIzq(NodoUno);

        return raiz;
    }
    
    public static void main(String[] args) {
        Integer [] nums = {1,2,2,2,2,3,6};


        for (int i = 0; i < nums.length; i++) {
            Nodo nodoDer = new Nodo();    
        }
    }
    
}
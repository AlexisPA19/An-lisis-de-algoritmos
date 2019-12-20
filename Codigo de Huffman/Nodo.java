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

    public void setNdooIzq(Nodo nodo){
        izq = nodo;
    }

}

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class huffmanUI extends JFrame implements ActionListener{
    /**
     *
     */
    private static final long serialVersionUID = 1L;
    private JLabel menssage_lb;
    private JTextField menssage_txtf;
    private JButton btn_codif;
    private JPanel panelMensaje;
    private JScrollPane scrollPanelTabla;
    private JTable tabla;
    private JPanel results;

    private Object[][] data;

    private String[] columnName = {"Caracter","Conteo","Codificacion","Bits"};

    public void actionPerformed(ActionEvent e) {
        getChars();
        tabla = new JTable(data,columnName);
        tabla.setPreferredScrollableViewportSize(new Dimension(300,100));
        tabla.setEnabled(false);
        scrollPanelTabla = new JScrollPane(tabla);
        results = new JPanel();
        //results.setLayout(new FlowLayout();
        results.add(new JLabel("Total de bits : 36"),BorderLayout.WEST);
        results.add(new JLabel("Mensaje codificado: 1010101010101010101010"),BorderLayout.EAST);
        Container contentPane = this.getContentPane();
        contentPane.add(scrollPanelTabla,BorderLayout.CENTER);
        contentPane.add(results,BorderLayout.SOUTH);

        contentPane.revalidate();

    }
    public void getChars(){
        String msn = this.menssage_txtf.getText();
        char array_msn[] = msn.toCharArray();
        ArrayList <Character> chars = new ArrayList<>();

        
        for (int i = 0; i < array_msn.length-1; i++) {
            if (chars.indexOf(array_msn[i]) == -1){
                chars.add(array_msn[i]);
            }
        }

        int array_frec_chars[] = new int[chars.size()];

        for (int i = 0; i < chars.size(); i++) {
            for (int j = 0; j < msn.length(); j++) {
                if (msn.charAt(j) == chars.get(i)) {
                    array_frec_chars[i]++;
                }   
            }
        }

        data = new Object[chars.size()][4];

        for (int i = 0; i < chars.size(); i++) {
            data[i][0] = new String(chars.get(i).toString());
            data[i][1] = new Integer(array_frec_chars[i]);
            data[i][2] = new String("101");
            data[i][3] = new Integer(array_frec_chars[i]*data[i][2].toString().length());
        }
        

        for (int x = 0; x < chars.size(); x++) {
            for (int i = 0; i < chars.size()-x-1; i++) {
                if(Integer.parseInt(data[i][1].toString()) > Integer.parseInt(data[i+1][1].toString())){
                    Object [] menor = data[i+1];
                    data[i+1] = data[i];
                    data[i] = menor;
                }
            }
        }
    }


    
    public huffmanUI(){
        
        super(String.format("C%cdigo de Huffman",162));
        setSize(700, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Panel Mensaje
        panelMensaje = new JPanel();
        panelMensaje.setLayout(new FlowLayout());

        menssage_lb= new JLabel("Mensaje a codificar:");
        menssage_txtf = new JTextField(20);
        btn_codif = new JButton("Codificar");
        btn_codif.addActionListener(this);

        panelMensaje.add(menssage_lb);
        panelMensaje.add(menssage_txtf);
        panelMensaje.add(btn_codif);

        Container contentPane = getContentPane();
        contentPane.add(panelMensaje,BorderLayout.NORTH);
        
    }

    public static void main(String[] args){
        huffmanUI app = new huffmanUI();
        app.setVisible(true);
    }

}
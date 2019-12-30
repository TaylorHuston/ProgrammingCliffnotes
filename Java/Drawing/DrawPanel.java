import java.awt.Graphics;
import javax.swing.JPanel;

public class DrawPanel extends JPanel {

    //Draw an x from the corners of the panel
    public void paintComponent(Graphics g) {
        //Ensure panel displays correctly
        //Should be the first method you call in any JPanel
        super.paintComponent(g);  

        int width = getWidth();
        int height = getHeight();

        g.drawLine(0,0,width,height);
        g.drawLine(0,height,width,0);
    }
}

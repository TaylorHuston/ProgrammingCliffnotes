import javax.swing.JFrame;

public class DrawPanelTest {

    public static void main(String[] args) {
        DrawPanel panel = new DrawPanel();

        //Frame to hold the panel
        JFrame app = new JFrame("Test");

        //Frame exits when closed
        app.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        app.add(panel);
        app.setSize(250,250);
        app.setVisible(true);
    }
}

/**
 * Created by Andrew on 08.11.2016.
 */
import java.awt.BorderLayout;
import java.awt.Dimension;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;
import org.gstreamer.Element;
import org.gstreamer.Gst;
import org.gstreamer.Pipeline;
import org.gstreamer.State;
import org.gstreamer.swing.VideoComponent;


public class Main {
    public static void main(String[] args) throws InterruptedException {
        args = Gst.init("PipelineLauncher", args);
        final String def = "rtspsrc location=rtsp://192.168.0.64:554/Streaming/channels/1 latency=0 ! decodebin ! ffmpegcolorspace name=testp";
        final Pipeline pipe = Pipeline.launch(def);

        SwingUtilities.invokeLater(new Runnable() {

            @Override
            public void run() {
                // Create the video component and link it in
                VideoComponent videoComponent = new VideoComponent();
                Element videosink = videoComponent.getElement();
                pipe.add(videosink);
                pipe.getElementByName("testp").link(videosink);
                pipe.setState(State.PAUSED);

                if (pipe.isPlaying()) {
                    System.out.println("Pipeline playing");
                } else {
                    System.out.println("Pipeline not playing");
                }

                // Start the pipeline processing
                pipe.play();
                pipe.setState(State.PLAYING);

                if (pipe.isPlaying()) {
                    System.out.println("Pipeline playing");
                } else {
                    System.out.println("Pipeline not playing");
                }

                // Now create a JFrame to display the video output
                JFrame frame = new JFrame("Swing Video Test");
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.add(videoComponent, BorderLayout.CENTER);
                videoComponent.setPreferredSize(new Dimension(800, 600));
                frame.pack();
                frame.setLocationRelativeTo(null);
                frame.setVisible(true);
            }
        });

        Gst.main();
        pipe.setState(State.NULL);
    }
}


/*



public class Main {



}

 */
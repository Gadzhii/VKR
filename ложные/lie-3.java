public class SafeThreadExample {
    public static void main(String[] args) {
        Thread thread = new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("This is a safe thread example.");
            }
        });
        thread.start();
    }
}

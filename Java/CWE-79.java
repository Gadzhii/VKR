import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.PrintWriter;

@WebServlet("/vulnerable")
public class VulnerableServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String userInput = request.getParameter("userInput");

        out.println("<html>");
        out.println("<body>");
        out.println("<h1>Vulnerable to XSS</h1>");
        out.println("<p>User Input: " + userInput + "</p>"); // This line is vulnerable to XSS
        out.println("</body>");
        out.println("</html>");
    }
}

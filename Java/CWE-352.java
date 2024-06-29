import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet("/transfer")
public class TransferServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Получаем параметры запроса
        String fromAccount = request.getParameter("fromAccount");
        String toAccount = request.getParameter("toAccount");
        String amount = request.getParameter("amount");

        // Выполняем перевод средств (условно, без реальной логики)
        // В реальном приложении здесь будет логика работы с базой данных или API
        performTransfer(fromAccount, toAccount, amount);

        // Отправляем ответ клиенту
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<h2>Transfer successful!</h2>");
        out.println("<p>Transferred " + amount + " from " + fromAccount + " to " + toAccount + ".</p>");
        out.println("</body></html>");
    }

    private void performTransfer(String fromAccount, String toAccount, String amount) {
        // Здесь должна быть логика перевода средств между счетами
        System.out.println("Transferring " + amount + " from " + fromAccount + " to " + toAccount);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("<html><body>");
        out.println("<form action='transfer' method='post'>");
        out.println("From Account: <input type='text' name='fromAccount'><br>");
        out.println("To Account: <input type='text' name='toAccount'><br>");
        out.println("Amount: <input type='text' name='amount'><br>");
        out.println("<input type='submit' value='Transfer'>");
        out.println("</form>");
        out.println("</body></html>");
    }
}


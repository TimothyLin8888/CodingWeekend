import java.util.*;

public class FinanceTracker {
    public static void main(String[] args){
        ArrayList<FinanceOperations> expensesArr = new ArrayList<>();
        try (Scanner scan = new Scanner(System.in)) {
            while (true){
                System.out.print("What case do you want to do: ");
                int choice = scan.nextInt();
                switch (choice) {
                    case 1:
                        System.out.println("case 1");
                        continue;
                    case 2:
                        System.out.println("Case 2");
                        continue;
                    case 3:
                        System.out.println("Case 3");
                        break;
                    default:
                        System.out.println("Nice choice");
                        continue;
                }
                break;
                /* 
                System.out.print("Enter your expense: ");
                double expense = scan.nextDouble();
                System.out.print("Ener your income: ");
                double income = scan.nextDouble();
                FinanceOperations expenses = new FinanceOperations(expense, income);
                expensesArr.add(expenses);
                for (int i = 0; i < expensesArr.size(); i++){
                    System.out.println(expensesArr.get(i).incomeMinusExpense(expense, income));
                }
                    */
            }
        }

    }
}

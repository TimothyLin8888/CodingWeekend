import java.util.*;

public class FinanceTracker {
    public static void main(String[] args){
        ArrayList<FinanceOperations> expensesArr = new ArrayList<>();
        FinanceOperations account = new FinanceOperations();
        try (Scanner scan = new Scanner(System.in)) {
            while (true){
                System.out.print("What case do you want to do: ");
                System.out.println("\n1) Add Expense\n2) Remove Expense\n3) View Expense\n4) Total Expense");
                System.out.println("5) Needs/Wants/Savings Calc\n6) Edit an expense\n7) To break");
                int choice = scan.nextInt();
                scan.nextLine();
                switch (choice) {
                    case 1:
                        System.out.println("Choose date: YYYY/MM/DD ");
                        String date = scan.nextLine();
                        System.out.println("Type a description about the expense: ");
                        String description = scan.nextLine();
                        System.out.println("How much money was it: ");
                        double expense = scan.nextDouble();
                        account = new FinanceOperations(expense, description, date);
                        expensesArr.add(account);
                        continue;
                    case 2:
                        if (expensesArr.size() == 0){
                            System.out.println("No expenses available");
                            continue;
                        }
                        System.out.println("Choose expense to remove: \n");
                        for (int i = 0; i < expensesArr.size(); i++){
                            System.out.println(i + 1 + ") Date: " + expensesArr.get(i).getDate() + " | Description: " + expensesArr.get(i).getDate() + " | Amount: " + expensesArr.get(i).getExpense());
                        }
                        int index = scan.nextInt();
                        expensesArr = account.removeExpense(index, expensesArr);
                        continue;
                    case 3:
                        for (int i = 0; i < expensesArr.size(); i++){
                            System.out.println(i + 1 + ") Date: " + expensesArr.get(i).getDate() + " | Description: " + expensesArr.get(i).getDescription() + " | Amount: " + expensesArr.get(i).getExpense());
                        }
                        continue;
                    case 4:
                        double total = 0;
                        for (int i = 0; i < expensesArr.size(); i++){
                            total += expensesArr.get(i).getExpense();
                        }
                        System.out.println(total);
                        continue;
                    case 5:
                        System.out.println("Enter your income: ");
                        double income = scan.nextInt();
                        System.out.println(account.needWantSave(income));
                        continue;
                    case 6:
                        if (expensesArr.size() == 0) {
                            System.out.println("Nothing to edit.");
                            continue;
                        }
                        for (int i = 0; i < expensesArr.size(); i++){
                            System.out.println(i + 1 + ") Date: " + expensesArr.get(i).getDate() + " | Description: " + expensesArr.get(i).getDescription() + " | Amount: " + expensesArr.get(i).getExpense());
                        }
                        System.out.println("Would you like to edit an Expense (Ep), Description (De), or Date (Da)");
                        String editChoice = scan.nextLine();
                        if (editChoice.toLowerCase().equals("ep")) {
                            System.out.print("Which expense do you want to edit: ");
                            int num = scan.nextInt();
                            System.out.println("What do you want to change it to: ");
                            double edit = scan.nextDouble();
                            expensesArr.get(num - 1).setExpense(edit);
                        } else if (editChoice.toLowerCase().equals("de")){
                            System.out.print("Which description do you want to edit: ");
                            int num = scan.nextInt();
                            System.out.println("What do you want to change it to: ");
                            String edit = scan.nextLine();
                            expensesArr.get(num - 1).setDescription(edit);
                        } else if (editChoice.toLowerCase().equals("da")){
                            System.out.print("Which date do you want to edit: ");
                            int num = scan.nextInt();
                            scan.nextLine();
                            System.out.println("What do you want to change it to: ");
                            String edit = scan.nextLine();
                            expensesArr.get(num - 1).setDate(edit);
                            System.out.println(expensesArr.get(num -1).getDate());
                        } else {
                            System.out.println("Not one of the options so escape back.");
                        }
                        continue;
                    default:
                        System.out.println("Goodbye");
                        break;
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

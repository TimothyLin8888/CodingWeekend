import java.util.ArrayList;
public class FinanceOperations {
    private double expense;
    private String description;
    private String date;
    public FinanceOperations(double expense, String description, String date){
        this.expense = expense;
        this.description = description;
        this.date = date;
    }

    public FinanceOperations(){
        this.expense = 0.0;
        this.description = "";
        this.date = "0000/00/00";
    }

    public ArrayList<FinanceOperations> removeExpense(int index, ArrayList<FinanceOperations> expenseArr){
        expenseArr.remove(index - 1);
        return expenseArr;
    }

    public String getDescription(){
        return description;
    }

    public double getExpense(){
        return expense;
    }

    public String getDate(){
        return date;
    }

    public void setDescription(String description){
        this.description = description;
    }

    public void setExpense(double expense){
        this.expense = expense;
    }

    public void setDate(String date){
        this.date = date;
    }

    public double incomeMinusExpense(double expense, double income){
        return income - expense;
    }

    public String needWantSave(double income){
        return "Needs: $" + income * .5 + "\nWants: $" + income * .3 + "\nSavings: $" + income * .2 + "\n";
    }
}

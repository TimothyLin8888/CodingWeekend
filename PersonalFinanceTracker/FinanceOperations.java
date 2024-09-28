public class FinanceOperations {
    private double expense;
    private double income;
    
    public FinanceOperations(double expense, double income){
        this.expense = expense;
        this.income = income;
    }

    public void addExpense(float expense){

    }

    public double getIncome(){
        return income;
    }

    public double getExpense(){
        return expense;
    }

    public void setIncome(double income){
        this.income = income;
    }

    public void setExpense(double expense){
        this.expense = expense;
    }

    public double incomeMinusExpense(double expense, double income){
        return income - expense;
    }
}

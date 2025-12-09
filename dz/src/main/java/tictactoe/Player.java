package tictactoe;

import java.util.Scanner;

public class Player {
    private final String name;
    private final char symbol;

    public Player(String name, char symbol) {
        this.name = name;
        this.symbol = symbol;
    }

    public String getName() {
        return name;
    }

    public char getSymbol() {
        return symbol;
    }

    public boolean makeMove(Board board) {
        try {
            Scanner scanner = new Scanner(System.in);

            System.out.println("\n" + this.name + " (" + this.symbol + "), ваш ход.");
            System.out.print("Введите номер строки (1-3): ");

            int row = Integer.parseInt(scanner.nextLine()) - 1;

            System.out.print("Введите номер столбца (1-3): ");
            
            int col = Integer.parseInt(scanner.nextLine()) - 1;

            if (board.makeMove(row, col, this.symbol)) {
                return true;
            } else {
                System.out.println("Эта ячейка уже занята или координаты неверны. Попробуйте снова.");
            }
        } catch (NumberFormatException e) {
            System.out.println("Пожалуйста, введите числа от 1 до 3.");
        } 
    
        return false;
    }
}

package tictactoe;

import java.util.ArrayList;
import java.util.List;

public class Board {

    private final char[][] grid;
    private static final int SIZE = 3;

    public Board() {
        grid = new char[SIZE][SIZE];
        initializeBoard();
    }

    public Board(Board other) {
        this.grid = new char[SIZE][SIZE];
        for (int i = 0; i < SIZE; i++) {
            System.arraycopy(other.grid[i], 0, this.grid[i], 0, SIZE);
        }
    }

    private void initializeBoard() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                grid[i][j] = ' ';
            }
        }
    }

    public void print() {
        System.out.println("\n  1   2   3");

        for (int i = 0; i < SIZE; i++) {
            System.out.print((i + 1) + " ");

            for (int j = 0; j < SIZE; j++) {
                System.out.print(grid[i][j]);
                if (j < SIZE - 1) {
                    System.out.print(" | ");
                }
            }

            System.out.println();

            if (i < SIZE - 1) {
                System.out.println("  ---------");
            }
        }
    }

    public List<int[]> getAvailableMoves() {
        List<int[]> moves = new ArrayList<>();
            for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (grid[i][j] == ' ') {
                    moves.add(new int[]{i, j});
                }
            }
        }
        return moves;
    }

    public boolean makeMove(int row, int col, char symbol) {
        if (row < 0 || row >= SIZE || col < 0 || col >= SIZE) {
            return false;
        }

        if (grid[row][col] != ' ') {
            return false;
        }

        grid[row][col] = symbol;
        return true;
    }

    public char checkWinner() {
        // Проверка строк
        for (int i = 0; i < SIZE; i++) {
            if (grid[i][0] != ' ' && grid[i][0] == grid[i][1] && grid[i][1] == grid[i][2]) {
                return grid[i][0];
            }
        }

        // Проверка столбцов
        for (int j = 0; j < SIZE; j++) {
            if (grid[0][j] != ' ' && grid[0][j] == grid[1][j] && grid[1][j] == grid[2][j]) {
                return grid[0][j];
            }
        }

        // Проверка диагоналей
        if (grid[0][0] != ' ' && grid[0][0] == grid[1][1] && grid[1][1] == grid[2][2]) {
            return grid[0][0];
        }

        if (grid[0][2] != ' ' && grid[0][2] == grid[1][1] && grid[1][1] == grid[2][0]) {
            return grid[0][2];
        }

        return ' ';
    }

    public boolean isFull() {
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) {
                if (grid[i][j] == ' ') {
                    return false;
                }
            }
        }

        return true;
    }
}

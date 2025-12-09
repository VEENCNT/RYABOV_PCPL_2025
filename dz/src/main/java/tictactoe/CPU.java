package tictactoe;

import java.util.List;
import java.util.Random;

public class CPU extends Player {
    // Вероятность того, что компьютер ошибется (в процентах)
    private final int maxErrorProbability = 25;

    public CPU(String name, char symbol) {
        super(name, symbol);
    }

    private int minimax(Board board, int depth, boolean isMaximizing) {
        if (board.checkWinner() == 'O') {
            return 10 - depth;
        }
        if (board.checkWinner() == 'X') {
            return depth - 10;
        }
        if (board.getAvailableMoves().isEmpty()) {
            return 0; // Ничья
        }
        
        if (isMaximizing) {
            // Максимизируем счет игрока (O)
            int bestScore = Integer.MIN_VALUE;
            for (int[] move : board.getAvailableMoves()) {
                Board newBoard = new Board(board);
                newBoard.makeMove(move[0], move[1], 'O');
                int score = minimax(newBoard, depth + 1, false);
                bestScore = Math.max(bestScore, score);
            }
            return bestScore;
        } else {
            // Минимизируем счет игрока (X)
            int bestScore = Integer.MAX_VALUE;
            for (int[] move : board.getAvailableMoves()) {
                Board newBoard = new Board(board);
                newBoard.makeMove(move[0], move[1], 'X');
                int score = minimax(newBoard, depth + 1, true);
                bestScore = Math.min(bestScore, score);
            }
            return bestScore;
        }
    }

    private int[] findBestMove(Board board) {
        int bestScore = Integer.MIN_VALUE;
        int[] bestMove = new int[]{-1, -1};
        
        // Пробуем все ходы
        for (int[] move : board.getAvailableMoves()) {
            Board newBoard = new Board(board);
            newBoard.makeMove(move[0], move[1], super.getSymbol());
            
            // Считает итоговый счет для каждого хода
            int score = minimax(newBoard, 0, false);
            
            // Ищем максимальный счет
            if (score > bestScore) {
                bestScore = score;
                bestMove = move;
            }
        }
        
        return bestMove;
    }

    public int[] findRandomMove(Board board) {
        Random random = new Random();

        List<int[]> availableMoves = board.getAvailableMoves();

        int randomMoveIndex = random.nextInt(availableMoves.size());

        return availableMoves.get(randomMoveIndex);
    }

    @Override
    public boolean makeMove(Board board) {
        System.out.println("\n" + super.getName() + " (" + super.getSymbol() + "), ваш ход.");

        Random random = new Random();
        int errorProbability = random.nextInt(100);

        int[] move = (errorProbability < maxErrorProbability) 
            ? findRandomMove(board) 
            : findBestMove(board);

        board.makeMove(move[0], move[1], super.getSymbol());
        return true;
    }
}
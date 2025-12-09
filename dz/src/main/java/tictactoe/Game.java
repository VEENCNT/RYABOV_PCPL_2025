package tictactoe;

import java.util.Scanner;

public class Game {

    private final Board board;
    private final Player[] players;

    private final int maxPlayerCount = 2;

    private int currentPlayerIndex;

    public Game() {
        this.board = new Board();
        this.players = new Player[maxPlayerCount];
        this.currentPlayerIndex = 0;
        
        initializePlayers();
    }

    private void initializePlayers() {
        Scanner scanner = new Scanner(System.in);

        int playerCount;
        char[] playerSymbols = {'X', 'O'};

        while (true) {
            try {
                System.out.println("Введите количество игроков (1 или 2): ");

                playerCount = Integer.parseInt(scanner.nextLine());
                
                if (playerCount == 1 || playerCount == 2) {
                    break;
                } else {
                    System.out.println("Пожайлуйста, введите целое число от 1 до 2 включительно");
                }
            } catch (NumberFormatException e) { 
                System.out.println("Пожайлуйста, введите целое число.");
            }
        }

        for (int i = 0; i < playerCount; i++) {
            System.out.println("Игрок " + (i + 1) + ", введите свое имя: ");
            String playerName = scanner.nextLine();

            if (playerName.isEmpty()) {
                playerName = "Игрок " + (i + 1);
            }

            players[i] = new Player(playerName, playerSymbols[i]);
        }

        if (playerCount == 1) {
            players[maxPlayerCount - 1] = new CPU("CPU", playerSymbols[maxPlayerCount - 1]);
        }
    }

    public void start() {
        System.out.println("\n=== НАЧАЛО ИГРЫ ===");
        board.print();

        while (true) {
            Player currentPlayer = players[currentPlayerIndex];

            // Ход текущего игрока
            if (!currentPlayer.makeMove(board)) {
                continue;
            }

            // Печатаем обновленное поле
            board.print();

            // Проверяем условия окончания игры
            if (board.checkWinner() != ' ') {
                System.out.println("Поздравляем! " + currentPlayer.getName() + " победил!");
                break;
            }

            if (board.isFull()) {
                System.out.println("Ничья! Поле полностью заполнено.");
                break;
            }

            // Передаем ход следующему игроку
            currentPlayerIndex = (currentPlayerIndex + 1) % 2;
        }
    }
}

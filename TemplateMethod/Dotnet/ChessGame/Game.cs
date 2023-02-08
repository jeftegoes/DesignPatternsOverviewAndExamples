namespace ChessGame
{
    public abstract class Game
    {
        protected int currentPlayer;
        protected readonly int _numberOfPlayer;

        public void Run()
        {
            Start();
            while (!HaveWinner)
                TakeTurn();
            Console.WriteLine($"Player {WinningPlayer} wins.");
        }

        protected Game(int numberOfPlayer)
        {
            _numberOfPlayer = numberOfPlayer;
        }

        protected abstract void Start();
        protected abstract void TakeTurn();
        protected abstract bool HaveWinner { get; }
        protected abstract int WinningPlayer { get; }
    }
}
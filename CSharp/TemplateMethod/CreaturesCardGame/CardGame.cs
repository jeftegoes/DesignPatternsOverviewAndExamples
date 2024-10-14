namespace CreaturesCardGame
{
    public abstract class CardGame
    {
        public Creature[] Creatures;

        public CardGame(Creature[] creatures)
        {
            Creatures = creatures;
        }

        public int Combat(int creature1, int creature2)
        {
            Creature first = Creatures[creature1];
            Creature second = Creatures[creature2];

            Hit(first, second);
            Hit(second, first);

            var firstAlive = first.Health > 0;
            var secondAlive = second.Health > 0;

            if (firstAlive == secondAlive)
                return -1;

            return firstAlive ? creature1 : creature2;
        }

        protected abstract void Hit(Creature attacker, Creature other);
    }
}
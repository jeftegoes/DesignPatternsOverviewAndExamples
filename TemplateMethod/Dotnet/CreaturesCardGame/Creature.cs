namespace CreaturesCardGame
{
    public class Creature
    {
        public string Name;
        public int Health;
        public int Attack;

        public Creature(string name, int attack, int health)
        {
            Name = name;
            Attack = attack;
            Health = health;
        }
    }
}
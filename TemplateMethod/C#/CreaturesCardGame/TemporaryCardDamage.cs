namespace CreaturesCardGame
{
    public class TemporaryCardDamage : CardGame
    {
        public TemporaryCardDamage(Creature[] creatures) : base(creatures)
        {

        }

        protected override void Hit(Creature attacker, Creature other)
        {
            var originalHealth = other.Health;

            other.Health -= attacker.Attack;

            if (other.Health >= 0)
                other.Health = originalHealth;
        }
    }
}
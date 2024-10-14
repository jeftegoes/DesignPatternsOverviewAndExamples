using CreaturesCardGame;

var orc = new Creature("Orc", 1, 2);
var elf = new Creature("Elf", 1, 3);

var creatures = new Creature[] { orc, elf };

const TypeCardGame typeCardGame = TypeCardGame.TemporaryCardDamage;

var winner = -1;

switch (typeCardGame)
{
    case TypeCardGame.TemporaryCardDamage:
        {
            var temporaryCardDamage = new TemporaryCardDamage(creatures);
            temporaryCardDamage.Combat(0, 1);
            winner = temporaryCardDamage.Combat(0, 1);
            break;
        }
    case TypeCardGame.PermanentCardDamage:
        {
            var permanentCardDamage = new PermanentCardDamage(creatures);
            permanentCardDamage.Combat(0, 1);
            winner = permanentCardDamage.Combat(0, 1);
            break;
        }
}
Console.WriteLine("Winner: {0}", winner);
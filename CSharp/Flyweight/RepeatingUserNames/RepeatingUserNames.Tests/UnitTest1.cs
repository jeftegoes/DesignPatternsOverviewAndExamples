namespace RepeatingUserNames.Tests;

public class UnitTest1
{
    public string RandomString()
    {
        var rand = new Random();
        return new string(
          Enumerable.Range(0, 10).Select(i => (char)('a' + rand.Next(26))).ToArray());
    }

    public void ForceGC()
    {
        GC.Collect();
        GC.WaitForPendingFinalizers();
        GC.Collect();
    }

    [Fact]
    public void TestUser()
    {
        var users = new List<User>();

        var firstNames = Enumerable.Range(0, 100).Select(_ => RandomString());
        var lastNames = Enumerable.Range(0, 100).Select(_ => RandomString());

        foreach (var firstName in firstNames)
            foreach (var lastName in lastNames)
                users.Add(new User($"{firstName} {lastName}"));

        ForceGC();
    }

    [Fact]
    public void TestUser2()
    {
        var users = new List<User2>();

        var firstNames = Enumerable.Range(0, 100).Select(_ => RandomString());
        var lastNames = Enumerable.Range(0, 100).Select(_ => RandomString());

        foreach (var firstName in firstNames)
            foreach (var lastName in lastNames)
                users.Add(new User2($"{firstName} {lastName}"));

        ForceGC();
    }
}
namespace SingletonDatabaseWithUnitTest
{
    public class DatabaseTest
    {
        [Fact]
        public void IsSingletonTest()
        {
            var database1 = Database.Instance;
            var database2 = Database.Instance;
            Assert.Equal(database1, database2);
            Assert.Equal(Database.Count, 1);
        }
    }
}
namespace SingletonDatabaseWithUnitTest.Test
{
    public class DatabaseRecordFinderTest
    {
        [Fact]
        public void GetTotalPopulationTest()
        {
            var databaseRecordFinder = new DatabaseRecordFinder();
            var names = new[] { "Seoul", "Mexico City" };
            int tp = databaseRecordFinder.GetTotalPopulation(names);
            Assert.Equal(tp, 17500000 + 17400000);
        }
    }
}
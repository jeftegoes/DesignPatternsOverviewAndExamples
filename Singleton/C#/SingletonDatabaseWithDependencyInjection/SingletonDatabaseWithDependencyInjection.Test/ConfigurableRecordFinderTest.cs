namespace SingletonDatabaseWithDependencyInjection.Test
{
    public class ConfigurableRecordFinderTest
    {
        [Fact]
        public void ConfigurablePopulationTest()
        {
            var configurableRecordFinder = new ConfigurableRecordFinder(new DummyDatabase());
            var names = new[] { "alpha", "gamma" };
            var tp = configurableRecordFinder.GetTotalPopulation(names);
            Assert.Equal(tp, 4);
        }
    }
}
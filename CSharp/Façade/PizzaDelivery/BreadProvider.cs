namespace Restaurant
{
    public class BreadProvider : IBread
    {
        public void GetGarlicBread()
        {
            Console.WriteLine("Getting Garlic Bread.");
        }

        public void GetCheesyGarlicBread()
        {
            GetCheese();
            Console.WriteLine("Getting Cheesy Garlic Bread.");
        }

        private void GetCheese()
        {
            Console.WriteLine("Getting Cheese.");
        }
    }
}
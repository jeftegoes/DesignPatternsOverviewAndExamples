namespace Restaurant
{
    public class RestaurantFacade
    {
        private IPizza _PizzaProvider;
        private IBread _BreadProvider;

        public RestaurantFacade()
        {
            _PizzaProvider = new PizzaProvider();
            _BreadProvider = new BreadProvider();
        }

        public void GetNonVegPizza()
        {
            _PizzaProvider.GetNonVegPizza();
        }

        public void GetVegPizza()
        {
            _PizzaProvider.GetVegPizza();
        }

        public void GetGarlicBread()
        {
            _BreadProvider.GetGarlicBread();
        }

        public void GetCheesyGarlicBread()
        {
            _BreadProvider.GetCheesyGarlicBread();
        }
    }
}
from concrete_strategy_a import ConcreteStrategyA
from concrete_strategy_b import ConcreteStrategyB
from context import Context

context = Context(ConcreteStrategyA())
print("Client: Strategy is set to normal sorting.")
context.do_some_business_logic()
print()

print("Client: Strategy is set to reverse sorting.")
context._strategy = ConcreteStrategyB()
context.do_some_business_logic()

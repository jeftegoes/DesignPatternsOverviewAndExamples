# Design patterns overview and examples <!-- omit in toc -->

## Contents <!-- omit in toc -->

- [1. Overview](#1-overview)
- [2. The Patterns](#2-the-patterns)
  - [2.1. Creational](#21-creational)
  - [2.2. Structural](#22-structural)
  - [2.3. Behavioral](#23-behavioral)
- [3. Others patterns](#3-others-patterns)
- [4. Gamma categorization](#4-gamma-categorization)
- [5. Creational](#5-creational)
  - [5.1. Builder](#51-builder)
    - [5.1.1. Motivation](#511-motivation)
    - [5.1.2. Summary](#512-summary)
  - [5.2. Factories](#52-factories)
    - [5.2.1. Motivation](#521-motivation)
    - [5.2.2. Summary](#522-summary)
  - [5.3. Prototype](#53-prototype)
    - [5.3.1. Motivation](#531-motivation)
    - [5.3.2. Summary](#532-summary)
  - [5.4. Singleton](#54-singleton)
    - [5.4.1. Motivation](#541-motivation)
    - [5.4.2. Summary](#542-summary)
  - [5.5. Creational Summary](#55-creational-summary)
- [6. Structural](#6-structural)
  - [6.1. Adapter](#61-adapter)
    - [6.1.1. Motivation](#611-motivation)
    - [6.1.2. Summary](#612-summary)
  - [6.2. Bridge](#62-bridge)
    - [6.2.1. Motivation](#621-motivation)
    - [6.2.2. Summary](#622-summary)
  - [6.3. Composite](#63-composite)
    - [6.3.1. Motivation](#631-motivation)
    - [6.3.2. Summary](#632-summary)
  - [6.4. Decorator](#64-decorator)
    - [6.4.1. Motivation](#641-motivation)
    - [6.4.2. Summary](#642-summary)
  - [6.5. Façade](#65-façade)
    - [6.5.1. Motivation](#651-motivation)
    - [6.5.2. Summary](#652-summary)
  - [6.6. Flyweight](#66-flyweight)
    - [6.6.1. Motivation](#661-motivation)
    - [6.6.2. Summary](#662-summary)
  - [6.7. Proxy](#67-proxy)
    - [6.7.1. Motivation](#671-motivation)
    - [6.7.2. Summary](#672-summary)
    - [6.7.3. Proxy vs Decorator](#673-proxy-vs-decorator)
  - [6.8. Structural Summary](#68-structural-summary)
- [7. Behavioral](#7-behavioral)
  - [7.1. Chain of Responsibility](#71-chain-of-responsibility)
    - [7.1.1. Motivation](#711-motivation)
    - [7.1.2. Summary](#712-summary)
  - [7.2. Command](#72-command)
    - [7.2.1. Motivation](#721-motivation)
    - [7.2.2. Summary](#722-summary)
  - [7.3. Interpreter](#73-interpreter)
    - [7.3.1. Motivation](#731-motivation)
    - [7.3.2. Summary](#732-summary)
  - [7.4. Iterator](#74-iterator)
    - [7.4.1. Motivation](#741-motivation)
    - [7.4.2. Summary](#742-summary)
  - [7.5. Mediator](#75-mediator)
    - [7.5.1. Motivation](#751-motivation)
    - [7.5.2. Summary](#752-summary)
  - [7.6. Memento](#76-memento)
    - [7.6.1. Motivation](#761-motivation)
    - [7.6.2. Summary](#762-summary)
  - [7.7. Null Object](#77-null-object)
    - [7.7.1. Motivation](#771-motivation)
    - [7.7.2. Summary](#772-summary)
  - [7.8. Observer](#78-observer)
    - [7.8.1. Motivation](#781-motivation)
    - [7.8.2. Summary](#782-summary)
  - [7.9. State](#79-state)
    - [7.9.1. Motivation](#791-motivation)
    - [7.9.2. Summary](#792-summary)
  - [7.10. Strategy](#710-strategy)
    - [7.10.1. Motivation](#7101-motivation)
    - [7.10.2. Summary](#7102-summary)
  - [7.11. Template Method](#711-template-method)
    - [7.11.1. Motivation](#7111-motivation)
    - [7.11.2. Summary](#7112-summary)
  - [7.12. Visitor](#712-visitor)
    - [7.12.1. Motivation](#7121-motivation)
    - [7.12.2. Summary](#7122-summary)
  - [7.13. Behavioral Summary](#713-behavioral-summary)
- [8. Duck Typing Mixins](#8-duck-typing-mixins)
- [9. Personal choices of GoF patterns](#9-personal-choices-of-gof-patterns)

# 1. Overview

- Design pattern are common architectural approaches.
- Popularized by the [Gang of Four book (1994)](http://wiki.c2.com/?GangOfFour).
  - Smaltalk and C++
- Translated to many OOP languages:
  - C#, Java, Python, JavaScript...
- Universally relevant.
  - Internalized in some programming languages.
  - Libraries.

# 2. The Patterns

## 2.1. Creational

- Builder
- Factories
  - Abstract factory
  - Factory Method
- Prototype
- Singleton

## 2.2. Structural

- Adapter
- Bridge
- Composite
- Decorator
- Façade
- Flyweight <<< BACK HERE WITH .NET BENCHMARK>>>
- Proxy

## 2.3. Behavioral

- Chain of responsibility
- Command
- Interpreter
- Iterator
- Mediator
- Memento
- Null Object
- Observer
- State
- Strategy
- Template Method
- Visitor

# 3. Others patterns

- Monostate
- Ambient Context
- Specification
- Unit of work
- Notification
- CQRS

# 4. Gamma categorization

- Design Patters are typically split into three categories.
- This is called *Gamma Categorization* after Erick Gamma, one of GoF authors.
- **Create patterns**
  - Deal with the creation (construction) of objects.
  - Explicit (constructor) vs. implicit (DI, reflection, etc.).
  - Wholesale (single statement) vs. piecewise (step-by-step).
- **Structural patters**
  - Concerned with the structure (e.g., class members).
  - Many patterns are wrappers that mimic the underlying class interface.
  - Stress the important of good API design.
- **Behavioral patterns**
  - They are all different, no central theme.

# 5. Creational

## 5.1. Builder

- When construction gets a little bit too complicated.
- When piecewise object construction is complicated, provide an API for doing it succinctly.

### 5.1.1. Motivation

- Some objects are simple and can be created in a single constructor call.
- Other objects require a lot of ceremony to create.
- Having an object with 10 constructor arguments is not productive.
- Instead, opt for piecewise construction.
- Builder provides an API for constructing an object step-by-step.

### 5.1.2. Summary

- A builder is a separate component for building an object.
- Can either give builder an initializer or return it via a static function.
- To make builder fluent, return self (Method chaining).
- Different facets of an object can be built with different builders working in tandem via a base class.

## 5.2. Factories

- Factory Method and Abstract Factory.

### 5.2.1. Motivation

- Object creation logic becomes too convoluted.
- Initializer (Constructor) is not descriptive.
  - Python
    - Name is always `__init__`
  - C#
    - Name mandated by name of containing type.
  - Cannot overload with same sets of arguments with different names.
  - Can turn into "optional parameter hell".
- Wholesale object creation (non-piecewise, unlike Builder) can be outsourced to:
  - A separate method (Factory Method).
  - That may exists in separate class (Factory).
  - Can create hierarchy of factories with Abstract Factory.
- A component responsible solely for the wholesale (not piecewise) creation of objects.

### 5.2.2. Summary

- A factory method is a static method that creates objects.
- A factory can take care of object creation.
- A factory can be external or reside inside the object as an inner class.
- Hierarchies of factories can be used to create related objects.

## 5.3. Prototype

- When it's easier to copy an existing object to fully initialize a new one.

### 5.3.1. Motivation

- Complicated objects (e.g., cars) aren't designed from scratch.
  - They reiterate existing designs.
- An existing (partially or fully constructed) design is a Prototype.
- We make a copy (clone) the prototype and customize it.
  - Requires "deep copy" support.
- We make the cloning convenient (e.g., via a Factory).
- A partially or fully initialized object that you copy (clone) and make use of.

### 5.3.2. Summary

- To implement a prototype, partially construct an object and store it somewhere.
- C#
  - Clone the prototype:
    - Implement your own deep copy functionality; or
    - Serialize and deserialize.
- Python
  - Deep copy the prototype.
  - A Factory provides a convenient API for using prototypes.
- Customize the resulting instance.

## 5.4. Singleton

### 5.4.1. Motivation

- For some components it only makes sense to have one in the system:
  - Database repository.
  - Object factory.
- E.g., the constructor call is expensive:
  - We only do it once.
  - We provide everyone with the same instance.
- Want to prevent anyone creating additional copies.
- Need to take care of lazy instantiation and thread safety.
- A component which is instantiated only once.

### 5.4.2. Summary

- Python
  - Different realizations of Singleton: Custom allocator, decorator, metaclass
  - Laziness is easy, just init on first request.
  - Monostate variation.
  - Testability issues.
- C#
  - Making a "safe" singleton is easy: construct a static `Lazy<T>` and return its `Value`.
  - Singletons are difficult to test.
  - Instead of directly using a singleton, consider depending on an abstraction (e.g., an interface).
  - Consider defining singleton lifetime in DI container.

## 5.5. Creational Summary

- **Builder:**
  - Separate component for when object construction gets too complicated.
  - Can create mutually cooperation sub-builders.
  - Often has a fluent interface.
- **Factories:**
  - Factory method more expressive than initializer.
  - Factory can be an outside class or inner class; inner class has the benefit of accessing private members.
- **Prototype:**
  - Creation of object from an existing object.
  - Requires explicit deep copy or copy through serialization.
- **Singleton:**
  - When you need to ensure just a single instance exists.
  - C#
    - Made thread-safe and lazy with Lazy<T>.
  - Python
    - Easy to make with a decorator or metaclass.
  - Consider using dependency injection.

# 6. Structural

## 6.1. Adapter

- Getting the interface you want from the interface you have.
- A construct which adapt an existing interface **X** to conform to the required interface **Y**.

### 6.1.1. Motivation

- Electrical devices have different power (interface) requirements:
  - Voltage (5V, 220V).
  - Socket/plug type (Europe, UK, USA).
- We cannot modify out gadgets to support every possible interface:
  - Some support possible (e.g., 120/220V).
- Thus, we use a special device (an adapter) to give us the interface we require from the interface we have.

### 6.1.2. Summary

- Implementing an Adapter is easy.
- Determine the API you have and the API you need.
- Create a component which aggregates (has a reference to, ...) the **adaptee**.
- Intermediate representations can pile up: use **caching** and other optimizations.

## 6.2. Bridge

- Connecting components together through abstractions.

### 6.2.1. Motivation

- Bridge prevents a "Cartesian product" complexity explosion.
- Examples:
  - Base class `ThreadScheduler`.
  - Can be preemptive or cooperative.
  - Can run on Windows or Unix.
    - End up with a 2x2 scenario: WindowsPTS, UnixPTS, WindowsCTS, UnixCTS.
- Bridge pattern avoids the entity explosion.
- A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).

### 6.2.2. Summary

- Decouple abstraction from implementation.
- Both can exist as hierarchies.
- A stronger form of encapsulation.

## 6.3. Composite

- Treating individual and aggregate objects uniformly.

### 6.3.1. Motivation

- Objects use other object's fields/properties/members through inheritance and composition.
- Composition lets us make compound objects.
  - E.g., a mathematical expression composed of simple expressions; or
  - A grouping of shapes that consists of several shapes.
- Composite design pattern is used to treat both single (scalar) and composite objects uniformly.
  - C#
    - I.e., `Foo` and `Collection<Foo>` have common APIs.
  - Python
    - I.e., `Foo` and `Sequence` (yielding Foo's) have common APIs.
- A mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.

### 6.3.2. Summary

- Objects can use other objects via inheritance/composition.
- Some composed and singular objects need similar/identical behaviors.
- Composite design pattern lets us treat both types of object uniformly.
- C#
  - has special support for the enumeration concept.
  - A single object can masquerade as collection with `yield return this`.
- Python
  - Python supports interaction with `__iter__` the `ItetableABC`.
  - A single object can make itself iterable by yelding `self` from `__iter__`.

## 6.4. Decorator

- Adding behavior without altering the class itself.

### 6.4.1. Motivation

- Want to augment an object with additional functionality.
- Do not want to rewrite or alter existing code (OCP).
- Want to keep new functionality separate (SRP).
- Need to be able to interact with existing structures.
- Two options:
  - Inherit from required object (if possible); some objects are sealed (C#)
  - Build a decorator, which simply references the decorated object(s).
- Facilitates the addition of behaviors to individual objects without inheriting from them.

### 6.4.2. Summary

- A decorator keeps the reference to the decorated object(s).
- Adds utility attributes an methods to augment the object's features.
- May or may not forward calls to the underlying object.
- Proxying of underlying calls can be done dynamically.
- C#
  - Exists in a static variation
    - `X<Y<Foo>>`
    - Very limited due to inability to inherit from type parameters.
- Python
  - Python's functional decorators wrap functions; no direct relation to the GoF Decorator pattern.

## 6.5. Façade

![Façade diagram](Images/UmlFa%C3%A7ade.png)

- Exposing several components through a single interface.

### 6.5.1. Motivation

- Balancing complexity and presentation/usability.
  - Typical home:
    - Many subsystems (electrical, sanitation).
    - Complex internal structure (e.g. floor layers).
    - End user is not exposed to internals.
  - Same with software:
    - Many systems working to provide flexibility.
    - API consumers want it to "just work".
- Provides a simple, easy to understand/user interface over a large and sophisticated body of code.

### 6.5.2. Summary

- Build a Façade to provide a simplified API over a set of classes.
- May with to (optionally) expose internal through the Façade.
- May allow users to "Escalate" to use more complex APIs if they need to.

## 6.6. Flyweight

- Space optimization!

### 6.6.1. Motivation

- Avoid redundancy when storing data.
- E.G., MMORPG.
  - Plenty of users with identical first/last names.
  - No sense in storing same first/last name over and over again.
  - Store a list of names and pointers to them.
- .NET performs string interning, so an identical string is stored only once.
- E.g., bold or italic text formatting in the console:
  - Don't want each character to have a formatting character.
  - Operate on ranges (e.g., line number, start:end positions).
- A space optimization technique that lets us use less memory by storing externally the data associated with similar objects.

### 6.6.2. Summary

- Store common data externally.
- Define the idea of "ranges" on homogeneous collections and store data related to those ranges.
- C#
  - .NET string interning is the Flyweight pattern.
- Python
  - Specify an index or a reference into the external data store.

## 6.7. Proxy

- An interface for accessing a particular resource.

### 6.7.1. Motivation

- You are calling `foo.Bar()`.
- This assumes that `foo` is the same process as `Bar()`.
- What if, later on, you want to put all `Foo-related` operations into a separate process.
  - Can you avoid changing your code?
- Proxy to the rescue!
  - Same interface, entirely different behavior.
- This is called a **communication proxy**.
  - Other types: logging, virtual, guarding, ...
- A class that functions as an interface to a particular resource.
- That resource may be remote, expensive to construct, or may require logging or some other added functionality.

### 6.7.2. Summary

- A proxy has the same interface as the underlying object.
- To create a proxy, simply replicate the existing interface of an object.
- Add relevant functionality to the redefined member functions.
- Different proxies (communication, logging, caching, etc.) have completely different behaviors.

### 6.7.3. Proxy vs Decorator

- Proxy provides an identical interface; decorator provides an enhanced interface.
- Decorator typically aggregates (or has reference to) what it is decorating; proxy doesn't have to.
- Proxy might not even be working with a materialized object.

## 6.8. Structural Summary

- **Adapter:**
  - Converts the interface you get to the interface you need.
- **Bridge:**
  - Decouple abstraction from implementation.
- **Composite:**
  - Allows clients to treat individual objects and compositions of objects uniformly.
- **Decorator:**
  - Attach additional responsibilities to object.
  - Python
    - Has functional decorators.
- **Façade:**
  - Provide a single unified interface over a set of classes/systems/interfaces.
  - Friendly and easy-to-use, but can provide access to low-level features.
- **Flyweight:**
  - Efficiently support very large numbers of similar objects.
- **Proxy:**
  - Provide a surrogate object that forwards calls to the real object while performing additional functions.
  - E.g., access control, communication, logging, etc.
  - Dynamic proxy creates a proxy dynamically, without the necessity of replicating the target object API.

# 7. Behavioral

## 7.1. Chain of Responsibility

- Sequence of handlers processing an event one after another.

### 7.1.1. Motivation

- Unethical behavior by an employee; who takes the blame?
  - Employee.
  - Manager.
  - CEO.
- You click a graphical element on a form
  - Button handles it, stops further processing.
  - Underlying group box.
  - Underlying windows.
- CCG computer game
  - Creature has attack and defense values.
  - Those can be boosted by other cards.
- A chain of components who all get a chance to process a command or a query, optionally having default processing implementation and an ability to terminate the processing chain.

### 7.1.2. Summary

- Chain of Responsibility can be implemented as a chain of references or a centralized construct.
- Enlist objects in the chain, possibly controlling their order.
- C#
  - Object removal from chain (e.g., in `Disponse()`)
- Python
  - Object removal from chain (e.g., in `__exit__`)

## 7.2. Command

- You shall not pass!

### 7.2.1. Motivation

- Ordinary statements are perishable.
  - Cannot undo a field/property assignment.
  - Cannot directly serialize a sequence of action (calls).
- Want an object that represents an operation.
  - Scenario 1:
    - X should change its property Y to Z.
    - X should do W().
  - Scenario 2:
    - `person` should change its `age` to value 22.
    - `car` should to `explode()`.
- Uses: GUI commands, multi-level undo/redo, macro recording and more!
- An object which represents an instruction to perform a particular action.
  - Contains all the information necessary for the action to be taken.

### 7.2.2. Summary

- Encapsulate all details of an operation in separate object.
- Define instruction for applying the command (either in the command itself, or elsewhere).
- Optionally define instruction for undoing the command.
- Can create composite commands (a.k.a macros).

## 7.3. Interpreter

- Interpreters are all around us, Even now, in this very room.

### 7.3.1. Motivation

- Textual input needs to be processed
  - E.g., turned into OOP structures.
- Some examples:
  - Programming languages compilers, interpreters and IDEs.
  - HTML, XML and similar.
  - Numeric expressions (3+4/5).
  - Regular expressions.
- Turning strings into OOP based structures in a complicated process.
- A component that processes structured text data.
- Does so by turning it into separate lexical token (lexing) and then interpreting sequences of said token (parsing).

### 7.3.2. Summary

- Barring simples cases, an interpreter acts in two stages:
  - Lexing turns text into a set of token.
  - Parsing tokens into meaningful constructs.
- Parse data can then be traversed.

## 7.4. Iterator

- How traversal of data structures happens and who makes it happen.

### 7.4.1. Motivation

- Iteration (traversal) is a core functionality of various data structures.
- An `interator` is a class that facilitates the traversal.
  - Keeps a reference to the current element.
  - Know how to move to a different element.
- In Python, the iterator protocol requires:
  - `__iter__()` to expose the iterator, which uses.
  - `__next__()` to return each of the iterated elements or `raise StopIteration` when it's done.
- In .NET iterator is an implicit construct
  - .NET builds a state machine around you `yield` return statements.
- An object (or, in .NET, a method) that facilitates the traversal of a data structure.

### 7.4.2. Summary

- An iterator specified how you can traverse an object.
- C#
  - An iterator object, unlike a method, cannot be recursive.
  - Generally, an `IEnumerable<T>` returning method is enough.
  - Iterator works through `duck typing` - You need a `GetEnumerator()` that `yields` a type that has Current and `MoveNext()`.
- Python
  - Stateful iterators cannot be recursive.
  - `yield` allows for much more succinct iteration.

## 7.5. Mediator

- Facilitates communication between components.

### 7.5.1. Motivation

- Components may go in and out of a system at any time.
  - Chat room participants.
  - Players in an MMORPG.
- It makes no sense for them to have direct references to one another.
  - Those references may go dead.
- Solution: Have then all refer to some central component that facilitates communication.
- A component that facilitates communication between other components without them necessarily being aware of each other or having direct (reference) access to each other.

### 7.5.2. Summary

- Create the mediator and have each object in the system refer to it.
  - C#
    - E.g., in a field.
  - Python
    - E.g., in a property.
- Mediator engages in bi-directional communication with its connected components.
- Mediator has functions the components can call.
- Components have functions the mediator can call.
- Event processing (e.g., Rx) libraries make communication easier to implement.

## 7.6. Memento

- Keep a memento of an object's state to return to that state.

### 7.6.1. Motivation

- An object or system goes through changes.
  - E.g., a bank account gets deposits and withdrawals.
- There are different ways of navigating those changes.
- One way is to record every change (Command) and teach a command to "undo" itself.
- Another is to simply save snapshots of the system (Memento).
- A token/handle representing the system state.
  - Lets us roll back to the state when the token was generated.
  - May or may not directly expose state information.

### 7.6.2. Summary

- Mementos are used to roll back states arbitrarily.
- A memento is simply a token/handle class with (typically) no function of its own.
- A memento is not required to expose directly the state(s) to which it reverts the system.
- Can be used to implement undo/redo.

## 7.7. Null Object

- A behavioral design pattern with no behaviors.

### 7.7.1. Motivation

- When component `A` uses component `B`, it typically assumes that `B` is non-null.
  - You inject `B`, not `B?` or some `Option<B>`.
  - You do not check for null (?.) on every call.
- There is no option of telling `A` not to use an instance of `B`:
  - Its use is hard-coded.
  - Thus, we build a no-op, non-functioning inheritor of `B` and pass it into `A`.
- A no-op object that conforms to the required interface, satisfying a dependency requirement of some other object.

### 7.7.2. Summary

- Implement the required interface.
- Rewrite the methods with empty bodies:
  - If method is non-void, `return default(T)`.
  - If these values are ever used, you are in trouble.
- Supply an instance of Null Object in place of actual object.
- Dynamic construction possible.
  - With associated performance implications.

## 7.8. Observer

- I am watching you!

### 7.8.1. Motivation

- We need to be informed when certain things happen.
  - Object's property changes.
  - Object does somenthing.
  - Some external event occurs.
- We want to listen to events and be notified when they occur.
  - Notifications should include useful data.
- Want to unsubscribe from events if we're no longer interested.
- Built into C# with the `event` keyword:
  - But then what is this `IObservable<T>` / `IObserver<T>` for?
  - What about `InotifyPropertyChanging`/`Changed`?
  - And what are `BindingList<T>` / `ObservableCollection<T>`?
- An observer is an object that wishes to be informed about events happening in the system.
  - The entity generating the events in an observable.

### 7.8.2. Summary

- Observer is an intrusive approach: an observable must provide an event to subscribe to.
- Subscription and unsubscription handled with addition/removal of items in a list.
- Property notification are easy; dependent property notifications are tricky.
- C#
  - Special care must be taken to prevent issues in multithreaded scenarios.
  - .NET comes with observable collections
  - `IObserver<T>` / `IObservable<T>` are used in stream processing (Reactive Extension).

## 7.9. State

- Fun with Finite State Machines.

### 7.9.1. Motivation

- Considerer an ordinary telephone.
- What you do with it depends on the state of the phone/line.
  - If it's ringing or you want to make a call, you can pick it up.
  - Phone must be off the hook to talk/make a call.
  - If you try calling someone, and it's busy, you put the handset down.
- Changes in state can be explicit or in response to event (Observer pattern).
- A pattern in which the object's behavior is determined by its state.
- An object transitions from on state to another (something needs to trigger a transition).
- A formalized construct which manages state and transitions is called a state machine.

### 7.9.2. Summary

- Given sufficient complexity, it pays to formally define possible states and events/triggers.
- Can define:
  - State entry/exit behaviors.
  - Action when a particular event causes a transition.
  - Guard conditions enabling/disabling a transitions.
  - Default action when no transitions are found for an event.

## 7.10. Strategy

- System behavior partially specified at runtime.

### 7.10.1. Motivation

- Many algorithms can be decomposed into higher and lower level parts.
- Making tea can be decomposed into:
  - The process of making a hot beverage (boil water, pour into cup); and
  - Tea-specific things (put teabag into water)
- The high-level algorithm can then be reused for making coffee or hot chocolate.
  - Supported by beverage-specific strategies.
- Enables the exact behavior of a system to be selected at run-time.
- Also know as a _policy_ (esp. in the C++ world).

### 7.10.2. Summary

- Define an algorithm at a high level.
- Define the interface you expect each strategy to follow.
- Provide for dynamic composition of strategies in the resulting object.

## 7.11. Template Method

- A high-level blueprint for an algorithm to be completed by inheritors.

### 7.11.1. Motivation

- Algorithms can be decomposed into common parts + specifics.
- Strategy pattern does this through composition.
  - High-level algorithm uses an interface.
  - Concrete implementations implement the interface.
- Template Method does the same thing through inheritance.
  - Overall algorithm makes use of abstract member.
  - Inheritors override the abstract members.
  - Parent template method invoked.
- Template Method, allows us to define the "skeleton" of the algorithm, with concrete implementations defined in subclasses.

### 7.11.2. Summary

- Define an algorithm at a high level.
- Define constituent parts as abstract method/properties.
- Inherit the algorithm class providing necessary overrides.

## 7.12. Visitor

- Allows adding extra behaviors to entire hierarchies of classes.
- Typically a tool for structure traversal rather than anything else.

### 7.12.1. Motivation

- Need to define a new operation on an entire class hierarchy.
  - E.g., make a document model printable to HTML/Markdown
- Do not want to keep modifying every class in the hierarchy.
- Need access to the non-common aspects of classes in the hierarchy.
  - I.e., an extension method won't do.
- Create an external component to handle rendering.
  - But avoid explicitly type checks.
- A pattern where a component (visitor) is allowed to traverse the entire inheritance hierarchy.
- Implemented by propagating a single `visit()` method throughout the entire hierarchy.

### 7.12.2. Summary

- C#
  - Propagate an accept `(Visitor visitor)` method throughout the entire hierarchy.
  - Create a visitor with Visit(Foo), Visit(Bar), ... for each element in the hierarchy.
  - Each `accept()` simply calls `visitor.Visit(this)`.
  - Using `dynamic`, we can invoke right overload based on argument type alone (dynamic dispatch).
- Python
  - OOP double-dispatch approach is not necessary in Python.
  - Make a visitor, decorating each "overload" with `@visitor`.
  - Call `visit()` and the entire structure gets traversed.

## 7.13. Behavioral Summary

- **Chain of Responsibility:**
  - Allow components to process information/events in a chain.
  - Each element in the chain refers to next element.
    - Or make a list and go through it.
- **Command:**
  - Encapsulate a request into a separate object.
  - Good for audit, replay, undo/redo.
  - Part of CQS/CQRS (Query is also, effectively, a command).
- **Interpreter:**
  - Transform textual input into object-oriented structures.
  - Used by interpreters, compilers, static analysis tool, etc.
  - _Compiler Theory_ is a separate branch of Computer Science.
- **Iterator:**
  - Provides an interface for accessing elements of an aggregate object.
  - C#
    - `IEnumerable<T>` should be used in 99% of cases.
  - Python
    - `__iter__` / `__next` are stateful, but yield is much more convenient.
- **Mediator:**
  - Provides mediation services between two objects.
  - E.g., message passing, chat room
- **Memento:**
  - Yields tokens representing system states.
  - Tokens do not allow direct manipulation, but can be used in appropriate APIs.
- **Observer:**
  - Allows notifications of changes/happenings in a component.
  - C#
    - Built with the `event` keyword.
    - Additional support provided for properties, collections and observable streams.
- **State:**
  - We model systems by having one of a possible states and transitions between these states.
  - Such a system if called a **state machine**.
  - Special frameworks exists to orchestrate state machines.
- **Strategy and Template Method**
  - Both patterns define an algorithm blueprint/placeholder.
  - Strategy uses ordinary composition, Template Method uses inheritance.
- **Visitor:**
  - Adding functionality to existing classes through double dispatch.
  - C#
    - `Dynamic` visitor possible, but with performance cost.

# 8. Duck Typing Mixins

- The `IScalar<T>` mixing is a real-world mixing.
- It's used in situations where you want a "true" implementation of a Composite pattern, i.e., when you want composite objects and scalar object to be both enumerable.

# 9. Personal choices of GoF patterns

- Most used:
  - Factory Method / Abstract Factory
  - Singleton
  - Adapter
  - Façade
  - Decorator
  - Proxy
  - State
  - Strategy (Composition) / Template method (Inheritance)
  - Command
  - Iterator
- Very very very specific uses:
  - Flyweight (Performance)
  - Interpreter (Compilator/Interpreter)

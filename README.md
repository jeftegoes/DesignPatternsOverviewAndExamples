# Design patterns overview and examples <!-- omit in toc -->

## Contents <!-- omit in toc -->

- [1. Overview](#1-overview)
- [2. The Patterns](#2-the-patterns)
- [3. Others patterns](#3-others-patterns)
- [4. Gamma categorization](#4-gamma-categorization)
- [5. Creational](#5-creational)
  - [5.1. Builder](#51-builder)
    - [5.1.1. Motivation](#511-motivation)
    - [5.1.2. Summary](#512-summary)
  - [5.2. Singleton](#52-singleton)
    - [5.2.1. Motivation](#521-motivation)
    - [5.2.2. Summary](#522-summary)
- [6. Structural](#6-structural)
  - [6.1. Adapter](#61-adapter)
    - [6.1.1. Motivation](#611-motivation)
    - [6.1.2. Summary](#612-summary)
  - [6.2. Bridge](#62-bridge)
  - [6.3. Composite](#63-composite)
    - [6.3.1. Motivation](#631-motivation)
    - [6.3.2. Summary](#632-summary)
  - [6.4. Façade](#64-façade)
    - [6.4.1. Motivation](#641-motivation)
    - [6.4.2. Summary](#642-summary)
  - [6.5. Flyweight](#65-flyweight)
    - [6.5.1. Motivation](#651-motivation)
    - [6.5.2. Summary](#652-summary)
- [7. Behavioral](#7-behavioral)
  - [7.1. Command](#71-command)
    - [7.1.1. Motivation](#711-motivation)
    - [7.1.2. Summary](#712-summary)
  - [7.2. Null Object](#72-null-object)
    - [7.2.1. Motivation](#721-motivation)
    - [7.2.2. Summary](#722-summary)
  - [7.3. Template Method](#73-template-method)
    - [7.3.1. Motivation](#731-motivation)
    - [7.3.2. Summary](#732-summary)
- [8. Duck Typing Mixins](#8-duck-typing-mixins)

# 1. Overview

- Design pattern are common architectural approaches.
- Popularized by the [Gang of Four book (1994)](http://wiki.c2.com/?GangOfFour).
  - Smaltalk and C++
- Translated to many OOP languages
  - C#, Java, Python, ...
- Universally relevant.
  - Internalized in some programming languages.
  - Libraries.

# 2. The Patterns

- Creational
  - **Builder**
  - Factories
    - Abstract factory
    - Factory Method
  - Prototype
  - **Singleton**
- Structural
  - **Adapter**
  - Bridge
  - Composite
  - **Decorator**
  - **Façade**
  - Flyweight <<< BACK HERE WITH .NET BENCHMARK>>>
  - Proxy
- Behavioral
  - Chain of responsability
  - Command
  - Interpreter
  - Iterator
  - **Mediator**
  - Memento
  - Null Object
  - Observer
  - State
  - **Strategy**
  - **Template Method**
  - **Visitor**

# 3. Others patterns

- Monostate
- Ambient Context
- Specification

# 4. Gamma categorization

- Design Patters are typically split in to three categories.
- This is called Gamma Categorization after Erick Gamma, one of GoF authors.
- Create patterns:
  - Deal with the creation (construction) of objects.
  - Explicit (constructor) vs. implicit (DI, reflection, etc.).
  - Wholesale (single statement) vs. piecewise (step-by-step).
- Structural patters:
  - Concerned with the structure (e.g., class members).
  - Many patterns are wrappers that mimic the underlying class interface.
  - Stress the importante of good API design.
- Behavioral patterns:
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
- To make builder fluent, return self.
- Different facets of an object can be built with different builders working in tandem via a base class.

## 5.2. Singleton

### 5.2.1. Motivation

- For some components it only makes sense to have one in the system:
  - Database repository.
  - Object factory.
- E.g., the constructor call is expensive:
  - We only do it once.
  - We provide everyone with the same instance.
- Want to prevent anyone creating additional copies.
- Need to take care of lazy instantiation and thread safety.
- A component which is instantiated only once.

### 5.2.2. Summary

- Making a 'safe' singleton is easy: construct a static `Lazy<T>` and return its `Value`.
- Singletons are difficult to test.
- Instead of directly using a singleton, consider depending on an abstraction (e,g,m an interface).
- Consider defining singleton lifetime in DI container.

# 6. Structural

## 6.1. Adapter

- Getting the interface you want from the interface you have.
- A construct which adapt an existing interface X to conform to the required interface Y.

### 6.1.1. Motivation

- Electrical devices have different power (interface) requirements:
  - Voltage (5V, 220V).
  - Socket/plug type (Europe, UK, USA).
- We cannot modify out gadgets to support every possible interface:
  - Some support possible (e.g, 120/220V).
- Thus, we use a special device (an adapter) to give us the interface we require from the interface we have.

### 6.1.2. Summary

- Implementing an Adapter is easy.
- Determine the API you have and the API you need.
- Create a component which aggregates (has a reference to, ...) the **adaptee**.
- Intermediate representations can pile up: use **caching** and other optimizations.

## 6.2. Bridge

- Connecting components together through abstractions.
- Bridge prevents a "Cartesian product" complexity explosion.
- Bridge pattern avoids the entity explosion.
- A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).
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
  - I.e., `Foo` and `Collection<Foo>` have common APIs.
- A mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.

### 6.3.2. Summary

- Objects can use other objects via inheritance/composition.
- Some composed and singular objects need similar/identical behaviors.
- Composite design pattern lets us treat both types of object uniformly.
- C# has special support for the enumeration concept.
- A single object can masquerade as collection with `yield return this`.

## 6.4. Façade

![Façade diagram](Images/UmlFa%C3%A7ade.png)

- Exposing several components through a single interface.

### 6.4.1. Motivation

- Balancing complexity and presentation/usability.
  - Typical home:
    - Many subsystems (electrical, sanitation).
    - Complex internal structure (e.g. floor layers).
    - End user is not exposed to internals.
  - Same with software:
    - Many systems working to provide flexibility.
    - API consumers want it to "just work".
- Provides a simple, easy to understand/user interface over a large and sophisticated body of code.

### 6.4.2. Summary

- Build a Façade to provide a simplified API over a set of classes.
- May with to (optionally) expose internal through the Façade.
- May allow users to "Escalate" to use more complex APIs if they need to.

## 6.5. Flyweight

- Space otimization!

### 6.5.1. Motivation

- Avoid redundancy when storing data.
- E.G., MMORPG.
  - Plenty of users with identical first/last names.
  - No sense in storing same first/last name over and over again.
  - Store a list of names and pointers to them.
- .NET performs string interning, so an identical string is stored only once.
- E.g., bold or italic text in the console:
  - Don't want each character to have a formatting character.
  - Operate on ranges (e.g., line number, start:end positions).
- A space optimization technique that lets us use less memory by storing externally the data associated with similar objects.

### 6.5.2. Summary

- Store common data externally.
- Define the idea of "ranges" on homogeneous collections and store data related to those ranges.
- .NET string interning is the Flyweight pattern.

# 7. Behavioral

## 7.1. Command

- You shall not pass!

### 7.1.1. Motivation

- Ordinary C# statements are perishable.
  - Cannot undo a field/property assignment.
  - Cannot directly serialize a sequence of action (calls).
- Want an object that represents an operation.
  - X should change its property Y to Z.
  - X should do W().
- Uses: GUI commands, multi-level undo/redo, macro recording and more!
- An object which represents an instruction to perform a particular action.
  - Contains all the information necessary for the action to be taken.

### 7.1.2. Summary

- Encapsulate all details of an operation in separate object.
- Define instruction for applying the command (either in the command itself, or elsewhere).
- Optionally define instruction for undoing the command.
- Can create composite commands (a.k.a macros).

## 7.2. Null Object

- A behavioral design pattern with no behaviors.

### 7.2.1. Motivation

- When component `A` uses component `B`, it typically assumes that `B` is non-null.
  - You inject `B`, not `B?` or some `Option<B>`.
  - You do not check for null (?.) on every call.
- There is no option of telling `A` not to use an instance of `B`:
  - Its use is hard-coded.
  - Thus, we build a no-op, non-functioning inheritor of `B` and pass it into `A`.
- A no-op object that conforms to the required interface, satisfying a dependency requirement of some other object.

### 7.2.2. Summary

- Implement the required interface.
- Rewrite the methods with empty bodies:
  - If method is non-void, `return default(T)`.
  - If these values are ever used, you are in trouble.
- Supply an instance of Null Object in place of actual object.
- Dynamic construction possible.
  - With associated performance implications.

## 7.3. Template Method

- A high-level blueprint for an algorithm to be completed by inheritors.

### 7.3.1. Motivation

- Algorithms can be decomposed into common parts + specifics.
- Strategy pattern does this through composition.
  - High-level algorithm uses an interface.
  - Concrete implementations implement the interface.
- Template Method does the same thing through inheritance.
  - Overall algorithm makes use of abstract member.
  - Inheritors override the abstract members.
  - Parent template method invoked.
- Template Method, allows us to define the "skeleton" of the algorithm, with concrete implementations defined in subclasses.

### 7.3.2. Summary

- Define an algorithm at a high level.
- Define constituent parts as abstract method/properties.
- Inherit the algorithm class providing necessary overrides.

# 8. Duck Typing Mixins

- The `IScalar<T>` mixing is a real-world mixing.
- It's used in situations where you want a 'true' implementation of a Composite pattern, i.e., when you want composite objects and scalar object to be both enumerable.

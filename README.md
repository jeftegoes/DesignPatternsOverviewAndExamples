# Design patterns overview and examples <!-- omit in toc -->

## Contents <!-- omit in toc -->

- [1. Overview](#1-overview)
- [2. The Patterns](#2-the-patterns)
- [3. Others patterns](#3-others-patterns)
- [4. Gamma categorization](#4-gamma-categorization)
- [5. Creational](#5-creational)
  - [5.1. Builder](#51-builder)
    - [5.1.1. Motivation](#511-motivation)
  - [5.2. Singleton](#52-singleton)
    - [5.2.1. Motivation](#521-motivation)
    - [5.2.2. Resume](#522-resume)
- [6. Structural](#6-structural)
  - [6.1. Bridge](#61-bridge)
  - [6.2. Composite](#62-composite)
  - [6.3. Façade](#63-façade)
    - [6.3.1. Motivation](#631-motivation)
    - [6.3.2. Resume](#632-resume)
  - [6.4. Command](#64-command)
- [7. Behavioral](#7-behavioral)
  - [7.1. Null Object](#71-null-object)
    - [7.1.1. Motivation](#711-motivation)
    - [7.1.2. Resume](#712-resume)
  - [7.2. Template Method](#72-template-method)
    - [7.2.1. Motivation](#721-motivation)
    - [7.2.2. Resume](#722-resume)
- [8. Duck Typing Mixins](#8-duck-typing-mixins)

# 1. Overview

- Design pattern are common architectural approaches.
- Popularized by the [Gang of Four book (1994)](http://wiki.c2.com/?GangOfFour).
- Universally relevant.
  - Internalized in some programming languages.
  - Libraries

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
  - Flyweight
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
  - **Specification**
  - **Template Method**
  - **Visitor**

# 3. Others patterns

- Monostate
- Ambient Context

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

### 5.2.2. Resume

- Making a 'safe' singleton is easy: construct a static `Lazy<T>` and return its `Value`.
- Singletons are difficult to test.
- Instead of directly using a singleton, consider depending on an abstraction (e,g,m an interface).
- Consider defining singleton lifetime in DI container.

# 6. Structural

## 6.1. Bridge

- Connecting components together through abstractions.
- Bridge prevents a "Cartesian product" complexity explosion.
- Bridge pattern avoids the entity explosion.
- A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).
- Decouple abstraction from implementation.
- Both can exist as hierarchies.
- A stronger form of encapsulation.

## 6.2. Composite

- Treating individual and aggregate objects uniformly.
- Objects use other object's fields/properties/members through inheritance and composition.
- Composition lets us make compound objects.
  - E.g., a mathematical expression composed of simple expressions; or
  - A grouping of shapes that consists of several shapes.
- Composite design pattern is used to treat both single (scalar) and composite objects uniformly.
  - I.e., `Foo` and `Collection<Foo>` have common APIs.
- A mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.

## 6.3. Façade

![Façade diagram](Images/UmlFa%C3%A7ade.png)

- Exposing several components through a single interface.

### 6.3.1. Motivation

- Balancing complexity and presentation/usability.
  - Typical home:
    - Many subsystems (electrical, sanitation).
    - Complex internal structure (e.g. floor layers).
    - End user is not exposed to internals.
  - Same with software:
    - Many systems working to provide flexibility.
    - API consumers want it to "just work".
- Provides a simple, easy to understand/user interface over a large and sophisticated body of code.

### 6.3.2. Resume

- Build a Façade to provide a simplified API over a set of classes.
- May with to (optionally) expose internal through the Façade.
- May allow users to "Escalate" to use more complex APIs if they need to.

## 6.4. Command



# 7. Behavioral

## 7.1. Null Object

- A behavioral design pattern with no behaviors.

### 7.1.1. Motivation

- When component `A` uses component `B`, it typically assumes that `B` is non-null.
  - You inject `B`, not `B?` or some `Option<B>`.
  - You do not check for null (?.) on every call.
- There is no option of telling `A` not to use an instance of `B`:
  - Its use is hard-coded.
  - Thus, we build a no-op, non-functioning inheritor of `B` and pass it into `A`.
- A no-op object that conforms to the required interface, satisfying a dependency requirement of some other object.

### 7.1.2. Resume

- Implement the required interface.
- Rewrite the methods with empty bodies:
  - If method is non-void, `return default(T)`.
  - If these values are ever used, you are in trouble.
- Supply an instance of Null Object in place of actual object.
- Dynamic construction possible.
  - With associated performance implications.

## 7.2. Template Method

- A high-level blueprint for an algorithm to be completed by inheritors.

### 7.2.1. Motivation

- Algorithms can be decomposed into common parts + specifics.
- Strategy pattern does this through composition.
  - High-level algorithm uses an interface.
  - Concrete implementations implement the interface.
- Template Method does the same thing through inheritance.
  - Overall algorithm makes use of abstract member.
  - Inheritors override the abstract members.
  - Parent template method invoked.
- Template Method, allows us to define the "skeleton" of the algorithm, with concrete implementations defined in subclasses.

### 7.2.2. Resume

- Define an algorithm at a high level.
- Define constituent parts as abstract method/properties.
- Inherit the algorithm class providing necessary overrides.

# 8. Duck Typing Mixins

- The `IScalar<T>` mixing is a real-world mixing.
- It's used in situations where you want a 'true' implementation of a Composite pattern, i.e., when you want composite objects and scalar object to be both enumerable.

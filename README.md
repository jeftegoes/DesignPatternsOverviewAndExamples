# Design patterns overview and examples <!-- omit in toc -->

## Contents <!-- omit in toc -->

- [1. Overview](#1-overview)
- [2. The Patterns](#2-the-patterns)
- [3. Gamma categorization](#3-gamma-categorization)
- [4. Creational](#4-creational)
  - [4.1. Builder](#41-builder)
    - [4.1.1. Motivation](#411-motivation)
- [5. Structural](#5-structural)
  - [5.1. Bridge](#51-bridge)
  - [5.2. Composite](#52-composite)
  - [5.3. Façade](#53-façade)
    - [5.3.1. Motivation](#531-motivation)
    - [5.3.2. Resume](#532-resume)
- [6. Behavioral](#6-behavioral)
  - [6.1. Null Object](#61-null-object)
  - [6.2. Template Method](#62-template-method)
    - [6.2.1. Motivation](#621-motivation)
    - [6.2.2. Resume](#622-resume)
- [7. Duck Typing Mixins](#7-duck-typing-mixins)

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
  - Adapter
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
  - Mediator
  - Memento
  - Null Object
  - Observer
  - State
  - **Strategy**
  - **Specification**
  - **Template Method**
  - **Visitor**

# 3. Gamma categorization

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

# 4. Creational

## 4.1. Builder

- When construction gets a little bit too complicated.
- When piecewise object construction is complicated, provide an API for doing it succinctly.

### 4.1.1. Motivation

- Some objects are simple and can be created in a single constructor call.
- Other objects require a lot of ceremony to create.
- Having an object with 10 constructor arguments is not productive.
- Instead, opt for piecewise construction.
- Builder provides an API for constructing an object step-by-step.

# 5. Structural

## 5.1. Bridge

- Connecting components together through abstractions.
- Bridge prevents a "Cartesian product" complexity explosion.
- Bridge pattern avoids the entity explosion.
- A mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).
- Decouple abstraction from implementation.
- Both can exist as hierarchies.
- A stronger form of encapsulation.

## 5.2. Composite

- Treating individual and aggregate objects uniformly.
- Objects use other object's fields/properties/members through inheritance and composition.
- Composition lets us make compound objects.
  - E.g., a mathematical expression composed of simple expressions; or
  - A grouping of shapes that consists of several shapes.
- Composite design pattern is used to treat both single (scalar) and composite objects uniformly.
  - I.e., `Foo` and `Collection<Foo>` have common APIs.
- A mechanism for treating individual (scalar) objects and compositions of objects in a uniform manner.

## 5.3. Façade

![Façade diagram](Images/UmlFa%C3%A7ade.png)

- Exposing several components through a single interface.

### 5.3.1. Motivation

- Balancing complexity and presentation/usability.
  - Typical home:
    - Many subsystems (electrical, sanitation).
    - Complex internal structure (e.g. floor layers).
    - End user is not exposed to internals.
  - Same with software:
    - Many systems working to provide flexibility.
    - API consumers want it to "just work".
- Provides a simple, easy to understand/user interface over a large and sophisticated body of code.

### 5.3.2. Resume

- Build a Façade to provide a simplified API over a set of classes.
- May with to (optionally) expose internal through the Façade.
- May allow users to "Escalate" to use more complex APIs if they need to.

# 6. Behavioral

## 6.1. Null Object

- A behavioral design pattern with no behaviors.

## 6.2. Template Method

- A high-level blueprint for an algorithm to be completed by inheritors.

### 6.2.1. Motivation

- Algorithms can be decomposed into common parts + specifics.
- Strategy pattern does this through composition.
  - High-level algorithm uses an interface.
  - Concrete implementations implement the interface.
- Template Method does the same thing through inheritance.
  - Overall algorithm makes use of abstract member.
  - Inheritors override the abstract members.
  - Parent template method invoked.
- Template Method, allows us to define the "skeleton" of the algorithm, with concrete implementations defined in subclasses.

### 6.2.2. Resume

- Define an algorithm at a high level.
- Define constituent parts as abstract method/properties.
- Inherit the algorithm class providing necessary overrides.

# 7. Duck Typing Mixins

- The `IScalar<T>` mixing is a real-world mixing.
- It's used in situations where you want a 'true' implementation of a Composite pattern, i.e., when you want composite objects and scalar object to be both enumerable.

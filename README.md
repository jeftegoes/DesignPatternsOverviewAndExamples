# Design patterns overview and examples <!-- omit in toc -->

## Contents <!-- omit in toc -->

- [1. Overview](#1-overview)
- [2. The Patterns](#2-the-patterns)
- [Gamma categorization](#gamma-categorization)
- [Builder](#builder)
  - [Motivation](#motivation)
- [Façade](#façade)

# 1. Overview

- Design pattern are common architectural approaches.
- Popularized by the [Gang of Four book (1994)](http://wiki.c2.com/?GangOfFour).
- Universally relevant.
  - Internalized in some programming languages.
  - Libraries

# 2. The Patterns

- Creational
  - Builder
  - Factories
    - Abstract factory
    - Factory Method
  - Prototype
  - Singleton
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

# Gamma categorization

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

# Builder

- When construction gets a little bit too complicated.
- When piecewise object construction is complicated, provide an API for doing it succinctly.

## Motivation

- Some objects are simple and can be created in a single constructor call.
- Other objects require a lot of ceremony to create.
- Having an object with 10 constructor arguments is not productive.
- Instead, opt for piecewise construction.
- Builder provides an API for constructing an object step-by-step.

# Façade

- Exposing several components through a single interface.
- Balancing complexity and presentation/usability.
  - Typical home:
    - Many subsystems (electrical, sanitation).
    - Complex internal structure (e.g. floor layers).
    - End user is not exposed to internals.
  - Same with software:
    - Many systems working to provide flexibility.
    - API consumers want it to "just work".
- Provides a simple, easy to understand/user interface over a large and sophisticated body of code.
- Build a Façade to provide a simplified API over a set of classes.
- May with to (optionally) expose internal through the Façade.
- May allow users to "Escalate" to use more complex APIs if they need to.

# Practical 08 – Semantic Network using Predicate Logic

## Aim
To demonstrate the concept of Semantic Network using predicate logic to represent knowledge.

---

## Introduction
A Semantic Network is a knowledge representation technique in Artificial Intelligence 
that represents concepts as nodes and relationships as links.

It is based on **predicate logic**, where relationships like "is-a", "has-a", and "can" 
are used to define knowledge.

---

## Concept
Semantic networks store knowledge in the form of:

- Nodes → Objects (Bird, Dog, Animal)
- Links → Relationships (ISA, HAS, CAN)

---

## Types of Relationships

1. ISA (Inheritance)
   - Represents "is-a" relationship
   - Example: Bird is an Animal

2. HAS-A (Property)
   - Represents attributes
   - Example: Animal has cells

3. CAN (Ability)
   - Represents abilities
   - Example: Bird can fly

---

## Working Principle
1. Define relationships using dictionaries.
2. Use functions to check inheritance.
3. Apply predicate logic to derive knowledge.
4. Support inheritance (child gets parent properties).

---

## Example
Bird → Animal  
Animal → has → Cells  

So, Bird has Cells.

---

## Advantages
- Easy to understand
- Supports inheritance
- Logical knowledge representation
- Useful in AI systems

---

## Applications
- Expert systems
- Natural language processing
- Knowledge-based systems
- AI reasoning

---

## Conclusion
Semantic networks effectively represent knowledge using relationships. 
Inheritance allows efficient reasoning and reduces redundancy in AI systems.
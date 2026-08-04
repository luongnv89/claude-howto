# Code Smells Catalog

A comprehensive reference of code smells based on Martin Fowler's *Refactoring* (2nd Edition). Code smells are symptoms of deeper problems—they indicate that something might be wrong with your code's design.

> "A code smell is a surface indication that usually corresponds to a deeper problem in the system." — Martin Fowler

---

## Bloaters

Code smells representing something that has grown too large to be handled effectively.

### Long Method

**Signs:**
- Method exceeds 30-50 lines
- Need to scroll to see the whole method
- Multiple levels of nesting
- Comments explaining what sections do

**Why it's bad:**
- Hard to understand
- Difficult to test in isolation
- Changes have unintended consequences
- Duplicate logic hides inside

**Refactorings:**
- Extract Method
- Replace Temp with Query
- Introduce Parameter Object
- Replace Method with Method Object
- Decompose Conditional

**Example (Before):**
```javascript
function processOrder(order) {
  // Validate order (20 lines)
  if (!order.items) throw new Error('No items');
  if (order.items.length === 0) throw new Error('Empty order');
  // ... more validation

  // Calculate totals (30 lines)
  let subtotal = 0;
  for (const item of order.items) {
    subtotal += item.price * item.quantity;
  }
  // ... tax, shipping, discounts

  // Send notifications (20 lines)
  // ... email logic
}
```

**Example (After):**
```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  sendOrderNotifications(order, totals);
  return { order, totals };
}
```

---

### Large Class

**Signs:**
- Class has many instance variables (>7-10)
- Class has many methods (>15-20)
- Class name is vague (Manager, Handler, Processor)
- Methods don't use all instance variables

**Why it's bad:**
- Violates Single Responsibility Principle
- Hard to test
- Changes ripple through unrelated features
- Difficult to reuse parts

**Refactorings:**
- Extract Class
- Extract Subclass
- Extract Interface

**Detection:**
```
Lines of code > 300
Number of methods > 15
Number of fields > 10
```

---

### Primitive Obsession

**Signs:**
- Using primitives for domain concepts (string for email, int for money)
- Arrays of primitives instead of objects
- String constants for type codes
- Magic numbers/strings

**Why it's bad:**
- No validation at type level
- Logic scattered across codebase
- Easy to pass wrong values
- Missing domain concepts

**Refactorings:**
- Replace Primitive with Object
- Replace Type Code with Class
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**Example (Before):**
```javascript
const user = {
  email: 'john@example.com',     // Just a string
  phone: '1234567890',           // Just a string
  status: 'active',              // Magic string
  balance: 10050                 // Cents as integer
};
```

**Example (After):**
```javascript
const user = {
  email: new Email('john@example.com'),
  phone: new PhoneNumber('1234567890'),
  status: UserStatus.ACTIVE,
  balance: Money.cents(10050)
};
```

---

### Long Parameter List

**Signs:**
- Methods with 4+ parameters
- Parameters that always appear together
- Boolean flags changing method behavior
- Null/undefined passed frequently

**Why it's bad:**
- Hard to call correctly
- Parameter order confusion
- Indicates method doing too much
- Hard to add new parameters

**Refactorings:**
- Introduce Parameter Object
- Preserve Whole Object
- Replace Parameter with Method Call
- Remove Flag Argument

**Example (Before):**
```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy) {
  // ...
}
```

**Example (After):**
```javascript
function createUser(personalInfo, address, options) {
  // personalInfo: { firstName, lastName, email, phone }
  // address: { street, city, state, zip }
  // options: { isAdmin, isActive, createdBy }
}
```

---

### Data Clumps

**Signs:**
- Same 3+ fields appear together repeatedly
- Parameters that always travel together
- Classes with field subsets belonging together

**Why it's bad:**
- Duplicate handling logic
- Missing abstraction
- Harder to extend
- Indicates hidden class

**Refactorings:**
- Extract Class
- Introduce Parameter Object
- Preserve Whole Object

**Example:**
```javascript
// Data clump: (x, y, z) coordinates
function movePoint(x, y, z, dx, dy, dz) { }
function scalePoint(x, y, z, factor) { }
function distanceBetween(x1, y1, z1, x2, y2, z2) { }

// Extract Point3D class
class Point3D {
  constructor(x, y, z) { }
  move(delta) { }
  scale(factor) { }
  distanceTo(other) { }
}
```

---

## Object-Orientation Abusers

Smells indicating incomplete or incorrect use of OOP principles.

### Switch Statements

**Signs:**
- Long switch/case or if/else chains
- Same switch in multiple places
- Switch on type codes
- Adding new cases requires changes everywhere

**Why it's bad:**
- Violates Open/Closed Principle
- Changes ripple to all switch locations
- Hard to extend
- Often indicates missing polymorphism

**Refactorings:**
- Replace Conditional with Polymorphism
- Replace Type Code with Subclasses
- Replace Type Code with State/Strategy

**Example (Before):**
```javascript
function calculatePay(employee) {
  switch (employee.type) {
    case 'hourly':
      return employee.hours * employee.rate;
    case 'salaried':
      return employee.salary / 12;
    case 'commissioned':
      return employee.sales * employee.commission;
  }
}
```

**Example (After):**
```javascript
class HourlyEmployee {
  calculatePay() {
    return this.hours * this.rate;
  }
}

class SalariedEmployee {
  calculatePay() {
    return this.salary / 12;
  }
}
```

---

### Temporary Field

**Signs:**
- Instance variables only used in some methods
- Fields set conditionally
- Complex initialization for certain cases

**Why it's bad:**
- Confusing—field exists but might be null
- Hard to understand object state
- Indicates conditional logic hiding

**Refactorings:**
- Extract Class
- Introduce Null Object
- Replace Temp Field with Local

---

### Refused Bequest

**Signs:**
- Subclass doesn't use inherited methods/data
- Subclass overrides to do nothing
- Inheritance used for code reuse, not IS-A relationship

**Why it's bad:**
- Wrong abstraction
- Violates Liskov Substitution Principle
- Misleading hierarchy

**Refactorings:**
- Push Down Method/Field
- Replace Subclass with Delegate
- Replace Inheritance with Delegation

---

### Alternative Classes with Different Interfaces

**Signs:**
- Two classes that do similar things
- Different method names for same concept
- Could be used interchangeably

**Why it's bad:**
- Duplicate implementations
- No common interface
- Hard to switch between

**Refactorings:**
- Rename Method
- Move Method
- Extract Superclass
- Extract Interface

---

## Change Preventers

Smells that make changes difficult—changing one thing requires changing many others.

### Divergent Change

**Signs:**
- One class changed for multiple different reasons
- Changes in different areas trigger same class edits
- Class is a "God class"

**Why it's bad:**
- Violates Single Responsibility
- High change frequency
- Merge conflicts

**Refactorings:**
- Extract Class
- Extract Superclass
- Extract Subclass

**Example:**
A `User` class changes for:
- Authentication changes
- Profile changes
- Billing changes
- Notification changes

→ Extract: `AuthService`, `ProfileService`, `BillingService`, `NotificationService`

---

### Shotgun Surgery

**Signs:**
- One change requires edits in many classes
- Small feature needs touching 10+ files
- Changes are scattered, hard to find all

**Why it's bad:**
- Easy to miss a spot
- High coupling
- Changes are error-prone

**Refactorings:**
- Move Method
- Move Field
- Inline Class

**Detection:**
Look for: adding one field requires changes in >5 files.

---

### Parallel Inheritance Hierarchies

**Signs:**
- Creating subclass in one hierarchy requires subclass in another
- Class prefixes match (e.g., `DatabaseOrder`, `DatabaseProduct`)

**Why it's bad:**
- Double the maintenance
- Coupling between hierarchies
- Easy to forget one side

**Refactorings:**
- Move Method
- Move Field
- Eliminate one hierarchy

---

## Dispensables

Something unnecessary that should be removed.

### Comments (Excessive)

**Signs:**
- Comments explaining what code does
- Commented-out code
- TODO/FIXME that linger forever
- Apologies in comments

**Why it's bad:**
- Comments lie (get out of sync)
- Code should be self-documenting
- Dead code causes confusion

**Refactorings:**
- Extract Method (name explains what)
- Rename (clarity without comments)
- Remove commented code
- Introduce Assertion

**Good vs Bad Comments:**
```javascript
// BAD: Explaining what
// Loop through users and check if active
for (const user of users) {
  if (user.status === 'active') { }
}

// GOOD: Explaining why
// Active users only - inactive are handled by cleanup job
const activeUsers = users.filter(u => u.isActive);
```

---

### Duplicate Code

**Signs:**
- Same code in multiple places
- Similar code with small variations
- Copy-paste patterns

**Why it's bad:**
- Bug fixes needed in multiple places
- Inconsistency risk
- Bloated codebase

**Refactorings:**
- Extract Method
- Extract Class
- Pull Up Method (in hierarchies)
- Form Template Method

**Detection Rule:**
Any code duplicated 3+ times should be extracted.

---

### Lazy Class

**Signs:**
- Class doesn't do enough to justify existence
- Wrapper with no added value
- Result of over-engineering

**Why it's bad:**
- Maintenance overhead
- Unnecessary indirection
- Complexity without benefit

**Refactorings:**
- Inline Class
- Collapse Hierarchy

---

### Dead Code

**Signs:**
- Unreachable code
- Unused variables/methods/classes
- Commented-out code
- Code behind impossible conditions

**Why it's bad:**
- Confusion
- Maintenance burden
- Slows down understanding

**Refactorings:**
- Remove Dead Code
- Safe Delete

**Detection:**
```bash
# Look for unused exports
# Look for unreferenced functions
# IDE "unused" warnings
```

---

### Speculative Generality

**Signs:**
- Abstract classes with one subclass
- Unused parameters "for future use"
- Methods that only delegate
- "Framework" for one use case

**Why it's bad:**
- Complexity without benefit
- YAGNI (You Ain't Gonna Need It)
- Harder to understand

**Refactorings:**
- Collapse Hierarchy
- Inline Class
- Remove Parameter
- Rename Method

---

## Couplers

Smells that represent excessive coupling between classes.

### Feature Envy

**Signs:**
- Method uses more data from another class than its own
- Many getter calls to another object
- Data and behavior are separated

**Why it's bad:**
- Wrong location for behavior
- Poor encapsulation
- Hard to maintain

**Refactorings:**
- Move Method
- Move Field
- Extract Method (then move)

**Example (Before):**
```javascript
class Order {
  getDiscountedPrice(customer) {
    // Uses customer data heavily
    if (customer.loyaltyYears > 5) {
      return this.price * customer.discountRate;
    }
    return this.price;
  }
}
```

**Example (After):**
```javascript
class Customer {
  getDiscountedPriceFor(price) {
    if (this.loyaltyYears > 5) {
      return price * this.discountRate;
    }
    return price;
  }
}
```

---

### Inappropriate Intimacy

**Signs:**
- Classes access each other's private parts
- Bidirectional references
- Subclasses know too much about parents

**Why it's bad:**
- High coupling
- Changes cascade
- Hard to modify one without other

**Refactorings:**
- Move Method
- Move Field
- Change Bidirectional to Unidirectional
- Extract Class
- Hide Delegate

---

### Message Chains

**Signs:**
- Long chains of method calls: `a.getB().getC().getD().getValue()`
- Client depends on navigation structure
- "Train wreck" code

**Why it's bad:**
- Fragile—any change breaks chain
- Violates Law of Demeter
- Coupling to structure

**Refactorings:**
- Hide Delegate
- Extract Method
- Move Method

**Example:**
```javascript
// Bad: Message chain
const managerName = employee.getDepartment().getManager().getName();

// Better: Hide delegation
const managerName = employee.getManagerName();
```

---

### Middle Man

**Signs:**
- Class that only delegates to another
- Half the methods are delegations
- No added value

**Why it's bad:**
- Unnecessary indirection
- Maintenance overhead
- Confusing architecture

**Refactorings:**
- Remove Middle Man
- Inline Method

---

## Smell Severity Guide

| Severity | Description | Action |
|----------|-------------|--------|
| **Critical** | Blocks development, causes bugs | Fix immediately |
| **High** | Significant maintenance burden | Fix in current sprint |
| **Medium** | Noticeable but manageable | Plan for near future |
| **Low** | Minor inconvenience | Fix opportunistically |

---

## Quick Detection Checklist

Use this checklist when scanning code:

- [ ] Any method > 30 lines?
- [ ] Any class > 300 lines?
- [ ] Any method with > 4 parameters?
- [ ] Any duplicated code blocks?
- [ ] Any switch/case on type codes?
- [ ] Any unused code?
- [ ] Any methods using another class's data heavily?
- [ ] Any long chains of method calls?
- [ ] Any comments explaining "what" not "why"?
- [ ] Any primitives that should be objects?

---

## Further Reading

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.)
- Kerievsky, J. (2004). *Refactoring to Patterns*
- Feathers, M. (2004). *Working Effectively with Legacy Code*

---

**Last Updated**: August 4, 2026
**Claude Code Version**: 2.1.220
**Sources**:
- https://code.claude.com/docs/en/skills
**Compatible Models**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
